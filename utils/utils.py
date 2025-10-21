import cv2
import matplotlib.pyplot as plt
import numpy as np

def equalizacion_local(img, tamaño_ventana, background=False):
    """
    Aplica ecualización de histograma local a una imagen para mejorar el contraste en áreas locales.
    Esto es útil para imágenes con iluminación desigual, ya que ajusta el contraste basándose en una ventana alrededor de cada píxel.
    
    Args:
        img: Imagen de entrada (numpy array en escala de grises)
        tamaño_ventana: Tupla (m, n) que define el tamaño de la ventana (altura, ancho) para la ecualización local
        binary: Si True, convierte la imagen a binaria umbralizando valores >= 200 a 255 (útil para imágenes con texto o marcas)
    
    Returns:
        resultado: Imagen procesada con ecualización local aplicada
    """
    
    # Desempaquetar el tamaño de la ventana en altura (m) y ancho (n).
    m, n = tamaño_ventana
    
    # Calcular el borde necesario para evitar errores en los bordes de la imagen
    # Se toma el máximo entre m y n, y se divide por 2 para obtener un borde simétrico
    # Ejemplo: si tamaño_ventana=(5,3), borde=2 (para cubrir la ventana en todos los lados)
    borde = max(m, n)
    borde = borde // 2
    
    # Crear una copia de la imagen para no modificar la original
    resultado = img.copy()
    # Obtener las dimensiones de la imagen (filas y columnas)
    rows, col = resultado.shape
    
    # Si se especifica background=True, se crea una máscara para píxeles >= 200 y se asigna 255 a esos píxeles
    # Esto en el caso de nuestra imagen hace que el fondo sea uniforme y no contenga pequeñas variaciones.
    if background:
        mask_background = resultado >= 200
        resultado[mask_background] = 255

    # Añadir un borde replicado alrededor de la imagen para manejar los píxeles en los bordes
    img_bordes = cv2.copyMakeBorder(resultado, borde, borde, borde, borde, cv2.BORDER_REPLICATE)
    
    # Iterar sobre cada píxel de la imagen original
    for fila in range(rows):
        for columna in range(col):
            # Extraer la ventana centrada en el píxel actual desde la imagen con bordes
            ventana = img_bordes[fila : fila + m, columna : columna + n]
            
            # Aplicar ecualización de histograma a la ventana completa
            ventana_eq = cv2.equalizeHist(ventana)
            
            # Asignar el valor del píxel central de la ventana ecualizada al píxel correspondiente en el resultado
            # El centro de la ventana es [m//2, n//2], lo que preserva la localización del píxel
            # Ejemplo: para ventana 5x5, el centro es [2,2]; esto reemplaza el píxel original con el ecualizado localmente
            resultado[fila, columna] = ventana_eq[m // 2, n // 2]
    
    # Retornar la imagen procesada
    return resultado

def indices_bordes(img, axis=0, candidates=10, diff=10):
    """
    Encuentra los índices de bordes más prominentes en una imagen.
    
    Args:
        img: Imagen de entrada (numpy array)
        axis: Eje a lo largo del cual sumar los bordes (0=filas, 1=columnas)
        candidates: Número máximo de candidatos a considerar
        diff: Distancia mínima entre bordes válidos
    """
    
    # Detección de bordes usando algoritmo de Canny
    edges = cv2.Canny(img, 100, 200)
    # Retorna imagen binaria donde píxeles blancos (255) son bordes
    
    # Calcular límite dimensional para evitar overflow
    shape_limit = img.shape[1-axis]
    # Si axis=0 usa shape[1] (ancho), si axis=1 usa shape[0] (alto)
    
    # Proteger contra candidates fuera de rango
    candidates = min(candidates, shape_limit)
    # Ejemplo: si imagen tiene 50 filas y candidates=100, se ajusta a 50
    
    # Encontrar los índices de bordes más prominentes
    indices = np.sort(np.argsort(np.sum(edges, axis=axis))[-candidates:])
    # 1. np.sum(): suma bordes por columna/fila según axis
    # 2. np.argsort(): índices ordenados por intensidad (menor a mayor)
    # 3. [-candidates:]: toma los últimos N (mayor intensidad)
    # 4. np.sort(): ordena espacialmente los índices seleccionados
    
    # Filtrado vectorizado de índices muy cercanos
    if len(indices) > 1:
        mask = np.concatenate([[True], np.diff(indices) >= diff])
        indices = indices[mask]
    # np.concatenate concantena la lista de indices con True para mantener siempre el primer elemento.
    # np.diff() calcula diferencias consecutivas: [10,15,17,25] → [5,2,8]
    # Máscara booleana mantiene índices con diferencia >= diff
    # Ejemplo: [10,15,17,25] con diff=3 y mask [True,True,False,True] = [10,15,25]

    if axis == 0 and len(indices) > 3:
        indices = np.delete(indices, 2)
    # Elimina la tercera columna si hay más de tres
    # Esto para evitar detectar los separadores de las preguntas como columnas válidas
    # Solo se aplica cuando se buscan columnas (axis=0)
    # El separador siempre es la tercera columna en el formulario
    
    return indices

def recortar_campos(img, filas, columnas):
    """
    Recorta sub-imágenes de preguntas basadas en índices de filas y columnas.
    Se omiten la primera y sexta fila y se añade un margen de 3 píxeles.
    
    Args:
        img: Imagen de entrada (numpy array)
        filas: Índices de filas que delimitan las preguntas
        columnas: Índices de columnas que delimitan las preguntas
    """
    recortes = []
    for i in range(len(filas)-1):
        if i == 0 or i == 5:
            continue
        for j in range(len(columnas)-1):
            campo = img[filas[i]+3:filas[i+1], columnas[j]+3:columnas[j+1]]
            recortes.append(campo)
    recortes = [recorte for i, recorte in enumerate(recortes) if i % 2 == 1]
    return recortes

def contar_caracteres(img):
    """
    Cuenta la cantidad de caracteres (componentes conectados) en una imagen binaria.
    Devuelve también las estadísticas de cada componente si state=True.

    Args:
        img: Imagen binaria de entrada (numpy array)
    """

    img_copy = img.copy()
    img_copy = cv2.threshold(img_copy, 128, 255, cv2.THRESH_BINARY_INV)[1]
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_copy, connectivity=8)

    return num_labels - 1

def detectar_espacio(img):
    """
    Detecta si hay espacios en blanco entre caracteres en una imagen binaria.
    Para 2 caracteres: se considera un espacio una separacion de 10 pixeles.
    Para más caracteres: usa 2.5 * mediana de distancias como umbral.
    
    Args:
        img: Imagen binaria de entrada (numpy array)
    """

    # Evitar modificar la imagen original
    img_copy = img.copy() 

    # Umbralización e inversión
    img_copy = cv2.threshold(img_copy, 128, 255, cv2.THRESH_BINARY_INV)[1]

    # Encontrar componentes conectados (caracteres).
    # Extraer stats y excluir el fondo.
    boxes = cv2.connectedComponentsWithStats(img_copy, connectivity=8)[2][1:]  
    
    if len(boxes) < 2:
        return False  # No hay suficientes caracteres para detectar espacios
    
    # Ordenar las cajas por posición izquierda (de izquierda a derecha)
    boxes_sorted = boxes[np.argsort(boxes[:, cv2.CC_STAT_LEFT])]
    
    # Calcular distancias horizontales entre caracteres
    distancias = []
    for i in range(len(boxes_sorted) - 1):
        letra_actual = boxes_sorted[i, cv2.CC_STAT_LEFT]
        ancho_letra = boxes_sorted[i, cv2.CC_STAT_WIDTH]
        letra_siguiente = boxes_sorted[i+1, cv2.CC_STAT_LEFT]
        
        # Distancia real entre caracteres (desde el final de uno al inicio del siguiente)
        dist = letra_siguiente - (letra_actual + ancho_letra)
        distancias.append(dist)
    
    if not distancias:
        return False
    
    # Caso especial: solo 2 caracteres
    if len(boxes_sorted) == 2:
        # Se considera un espacio una separación de 10 píxeles.
        umbral_espacio = 10
    else:
        # Calcular la mediana de las distancias positivas (ignorando solapamientos)
        mediana_distancia = np.median([d for d in distancias if d > 0])
        # Definir umbral de espacio como 2.5 veces la mediana
        umbral_espacio = 2.5 * mediana_distancia
    
    # Verificar si alguna distancia supera el umbral (indicando un espacio)
    return any(d > umbral_espacio for d in distancias)

def analizar_respuesta(img):
    """
    Analiza una imagen de respuesta para determinar si se marcó exactamente una opción.
    
    Args:
        img: Imagen en escala de grises del campo de respuesta.
    
    Returns:
        bool: True si se marcó exactamente una opción, False en caso contrario.
    """
    # Contar los caracteres en la imagen
    caracteres = contar_caracteres(img)

    # Restar 1 para no contar el separador.
    num_opciones_marcadas = caracteres - 1 

    # Verificar si se marcó exactamente una opción con un único carácter
    return num_opciones_marcadas == 1


def validacion_imagen(img, resultado_validacion):
    """
    Agrega texto de validación a una imagen.
    
    Args:
        img: Imagen donde se va a agregar el texto
        resultado_validacion: Diccionario con booleanos para cada parámetro de validación
        
    Returns:
        output_img: Imagen con el texto "BIEN" o "MAL" agregado
    """
    # Crear copia de la imagen de entrada
    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) if len(img.shape) == 2 else img.copy()
    
    # Verificar si todos los valores del diccionario son True
    validacion_exitosa = all(resultado_validacion.values())
    
    # Determinar texto y color
    texto = "BIEN" if validacion_exitosa else "MAL"
    color = (0, 255, 0) if texto == "BIEN" else (255, 0, 0)
    
    # Configurar texto
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    thickness = 2
    text_size = cv2.getTextSize(texto, font, font_scale, thickness)[0]
    x = output_img.shape[1] - text_size[0] - 10
    y = output_img.shape[0] // 2 + text_size[1] // 2
    
    # Dibujar borde negro y texto
    cv2.putText(output_img, texto, (x, y), font, font_scale, (0, 0, 0), thickness + 2)
    cv2.putText(output_img, texto, (x, y), font, font_scale, color, thickness)
    
    return output_img