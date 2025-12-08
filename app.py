import os
import hashlib # Importamos librería de hash

def run_app():
    print("Iniciando aplicacion segura...")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

    if AWS_ACCESS_KEY_ID:
        print(f"Conectando con la llave: {AWS_ACCESS_KEY_ID}")

    # VULNERABILIDAD SAST: Uso de MD5 (Inseguro)
    password = "supersecretpassword"
    # cambio md5 por sha256
    hash_obj = hashlib.sha256(password.encode()) 
    print(f"Hash seguro: {hash_obj.hexdigest()}")

if __name__ == "__main__":
    run_app()
