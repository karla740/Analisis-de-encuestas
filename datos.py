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


# REPORTES 16-20
print("\n" + "="*70)
print("REPORTES 16 AL 20".center(70,"-"))
print("="*70)

# REPORTE 16: Relación entre trabajar y promedio académico
print("\n16. Relación entre trabajar y promedio académico")

# Variables acumuladoras
prom_trabajan = 0
prom_no_trabajan = 0
cant_trabajan = 0
cant_no_trabajan = 0

# Recorremos todos los estudiantes
for est in estudiantes_db:
    # est[1][0] = si trabaja ("sí" o "no")
    trabaja = est[1][0].strip().lower()
    
    # est[2][0] = promedio académico
    promedio = est[2][0]
    
    # Separamos en dos grupos
    if trabaja == "sí":
        prom_trabajan += promedio
        cant_trabajan += 1
    else:
        prom_no_trabajan += promedio
        cant_no_trabajan += 1

# Calculamos promedios evitando división entre 0
if cant_trabajan > 0:
    print(f"   Estudiantes que trabajan: {cant_trabajan} → Promedio: {prom_trabajan/cant_trabajan:.2f}")
else:
    print("   No hay estudiantes que trabajan")

if cant_no_trabajan > 0:
    print(f"   Estudiantes que NO trabajan: {cant_no_trabajan} → Promedio: {prom_no_trabajan/cant_no_trabajan:.2f}")
else:
    print("   No hay estudiantes que no trabajan")

# REPORTE 17: Relación entre calidad de internet y promedio
print("\n17. Relación entre calidad de internet y promedio académico")

# Acumuladores
suma_buena = 0
suma_mala = 0
cont_buena = 0
cont_mala = 0

for est in estudiantes_db:
    try:
        # est[3][3] = pregunta sobre calidad de internet (escala 1–5)
        q10 = int(est[3][3])
        promedio = est[2][0]
        
        # Clasificamos calidad
        if q10 >= 3:
            suma_buena += promedio
            cont_buena += 1
        else:
            suma_mala += promedio
            cont_mala += 1
    except:
        # Si hay error en datos, se ignora el registro
        continue

# Mostramos resultados
if cont_buena > 0:
    print(f"   Buena calidad (≥3): {cont_buena} → Promedio: {suma_buena/cont_buena:.2f}")
else:
    print("   No hay datos de buena calidad")

if cont_mala > 0:
    print(f"   Mala calidad (<3): {cont_mala} → Promedio: {suma_mala/cont_mala:.2f}")
else:
    print("   No hay datos de mala calidad")

# REPORTE 18: Relación entre horas de estudio y promedio
print("\n18. Relación entre horas de estudio y promedio académico")

niveles = []
suma_por_horas = []
conteo_por_horas = []

for est in estudiantes_db:
    horas = est[2][1]
    promedio = est[2][0]
    
    if horas in niveles:
        pos = niveles.index(horas)
        suma_por_horas[pos] += promedio
        conteo_por_horas[pos] += 1
    else:
        niveles.append(horas)
        suma_por_horas.append(promedio)
        conteo_por_horas.append(1)

print("   Promedio académico según horas de estudio:")

for i in range(len(niveles)):
    prom = suma_por_horas[i] / conteo_por_horas[i]
    print(f"      {niveles[i]} horas: {prom:.2f} ({conteo_por_horas[i]} estudiantes)")

# REPORTE 19: Porcentaje de interés en cursos virtuales
print("\n19. Porcentaje de estudiantes interesados en cursos virtuales")

interesados = 0

for est in estudiantes_db:
    try:
        # Última pregunta del bloque (escala 1–5)
        q20 = int(est[3][-1])
        
        # Consideramos interés alto si ≥ 4
        if q20 >= 4:
            interesados += 1
    except:
        continue

total_estudiantes = len(estudiantes_db)

if total_estudiantes > 0:
    porcentaje = (interesados / total_estudiantes) * 100
    print(f"   Interesados: {interesados} ({porcentaje:.2f}%)")
else:
    print("   No hay datos disponibles")

# REPORTE 20: Perfil predominante del estudiante
print("\n20. Perfil predominante según respuestas más frecuentes")

def moda(lista):
    valores = []
    conteos = []
    
    for elemento in lista:
        if elemento in valores:
            pos = valores.index(elemento)
            conteos[pos] += 1
        else:
            valores.append(elemento)
            conteos.append(1)
    
    max_count = max(conteos)
    pos_max = conteos.index(max_count)
    
    return valores[pos_max], max_count

# Extraemos listas
lista_carreras = [est[0][1] for est in estudiantes_db]
lista_semestres = [est[0][2] for est in estudiantes_db]
lista_jornadas = [est[0][3] for est in estudiantes_db]
lista_trabaja = [est[1][0].strip().lower() for est in estudiantes_db]
lista_promedios = [round(est[2][0]) for est in estudiantes_db]

lista_estres = []
lista_satisfaccion = []

for est in estudiantes_db:
    try:
        lista_estres.append(int(est[3][1]))
        lista_satisfaccion.append(int(est[3][3]))
    except:
        continue

# Calculamos modas
carrera_pred = moda(lista_carreras)
semestre_pred = moda(lista_semestres)
jornada_pred = moda(lista_jornadas)
trabaja_pred = moda(lista_trabaja)
prom_pred = moda(lista_promedios)

estres_pred = moda(lista_estres) if lista_estres else ("N/A", 0)
sat_pred = moda(lista_satisfaccion) if lista_satisfaccion else ("N/A", 0)

print("   Perfil predominante:")
print(f"   - Carrera: {carrera_pred[0]} ({carrera_pred[1]} estudiantes)")
print(f"   - Semestre: {semestre_pred[0]}")
print(f"   - Jornada: {jornada_pred[0]}")
print(f"   - Trabaja: {trabaja_pred[0]}")
print(f"   - Promedio: {prom_pred[0]}")
print(f"   - Estrés: {estres_pred[0]}")
print(f"   - Satisfacción: {sat_pred[0]}")

print("\n¡Reportes 16 al 20 completados!")
print("")
