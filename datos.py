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
            
            # Salta los encabezados para procesar solo los datos
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

# Validación de la estructura
if estudiantes_db:
    print(f"Se cargaron {len(estudiantes_db)} estudiantes.")

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
            
            # 2. Respuestas Económicas/Personales (Índice 4: El "No/Sí")
            trabaja = fila[4]
            economicas = [trabaja]
            
            # 3. Respuestas Académicas
            promedio      = float(fila[5])
            horas_estudio = int(fila[6])
            academicas = [promedio, horas_estudio]
            
            # 4. Resto de la encuesta (Índices del 7 al 25)
            # Como son preguntas de escala (ej. 1 al 5), las guardamos todas juntas en una lista
            respuestas_encuesta = fila[7:] 
            
            # Estructura Final Anidada
            estudiante_organizado = [
                generales,            # Posición 0
                economicas,           # Posición 1
                academicas,           # Posición 2
                respuestas_encuesta   # Posición 3 (Aquí va TODA la tecnología y percepción)
            ]
            
            base_datos_organizada.append(estudiante_organizado)
            
        except ValueError as e:
            # Muestra los errores.
            print(f"Error en la fila del estudiante {fila[0]}: {e}")
            
    return base_datos_organizada

# --- EJECUCIÓN ---
estudiantes_db = organizar_estudiantes(estudiantes_db)

print("Información organizada exitosamente.")

# Reporte 1: Total de encuestados. 
total_encuestados = len(estudiantes_db)
print(f"1. Total de encuestados: {total_encuestados}")

#Reporte 2 -6 ---------------------------------------------------------------------------------------------------------------------------------------
#Cantidad de estudiantes por carrera
print("\n Bloque 2: Reporte por carrera")
sistemas=0
electronica=0
electrica=0

for est in estudiantes_db:
    carrera =est [0][1]
    if carrera == "Ingeniería de Sistemas":
        sistemas+=1
    elif carrera == "Ingeniería Electrónica":
        electronica+=1
    elif carrera == "Ingeniería Eléctrica":
        electrica+=1

print(f"Estudiantes en Ign. Sistemas: {sistemas}")
print(f"Estudiantes en Ign. Electrónica: {electronica}")
print(f"Estudiantes en Ign. Eléctrica: {electrica}")

#Cantidad de estudiantes por semestre. 
print("\n Bloque 3: Reporte por semestre")
semestre_conteo=[0]*11
for est in estudiantes_db:
    semestre= est [0][2]
    if 1<= semestre <= 10:
        semestre_conteo[semestre] +=1
for i in range (1, len(semestre_conteo)):
    print(f"Semestre {i}: {semestre_conteo[i]}")

#Cantidad de estudiantes por jornada.
print("\n--- REPORTE 4: CANTIDAD DE ESTUDIANTES POR JORNADA ---")
matutina = 0
vespertina = 0
nocturna = 0

for est in estudiantes_db:
    jornada = est[0][3].strip().capitalize() 
    if jornada == "Matutina":
        matutina += 1
    elif jornada == "Vespertina":
        vespertina += 1
    elif jornada == "Nocturna":
        nocturna += 1

print(f"Estudiantes en Jornada Matutina: {matutina}")
print(f"Estudiantes en Jornada Vespertina: {vespertina}")
print(f"Estudiantes en Jornada Nocturna: {nocturna}")

#Porcentaje de estudiantes que trabajan y que no trabajan.
print("\n--- REPORTE 5: PORCENTAJE DE ESTUDIANTES SEGÚN SITUACIÓN LABORAL ---")

total_estudiantes = len(estudiantes_db)

if total_estudiantes > 0:
    trabajan_conteo = 0
    for est in estudiantes_db:
        if est[1][0].strip().lower() == "sí":
            trabajan_conteo += 1
    
    no_trabajan_conteo = total_estudiantes - trabajan_conteo
    
    porcentaje_trabajan = (trabajan_conteo / total_estudiantes) * 100
    porcentaje_no_trabajan = (no_trabajan_conteo / total_estudiantes) * 100
    
    print(f"Total de estudiantes analizados: {total_estudiantes}")
    print(f"Trabajan: {trabajan_conteo} ({porcentaje_trabajan:.2f}%)")
    print(f"No trabajan: {no_trabajan_conteo} ({porcentaje_no_trabajan:.2f}%)")
else:
    print("No hay datos suficientes para calcular porcentajes.")

#Promedio general del promedio académico reportado.
print("\n--- REPORTE 6: PROMEDIO GENERAL ACADÉMICO ---")

suma_promedios = 0.0
total_registros = len(estudiantes_db)

if total_registros > 0:
    for est in estudiantes_db:
        promedio_individual = est[2][0]
        suma_promedios += promedio_individual
    
    promedio_general = suma_promedios / total_registros
    
    print(f"La suma total de los promedios es: {suma_promedios:.2f}")
    print(f"El promedio general de la población estudiantil es: {promedio_general:.2f}")
else:
    print("No se encontraron registros para calcular el promedio.")


# REPORTES 7 - 9 ========================================================================================================
print("\n" + "="*70)
print("REPORTES 7 AL 9".center(70,"-"))
print("="*70)

# REPORTE 7: Promedio académico por carrera
print("\n7. Promedio académico por carrera")
carreras_r7 = []            # carreras en reporte 7
sumas_promedio_r7 = []      # sumas de promedios en reporte 7
conteos_carrera_r7 = []     # conteo de carreras en reporte 7

for est in estudiantes_db:
    carrera = est[0][1]      # est[0] = generales   [1] carrera
    promedio = est[2][0]     # est[2] = academicas  [0] promedio

    if carrera in carreras_r7:
        posicion_carrera = carreras_r7.index(carrera)
        sumas_promedio_r7[posicion_carrera] += promedio
        conteos_carrera_r7[posicion_carrera] += 1
    else:
        carreras_r7.append(carrera)
        sumas_promedio_r7.append(promedio)
        conteos_carrera_r7.append(1)

#Promedio por carrera
for indice_carrera in range(len(carreras_r7)):
    promedio_final = sumas_promedio_r7[indice_carrera] / conteos_carrera_r7[indice_carrera]
    nombre_carrera = carreras_r7[indice_carrera]
    
    print(f"{nombre_carrera}: {promedio_final:.2f}")


# REPORTE 8: Promedio académico por semestre
print("\n8. Promedio académico por semestre")
semestres_r8 = []           # semestres en reporte 8
sumas_promedio_r8 = []      # sumas de promedios en reporte 8
conteos_semestre_r8 = []    # conteo de semestres en reporte 8

for est in estudiantes_db:
    semestre = est[0][2]     # est[0] = generales   [2] semestre
    promedio = est[2][0]     # est[2] = academicas  [0] promedio
    
    if semestre in semestres_r8:
        pos = semestres_r8.index(semestre)
        sumas_promedio_r8[pos] += promedio
        conteos_semestre_r8[pos] += 1
    else:
        semestres_r8.append(semestre)
        sumas_promedio_r8.append(promedio)
        conteos_semestre_r8.append(1)

# Promedio por semestre
for indice_semestre in range(len(semestres_r8)):
    promedio_final = sumas_promedio_r8[indice_semestre] / conteos_semestre_r8[indice_semestre]
    numero_semestre = semestres_r8[indice_semestre]
    
    print(f"Semestre {numero_semestre}: {promedio_final:.2f}")


# REPORTE 9: Cantidad de estudiantes con acceso a internet en casa (Se cambia a calidad al ser respuesta de escala)
print("\n9. Cantidad de estudiantes según calidad de acceso a internet en casa")
internet_bueno = 0  # Escala 3, 4, 5
internet_malo = 0   # Escala 1, 2

for est in estudiantes_db:
    try:
        calidad_internet = int(est[3][8])
        if calidad_internet >= 3:
            internet_bueno += 1
        else:
            internet_malo += 1
    except ValueError:
        continue

print(f"Cantidad de estudiantes con calidad de internet Aceptable/Buena: {internet_bueno}")
print(f"Cantidad de estudiantes con calidad de internet Deficiente: {internet_malo}")

# REPORTES 11 - 15 ========================================================================================================
print("\n" + "="*70)
print("REPORTES 11 AL 15".center(70,"-"))
print("="*70)
# Reporte 11. Cantidad de estudiantes según horas de estudio semanal.
def reporte_11_horas_estudio(base_datos):
    conteo_horas = {}

    for est in base_datos:
        horas = est[2][1]  # academicas -> horas_estudio

        if horas in conteo_horas:
            conteo_horas[horas] += 1
        else:
            conteo_horas[horas] = 1
    print("\n--- REPORTE 11 ---")
    print("Cantidad de estudiantes según horas de estudio semanal:\n")

    for horas in sorted(conteo_horas):
        print(f"{horas} horas: {conteo_horas[horas]} estudiantes")
reporte_11_horas_estudio(estudiantes_db)

# Reporte 12. Nivel de satisfacción general con la carrera.
def reporte_12_satisfaccion(base_datos):
    # Lista para contar niveles 1 a 5
    conteo = [0, 0, 0, 0, 0]  # índice 0→nivel1, 1→nivel2...
    for est in base_datos:
        try:
            nivel = int(est[3][17])  # q18
            # Ajustamos índice (nivel 1 va en posición 0)
            conteo[nivel - 1] += 1
        except:
            continue
    print("\n--- REPORTE 12 ---")
    print("Nivel de satisfacción general con la carrera:\n")
    total = sum(conteo)

    for i in range(5):
        porcentaje = (conteo[i] / total) * 100
        print(f"Nivel {i+1}: {conteo[i]} estudiantes ({porcentaje:.2f}%)")

reporte_12_satisfaccion(estudiantes_db)

# Reporte 13. Nivel de estrés académico general.
def reporte_13_estres(base_datos):
    # Lista para niveles 1 a 5
    conteo = [0, 0, 0, 0, 0]
    for est in base_datos:
        try:
            nivel = int(est[3][18])  # q19

            conteo[nivel - 1] += 1
        except:
            continue

    print("\n--- REPORTE 13 ---")
    print("Nivel de estrés académico general:\n")
    total = sum(conteo)

reporte_13_estres(estudiantes_db)

# Reporte 14. Curso percibido como mas dificil
def reporte_14_curso_dificil(base_datos):
    conteo = [0, 0, 0, 0, 0]

    for est in base_datos:
        try:
            valor = int(est[3][9])  # q10 (curso más difícil)
            conteo[valor - 1] += 1
        except:
            continue

    print("\n--- REPORTE 14 ---")
    print("Curso percibido como más difícil:\n")

    maximo = max(conteo)
    posicion = conteo.index(maximo)

    print(f"Valor más frecuente: {posicion + 1} ({maximo} estudiantes)")
reporte_14_curso_dificil(estudiantes_db)

# Reporte 15. Carrera con mayor nivel promedio de estrés. 
def reporte_15_estres_por_carrera(base_datos):
    carreras = []
    suma_estres = []
    conteo = []

    for est in base_datos:
        try:
            carrera = est[0][1]
            estres = int(est[3][10])  # q11 = estrés
            if carrera in carreras:
                pos = carreras.index(carrera)
                suma_estres[pos] += estres
                conteo[pos] += 1
            else:
                carreras.append(carrera)
                suma_estres.append(estres)
                conteo.append(1)
        except:
            continue
    print("\n--- REPORTE 15 ---")
    print("Carrera con mayor nivel promedio de estrés:\n")
    promedios = []
    for i in range(len(carreras)):
        promedio = suma_estres[i] / conteo[i]
        promedios.append(promedio)
        print(f"{carreras[i]}: {promedio:.2f}")
    maximo = max(promedios)
    pos_max = promedios.index(maximo)
    print(f"\nCarrera con mayor estrés promedio: {carreras[pos_max]} ({maximo:.2f})")


reporte_15_estres_por_carrera(estudiantes_db)

# REPORTES 16-20 ========================================================================================================
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
