import os

def run_app():
    print("Iniciando aplicacion segura... o tal vez no.")

    # SOLUCIÓN: Leemos del entorno del sistema, no del archivo.
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    if AWS_ACCESS_KEY_ID:
        print(f"Conectando con la llave: {AWS_ACCESS_KEY_ID}")
    else:
        print("No se encontró credencial, pero el código es seguro.")

if __name__ == "__main__":
    run_app()
