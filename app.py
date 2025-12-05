import os
import hashlib # Importamos librería de hash

def run_app():
    print("Iniciando aplicacion segura...")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

    if AWS_ACCESS_KEY_ID:
        print(f"Conectando con la llave: {AWS_ACCESS_KEY_ID}")

    # VULNERABILIDAD SAST: Uso de MD5 (Inseguro)
    password = "supersecretpassword"
    # Bandit detectará que 'md5' es una función prohibida
    hash_obj = hashlib.md5(password.encode()) 
    print(f"Hash inseguro: {hash_obj.hexdigest()}")

if __name__ == "__main__":
    run_app()
