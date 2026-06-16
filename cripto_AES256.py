import os
import argparse
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def generar_clave(contrasenia_usuario: str) -> bytes:
    # Hacemos un hash SHA-256 para asegurarnos de que la clave tenga justo 32 bytes (lo que pide AES-256)
    return hashlib.sha256(contrasenia_usuario.encode('utf-8')).digest()

# def config

def cifrar_archivo(ruta_origen: str, ruta_destino: str, contrasenia: str):
    clave = generar_clave(contrasenia)
    iv = os.urandom(16) # Metemos un IV aleatorio para más seguridad
    
    # Leemos todo el archivo que pasaron por parámetro
    with open(ruta_origen, 'rb') as archivo_in:
        datos_originales = archivo_in.read()
        
    # Le metemos padding (relleno) para que los bloques cierren en 16 bytes exactos
    rellenador = padding.PKCS7(128).padder()
    datos_con_padding = rellenador.update(datos_originales) + rellenador.finalize()
    
    # Configuramos el cifrador con la clave y el IV en modo CBC
    cifrador = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    encriptador = cifrador.encryptor()
    datos_cifrados = encriptador.update(datos_con_padding) + encriptador.finalize()
    
    # Guardamos el IV pegado al principio y despues la data cifrada
    with open(ruta_destino, 'wb') as archivo_out:
        archivo_out.write(iv + datos_cifrados)
        
    print(f"¡Listo! Archivo encriptado y guardado en '{ruta_destino}'")

def descifrar_archivo(ruta_origen: str, ruta_destino: str, contrasenia: str):
    clave = generar_clave(contrasenia)
    
    # Abrimos el archivo cifrado
    with open(ruta_origen, 'rb') as archivo_in:
        contenido = archivo_in.read()
        
    # Separamos el IV (los primeros 16 bytes) del resto de la data
    iv = contenido[:16]
    datos_cifrados = contenido[16:]
    
    # Preparamos el descifrador
    cifrador = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    desencriptador = cifrador.decryptor()
    datos_con_padding = desencriptador.update(datos_cifrados) + desencriptador.finalize()
    
    # Le sacamos el padding que le agregamos al cifrar
    sacar_relleno = padding.PKCS7(128).unpadder()
    datos_originales = sacar_relleno.update(datos_con_padding) + sacar_relleno.finalize()
    
    # Guardamos el archivo original de nuevo
    with open(ruta_destino, 'wb') as archivo_out:
        archivo_out.write(datos_originales)
        
    print(f"¡Listo! Archivo desencriptado con éxito en '{ruta_destino}'")

if __name__ == "__main__":
    # Configuración de la consola para pasarle los datos por terminal
    parser = argparse.ArgumentParser(description="TP2 Criptografía - Cifrador AES-256")
    parser.add_argument("accion", choices=["cifrar", "descifrar"], help="Elegí si vas a cifrar o descifrar")
    parser.add_argument("archivo_in", help="Ruta del archivo original")
    parser.add_argument("archivo_out", help="Ruta del archivo de salida")
    parser.add_argument("clave", help="Contraseña para cifrar/descifrar")
    
    argumentos = parser.parse_args()
    
    try:
        if argumentos.accion == "cifrar":
            cifrar_archivo(argumentos.archivo_in, argumentos.archivo_out, argumentos.clave)
        elif argumentos.accion == "descifrar":
            descifrar_archivo(argumentos.archivo_in, argumentos.archivo_out, argumentos.clave)
    except ValueError:
        print("¡Ups! Error: La contraseña está mal o el archivo está corrupto.")
    except Exception as e:
        print(f"Apareció un error raro: {e}")