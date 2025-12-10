# =========================================================
# SCRIPT PYSPARK: INGESTA DE DATOS DE LOTE (D1 - TRANSACCIONES)
# Objetivo: Cargar datos históricos de ventas en el Lakehouse
# Formato: Delta Lake (para ACID properties)
# =========================================================

# 1. Definición de la ruta de origen de los datos (simulación)
# En Fabric, esta ruta apuntaría al almacenamiento de archivos RAW (ej. un CSV/JSON cargado)
# Sustituir 'abfss://...' por la ruta de tu archivo CSV/JSON si lo tienes.
file_path = "Files/transactions/raw_sales_data.csv"

# 2. Carga del DataFrame inicial (Asumiendo que el archivo está en el Lakehouse)
try:
    df_sales = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(file_path)

    print("✅ Datos de ventas RAW cargados correctamente en DataFrame PySpark.")

except Exception as e:
    print(f"❌ Error al cargar datos: {e}")

# 3. Transformación básica (Limpieza/Selección de columnas)
# Aseguramos que la columna de fecha sea tipo Date y seleccionamos campos clave.
from pyspark.sql.functions import col, to_date

df_transformed = df_sales.withColumn("OrderDate", to_date(col("OrderDate"), "MM/dd/yyyy")) \
                         .select("TransactionID", "OrderDate", "PaymentMethod", "SalesAmount", "DeliveryID")

# 4. Ingesta Final en la Tabla Delta Lake (Tabla gestionada en el Lakehouse)
# Ruta del Lakehouse (Tables) - Aquí se crea la tabla 'transactions_raw_delta'

# Nombre del Lakehouse (Reemplazar con el nombre de tu Lakehouse)
lakehouse_name = "mylakehouse_d4_consumo"
table_name = "transactions_raw_delta"

# Definición de la ruta ABFSS en Fabric (Target)
target_path = f"Tables/{table_name}"

# Escritura del DataFrame en formato Delta Lake
df_transformed.write.format("delta") \
    .mode("overwrite") \
    .option("path", target_path) \
    .saveAsTable(f"{lakehouse_name}.{table_name}")

print(f"✅ Datos escritos en formato Delta Lake en la tabla: {table_name}")

# 5. Verificación (Opcional: Muestra una pequeña parte de los datos)
df_final = spark.read.table(f"{lakehouse_name}.{table_name}")
print("\n📋 Muestra de datos finales en Delta Lake:")
df_final.show(5)

# =========================================================
