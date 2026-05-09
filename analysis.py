import fitparse
import pandas as pd
import matplotlib.pyplot as plt

## El script que voy a construir es para cargar el archivo 
## limpiar datos, cargar y convertir los datos 
## 4. Resumen en consola
## Imprime las métricas clave directamente en la terminal: FC media, FC máxima, distancia, velocidad.
## 5. Gráficos Genera dos gráficos apilados: FC arriba, velocidad abajo. 
# Los guarda como imagen PNG en tu carpeta.
#  Exportar CSV Guarda todos los datos en un archivo Excel-compatible. 
# Útil para análisis posteriores o para mostrarle a un cliente.

## Autor: Diego Medina 
## 8 de mayo de 2026

# 1. CARGAR EL ARCHIVO 
fitfile = fitparse.FitFile("22035011625_ACTIVITY.fit")

# 2. Extraer datos y guardo en datos 
registros = []

for record in fitfile.get_messages("record"):
    datos = {}
    for field in record:
        datos[field.name] = field.value
    registros.append(datos)

# 3. Creamos Dataframe 
df= pd.DataFrame(registros)
print(df.columns.tolist())

 #4. Limpiar y convertir datos 
if "speed" in df.columns:
    df["velocidad_kmh"]=df["speed"]*3.6
if "distance" in df.columns:
    df["distancia_km"] = df["distance"] / 1000
# Resumen en consola 
print("=== RESUMEN DE ACTIVIDAD ===")
if "heart_rate" in df.columns:
    print(f"FC media:              {df['heart_rate'].mean():.0f} bpm")
    print(f"FC máxima:             {df['heart_rate'].max():.0f} bpm")
if "distancia_km" in df.columns:
    print(f"Distancia:             {df['distancia_km'].max():.2f} km")
if "velocidad_kmh" in df.columns:
    print(f"Velocidad media:       {df['velocidad_kmh'].mean():.1f} km/h")
if "enhanced_altitude" in df.columns:
    print(f"Altitud máxima:        {df['enhanced_altitude'].max():.0f} m")
if "cadence" in df.columns:
    print(f"Cadencia media:        {df['cadence'].mean():.0f} spm")
if "step_length" in df.columns:
    print(f"Longitud de zancada:   {df['step_length'].mean():.0f} mm")
if "vertical_oscillation" in df.columns:
    print(f"Oscilación vertical:   {df['vertical_oscillation'].mean():.1f} mm")
if "vertical_ratio" in df.columns:
    print(f"Ratio vertical:        {df['vertical_ratio'].mean():.1f} %")

# graficos 

fig, axes = plt.subplots(3, 1, figsize=(12, 10))

if "heart_rate" in df.columns:
    axes[0].plot(df["heart_rate"], color="red", linewidth=0.8)
    axes[0].set_title("Frecuencia Cardíaca")
    axes[0].set_ylabel("bpm")
    axes[0].grid(True, alpha=0.3)

if "velocidad_kmh" in df.columns:
    axes[1].plot(df["velocidad_kmh"], color="blue", linewidth=0.8)
    axes[1].set_title("Velocidad")
    axes[1].set_ylabel("km/h")
    axes[1].grid(True, alpha=0.3)

if "cadence" in df.columns:
    axes[2].plot(df["cadence"], color="green", linewidth=0.8)
    axes[2].set_title("Cadencia")
    axes[2].set_ylabel("spm")
    axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("resultado.png", dpi=150)
plt.show()
print("Gráfico guardado como resultado.png")

# Exportar a CSV 
df.to_csv("datos_actividad.csv", index=False)
print("Datos exportados a datos_actividad.csv")