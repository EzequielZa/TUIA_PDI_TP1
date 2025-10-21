# TUIA - Procesamiento Digital de Imágenes - TP1

Este repositorio contiene los ejercicios del Trabajo Práctico 1 de la materia Procesamiento Digital de Imágenes (PDI) de la carrera TUIA.

## 📋 Requisitos

- Python 3.x instalado en tu sistema
- Librerías necesarias:
  - OpenCV (`opencv-python`)
  - NumPy (`numpy==1.26.4`)
  - Matplotlib (`matplotlib==3.10.3`)
  - Pandas (`pandas==2.2.2`)

## 🚀 Cómo ejecutar los scripts

Los scripts se pueden ejecutar directamente desde la línea de comandos utilizando el intérprete de Python, siempre y cuando tengas las dependencias instaladas en el intérprete de Python global.

### Ejecución con Python global

Si tienes las librerías instaladas globalmente, simplemente ejecuta:

#### Ejecutar Ejercicio 1

```bash
python ejercicio_1.py
```

#### Ejecutar Ejercicio 2

```bash
python ejercicio_2.py
```

### Ejecución con entorno virtual

Si prefieres usar un entorno virtual (recomendado para gestionar dependencias), puedes ejecutar los scripts utilizando la ruta al `python.exe` de tu entorno:

#### Windows

```bash
ruta\al\entorno\Scripts\python.exe ejercicio_1.py
ruta\al\entorno\Scripts\python.exe ejercicio_2.py
```

**Ejemplo:**
```bash
.\venv\Scripts\python.exe ejercicio_1.py
.\venv\Scripts\python.exe ejercicio_2.py
```

#### Linux/MacOS

```bash
ruta/al/entorno/bin/python ejercicio_1.py
ruta/al/entorno/bin/python ejercicio_2.py
```

**Ejemplo:**
```bash
./venv/bin/python ejercicio_1.py
./venv/bin/python ejercicio_2.py
```

## 📦 Instalación de dependencias

Para instalar todas las librerías necesarias con las versiones específicas:

```bash
pip install numpy==1.26.4 matplotlib==3.10.3 pandas==2.2.2 opencv-python
```

O si usas un entorno virtual:

**Windows:**
```bash
ruta\al\entorno\Scripts\pip.exe install numpy==1.26.4 matplotlib==3.10.3 pandas==2.2.2 opencv-python
```

**Linux/MacOS:**
```bash
ruta/al/entorno/bin/pip install numpy==1.26.4 matplotlib==3.10.3 pandas==2.2.2 opencv-python
```

### Ver versiones instaladas

Para verificar las versiones de las librerías instaladas:

```bash
pip show opencv-python matplotlib numpy pandas
```

O para ver todas tus dependencias:

```bash
pip freeze
```

## 📂 Estructura del proyecto

```
TUIA_PDI_TP1/
├── ejercicio_1.py
├── ejercicio_2.py
└── README.md
```

## 👨‍💻 Autor

**Ezequiel Za** - [@EzequielZa](https://github.com/EzequielZa)

## 📝 Notas

Este proyecto fue desarrollado como parte del curso de Procesamiento Digital de Imágenes de la Tecnicatura Universitaria en Inteligencia Artificial (TUIA).