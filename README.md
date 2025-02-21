# Web Mapping de Volcanes y Población Mundial

## 📌 Descripción del Proyecto

Este proyecto consiste en la creación de un **mapa interactivo** utilizando `Folium` en Python. En este mapa se pueden visualizar:

- 🌋 **Volcanes en Estados Unidos**, con marcadores de colores según su altura.
- 🌍 **Países del mundo**, coloreados según su población total.

El objetivo principal es proporcionar una representación visual de la distribución de volcanes y la densidad poblacional.

---

## 🚀 Tecnologías y Módulos Utilizados

- 🗺️ **Folium**: Para la generación de mapas interactivos.
- 📊 **Pandas**: Para la manipulación y lectura de datos de volcanes desde un archivo CSV.
- 🌎 **GeoJSON**: Para representar la información geoespacial de los países y su población.

---

## 📂 Datos Utilizados

📌 **Volcanes:** Archivo `Volcanoes.txt` con:

- Latitud y longitud.
- Elevación (msnm).

📌 **Población Mundial:** Archivo `world.json` con:

- Datos geográficos de los países.
- Población registrada en 2005.

---

## 🌟 Características Principales

- **Volcanes**: Representados con `CircleMarkers` de colores:

  - 🟢 **Verde**: Menos de 1000 m.
  - 🟠 **Naranja**: Entre 1000 y 3000 m.
  - 🔴 **Rojo**: Más de 3000 m.

- **Países**: Coloreados según su población:

  - 🟢 **Verde**: < 10M habitantes.
  - 🟠 **Naranja**: 10M - 20M habitantes.
  - 🔴 **Rojo**: > 20M habitantes.

- **Interactividad**: Al hacer clic en un volcán o país, se muestra información detallada.

- **Control de Capas**: Permite activar o desactivar la visualización de volcanes y población.

---





