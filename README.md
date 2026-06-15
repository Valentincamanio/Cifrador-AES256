# TP2 - Criptografía
### Seguridad Informática - Universidad Nacional de Quilmes 

Herramienta de consola (CLI) desarrollada en Python para el Trabajo Práctico. El programa permite tomar un archivo cualquiera y devolver el mismo archivo cifrado con AES-256, así como tomar por entrada un archivo cifrado con AES-256 y devolver el archivo original.

## 🛠️ Requisitos Previos

Para correr el código fuente y hacer pruebas locales, necesitan tener instalado Python en sus máquinas y la librería de criptografía.

1. Clonar este repositorio.
2. Abrir la terminal en la carpeta del proyecto.
3. Instalar la dependencia principal ejecutando:
   ```bash
   pip install cryptography

## Cómo usar el script (Modo Desarrollo)

El script se ejecuta directamente desde la consola pasando 4 parámetros obligatorios: la acción (cifrar o descifrar), el archivo de entrada, el nombre del archivo de salida y una contraseña.
1.  Generar el ejecutable en un solo archivo:
python -m PyInstaller --onefile cripto_AES256.py
2. Para encriptar un archivo: 
dist/ cripto_tp2.py cifrar documento.pdf documento_cifrado.aes miclave123
3. Para desencriptar un archivo:
dist/ cripto_tp2.py descifrar documento_cifrado.aes documento_recuperado.pdf miclave123
