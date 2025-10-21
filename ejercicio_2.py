from utils import *
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PLOT = False  # Mostrar imágenes intermedias

# Definir DataFrame vacío fuera del bucle
df = pd.DataFrame()

for i in range(1, 6):

    img = cv2.imread(f'formulario_0{i}.png', cv2.IMREAD_GRAYSCALE)

    if PLOT:
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.title(f'Formulario 0{i}')
        plt.show()

    filas = indices_bordes(img, axis=1, candidates=20)

    if PLOT:
        for j, fila in enumerate(filas):
            plt.imshow(img, cmap='gray', vmin=0, vmax=255)
            plt.axhline(y=fila, color='r', linestyle='--', label=f'Fila {j+1}' if j==0 else "")
        plt.axis('off')
        plt.show()

    columnas = indices_bordes(img, axis=0, candidates=20, diff=170)

    if PLOT:
        for j, columna in enumerate(columnas):
            plt.imshow(img, cmap='gray', vmin=0, vmax=255)
            plt.axvline(x=columna, color='b', linestyle='--', label=f'Columna {j+1}' if j==0 else "")
        plt.axis('off')
        plt.show()

    recortes = recortar_campos(img, filas, columnas)

    if PLOT:
        for j, recorte in enumerate(recortes):
            plt.subplot(5, 4, j+1)
            plt.imshow(recorte, cmap='gray', vmin=0, vmax=255)
            plt.title(f'Recorte {j}')
        plt.show()

    datos = {
        'Nombre y Apellido': recortes[0],
        'Edad': recortes[1],
        'Mail': recortes[2],
        'Legajo': recortes[3],
        'Pregunta 1': recortes[4],
        'Pregunta 2': recortes[5],
        'Pregunta 3': recortes[6],
        'Comentarios': recortes[7],
    }

    nombre_apellido_valido = (contar_caracteres(datos['Nombre y Apellido']) <= 25) and (detectar_espacio(datos['Nombre y Apellido']))
    edad_valida = (contar_caracteres(datos['Edad']) > 1) and (contar_caracteres(datos['Edad']) <= 3) and (not detectar_espacio(datos['Edad']))
    mail_valido = (contar_caracteres(datos['Mail']) <= 25) and (not detectar_espacio(datos['Mail']))
    legajo_valido = (contar_caracteres(datos['Legajo']) == 8) and (not detectar_espacio(datos['Legajo']))
    pregunta_1_valida = analizar_respuesta(datos['Pregunta 1'])
    pregunta_2_valida = analizar_respuesta(datos['Pregunta 2'])
    pregunta_3_valida = analizar_respuesta(datos['Pregunta 3'])
    comentarios_validos = (contar_caracteres(datos['Comentarios']) > 0) and (contar_caracteres(datos['Comentarios']) <= 25)

    resultados = {
        'Nombre y Apellido': nombre_apellido_valido,
        'Edad': edad_valida,
        'Mail': mail_valido,
        'Legajo': legajo_valido,
        'Pregunta 1': pregunta_1_valida,
        'Pregunta 2': pregunta_2_valida,
        'Pregunta 3': pregunta_3_valida,
        'Comentarios': comentarios_validos,
    }

    for campo, resultado in resultados.items():
        status = "OK" if resultado else "MAL"
        print(f"{campo}: {status}")
    print("\n" + "-"*30 + "\n")

    img_validada = validacion_imagen(datos['Nombre y Apellido'], resultados)
    plt.imshow(img_validada, vmin=0, vmax=255)
    plt.show()

    # Agregar fila al DataFrame
    resultados_con_id = {'ID': f'0{i}'}
    resultados_con_id.update({campo: "OK" if resultado else "MAL" for campo, resultado in resultados.items()})
    
    # Concatenar la nueva fila al DataFrame
    df = pd.concat([df, pd.DataFrame([resultados_con_id])], ignore_index=True)

# Guardar el DataFrame completo después del bucle
df.to_csv('resultados_formularios.csv', index=False)