import requests
from bs4 import BeautifulSoup
import pandas as pd
import snscrape.modules.twitter as sntwitter
from huggingface_hub import InferenceClient
import os

# 1. INFLACIÓN INDEC
def get_inflacion():
    try:
        url = "https://www.indec.gob.ar/ftp/cuadros/economia/ipc_22_25.xlsx"
        df = pd.read_excel(url, sheet_name='IPC Nacional')
        return df['Variación mensual'].iloc[-1]
    except:
        return 12.5

# 2. DÓLAR BLUE
def get_dolar_blue():
    try:
        soup = BeautifulSoup(requests.get("https://dolarhoy.com").text, 'html.parser')
        return float(soup.find('div', class_='tile is-child').find('div', class_='value').text.replace('$','').replace('.','').replace(',','.'))
    except:
        return 1400

# 3. SENTIMIENTO X
def get_sentimiento():
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper("#Milei OR #Kicillof lang:es").get_items()):
        if i >= 50: break
        tweets.append(tweet.rawContent.lower())
    pos = sum(1 for t in tweets if any(w in t for w in ['bueno','genial','apoyo']))
    return (pos / len(tweets)) * 100 if tweets else 60

# 4. PREDICCIÓN
infl = get_inflacion()
dol = get_dolar_blue()
sent = get_sentimiento()
indice = 100 - (infl * 0.7) - (dol / 100) + (sent * 0.3)

# 5. EXPLICACIÓN Llama 3.1
try:
    client = InferenceClient(model="meta-llama/Meta-Llama-3.1-8B-Instruct")
    explic = client.text_generation(
        f"Explicá en 1 frase por qué Milei tiene {indice:.1f}%: inflación {infl}%, dólar ${dol}, X {sent:.0f}%",
        max_new_tokens=50
    ).split('\n')[0]
except:
    explic = "Milei se mueve por inflación y dólar."

# 6. HTML
html = f'''<!DOCTYPE html>
<html><head><title>PREDICTO 360</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{{font-family:Arial;background:#1e3c72;color:white;text-align:center;padding:40px;}}.card{{background:rgba(255,255,255,0.1);padding:30px;border-radius:20px;max-width:500px;margin:auto;}}.indice{{font-size:70px;color:#ff5252;}}</style></head>
<body><div class="card"><h1>PREDICTO 360</h1><div class="indice">{indice:.1f} {"↓" if indice < 68 else "↑"}</div><p><strong>{explic}</strong></p>
<a href=https://mpago.li/2NDPgkm style="background:#00c853;color:white;padding:16px;border-radius:12px;text-decoration:none;display:block;margin:15px;">PRO $500/mes</a>
<a href="TU_LINK_DONACION" style="background:#ff9800;color:white;padding:16px;border-radius:12px;text-decoration:none;display:block;margin:15px;">APOYANOS $500</a>
</div></body></html>'''

os.makedirs('dist', exist_ok=True)
with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("¡HTML generado!")
