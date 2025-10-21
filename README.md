# TUIA - Procesamiento Digital de Imágenes - TP1

Este repositorio contiene los ejercicios del Trabajo Práctico 1 de la materia Procesamiento Digital de Imágenes (PDI) de la Tecnicatura Universitaria en Inteligencia Artificial (TUIA).

## 📋 Requisitos

- **Python 3.10.4**
- **Librerías necesarias:**
  - `opencv-contrib-python==4.10.0.84`
  - `numpy==1.26.4`
  - `matplotlib==3.10.3`
  - `pandas==2.2.2`

## 🚀 Cómo ejecutar los scripts

Los scripts se pueden ejecutar directamente desde la línea de comandos utilizando el intérprete de Python, siempre y cuando tengas las dependencias instaladas.

### Opción 1: Ejecución con Python global

Si tienes las librerías instaladas en tu Python global:

```bash
python ejercicio_1.py
```

```bash
python ejercicio_2.py
```

### Opción 2: Ejecución con entorno virtual

Si utilizas un entorno virtual (recomendado), ejecuta los scripts con la ruta al ejecutable de Python de tu entorno:

<details>
<summary><b>🪟 Windows</b></summary>

```bash
# Sintaxis general
ruta\al\entorno\Scripts\python.exe ejercicio_1.py
ruta\al\entorno\Scripts\python.exe ejercicio_2.py
```

```bash
# Ejemplo con entorno llamado "venv"
.\venv\Scripts\python.exe ejercicio_1.py
.\venv\Scripts\python.exe ejercicio_2.py
```

</details>

<details>
<summary><b>🐧 Linux / 🍎 macOS</b></summary>

```bash
# Sintaxis general
ruta/al/entorno/bin/python ejercicio_1.py
ruta/al/entorno/bin/python ejercicio_2.py
```

```bash
# Ejemplo con entorno llamado "venv"
./venv/bin/python ejercicio_1.py
./venv/bin/python ejercicio_2.py
```

</details>

## 📦 Instalación de dependencias

### Instalación rápida con requirements.txt

```bash
pip install -r requirements.txt
```

### Instalación manual

```bash
pip install opencv-contrib-python==4.10.0.84 numpy==1.26.4 matplotlib==3.10.3 pandas==2.2.2
```

<details>
<summary><b>Instalación en entorno virtual</b></summary>

**Windows:**
```bash
ruta\al\entorno\Scripts\pip.exe install -r requirements.txt
```

**Linux/macOS:**
```bash
ruta/al/entorno/bin/pip install -r requirements.txt
```

</details>

### 🔍 Verificar versiones instaladas

Para verificar que las librerías estén correctamente instaladas:

```bash
pip show opencv-contrib-python numpy matplotlib pandas
```

Para ver todas las dependencias instaladas:

```bash
pip freeze
```

## 📂 Estructura del proyecto

```
TUIA_PDI_TP1/
├── ejercicio_1.py              # Script principal - Ejercicio 1
├── ejercicio_2.py              # Script principal - Ejercicio 2
├── utils/                      # Módulo de utilidades
│   ├── __init__.py
│   └── utils.py
├── Imagen_con_detalles_escondidos.tif  # Imagen para ejercicio 1
├── formulario_01.png           # Formulario 1
├── formulario_02.png           # Formulario 2
├── formulario_03.png           # Formulario 3
├── formulario_04.png           # Formulario 4
├── formulario_05.png           # Formulario 5
├── resultados_formularios.csv  # Resultados del procesamiento
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

## 📝 Descripción de los ejercicios

### Ejercicio 1
Procesamiento de imagen con detalles escondidos mediante ecualización local de histograma con diferentes tamaños de ventana.

### Ejercicio 2
Análisis y validación automática de formularios mediante procesamiento de imágenes, detección de bordes y extracción de campos.

## 👨‍💻 Autor

**Ezequiel Za** - [@EzequielZa](https://github.com/EzequielZa)

## 📝 Notas

Este proyecto fue desarrollado como parte del curso de Procesamiento Digital de Imágenes de la Tecnicatura Universitaria en Inteligencia Artificial (TUIA).