# SGS Encrypt Files (Python)

Este proyecto es una **Prueba de Concepto (PoC)** diseñada para demostrar el funcionamiento de scripts de cifrado de archivos y la gestión de claves simétricas mediante protocolos de red (SMTP). 

> [!CAUTION]
> **USAR CON PRECAUCIÓN:** Este script cifra los archivos del escritorio y **elimina los originales**. Asegúrate de configurar correctamente las variables de correo antes de probarlo, o perderás el acceso a tus archivos.

---

## 🚀 Funcionalidades

El script detecta automáticamente el sistema operativo y actúa sobre la carpeta del **Escritorio**:

* **Cifrado Robusto:** Utiliza la librería `cryptography` con el estándar Fernet (AES).
* **Multiplataforma:** Compatible con Windows y distribuciones Linux (vía `xdg-user-dir`).
* **Gestión de Claves:** Genera una clave única por ejecución y la envía por correo electrónico automáticamente.
* **Extensión Personalizada:** Los archivos cifrados se renombran con la extensión `.sgs`.



---

## 🛠️ Configuración Inicial

Para que el sistema de envío de claves funcione, debes editar las siguientes variables en el código fuente:

1.  **`direccion_correo`**: Introduce tu dirección de Gmail.
2.  **`developer_key_gmail`**: No es tu contraseña habitual. Debes usar una **"Contraseña de Aplicación"** generada desde tu cuenta de Google (Seguridad > Verificación en dos pasos > Contraseñas de aplicaciones).

### Instalación de dependencias
Es necesario instalar la librería encargada del cifrado antes de ejecutar el script:

```bash
pip install cryptography
