import csv

def cargar_datos(ruta_archivo):
    """
    1. LECTURA DEL ARCHIVO
    Lee el archivo CSV y retorna una lista de listas anidadas.
    """
    base_datos = []
    
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            # Usamos el lector estándar de CSV
            lector = csv.reader(archivo)
            
            # Saltamos los encabezados para procesar solo datos puros
            encabezados = next(lector)
            
            for fila in lector:
                # Siguiendo la guía de "Listas dentro de listas":
                # Cada 'estudiante' es una lista con sus valores individuales
                # IMPORTANTE: Se mantienen los datos como strings inicialmente 
                # para evitar el ValueError hasta que se mapeen los índices correctos.
                estudiante = fila 
                
                # Agregamos la sub-lista a nuestra lista principal (Estructura Anidada)
                base_datos.append(estudiante)
                
        return base_datos

    except FileNotFoundError:
        print("❌ Error: El archivo no existe en la ruta especificada.")
        return []

# --- EJECUCIÓN ---
nombre_archivo = 'encuesta_ingenieria_10000_respuestas.csv'
estudiantes_db = cargar_datos(nombre_archivo)

# Validación de la estructura (como en la guía)
if estudiantes_db:
    print(f"¡Éxito! Se cargaron {len(estudiantes_db)} estudiantes.")
    print(f"Ejemplo del primer registro (Lista simple dentro de la anidada):")
    print(estudiantes_db[0])

