# 🚀 Data Mesh en Microsoft Fabric: Análisis Unificado para Logística y Gobernanza

## 📌 Introducción

Este proyecto demuestra la implementación exitosa de una arquitectura **Data Mesh** en **Microsoft Fabric** para resolver la fragmentación de datos de una compañía que gestiona envíos con múltiples operadores logísticos (DHL, FedEx, UPS, LocalPost).

El objetivo fue unificar el análisis de tres dominios de negocio dispares (Transacciones, Logística y Gobernanza) en un único **Modelo Semántico**, permitiendo un análisis híbrido de datos de **Lote** y **Near Real-Time** (Casi en Tiempo Real).

---

## 🏗️ Arquitectura del Data Mesh en Fabric

Se establecieron tres **Productos de Datos (Dominios)** independientes, consumidos de forma centralizada sin duplicación masiva de datos.

### 1. Los Dominios de Datos (Productos)

| Dominio | Contenido | Valor de Negocio | Tecnología de Origen |
| :--- | :--- | :--- | :--- |
| **D1: Transacciones** | Registros de Ventas e Ingresos. | Datos de lote (Históricos). | **Lakehouse** (Delta Lake) |
| **D2: Logística** | Estado, Operador (`Carrier`), Tiempo de Entrega. | Datos operativos (Near Real-Time). | **KQL Database (Eventhouse)** |
| **D3: Gobernanza** | Logs del sistema y Cumplimiento de SLA. | Datos de calidad y riesgo (Near Real-Time). | **KQL Database (Eventhouse)** |

### 2. Eje Central de Gobernanza y Consumo

El proceso clave de Ingeniería de Datos se centró en la creación de un **Lakehouse de Consumo** (D4) que actúa como la capa de gobernanza.

* **Ingesta (KQL):** Los datos de Logística (D2) y Gobernanza (D3) se ingirieron directamente en las bases de datos KQL para manejar el alto volumen y la velocidad.
* **Zero-Copy con OneLake Shortcuts:** Para evitar copiar datos, se utilizaron **OneLake Shortcuts** dentro del Lakehouse de consumo (D4). Estos *shortcuts* apuntan directamente a los datos de origen en KQL, garantizando que el análisis siempre esté actualizado con la información casi en tiempo real.
* **Modelo Semántico:** Se creó el **Modelo de Datos** de Power BI a partir de este Lakehouse de consumo, estableciendo las relaciones clave entre los tres dominios para permitir consultas complejas (ej: relacionar fallos de SLA (D3) con una venta específica (D1)).

---

## 📊 Dashboard y Valor Analítico: El Eje de la Experiencia

El dashboard final es el resultado de superar los desafíos de visualización y latencia de la plataforma, transformando los datos en métricas accionables.

### 1. Medidas DAX y KPIs Clave
El modelo semántico incluye las métricas fundamentales para la auditoría y estrategia:
* `[Tiempo Promedio Entrega (días)]`
* `[Tasa Incumplimiento SLA]`
* `[Total Envíos]`

### 2. Ajustes de Interfaz y Usabilidad (Ingeniería de BI)
* **Corrección de Rendimiento:** Se resolvió el problema de latencia de los *shortcuts* de KQL para asegurar la sincronización de datos.
* **Comunicación de Datos:** Se ajustó el Eje Y de los gráficos de eficiencia para **magnificar las pequeñas diferencias** entre los operadores logísticos (ej: ajuste de rango de 6 a 7 días).
* **Tendencia Clara:** Se configuró el Eje X del gráfico de líneas como **Continuo/Categórico** con formato `MMM-yy` para obtener una línea de tendencia limpia, eliminando el ruido.

### 3. Visualizaciones Clave y Segmentador

| Visualización | Dominios Integrados | Valor de Negocio |
| :--- | :--- | :--- |
| **Mapa de Ventas** | D1 + D2 | Estrategia de inventario y demanda por región de entrega. |
| **Auditoría SLA** | D1 + D3 | Riesgo tecnológico: correlación entre fallas del sistema y métodos de pago. |
| **Rendimiento Operadores** | D2 | Auditoría de costos y eficiencia (¿Quién es el operador más rápido?). |
| **Tendencia Histórica** | D2 | Planificación: ¿La eficiencia de entrega está mejorando o empeorando con el tiempo? |

El **Segmentador de Operador Logístico** permite a los usuarios filtrar todo el análisis para auditar el rendimiento de un único `Carrier`.

---

## 🖼️ Resultado Final del Dashboard

Puedes ver la interfaz y el diseño final del dashboard en la siguiente imagen:


**Enlace a la imagen en este repositorio:** https://github.com/Nicolenki7/DataMesh_Fabric_Logistics/blob/9553fe4f96897b9ea14ff138f717606fec1f1f4f2e/dashboard%20datamesh_foto.png

## 🔗 Demo Interactiva

Accede a la experiencia interactiva de Power BI en Fabric:

[**Acceder al Dashboard en Fabric**](https://app.fabric.microsoft.com/reportEmbed?reportId=75459c29-c7dd-404b-b4e2-f4a256e3a6a8&autoAuth=true&ctid=5153b8f5-97d1-4e1b-827f-2fb1bad4128f&actionBarEnabled=true&reportCopilotInEmbed=true)
