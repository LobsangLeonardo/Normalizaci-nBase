#Nombre: Armenta Fuentes Lobsang Leonardo
import pandas as pd
import mysql.connector

# Lectura del archivo Excel.
archivo_excel = "inegiE.xlsx"  
dfs = pd.read_excel(archivo_excel, sheet_name=None, engine="openpyxl")

# Imprime el nombre de cada tabla y sus primeras filas.
for hoja, df in dfs.items():
    print(f"Hoja: {hoja}, primeras filas:\n", df.head())
    
# La definicion de las tablas.
tablas = {
    "Ubicacion": ["id", "tipo_vial", "numero_ext", "edificio_e", "numero_int", "tipo_asent", "cod_postal", "cve_mun", "cve_loc", "latitud", "longitud"],
    "Municipio": ["id", "nomb_asent", "cve_mun"],
    "Establecimiento": ["id", "nom_estab", "raz_social", "codigo_act", "fecha_alta"],
    "Contactos": ["id", "telefono", "correoelec", "www", "contactos"]
}
# Conexion de la base de datos de MySQL (contraseña no real).
conn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="123", 
    database="DB_inegi"
)
#La insercion de los datos, va cargando de 1000 lotes de datos de as filas. 
cursor = conn.cursor()
# El tamaño de los lotes.
batch_size = 1000
for hoja, df in dfs.items():
    # Verifica que la tabla sea correcta.
    if hoja in tablas:
        columnas = tablas[hoja]
        placeholders = ", ".join(["%s"] * len(columnas))
        sql = f"INSERT INTO {hoja} ({', '.join(columnas)}) VALUES ({placeholders})"
        batch_data = []
        for i, row in df.iterrows():
            row_data = []
            for col in columnas:
                val = row[col]
                if pd.isna(val):
                    row_data.append(None)
                else:
                    row_data.append(val)
            
            batch_data.append(tuple(row_data))
            if len(batch_data) >= batch_size or i == len(df) - 1:
                try:
                    cursor.executemany(sql, batch_data)
                    conn.commit()
                    print(f"Lote de {len(batch_data)} registros insertados en {hoja}.")
                    batch_data = []
                except Exception as e:
                    # Si hay un error, se va a reinvertir el proceso para evitar problemas.
                    print(f"Error al insertar lote en {hoja}: {e}")
                    conn.rollback()
                    
        print(f"Datos {hoja} insertados correctamente.")
        # Cierra las conexiones.
        cursor.close()
        conn.close()