"""
tutelaapp — Módulo RAG (Recuperación y Generación Aumentada con Fuentes)
Curso: Derecho e Inteligencia Artificial (Pontificia Universidad Javeriana, 2026-II)
Estudiante: María Paula Rodríguez Valencia
"""

import os
import glob

# Advertencia legal obligatoria innegociable
ADVERTENCIA_LEGAL = (
    "⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal "
    "ni sustituye la consulta con un abogado."
)

def cargar_corpus(ruta_corpus="corpus"):
    """Carga los archivos de normas guardados en la carpeta corpus/"""
    documentos = []
    archivos = glob.glob(f"{ruta_corpus}/*.txt")
    for archivo in archivos:
        with open(archivo, "r", encoding="utf-8") as f:
            documentos.append({"fuente": os.path.basename(archivo), "texto": f.read().strip()})
    return documentos

def buscar_en_corpus(consulta, documentos):
    """Busca en el corpus los artículos relevantes para el caso consultado."""
    coincidencias = []
    for doc in documentos:
        lineas = doc["texto"].split("\n\n")
        for bloque in lineas:
            if any(palabra in consulta.lower() for palabra in ["medicamento", "salud", "tutela", "eps", "demora", "agotado"]):
                coincidencias.append(f"[{doc['fuente']}]\n{bloque}")
    if coincidencias:
        return "\n\n---\n\n".join(coincidencias[:3])
    return "\n\n".join([d["texto"] for d in documentos])

def construir_prompt(consulta_usuario, contexto_juridico):
    """Arma el prompt para el modelo con las citas obligatorias y la regla anti-alucinación."""
    return f"""Eres tutelaapp, asistente jurídico académico creado para orientar sobre barreras de medicamentos.

{ADVERTENCIA_LEGAL}

FUENTES OFICIALES RECUPERADAS DEL CORPUS:
{contexto_juridico}

CONSULTA:
"{consulta_usuario}"

REGLAS ESTRICTAS:
1. Responde en español claro ("en cristiano").
2. CITA SIEMPRE la norma y artículo del contexto recuperado (ej. Art. 6 Ley 1751/2015).
3. ANTI-ALUCINACIÓN: Si te preguntan algo que no esté sustentado en estas fuentes, di con sinceridad: "No tengo información jurídica suficiente en el corpus". NUNCA inventes leyes ni artículos.
4. No garantizas resultados judiciales ni emites conceptos médicos.

RESPUESTA JURÍDICA ORIENTADORA:"""

if __name__ == "__main__":
    print("⚖️ tutelaapp RAG — Sistema cargado con éxito.")
    docs = cargar_corpus()
    print(f"Normas oficiales cargadas: {len(docs)}")
