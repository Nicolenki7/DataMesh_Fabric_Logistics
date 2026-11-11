# Ruta abierta · qué queda y qué falta

## Estado original (se conserva)

Este proyecto se construyó en **Microsoft Fabric** con arquitectura Data Mesh multi-dominio.
La evidencia sigue en el repositorio: `01_Architecture_and_Ingestion/Ingestion.py`, el modelo semántico
(`02_Data_Modeling_and_DAX/DAX_Measures.dax`), el dashboard (`Dashboard Logística en DataMesh.pbix`),
el PDF ejecutivo y las capturas de arquitectura y linaje.

Ese trabajo es real y está documentado. Lo que cambió es el acceso al entorno.

## Por qué no hay un port ejecutable todavía

El repositorio **no versiona datos**: el dataset vive en OneLake y se accede por Shortcuts.
Un modelo sin datos no se puede ejecutar, y publicar consultas que nunca corrieron sería vender humo.
Ese es el bloqueo, y es explícito.

## Camino concreto para reabrirlo

1. **Exportar un extracto** de cada dominio a Parquet o CSV (unas 10-50 mil filas alcanzan para demostrar el diseño).
2. **Reconstruir el modelo** con `dbt` sobre DuckDB: `models/staging`, `models/marts`, y un `sources.yml`
   por dominio. El `.dax` existente es la especificación de las métricas; se traduce a SQL.
3. **Calidad por dominio**: un test por fuente (`unique`, `not_null`, `relationships`) más un test de contrato
   que falle si cambia el esquema, como en `ETL_Egatur_INE_Esp`.
4. **Orquestación**: Dagster o Airflow con una partición por dominio, respetando la idea de ownership del Data Mesh.
5. **Visualización**: Superset o Metabase sobre las tablas de `marts`.

## Referencia ya funcionando

`Tech_GlobalStore_Retail_Analysis-Fabric` tiene este mismo ejercicio resuelto y verificado:
carpeta `stack-abierto/` con un esquema estrella en DuckDB, cuatro vistas de KPIs y siete controles de calidad
que devuelven código de error si el dato cambia. Ese es el patrón a replicar acá.

## Qué se mantiene igual

El diseño de dominios, el linaje y la gobernanza son decisiones, no herramientas.
Eso no se pierde al cambiar Fabric por DuckDB, dbt y Superset.
