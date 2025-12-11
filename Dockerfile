# 1. IMAGEN BASE: Usamos una versión "slim" (ligera) de Python para reducir superficie de ataque
# Evitamos la versión "latest" porque cambia sin aviso.
FROM python:3.10-slim

# 2. VARIABLES DE ENTORNO:
# Evita que Python genere archivos __pycache__ y asegura que los logs salgan directo a la consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. SEGURIDAD (Mínimo Privilegio):
# Creamos un usuario de sistema llamado 'appuser' sin contraseña.
# No usaremos 'root' para correr la app.
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# 4. DIRECTORIO DE TRABAJO:
WORKDIR /app

# 5. INSTALACIÓN DE DEPENDENCIAS:
# Copiamos solo el requirements primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. COPIA DEL CÓDIGO:
COPY . .

# 7. PERMISOS:
# Le regalamos la carpeta /app al usuario 'appuser'
RUN chown -R appuser:appgroup /app

# 8. CAMBIO DE USUARIO:
# A partir de aquí, todo se ejecuta como un mortal, no como Dios (root).
USER appuser

# 9. PUERTO:
# Documentamos que la app escucha en el 5000 (puerto default de Flask)
EXPOSE 5000

# 10. EJECUCIÓN:
# Lanzamos la app.
CMD ["python", "app.py"]
