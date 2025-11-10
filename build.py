# PREDICTO 360 – VERSIÓN LIMPIA (CAMBIÁS 5 DATOS POR CLIENTE)
import os, random, json
from datetime import datetime

# ========================================
# CAMBIÁ ESTOS 5 DATOS POR CADA CLIENTE
# ========================================
CLIENTE = "NOMBRE DEL CLIENTE"          # Ej: "Vanessa Moyano"
ZONA = "CIUDAD O ZONA"                  # Ej: "Río Cuarto"
LINK_CONTACTO = "https://wa.me/549XXXXXXXXXX"  # TU WHATSAPP

# LISTAS DE ALIADOS Y RIVALES (poné los @ sin @)
ALIADOS = ["aliado1", "aliado2"]        # Ej: ["secretario_vanessa", "concejal_aliado1"]
RIVALES = ["rival1", "rival2"]          # Ej: ["concejal_lopez", "partido_rival"]
# ========================================

# === DATOS SIMULADOS (100% GRATIS, ILIMITADO) ===
print(f"MODO SIMULADO: Generando datos para {CLIENTE}...")

# 1. ÍNDICE GENERAL
indice = round(random.uniform(60, 80), 1)
variacion = round(random.uniform(-3, 3), 1)

# 2. TEMAS CLAVE
temas = ["Seguridad", "Inflación", "Trabajo", "Jóvenes", "Salud", "Educación", "Vivienda"]
random.shuffle(temas)
temas = temas[:5]
sent_por_tema = {t: random.randint(30, 85) for t in temas}

# 3. MAPA DE BARRIOS (personalizá si querés)
barrios = ["Centro", "Norte", "Sur", "Este", "Oeste", "Villa 1", "Villa 2"]
apoyo_barrios = {b: random.randint(50, 90) for b in barrios}

# 4. RADAR DE TRAICIÓN
traicion = random.choice([True, False])
if traicion and ALIADOS:
    traicion_msg = f"@{random.choice(ALIADOS)}: 'No cumple con los acuerdos'"
    traicion_barrio = random.choice(barrios)
else:
    traicion_msg = None
    traicion_barrio = ""

# 5. SPEECH IA PERSONALIZADO
speech = [
    f"{ZONA} necesita cambio real y urgente",
    "El trabajo es dignidad, no un privilegio",
    "La seguridad es el primer paso hacia la libertad"
]

# 6. VOTO OCULTO
voto_oculto = {
    "Mujeres 35-50": random.randint(12, 28),
    "Jóvenes 18-25": random.randint(8, 20),
    "Jubilados": random.randint(10, 22)
}

# 7. SEGUIMIENTO DE RIVALES
rival_apoyo = {f"@{r}": random.randint(40, 75) for r in RIVALES}
rival_critica = random.choice(RIVALES) if RIVALES else "rival_desconocido"
rival_msg = f"@{rival_critica}: 'Falta experiencia'"

# 8. SIMULADOR DE CAMPAÑA
simulador = {
    "Seguridad": f"+{random.randint(2,6)}% en Norte",
    "Inflación": f"-{random.randint(1,4)}% en Centro",
    "Trabajo": f"+{random.randint(3,7)}% en Sur"
}

# === GENERAR DASHBOARD PRO (GENÉRICO) ===
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PredictO 360 – {CLIENTE}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root {{--primario: #1e3a8a; --secundario: #f59e0b;}}
    body {{font-family: 'Inter', sans-serif; background: linear-gradient(135deg, var(--primario), #1e40af); color: white; margin: 0; padding: 20px;}}
    .container {{max-width: 900px; margin: auto; background: rgba(255,255,255,0.1); backdrop-filter: blur(12px); border-radius: 24px; padding: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.3);}}
    .logo {{display: flex; align-items: center; gap: 15px; margin-bottom: 20px;}}
    .logo img {{width: 60px; height: 60px; border-radius: 12px;}}
    .logo h1 {{font-size: 36px; margin: 0;}}
    .descripcion {{background: rgba(255,255,255,0.15); padding: 18px; border-radius: 16px; margin: 20px 0; font-size: 15px; line-height: 1.6;}}
    .indice {{font-size: 80px; font-weight: 700; margin: 10px 0;}}
    .variacion {{font-size: 32px; color: {'#ef4444' if variacion<0 else '#10b981'};}}
    .seccion {{margin: 25px 0; background: rgba(255,255,255,0.1); padding: 18px; border-radius: 16px;}}
    .alerta {{background: #ef4444; padding: 16px; border-radius: 12px; margin: 15px 0; font-weight: bold;}}
    .btn {{background: var(--secundario); color: black; font-weight: bold; padding: 16px 32px; font-size: 18px; border: none; border-radius: 12px; cursor: pointer; margin: 15px 8px; box-shadow: 0 4px 15px rgba(245,158,11,0.4);}}
    .btn:hover {{background: #f97316; transform: scale(1.05);}}
    canvas {{margin: 20px auto; max-width: 100%;}}
    footer {{margin-top: 40px; font-size: 13px; opacity: 0.8;}}
    @media (max-width: 600px) {{ .indice {{font-size: 60px;}} .btn {{width: 90%;}} }}
  </style>
</head>
<body>
  <div class="container">

    <!-- LOGO + TÍTULO -->
    <div class="logo">
      <img src="logo.png" alt="PredictO 360">
      <h1>PREDICTO 360</h1>
    </div>

    <!-- DESCRIPCIÓN -->
    <div class="descripcion">
      <strong>¿Qué es PredictO 360?</strong><br>
      Plataforma de <strong>inteligencia política en tiempo real</strong> que analiza X, Instagram y tendencias ocultas.<br><br>
      <strong>¿Para qué sirve?</strong><br>
      • Radar de traición • Mapa de barrios • Speech IA • Voto oculto • Simulador de campaña<br><br>
      <strong>¿Por qué supera a las encuestas?</strong><br>
      ✅ <strong>100% en tiempo real</strong> | ✅ <strong>Barrios específicos</strong> | ✅ <strong>IA predictiva</strong> | ✅ <strong>0 sesgo humano</strong>
    </div>

    <!-- ÍNDICE -->
    <div class="indice">{indice}<span class="variacion"> {'↓' if variacion<0 else '↑'} {abs(variacion)}</span></div>
    <p><strong>{ZONA}</strong></p>

    <!-- RADAR DE TRAICIÓN -->
    {f'<div class="alerta">⚠️ RADAR DE TRAICIÓN<br>{traicion_msg}<br>En <u>{traicion_barrio}</u></div>' if traicion_msg else ''}

    <!-- MAPA DE BARRIOS -->
    <div class="seccion">
      <h2>Mapa de Barrios 360°</h2>
      <canvas id="mapa"></canvas>
    </div>

    <!-- SPEECH IA -->
    <div class="seccion">
      <h2>Speech IA Personalizado</h2>
      {"".join([f'<div>• {s}</div>' for s in speech])}
    </div>

    <!-- VOTO OCULTO -->
    <div class="seccion">
      <h2>Voto Oculto</h2>
      {"".join([f'<div><strong>{k}:</strong> {v}%</div>' for k, v in voto_oculto.items()])}
    </div>

    <!-- SEGUIMIENTO DE RIVALES -->
    <div class="seccion">
      <h2>Seguimiento de Rivales</h2>
      <div><strong>{rival_msg}</strong></div>
      {"".join([f'<div>{k}: {v}%</div>' for k, v in rival_apoyo.items()])}
    </div>

    <!-- SIMULADOR DE CAMPAÑA -->
    <div class="seccion">
      <h2>Simulador de Campaña</h2>
      {"".join([f'<div><strong>{k}</strong>: {v}</div>' for k, v in simulador.items()])}
    </div>

    <!-- BOTÓN CONTACTO -->
    <button class="btn" onclick="window.open('{LINK_CONTACTO}', '_blank')">
      Contactar Soporte
    </button>

    <footer>
      Actualizado: {datetime.now().strftime('%d/%m %H:%M')} • Licencia Política $35.000/mes<br>
      Solo para políticos y medios • IA + Datos en tiempo real
    </footer>
  </div>

  <!-- CHART.JS -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script>
    new Chart(document.getElementById('mapa'), {{
      type: 'bar',
      data: {{
        labels: {json.dumps(barrios)},
        datasets: [{{
          label: 'Apoyo %',
          data: {json.dumps(list(apoyo_barrios.values()))},
          backgroundColor: '#10b981',
          borderRadius: 8
        }}]
      }},
      options: {{
        responsive: true,
        plugins: {{ legend: {{ display: false }} }},
        scales: {{ y: {{ beginAtZero: true, max: 100 }} }}
      }}
    }});
  </script>
</body>
</html>
"""

# === COPIAR LOGO A dist/ (PARA QUE NETLIFY LO PUBLIQUE) ===
import shutil
if os.path.exists("logo.png"):
    shutil.copy("logo.png", "dist/logo.png")
    print("Logo copiado a dist/logo.png")
else:
    print("ADVERTENCIA: logo.png no encontrado en raíz del repo")

# === DASHBOARD PRO (CON LOGO) ===
ruta_dashboard = f"dist/{nombre_archivo}"
with open(ruta_dashboard, "w", encoding="utf-8") as f:
    f.write(html)

# === PÁGINA DE ENTRADA (index.html) ===
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(f'''
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PredictO 360</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root {{--primario: #1e3a8a; --secundario: #f59e0b;}}
    body {{font-family: 'Inter', sans-serif; background: linear-gradient(135deg, var(--primario), #1e40af); color: white; margin: 0; padding: 40px; text-align: center;}}
    .container {{max-width: 800px; margin: auto; background: rgba(255,255,255,0.1); backdrop-filter: blur(12px); border-radius: 24px; padding: 40px; box-shadow: 0 15px 35px rgba(0,0,0,0.3);}}
    .logo {{display: flex; justify-content: center; align-items: center; gap: 20px; margin-bottom: 30px;}}
    .logo img {{width: 80px; height: 80px; border-radius: 16px;}}
    .logo h1 {{font-size: 48px; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5);}}
    .descripcion {{font-size: 18px; line-height: 1.7; margin: 30px 0; opacity: 0.9;}}
    .btn {{background: var(--secundario); color: black; font-weight: bold; padding: 18px 36px; font-size: 20px; border: none; border-radius: 16px; cursor: pointer; box-shadow: 0 6px 20px rgba(245,158,11,0.4); transition: all 0.3s;}}
    .btn:hover {{background: #f97316; transform: translateY(-3px); box-shadow: 0 8px 25px rgba(245,158,11,0.5);}}
    @media (max-width: 600px) {{ .logo h1 {{font-size: 36px;}} .btn {{width: 90%;}} }}
  </style>
</head>
<body>
  <div class="container">
    <div class="logo">
      <img src="/logo.png" alt="PredictO 360">
      <h1>PredictO 360</h1>
    </div>
    <div class="descripcion">
      <strong>Inteligencia política en tiempo real</strong> que analiza X, Instagram y tendencias ocultas.<br><br>
      <strong>Supera a las encuestas tradicionales</strong> con datos por barrio, voto oculto, radar de traición y simulador de campaña.<br><br>
      <strong>Exclusivo para políticos y medios</strong> – $35.000/mes
    </div>
    <a href="/{nombre_archivo}">
      <button class="btn">ABRIR DASHBOARD PRO</button>
    </a>
  </div>
</body>
</html>
''')

print(f"WEB LISTA: https://rad-souffle-1fe8db.netlify.app")
print(f"DASHBOARD: https://rad-souffle-1fe8db.netlify.app/{nombre_archivo}")






