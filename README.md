#Prueba Técnica – Integración API REST 3.0 de Khipu (DemoBank)

## Descripción

Este proyecto demuestra la integración real con la **API REST 3.0 de Khipu**, utilizando una cuenta en modo desarrollador, para generar cobros de hasta $5.000 CLP en el entorno de pruebas DemoBank.  
Toda la integración se realiza exclusivamente vía API, sin creación de pagos manuales en el portal.

---

## Estructura del proyecto

```
khipu_api_demo/
│
├── app.py                # Backend en Python/Flask
├── requirements.txt      # Dependencias
├── .env.example          # Variables de entorno de ejemplo
├── README.md             # Este archivo
└── evidencias/           # Capturas del proceso de integración
```

---

## Variables de entorno

Crea un archivo `.env` en la raíz del proyecto con tu API Key de Khipu:

```
KHIPU_API_KEY=tu_api_key_de_desarrollo
```

*No incluyas el `.env` real en tu repositorio.*

---

## Instalación y ejecución

1. Clona el repositorio.
2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate          # En Windows
    # source venv/bin/activate     # En Mac/Linux
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Crea el archivo `.env` con tu API Key de desarrollador.
5. Ejecuta el backend:
    ```bash
    flask run
    ```
6. El servicio quedará disponible en:  
   `http://127.0.0.1:5000/`

---

## Uso con Postman

**Endpoint:**  
`POST http://127.0.0.1:5000/crear-pago`

**Body (JSON):**
```json
{
  "subject": "Pago prueba integración Khipu",
  "amount": 4990,
  "transaction_id": "tx-khipu-001",
  "return_url": "https://micliente.com/ok",
  "cancel_url": "https://micliente.com/cancel",
  "notify_url": "https://micliente.com/webhook"
}
```

**Respuesta exitosa:**  
```json
{
  "app_url": "khipu://pos/xxxxxxxxxxxx",
  "payment_id": "xxxxxxxxxxxx",
  "payment_url": "https://khipu.com/payment/info/xxxxxxxxxxxx",
  "ready_for_terminal": false,
  "simplified_transfer_url": "https://app.khipu.com/payment/simplified/xxxxxxxxxxxx",
  "transfer_url": "https://khipu.com/payment/manual/xxxxxxxxxxxx"
}
```

Abre el `payment_url` en tu navegador para simular el pago con DemoBank.

---

## Evidencia de integración

Las capturas están disponibles en la carpeta `/evidencias/`:

- `01-cuenta-dev-khipu.png`: Creación de la cuenta en modo desarrollador
- `02-llave-api-khipu.png`: Generación de la API Key de pruebas
- `03-postman-200ok.png`: Ejecución exitosa vía API (200 OK)
- `04-flujo-pago.png`: (Opcional) Flujo completo de pago en DemoBank

---

## Observaciones y recomendaciones

- Se utiliza la **API REST 3.0** de Khipu:  
  `https://payment-api.khipu.com/v3/payments`
- Autenticación mediante header `x-api-key`
- Todo el flujo de pago se realiza por API (no manual)
- Para ambiente productivo solo debes cambiar la API Key por la real
- Usa `.env.example` y **nunca** subas tu `.env` real

---

## Contacto

Si tienes dudas técnicas o sugerencias, puedes contactarme por GitHub.

---

**¡Gracias por revisar la prueba!**"# Api_demo" 
