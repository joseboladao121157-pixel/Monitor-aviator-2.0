import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

TOKEN = "9047998790:AAFtkfnemjR1kzvP6rHDvGP53XXIZ1kHWio"
CHAT_ID = "8691122425"

@app.route('/')
def home():
    return "Servidor online 24h!"

def enviar_mensagem(texto):
    url = f"https://telegram.org{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": texto})

def monitoramento():
    enviar_mensagem("🚀 Sistema conectado! Seu monitor 24h já está ativo no celular.")
    while True:
        time.sleep(15)

if __name__ == "__main__":
    threading.Thread(target=monitoramento, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
