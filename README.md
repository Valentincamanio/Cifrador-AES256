# TP2 - Criptografía
### Seguridad Informática - Universidad Nacional de Quilmes 

Herramienta de consola (CLI) desarrollada en Python para el Trabajo Práctico 2 de Seguridad Informatica en la UNQ. El programa permite tomar un archivo cualquiera y devolver el mismo archivo cifrado con AES-256, así como tomar por entrada un archivo cifrado con AES-256 y devolver el archivo original.

## 🛠️ Requisitos Previos

1. Abrir terminal 
2. Ir a la carpeta donde está el proyecto. (cd C:\Users\Pc\Cifrador-AES256)
3. Abrir terminal 
4. Ejecutar comando: pip install -r requirements.txt

## Cómo usar el script (Modo Desarrollo)

El script se ejecuta directamente desde la consola pasando 4 parámetros obligatorios: la acción (cifrar o descifrar), el archivo de entrada, el nombre del archivo de salida y una contraseña.

Para cifrar: python cripto_AES256.py cifrar archivo_original.txt archivo_cifrado.aes miclave123

Para descifrar: python cripto_AES256.py descifrar archivo_cifrado.aes archivo_recuperado.txt miclave123

Donde:
   - archivo_original.txt es el archivo que se quiere cifrar.
   - archivo_cifrado.aes es el archivo cifrado que se va a generar.
   - miclave123 es la contraseña elegida para cifrar el archivo.

