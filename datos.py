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
                estudiante = fila 
                
                # Agregamos la sub-lista a nuestra lista principal
                base_datos.append(estudiante)
                
        return base_datos

    except FileNotFoundError:
        print("Error: El archivo no existe en la ruta especificada.")
        return []

# --- EJECUCIÓN ---
nombre_archivo = 'encuesta_ingenieria_10000_respuestas.csv'
estudiantes_db = cargar_datos(nombre_archivo)

# Validación de la estructura (como en la guía)
if estudiantes_db:
    print(f"Se cargaron {len(estudiantes_db)} estudiantes.")
    print(f"Ejemplo del primer registro:")
    print(estudiantes_db[0])

def organizar_estudiantes(lista_cruda):
    """
    2 y 3. DISEÑO Y ORGANIZACIÓN DE DATOS
    """
    base_datos_organizada = []
    
    for fila in lista_cruda:
        try:
            # 1. Datos Generales (Índices 0 al 3)
            id_estudiante = int(fila[0])
            carrera       = fila[1]
            semestre      = int(fila[2])
            jornada       = fila[3]
            generales = [id_estudiante, carrera, semestre, jornada]
            
            # 2. Respuestas Económicas/Personales (Índice 4: El "No")
            trabaja = fila[4]
            economicas = [trabaja]
            
            # 3. Respuestas Académicas
            promedio      = float(fila[5])
            horas_estudio = int(fila[6])
            academicas = [promedio, horas_estudio]
            
            # 4. Resto de la encuesta (Índices del 7 al 25)
            # Como son preguntas de escala (ej. 1 al 5), las guardamos todas juntas en una lista
            # Las dejamos como texto temporalmente para evitar errores
            respuestas_encuesta = fila[7:] 
            
            # Estructura Final Anidada (Punto 3 de tu guía)
            estudiante_organizado = [
                generales,            # Posición 0
                economicas,           # Posición 1
                academicas,           # Posición 2
                respuestas_encuesta   # Posición 3 (Aquí va TODA la tecnología y percepción)
            ]
            
            base_datos_organizada.append(estudiante_organizado)
            
        except ValueError as e:
            # Si hay una fila corrupta, te avisará pero no detendrá el programa
            print(f"Error en la fila del estudiante {fila[0]}: {e}")
            
    return base_datos_organizada

# --- EJECUCIÓN (Añade esto debajo de tu código actual) ---
estudiantes_db = organizar_estudiantes(estudiantes_db)

print("Información organizada exitosamente.")
print("Ejemplo de la nueva estructura anidada del primer estudiante:")
print(estudiantes_db[0])

print("\n--- BLOQUE 1: CONTEOS Y SUMATORIAS ---")

# Reporte 1: Conteo de estudiantes que trabajan
trabajan = 0
for est in estudiantes_db:
    if est[1][0].strip().lower() == "sí": # est[1][0] es 'trabaja'
        trabajan += 1
print(f"Reporte 1. Estudiantes que trabajan: {trabajan}")