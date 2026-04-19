import csv

archivo_csv = 'encuesta_ingenieria_10000_respuestas.csv'   

# Arreglo vacio donde se guarda los datos anidados
encuesta = []

# lectura de archivo csv
with open(archivo_csv, newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    header = next(lector)        # Saltamos la primera fila (encabezados)
    
    print(f"Columnas detectadas: {len(header)}")
    
    for fila in lector:
        if len(fila) != 26:
            continue  # Por si hay filas corruptas
        
        try:
            estudiante = [
                int(fila[0]),                                   # id_encuestado
                
                [                                               # Bloque 1: Datos Generales
                    fila[1],                                    # carrera
                    int(fila[2]),                               # semestre
                    fila[3],                                    # jornada
                    fila[4],                                    # trabaja (Sí/No)
                    int(fila[5])                                # promedio_actual
                ],
                
                [int(x) for x in fila[6:15]],                   # Bloque 2: q01 a q09 (9 valores)
                
                [int(x) for x in fila[15:20]],                  # Bloque 3: q10 a q14 (5 valores)
                
                [int(x) for x in fila[20:26]]                   # Bloque 4: q15 a q20 (6 valores)
            ]
            encuesta.append(estudiante)
            
        except ValueError:
            print("Error al convertir datos en fila:", fila[0])
            continue

# verificacion
print(f"\nTotal de encuestados cargados: {len(encuesta)}")
print("\nPrimer estudiante (ejemplo):")
print(encuesta[0])

print("\nSegundo estudiante:")
print(encuesta[1])