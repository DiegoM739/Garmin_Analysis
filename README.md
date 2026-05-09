# Garmin Activity Analysis

Análisis automatizado de datos de entrenamiento desde archivos `.fit` de Garmin usando Python.

## ¿Qué hace?

- Lee archivos `.fit` exportados desde Garmin Connect
- Extrae métricas de rendimiento y biomecánica de carrera
- Genera gráficos de FC, velocidad y cadencia
- Exporta todos los datos a CSV para análisis posterior

## Métricas analizadas

| Métrica | Descripción |
|---|---|
| Frecuencia cardíaca | Media y máxima en bpm |
| Velocidad | Conversión automática a km/h |
| Cadencia | Pasos por minuto |
| Oscilación vertical | Movimiento vertical en mm |
| Ratio vertical | Eficiencia de carrera en % |
| Longitud de zancada | En mm |

## Tecnologías

- Python 3.13
- fitparse
- pandas
- matplotlib

## Autor

Diego Medina — Fisioterapeuta y estudiante de Ingeniería en Software  
Especialidad: análisis de datos aplicado a salud y rendimiento deportivo
