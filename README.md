# 🎥 AVI to MP4 High-Efficiency Converter (test)

Una herramienta de línea de comandos (CLI) optimizada para la transcodificación de archivos de video legacy (AVI) al estándar moderno MP4 (H.264/AAC), equilibrando la fidelidad visual y el peso del archivo.

## 🚀 ¿Por qué este proyecto?
El formato AVI, aunque robusto, carece de la eficiencia de compresión y la compatibilidad web de los contenedores modernos. Este script automatiza la migración de archivos antiguos a un formato listo para streaming y dispositivos móviles.



## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Core Engine:** FFmpeg
* **Librería de Wrapper:** `ffmpeg-python`
* **Gestión de Rutas:** `pathlib`

## 🧠 Desafíos Técnicos y Soluciones

### 1. Optimización de Calidad vs. Peso (CRF)
En lugar de usar un bitrate fijo, el script implementa **Constant Rate Factor (CRF)**. 
* **Solución:** Se configuró un valor de `crf=23` por defecto, que es el "punto dulce" para mantener una calidad imperceptible al ojo humano mientras se reduce el peso del archivo hasta en un 60%.

### 2. Manejo de Codecs de Audio
Muchos archivos AVI antiguos usan audio PCM o MP3. 
* **Solución:** Se fuerza la conversión a **AAC (Advanced Audio Coding)** a 192kbps para asegurar que el audio se escuche correctamente en cualquier navegador o smartphone moderno.

## 💻 Instalación

1. **Prerrequisitos:** Tener instalado [FFmpeg](https://ffmpeg.org/download.html) en tu sistema.
2. **Clonar repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/avi-to-mp4-converter.git](https://github.com/tu-usuario/avi-to-mp4-converter.git)
   cd avi-to-mp4-converter
