# API REST con Django REST Framework

Backend desarrollado con **Django REST Framework (DRF)** como proyecto de aprendizaje. Su objetivo principal fue aprender a construir una API REST, trabajar con serializadores y autenticación JWT, y conectarla con una aplicación frontend creada en Angular.

El proyecto expone recursos para usuarios, productos, publicaciones de blog, servicios, clientes y compras.

## Objetivo del proyecto

Este repositorio fue creado con fines educativos para practicar:

- Creación y organización de una API con Django y DRF.
- Modelado de datos con el ORM de Django.
- Conversión de modelos a JSON mediante serializadores.
- Creación de endpoints para consultar y registrar información.
- Registro y autenticación de usuarios.
- Generación y renovación de tokens JWT.
- Configuración de CORS para comunicar Django con Angular.
- Consumo de la API desde una aplicación frontend.

El frontend relacionado se encuentra en el repositorio [Angular](https://github.com/Evangelistabv/Angular).

## Funcionalidades

### Usuarios

- Registro de usuarios.
- Inicio de sesión mediante nombre o correo electrónico.
- Consulta de datos de usuario a partir de un token.
- Obtención y renovación de tokens JWT.
- Modelo de usuario personalizado basado en correo electrónico.

### Productos

- Consulta de productos.
- Registro de productos.
- Datos de nombre y precio.

### Blog

- Consulta de publicaciones.
- Registro de publicaciones.
- Soporte para título, contenido e imagen.

### Servicios

- Consulta de servicios.
- Registro de servicios.
- Soporte para título, descripción e imagen.

### Clientes y compras

- Registro de clientes con nombre, correo y total de compra.
- Registro de productos asociados a una compra.
- Validación para impedir que la suma de los productos supere el total asignado a la compra.
- Relación entre cada cliente y sus productos comprados.

## Tecnologías utilizadas

- Python
- Django 4.2
- Django REST Framework
- Simple JWT
- SQLite
- Django CORS Headers
- WhiteNoise
- Gunicorn

## Estructura del proyecto

```text
APIs/       Configuración general y rutas principales
users/      Usuarios, registro, acceso y autenticación JWT
products/   Productos disponibles para el frontend
blog/       Publicaciones del blog
services/   Servicios e imágenes
tickets/    Clientes, compras y validación de importes
media/      Archivos multimedia
manage.py   Utilidad de administración de Django
```

## Endpoints

Todos los endpoints de la aplicación comienzan con `/api/`.

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/api/users/` | Registrar un usuario |
| POST | `/api/users/login/` | Validar nombre o correo y contraseña |
| POST | `/api/users/profile/` | Consultar un usuario mediante un token |
| POST | `/api/users/token/` | Obtener tokens JWT |
| POST | `/api/users/token/refresh/` | Renovar el token de acceso |
| GET, POST | `/api/products/` | Listar o crear productos |
| GET, POST | `/api/post/` | Listar o crear publicaciones |
| GET, POST | `/api/services/` | Listar o crear servicios |
| GET, POST | `/api/customers/` | Listar o crear clientes |
| GET, POST | `/api/purchases/` | Listar o crear compras |

El proyecto también incluye el panel de administración de Django en `/admin/`.

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Evangelistabv/APIs.git
cd APIs
```

### 2. Crear y activar un entorno virtual

Linux o macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

Los modelos de blog y servicios utilizan `ImageField`. Si el entorno indica que falta soporte para imágenes, instala Pillow:

```bash
python -m pip install Pillow
```

### 4. Preparar la base de datos

```bash
python manage.py migrate
```

Opcionalmente, crea un usuario administrador:

```bash
python manage.py createsuperuser
```

### 5. Iniciar el servidor

```bash
python manage.py runserver
```

La API estará disponible en [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

## Ejemplos de uso

### Crear un producto

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Producto de ejemplo","price":"99.90"}'
```

### Consultar productos

```bash
curl http://127.0.0.1:8000/api/products/
```

### Registrar un usuario

```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"name":"usuario_demo","email":"demo@example.com","password":"cambia-esta-clave"}'
```

### Obtener tokens JWT

```bash
curl -X POST http://127.0.0.1:8000/api/users/token/ \
  -H "Content-Type: application/json" \
  -d '{"email":"demo@example.com","password":"cambia-esta-clave"}'
```

## Integración con Angular

La configuración CORS contempla un cliente Angular ejecutándose localmente. El frontend puede consumir los endpoints mediante `HttpClient`, por ejemplo:

```typescript
this.http.get<Product[]>('http://127.0.0.1:8000/api/products/');
```

Para una URL de Angular diferente, debe añadirse su origen permitido en `CORS_ALLOWED_ORIGINS`.

## Estado del proyecto

Este es un proyecto educativo. Algunas decisiones se conservaron como parte del proceso de aprendizaje y necesitan ajustes antes de utilizarse en producción:

- La configuración actual mantiene el modo de depuración activado.
- La clave secreta debe trasladarse a una variable de entorno.
- Las respuestas de usuario deben evitar exponer el campo de contraseña, incluso cuando contiene un hash.
- Los listados de clientes y compras están configurados actualmente con conjuntos de consulta vacíos.
- Las dependencias deberían fijar versiones compatibles para permitir instalaciones reproducibles.
- La configuración de seguridad, permisos y CORS debe revisarse antes de un despliegue público.

## Autor

**Daniel Evangelista** — [Evangelistabv en GitHub](https://github.com/Evangelistabv)

Proyecto realizado para aprender Django REST Framework y su integración con una aplicación Angular.
