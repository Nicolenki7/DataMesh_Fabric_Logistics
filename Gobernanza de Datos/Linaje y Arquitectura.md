# 🗺️ Linaje de Datos y Arquitectura de la Malla (Data Mesh)

Este documento explica el flujo de datos del proyecto y el propósito de cada conexión, tal como se visualiza en el diagrama de Linaje de Microsoft Fabric.

## 1. Definición de Nodos de Origen (Dominios)

El diagrama de linaje muestra tres fuentes de origen distintas:

| Nombre del Origen | Propósito | Tecnología | Flujo de Datos |
| :--- | :--- | :--- | :--- |
| **D1: Transacciones** | Ventas e ingresos. | Lakehouse | Lote (Batch) |
| **D2: Logística** | Movimiento de envíos. | KQL Database | Near Real-Time |
| **D3: Gobernanza** | Logs de cumplimiento SLA. | KQL Database | Near Real-Time |

## 2. La Conexión Central (OneLake Shortcuts)

El diagrama muestra que el **Lakehouse de Consumo (D4)** no recibe datos por *pipeline*, sino por conexión directa.

* **Conexión:** Las tablas de D2 y D3 (KQL) están conectadas a D4 (Lakehouse) mediante **OneLake Shortcuts**.
* **Ventaja:** Esta técnica de "Zero-Copy" evita duplicar los datos. El Linaje demuestra que el modelo semántico está leyendo los datos de Logística **directamente desde la fuente KQL** (a través del Shortcut), garantizando actualidad y minimizando el costo de almacenamiento.

## 3. Modelo Semántico y Consumo Final

* **Nodo:** Modelo Semántico de Power BI (el cubo de datos).
* **Dependencia:** Este nodo consume datos de las tablas unificadas en D4. El linaje confirma que cualquier cambio en la base de datos KQL (D2) se propagará a través del Shortcut, actualizando el Modelo Semántico y, finalmente, el Dashboard de Power BI.

## Conclusión

El diagrama de linaje confirma que la arquitectura **Data Mesh** se implementó correctamente, manteniendo la descentralización de los dominios mientras se logra un punto central de análisis gobernable (D4 Lakehouse).
