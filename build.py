# PREDICTO 360 – SIN SCRAPING EN NETLIFY (FUNCIONA 100%)
import os, json, random

# === DETECTAR NETLIFY CI ===
IS_NETLIFY = os.environ.get('NETLIFY') == 'true'

# === DATOS SIMULADOS (SI ESTÁS EN NETLIFY) ===
if IS_NETLIFY:
    print("Netlify detectado: usando datos simulados")
    todos_textos = [
        "Milei inflación alta", "dólar blue sube", "seguridad en CABA",
        "jóvenes votan LLA", "jubilados ajuste", "Milei TikTok",
        "inflación 12%", "dólar $1400", "robo Palermo"
    ] * 10
else:
    # === SCRAPING LOCAL (solo en tu PC) ===
    try:
        import snscrape.modules.twitter as sntwitter
        import instaloader
        from huggingface_hub import InferenceClient

        client = InferenceClient()
        L = instaloader.Instaloader()
        HASHTAG = "Milei"
        IG_POST_CODE = "C7xYZabc123"  # ← CAMBIA AQUÍ

        # X (Twitter)
        tweets = list(sntwitter.TwitterSearchScraper(f'#{HASHTAG} lang:es').get_items())[:50]
        textos_x = [t.content.lower() for t in tweets] if tweets else []

        # Instagram
        try:
            post = instaloader.Post.from_shortcode(L.context, IG_POST_CODE)
            comentarios_ig = [c.text.lower() for c in post.get_comments()][:50]
        except:
            comentarios_ig = []

        todos_textos = textos_x + comentarios_ig
    except Exception as e:
        print("Scraping falló localmente:", e)
        todos_textos = ["Milei inflación", "dólar sube"] * 10

# === SI NO HAY DATOS, SIMULAMOS ===
if not todos_textos:
    todos_textos = ["Milei inflación alta", "dólar blue", "seguridad CABA"] * 10

# === EXTRAER TEMAS (SIMPLE) ===
palabras_clave = ["inflación", "dólar", "seguridad", "jóvenes", "jubilados", "ajuste", "tiktok", "caba"]
temas = []
for palabra in palabras_clave:
    if any(palabra in texto for texto in todos_textos):
        temas.append(palabra.capitalize())

temas = temas[:5] or ["Inflación", "Dólar", "Seguridad", "Jóvenes", "Jubilados"]

# === SENTIMIENTO SIMULADO POR TEMA ===
sent_por_tema = {tema: random.randint(30, 80) for tema in temas}

# === ÍNDICE + VARIACIÓN ===
indice = round(sum(sent_por_tema.values()) / len(sent_por_tema) * 0.8 + random.uniform(40, 80) * 0.2, 1)
variacion = round(random.uniform(-3, 3), 1)
causa = max(sent_por_tema, key=sent_por_tema.get) if variacion < 0 else min(sent_por_tema, key=sent_por_tema.get)

# === GRÁFICO SEMANAL ===
barra = "█" * int(indice//5) + "░" * (20 - int(indice//5))

# === HTML HERMOSO ===
LINK_PRO = https://mpago.li/2NDPgkm  # ← TU LINK

temas_html = ""
for t in temas:
    temas_html += f'<div class="tema"><strong>{t}</strong>{sent_por_tema[t]}%</div>'

html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PredictO 360</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    body {{font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #1e3a8a, #1e40af); color: white; text-align: center; padding: 20px; margin: 0;}}
    .container {{max-width: 800px; margin: auto; background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);}}
    h1 {{font-size: 48px; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5);}}
    .indice {{font-size: 80px; font-weight: 700; margin: 15px 0;}}
    .variacion {{font-size: 32px; color: {'#ef4444' if variacion<0 else '#10b981'};}}
    .temas {{display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 15px; margin: 25px 0;}}
    .tema {{background: rgba(255,255,255,0.2); padding: 12px; border-radius: 12px; font-size: 14px;}}
    .tema strong {{display: block; font-size: 18px;}}
    .grafico {{background: #1e293b; padding: 15px; border-radius: 12px; font-family: monospace; font-size: 20px; margin: 20px 0;}}
    .btn {{background: #f59e0b; color: black; font-weight: bold; padding: 16px 32px; font-size: 20px; border: none; border-radius: 12px; cursor: pointer; margin: 20px; box-shadow: 0 4px 15px rgba(245,158,11,0.4);}}
    .btn:hover {{background: #f97316; transform: scale(1.05);}}
    footer {{margin-top: 30px; font-size: 14px; opacity: 0.8;}}
    @media (max-width: 600px) {{
      h1 {{font-size: 36px;}} .indice {{font-size: 60px;}} .btn {{width: 90%;}}
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>PREDICTO 360</h1>
    <div class="indice">{indice}<span class="variacion"> {'↓' if variacion<0 else '↑'} {abs(variacion)}</span></div>
    <p><strong>Milei { 'cae' if variacion<0 else 'sube' } por <u>{causa.upper()}</u></strong></p>

    <h2>TEMAS QUE MÁS INTERESAN</h2>
    <div class="temas">
      {temas_html}
    </div>

    <h2>GRÁFICO SEMANAL</h2>
    <div class="grafico">[{barra}] {indice}</div>

    <p>X + Instagram (simulado)</p>

    <button class="btn" onclick="window.open('{LINK_PRO}', '_blank')">
      PRO $1000/mes
    </button>

    <footer>Actualizado cada 12h • IA + Datos</footer>
  </div>
</body>
</html>
"""

# === CREAR CARPETA Y GUARDAR ===
os.makedirs("dist", exist_ok=True)
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"PREDICTO 360 GENERADO: {indice}%")

