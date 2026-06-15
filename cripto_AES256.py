import os
import argparse
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def get_key(password: str) -> bytes:
    """Genera una clave AES-256 de exactamente 32 bytes usando SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).digest()

def encrypt_file(input_path: str, output_path: str, password: str):
    # 1. Generamos clave e IV
    key = get_key(password)
    iv = os.urandom(16) # Vector de Inicialización aleatorio
    
    # 2. Leemos el archivo original
    with open(input_path, 'rb') as f:
        data = f.read()
        
    # 3. Aplicamos padding (Relleno para que cierre en bloques de 16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # 4. Ciframos en modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # 5. Guardamos el IV seguido de los datos cifrados
    with open(output_path, 'wb') as f:
        f.write(iv + encrypted_data)
    print(f"[*] Éxito: Archivo cifrado guardado en '{output_path}'")

def decrypt_file(input_path: str, output_path: str, password: str):
    key = get_key(password)
    
    # 1. Leemos el archivo cifrado
    with open(input_path, 'rb') as f:
        file_content = f.read()
        
    # 2. Extraemos el IV (primeros 16 bytes) y los datos cifrados (el resto)
    iv = file_content[:16]
    encrypted_data = file_content[16:]
    
    # 3. Desciframos
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # 4. Quitamos el padding
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    # 5. Guardamos el archivo original
    with open(output_path, 'wb') as f:
        f.write(data)
    print(f"[*] Éxito: Archivo descifrado guardado en '{output_path}'")

if __name__ == "__main__":
    # Configuración de la interfaz por consola (CLI)
    parser = argparse.ArgumentParser(description="Herramienta de Cifrado AES-256")
    parser.add_argument("modo", choices=["cifrar", "descifrar"], help="Operación a realizar")
    parser.add_argument("entrada", help="Ruta del archivo origen")
    parser.add_argument("salida", help="Ruta del archivo destino")
    parser.add_argument("password", help="Contraseña para proteger el archivo")
    
    args = parser.parse_args()
    
    try:
        if args.modo == "cifrar":
            encrypt_file(args.entrada, args.salida, args.password)
        elif args.modo == "descifrar":
            decrypt_file(args.entrada, args.salida, args.password)
    except ValueError:
        print("[!] Error: Contraseña incorrecta o archivo corrupto.")
    except Exception as e:
        print(f"[!] Ocurrió un error inesperado: {e}")