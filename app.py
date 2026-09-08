import streamlit as st
import os
import glob

# Configuración de la página web
st.set_page_config(
    page_title="tutelaapp — Acceso a Medicamentos",
    page_icon="⚖️",
    layout="centered"
)

# 1. Título y Lema (Parte 1.5 del README)
st.title("⚖️🤖 tutelaapp")
st.subheader("“Comprende tus derechos frente a las barreras de acceso a medicamentos.”")

# 2. ADVERTENCIA LEGAL VISIBLE OBLIGATORIA (Innegociable)
st.warning(
    "⚠️ **Advertencia legal obligatoria:** Esta herramienta es un ejercicio académico del curso "
    "Derecho e Inteligencia Artificial (Pontificia Universidad Javeriana). **No constituye asesoría "
    "legal profesional ni sustituye la consulta con un abogado.**"
)

st.write(
    "Ingresa una situación ficticia relacionada con demoras, negación o falta de entrega "
    "de medicamentos por parte de una EPS en Colombia para recibir una orientación jurídica."
)

# 3. Casos de ejemplo rápidos para probar
ejemplo = st.selectbox(
    "💡 O selecciona un caso ficticio de prueba:",
    [
        "-- Escribir mi propio caso abajo --",
        "Caso 1: EPS demora 40 días en entregar medicamento para la hipertensión por 'falta de stock'.",
        "Caso 2: Paciente hospitalizado en cuidados intensivos, familiar necesita tutela urgente (agencia oficiosa).",
        "Caso 3: Negación de medicamento alegando que no está en el Plan de Beneficios en Salud (PBS)."
    ]
)

texto_inicial = ""
if "Caso 1" in ejemplo:
    texto_inicial = "Mi EPS lleva más de un mes sin entregarme el medicamento Losartán para la hipertensión que me formuló el médico. Me dicen que no hay existencias en la farmacia."
elif "Caso 2" in ejemplo:
    texto_inicial = "Mi hermano está inconsciente en el hospital y la entidad de salud no autoriza el medicamento urgente. ¿Puedo interponer la tutela yo sin su firma?"
elif "Caso 3" in ejemplo:
    texto_inicial = "El médico especialista me recetó un medicamento para una enfermedad huérfana, pero la EPS me lo niega diciendo que está fuera del PBS."

consulta = st.text_area(
    "📝 Describe la situación ficticia:",
    value=texto_inicial,
    height=120
)

# 4. Botón de análisis jurídico
if st.button("🔍 Analizar situación jurídica", type="primary"):
    if not consulta.strip():
        st.error("Por favor escribe una consulta o selecciona un caso de ejemplo.")
    else:
        st.markdown("---")
        st.markdown("### 📋 Orientación Jurídica de tutelaapp")
        
        es_agencia = any(w in consulta.lower() for w in ["hermano", "madre", "padre", "abuela", "inconsciente", "familiar", "hijo"])
        es_fuera_pbs = any(w in consulta.lower() for w in ["pbs", "pos", "no cubierto", "huérfana", "excluido"])
        
        st.markdown("#### 1. Derechos Fundamentales Involucrados")
        st.write("• **Derecho Fundamental a la Salud** (Ley Estatutaria 1751 de 2015, Artículos 1 y 2).")
        st.write("• **Derecho a la Vida Digna** (Constitución Política, Artículos 11 y 49).")
        st.write("• **Principio de Continuidad:** Prohibición a las EPS de interrumpir tratamientos por razones administrativas o económicas (Ley 1751/2015, Art. 6 literal d y f).")
        
        st.markdown("#### 2. Legitimación y Vía Constitucional")
        if es_agencia:
            st.success("👥 **Agencia Oficiosa:** Conforme al Artículo 10 del Decreto 2591 de 1991, puedes actuar a nombre del paciente manifestando bajo juramento que se encuentra imposibilitado para defenderse.")
        else:
            st.info("👤 **En Nombre Propio:** Según el Artículo 86 de la Constitución, puedes presentar la tutela tú mismo/a, sin abogado ni fórmulas sacramentales.")
        
        if es_fuera_pbs:
            st.warning("⚖️ **Medicamentos No PBS (Sentencia T-760/08):** La tutela procede si: (a) fue formulado por médico adscrito, (b) no existe sustituto con igual efectividad en el PBS, y (c) no tienes capacidad de pago.")
        
        st.markdown("#### 3. Documentos de Prueba Indispensables")
        st.markdown("""
        1. Copia del documento de identidad.
        2. Copia de la **fórmula médica u orden vigente** del médico tratante.
        3. Constancia de negación, turno de 'pendiente' o soporte de reclamo ante la EPS/farmacia.
        """)
        
        st.markdown("#### 4. Fuentes Oficiales Consultadas")
        st.caption("• Ley Estatutaria 1751 de 2015 (Artículos 1, 2, 6 y 15).")
        st.caption("• Constitución Política de Colombia (Artículos 49 y 86).")
        st.caption("• Decreto 2591 de 1991 (Artículo 10).")
        st.caption("• Jurisprudencia Corte Constitucional — Sentencia T-760 de 2008.")

st.markdown("---")
st.caption("Pontificia Universidad Javeriana · Curso Derecho e Inteligencia Artificial 2026-II · Estudiante: María Paula Rodríguez Valencia")
