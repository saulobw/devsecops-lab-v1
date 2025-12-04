import os

def run_app():
    print("Iniciando aplicacion segura... o tal vez no.")

    # VULNERABILIDAD INTENCIONAL: Credencial "Hardcoded"
    # Esto es lo que Gitleaks detectará más adelante.
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE" 
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

    print(f"Conectando con la llave: {AWS_ACCESS_KEY_ID}")

if __name__ == "__main__":
    run_app()
