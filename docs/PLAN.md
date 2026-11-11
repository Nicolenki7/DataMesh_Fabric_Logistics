# Plan de ejecucion

## Estado actual
- Data Mesh en Fabric: ingesta (`01_Architecture_and_Ingestion/Ingestion.py`), modelo semantico + DAX, gobernanza y linaje documentados.
- `LICENSE`, `requirements.txt` y `.gitignore` anadidos.

## Proximos pasos
1. Contrato de datos por dominio (columnas, tipos, nulos permitidos) en `contracts/`.
2. Trazabilidad: cada medida DAX debe apuntar a su columna de origen en una tabla de linaje.
3. Convertir la nota de gobernanza a Markdown con ownership por dominio.
4. Mover el `.pbix` a `docs/` y mantener el DAX como texto versionado.

## Criterio de aceptacion
- Cada dominio tiene contrato, owner y test de esquema.

## Riesgos
- Sin contratos, un cambio en origen rompe el modelo semantico sin aviso.
