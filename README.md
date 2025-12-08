# 🛡️ DevSecOps Security Pipeline Lab

![Build Status](https://img.shields.io/badge/Build-Passing-success?style=for-the-badge&logo=github)
![Security](https://img.shields.io/badge/Security-Shift--Left-blue?style=for-the-badge&logo=security)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)

## 📋 Descripción del Proyecto

Este repositorio aloja una implementación práctica de una **Pipeline CI/CD Segura (DevSecOps)** utilizando **GitHub Actions**. El objetivo principal es demostrar la integración de controles de seguridad automatizados en el ciclo de vida del desarrollo de software (SDLC), siguiendo la filosofía "Shift-Left".

El proyecto consiste en una aplicación Python intencionalmente vulnerable que es sanitizada automáticamente mediante múltiples barreras de seguridad antes de permitir su despliegue.

## 🏗️ Arquitectura y Herramientas

El pipeline integra las siguientes herramientas de seguridad de código abierto:

| Herramienta | Tipo de Análisis | Función en el Pipeline |
| :--- | :--- | :--- |
| **Gitleaks** | Secret Scanning | Detecta credenciales, API Keys y secretos hardcodeados en el código para prevenir fugas de información. |
| **Trivy** | SCA (Software Composition Analysis) | Escanea las dependencias del proyecto (`requirements.txt`) en busca de vulnerabilidades conocidas (CVEs). |
| **Bandit** | SAST (Static Application Security Testing) | Analiza el código fuente de Python en busca de patrones de programación inseguros (ej. algoritmos de hash débiles). |

## 🚀 Flujo de Trabajo (Workflow)

Cada vez que un desarrollador realiza un `push` a la rama principal:

1.  **Checkout:** Se descarga el código en el entorno de ejecución.
2.  **Detección de Secretos:** Gitleaks escanea el historial de git. Si encuentra secretos, **rompe el build**.
3.  **Análisis de Dependencias:** Trivy verifica las librerías instaladas. Si encuentra CVEs Críticos/Altos, **rompe el build**.
4.  **Auditoría de Código:** Bandit analiza la sintaxis de Python. Si detecta funciones inseguras (como MD5), genera alertas de seguridad.
5.  **Reporte:** Los hallazgos se suben automáticamente a la pestaña **GitHub Security** para su gestión y remediación.

## 🛠️ Instalación y Uso Local

Si deseas replicar este laboratorio en tu máquina:

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/TU_USUARIO/devsecops-lab-v1.git](https://github.com/TU_USUARIO/devsecops-lab-v1.git)
    ```
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ejecuta la aplicación segura:
    ```bash
    python3 app.py
    ```

## 🎓 Aprendizajes Clave

* Configuración de **GitHub Actions** para automatización CI/CD.
* Implementación de políticas de **Build Breaker** (detener el despliegue ante fallos de seguridad).
* Gestión de **falsos positivos** y remediación de vulnerabilidades reales.
* Uso de **Variables de Entorno** para la gestión segura de credenciales.
* Reemplazo de criptografía débil (MD5) por estándares seguros (SHA256).

---
*Desarrollado con ❤️ y ☕ como parte de mi formación en Ciberseguridad y DevSecOps.*
