from collections import defaultdict

def convertir_a_float(valor):
    """Convierte un valor a float, maneja comas decimales"""
    if isinstance(valor, (int, float)):
        return float(valor)
    # Convertir string con coma a punto
    valor_str = str(valor).replace(',', '.')
    return float(valor_str)

def obtener_promedio_por_estudiante_curso(calificaciones):
    datos = defaultdict(lambda: defaultdict(list))
    for c in calificaciones:
        estudiante = c.estudiante.username
        curso = c.materia.curso.nombre
        datos[estudiante][curso].append(convertir_a_float(c.nota))
    promedios = {}
    for estudiante, cursos in datos.items():
        promedios[estudiante] = {}
        for curso, notas in cursos.items():
            promedios[estudiante][curso] = round(sum(notas)/len(notas), 2) if notas else 0
    return promedios

def obtener_promedio_por_curso(calificaciones):
    datos_cursos = defaultdict(list)
    for c in calificaciones:
        nombre_curso = c.materia.curso.nombre
        datos_cursos[nombre_curso].append(convertir_a_float(c.nota))
    promedios = {}
    for curso, notas in datos_cursos.items():
        promedios[curso] = round(sum(notas)/len(notas), 2) if notas else 0
    return promedios
