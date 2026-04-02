import requests
import pandas as pd
import random


SDW_API = 'https://sdw-2023-prd.up.railway.app'

NOMES = ["Wellington Oliveira", "Ana Silva", "Bruno Souza", "Carla Dias", "Diego Santos"]

def montar_usuario(uid):
    nome = NOMES[(uid - 1) % len(NOMES)] if uid <= len(NOMES) else f"Cliente {uid}"

    return {
        "id": uid,
        "name": nome,
        "account": {
            "id": uid,
            "number": f"01.{str(uid).zfill(6)}-4",
            "agency": "2030",
            "balance": round(random.uniform(100.0, 5000.0), 2),
            "limit": 1000
        },
        "card": {
            "id": uid,
            "number": f"xxxx xxxx xxxx {random.randint(1000, 9999)}",
            "limit": random.choice([1000, 2000, 5000])
        },
        "features": [
            {"id": 1, "icon": "pix.svg",  "description": "PIX"},
            {"id": 2, "icon": "pay.svg", "description": "Pagar"}
        ],
        "news": []
    }



try:
    df = pd.read_csv('SDW2023.csv')
    ids = df['UserID'].tolist()
except Exception as e:
    print(f"Não consegui ler o CSV: {e}")
    ids = [1]

usuarios = [montar_usuario(i) for i in ids]
print(f"{len(usuarios)} usuário(s) carregado(s).\n")



print("Gerando mensagens...")

for u in usuarios:
    nome = u['name']
    saldo = u['account']['balance']
    limite = u['card']['limit']
    final = u['card']['number'].split()[-1]

    if saldo > 2000:
        msg = f"Olá {nome}! Seu saldo de R${saldo:.2f} tá parado. Que tal investir e liberar mais limite no cartão final {final}?"
    elif limite > 3000:
        msg = f"Ei {nome}, seu cartão com limite de R${limite} é VIP! Use hoje e garanta cashback nas compras."
    else:
        msg = f"{nome}, com seu saldo atual e limite de R${limite} dá pra montar uma reserva de emergência. Vale pensar."

    u['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/pi-credit-card.svg",
        "description": msg
    })

    print(f"  {nome}: {msg}")