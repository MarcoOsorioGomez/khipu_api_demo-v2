from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('KHIPU_API_KEY')
BASE_URL = "https://payment-api.khipu.com/v3"

@app.route('/crear-pago', methods=['POST'])
def crear_pago():
    data = request.json
    payload = {
        "subject": data.get("subject", "Pago de prueba"),
        "amount": data.get("amount", 4990),
        "currency": "CLP",
        "transaction_id": data.get("transaction_id", "demo-tx-001"),
        "return_url": data.get("return_url", "https://micliente.com/ok"),
        "cancel_url": data.get("cancel_url", "https://micliente.com/cancel"),
        "notify_url": data.get("notify_url", "https://micliente.com/webhook")
    }

    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }

    try:
        response = requests.post(
            f"{BASE_URL}/payments",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return jsonify(response.json()), response.status_code

    except requests.exceptions.HTTPError as e:
        print("❌ Error HTTP:", e)
        print("Código:", response.status_code)
        print("Respuesta:", response.text)
        return jsonify({
            "error": "Error HTTP al llamar a Khipu",
            "detalle": response.text
        }), response.status_code

    except Exception as e:
        print("❌ Error inesperado:", e)
        return jsonify({
            "error": "Error general al procesar respuesta de Khipu"
        }), 500

@app.route('/')
def index():
    return "✅ API Khipu 3.0 activa. Usa POST /crear-pago para generar un cobro."

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
