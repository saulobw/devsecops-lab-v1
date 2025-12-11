# 🛡️ End-to-End DevSecOps & Secure Supply Chain Lab

![Build Status](https://img.shields.io/badge/Build-Passing-success?style=for-the-badge&logo=github)
![Docker](https://img.shields.io/badge/Container-Hardened-blue?style=for-the-badge&logo=docker)
![Sigstore](https://img.shields.io/badge/Integrity-Signed-purple?style=for-the-badge&logo=letsencrypt)
![Security](https://img.shields.io/badge/Security-Shift--Left-red?style=for-the-badge&logo=security)

## 📋 Descripción del Proyecto

Este proyecto demuestra la implementación de una **Cadena de Suministro de Software Segura (Secure Software Supply Chain)**. Evoluciona desde la protección del código fuente hasta la entrega de artefactos inmutables y firmados criptográficamente.

El pipeline integra controles de seguridad automatizados (SAST, SCA, Secret Scanning) y extiende la seguridad a la infraestructura mediante **Container Hardening** y **Firma Digital de Imágenes**.

## 🏗️ Arquitectura de Defensa en Profundidad

El sistema impone barreras de seguridad en dos fases críticas:

### FASE 1: Seguridad del Código (AppSec)
| Herramienta | Función |
| :--- | :--- |
| **Gitleaks** | Prevención de fuga de credenciales y secretos (Secret Scanning). |
| **Trivy (FS)** | Detección de vulnerabilidades en dependencias de la aplicación. |
| **Bandit** | Análisis estático (SAST) para código Python y corrección de criptografía débil. |

### FASE 2: Seguridad del Contenedor (InfraSec & Integrity)
| Herramienta | Función |
| :--- | :--- |
| **Docker (Slim)** | Construcción de imágenes optimizadas con principio de mínimo privilegio (Non-root user). |
| **Trivy (Image)** | Escaneo de vulnerabilidades del Sistema Operativo base del contenedor. |
| **Dockle** | Auditoría de cumplimiento de estándares **CIS Benchmarks** y buenas prácticas de Docker. |
| **Cosign** | **Firma Digital y Verificación** para garantizar la inmutabilidad e integridad del artefacto. |

## 🚀 Flujo de Trabajo (The Pipeline)

1.  **Commit:** El desarrollador envía código.
2.  **Code Gates:** Gitleaks, Bandit y Trivy escanean el código. Si falla, se bloquea el build.
3.  **Build Seguro:** Se construye la imagen Docker usando usuarios sin privilegios (`appuser`).
4.  **Audit:** Dockle verifica la configuración del contenedor.
5.  **Signing:** Se sube la imagen a **GHCR** y se firma con **Cosign**.
6.  **Verify:** Se valida la firma criptográfica antes de cualquier despliegue.

## 🛠️ Verificación de Integridad (Demo)

Para verificar que la imagen producida en este laboratorio es auténtica y no ha sido manipulada, utiliza la clave pública adjunta en el repositorio:

```bash
# Requiere tener Cosign instalado
cosign verify --key cosign.pub ghcr.io/TU_USUARIO/devsecops-app:v1
