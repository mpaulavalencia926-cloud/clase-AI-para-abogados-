# ⚖️🤖 tutelaapp — Derecho e Inteligencia Artificial

**Pontificia Universidad Javeriana · 2026-II**  
**Estudiante:** María Paula Rodríguez Valencia  
**Docente:** Pedro Ardila  
**Nombre del proyecto:** tutelaapp  
**Fecha de inicio:** 06/09/2026

---

## 📋 Parte 1 — Descripción del proyecto

### 1.1 El problema jurídico

En Colombia, algunas personas enfrentan barreras para acceder oportunamente a medicamentos que necesitan, por ejemplo, debido a la negación, demora o falta de entrega por parte de una EPS u otra entidad responsable. Estas situaciones pueden comprometer derechos fundamentales como la salud y, dependiendo de las circunstancias del caso, la vida y la dignidad humana. Actualmente, una persona que enfrenta este problema debe identificar por sí misma si la situación puede tener relevancia constitucional, buscar las normas y sentencias aplicables y entender cómo presentar una acción de tutela. Esto puede ser especialmente difícil para una persona que no tiene conocimientos jurídicos. Mi herramienta busca orientar al usuario sobre los elementos jurídicos relevantes de un caso ficticio de barrera de acceso a medicamentos, utilizando únicamente un corpus jurídico previamente seleccionado. La herramienta no pretende decidir si una tutela será concedida, sino facilitar la identificación y comprensión de los fundamentos jurídicos que podrían ser relevantes.

### 1.2 Usuarios

El usuario ideal es una persona en Colombia que enfrenta una demora, negación o barrera para recibir un medicamento que le ha sido formulado y quiere comprender qué relevancia jurídica puede tener su situación. También podría ser utilizada con fines académicos por estudiantes que quieran estudiar la protección constitucional del derecho a la salud. El usuario ingresará una descripción ficticia de su situación y la herramienta formulará una orientación jurídica basada en las fuentes incorporadas. Para proteger los datos personales, durante las pruebas no se utilizarán nombres, números de identificación, historias clínicas ni otros datos personales reales. Al finalizar el proyecto, al menos una persona externa al curso probará la herramienta utilizando un caso ficticio.

### 1.3 Qué hace y qué NO hace

| **✅ Sí hace** | **❌ No hace** |
|---|---|
| Recibe una descripción de una situación ficticia relacionada con una barrera de acceso a medicamentos. | No reemplaza a un abogado. |
| Identifica los posibles derechos fundamentales involucrados según el corpus jurídico. | No diagnostica enfermedades ni recomienda medicamentos o tratamientos. |
| Explica qué normas y sentencias del corpus podrían ser relevantes. | No garantiza que una tutela sea concedida. |
| Orienta sobre los elementos jurídicos que podrían analizarse en una acción de tutela. | No presenta tutelas automáticamente ni actúa como representante del usuario. |
| Cita las fuentes jurídicas utilizadas y reconoce cuando no tiene información suficiente. | No inventa normas, sentencias ni hechos del caso. |

### 1.4 Marco jurídico y fuentes

El corpus inicial será pequeño y estará compuesto por fuentes jurídicas públicas. La herramienta utilizará estas fuentes para identificar los posibles derechos involucrados y explicar los fundamentos jurídicos de manera comprensible.

- **Constitución Política de Colombia de 1991**, especialmente los artículos 48 y 49, relacionados con la seguridad social y el derecho a la salud.  
  [Consultar Constitución Política](https://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991.html)

- **Ley Estatutaria 1751 de 2015**, por medio de la cual se regula el derecho fundamental a la salud.  
  [Consultar Ley 1751 de 2015](https://www.secretariasenado.gov.co/senado/basedoc/ley_1751_2015.html)

- **Jurisprudencia:** Se incorporarán sentencias de la Corte Constitucional relacionadas con el acceso a medicamentos y la protección del derecho a la salud, una vez sean seleccionadas y verificadas para el corpus del proyecto.

### 1.5 Nombre y lema

**Nombre:** tutelaapp

**Lema:** “Comprende tus derechos frente a las barreras de acceso a medicamentos.”

---

## 🗺️ Parte 2 — Plan de desarrollo

### 2.1 Hitos del proyecto

| Hito | Qué debo lograr | Estado |
|---|---|---|
| **M0 — Descripción y plan** | Completar las Partes 1 y 2 del README. | 🟡 En desarrollo |
| **M1 — Asistente con instrucciones v1** | Crear las instrucciones del asistente y probarlas en una herramienta gratuita de chat. | ⬜ Pendiente |
| **M2 — Casos de prueba documentados** | Elaborar al menos 5 casos de prueba y guardar sus resultados en `docs/casos-de-prueba.md`. | ⬜ Pendiente |
| **M3 — Corpus conectado (RAG)** | Conectar el corpus jurídico para que el asistente cite las fuentes utilizadas y no invente. | ⬜ Pendiente |
| **M4 — Interfaz web desplegada** | Crear una interfaz web, obtener una URL pública y realizar una prueba con un usuario externo. | ⬜ Pendiente |
| **M5 — Análisis crítico y demo** | Completar la Parte 7 y preparar la presentación de 5 minutos. | ⬜ Pendiente |

### 2.2 Bitácora de avance semanal

| Semana | Qué hice | Enlace / captura | Dudas para la clase |
|---|---|---|---|
| **1** | Delimité el problema jurídico, los usuarios, el alcance y las fuentes de tutelaapp. | Enlace al README | ¿El alcance es suficientemente pequeño? |
| **2** | | | |
| **3** | | | |
| **4** | | | |
| **5** | | | |

---

## 🛠️ Parte 3 — Stack técnico recomendado

### 3.1 ¿Cómo funcionará tutelaapp?

La herramienta tendrá una interfaz web donde el usuario podrá escribir una situación ficticia relacionada con una barrera de acceso a medicamentos. Esa consulta será procesada por un sistema que buscará información en un corpus jurídico previamente seleccionado y utilizará un modelo de inteligencia artificial para generar una orientación basada en las fuentes encontradas.

La arquitectura propuesta es:

**Usuario → Interfaz web → LangChain → OpenRouter → Corpus jurídico (RAG) → Respuesta con fuentes**

### 3.2 Herramientas que utilizaré

| Pieza | Herramienta | ¿Para qué sirve? |
|---|---|---|
| **Interfaz web** | Streamlit o una interfaz generada con IA | Es la página que verá el usuario. |
| **Orquestación** | LangChain | Organiza la consulta, la búsqueda en el corpus y la respuesta. |
| **Modelo de IA** | OpenRouter | Permite utilizar un modelo de lenguaje para redactar la orientación. |
| **Memoria de fuentes (RAG)** | LangChain + Chroma o FAISS | Permite que la respuesta se base en las normas incorporadas. |
| **Repositorio** | GitHub | Guarda el código, los documentos y el historial de avances. |
| **Despliegue** | Vercel o Streamlit Community Cloud | Permite publicar la herramienta para que otras personas puedan abrirla. |

### 3.3 ¿Por qué elegí estas herramientas?

Elegí estas herramientas porque el proyecto busca demostrar que una estudiante de Derecho puede construir una herramienta sencilla con asistencia de IA, sin necesidad de programar todo desde cero. La interfaz permitirá que el usuario interactúe con el sistema, mientras que LangChain organizará el proceso de búsqueda y respuesta. El uso de RAG será importante porque la herramienta debe responder con base en un corpus jurídico previamente seleccionado y no únicamente con lo que el modelo recuerde. GitHub permitirá conservar el historial de cambios y mostrar el proceso de desarrollo.

---

## 🚀 Parte 4 — Ruta de despliegue

### 4.1 Meta del proyecto

La meta es que tutelaapp tenga una **URL pública** que pueda abrir otra persona desde su navegador. La herramienta deberá permitir escribir una consulta ficticia, recibir una orientación jurídica y mostrar de manera visible la advertencia de que se trata de un ejercicio académico.

### 4.2 Ruta elegida

**Ruta principal: GitHub + Vercel**, si la interfaz se construye con Next.js.

El proceso será:

1. Crear y organizar los archivos del proyecto.
2. Subir el código al repositorio de GitHub.
3. Crear una cuenta gratuita en Vercel.
4. Importar el repositorio.
5. Configurar las variables de entorno necesarias.
6. Desplegar la aplicación.
7. Probar la URL desde otro navegador o dispositivo.
8. Guardar evidencia del funcionamiento.

### 4.3 Checklist de despliegue

- [ ] La interfaz web funciona.
- [ ] La URL pública abre correctamente.
- [ ] La advertencia legal es visible.
- [ ] No hay claves API ni secretos en el código.
- [ ] La herramienta fue probada por otra persona.
- [ ] Se guardó evidencia de la prueba.
- [ ] Se anotó la URL pública en este README.

**URL pública:** `[Se completará cuando la aplicación esté desplegada]`

---

## 🧠 Parte 5 — Guía de prompting para vibe coding

### 5.1 ¿Qué es el prompting en mi proyecto?

El prompting es la forma de darle instrucciones a la inteligencia artificial para que construya y responda de acuerdo con el objetivo jurídico de tutelaapp. En este proyecto, mi función como estudiante de Derecho no es solamente pedirle a la IA que programe, sino definir el problema, seleccionar las fuentes, establecer los límites y verificar que las respuestas sean jurídicamente responsables.

### 5.2 Reglas que seguiré

1. Trabajaré **un hito a la vez**.
2. Explicaré a la IA el contexto jurídico antes de pedirle código.
3. Pediré que me explique cada paso en un lenguaje que pueda entender.
4. Guardaré los avances mediante commits en GitHub.
5. No utilizaré datos personales reales en las pruebas.
6. Verificaré las respuestas jurídicas con las fuentes del corpus.
7. Si la IA no tiene una fuente suficiente, deberá reconocerlo.
8. No permitiré que la herramienta invente normas o sentencias.

### 5.3 Prompt de arranque para M1

> Soy estudiante de Derecho de primer semestre y estoy construyendo un proyecto académico llamado tutelaapp. Mi herramienta busca orientar sobre los posibles fundamentos jurídicos de casos ficticios de barreras de acceso a medicamentos en Colombia.
>
> Quiero que me ayudes a crear las instrucciones de mi asistente jurídico. El asistente debe:
>
> 1. Responder únicamente con base en el corpus jurídico que yo le proporcione.
> 2. Identificar los posibles derechos fundamentales involucrados.
> 3. Citar la norma o sentencia que utiliza.
> 4. Decir “no tengo información suficiente en el corpus” cuando no encuentre una fuente.
> 5. No inventar normas, sentencias ni hechos.
> 6. No garantizar que una tutela será concedida.
> 7. Incluir esta advertencia en cada respuesta: “Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.”
> 8. No diagnosticar enfermedades ni recomendar medicamentos o tratamientos.
>
> Explícame cómo construir este prompt paso a paso y dame una primera versión que pueda probar en una herramienta gratuita de chat.

### 5.4 Prompt de arranque para M3

> Tengo un corpus jurídico sobre el derecho a la salud y las barreras de acceso a medicamentos. Quiero conectar esas fuentes a mi asistente mediante RAG. Guíame paso a paso, explicándome como a alguien que no sabe programar. Al final, el asistente debe responder únicamente con base en las fuentes recuperadas y citar el artículo o sentencia utilizado.

### 5.5 Prompt de arranque para M4

> Crea una interfaz web sencilla para tutelaapp. Debe tener un recuadro para escribir una consulta ficticia, un espacio para mostrar la respuesta, el nombre de la herramienta y una advertencia legal visible. Explícame qué archivo debo tocar y qué debo copiar. Después guíame para desplegarla gratis con mi repositorio de GitHub. No sé programar: dime exactamente qué archivo tocar y qué copiar.

---

## ⚖️ Parte 6 — Ética, datos y responsabilidad

### 6.1 Advertencia visible obligatoria

La interfaz de tutelaapp mostrará de manera visible:

> **“Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.”**

### 6.2 Protección de datos

Durante las pruebas no se utilizarán nombres, números de identificación, historias clínicas ni otros datos personales reales. Los usuarios de prueba utilizarán situaciones ficticias o datos inventados. La herramienta se diseñará para no recolectar ni almacenar datos personales reales de los usuarios de prueba.

### 6.3 Corpus público

El corpus estará compuesto únicamente por fuentes jurídicas públicas, como leyes, decretos y jurisprudencia publicada. No se utilizarán documentos privados ni información personal de usuarios.

### 6.4 Anti-alucinaciones

El asistente deberá citar la fuente jurídica de cada afirmación relevante. Cuando no encuentre una fuente suficiente, deberá reconocer que no tiene información suficiente en el corpus. También se realizarán casos de prueba para comprobar que no invente normas, sentencias ni hechos.

### 6.5 Responsabilidad

Como estudiante de Derecho, debo verificar las respuestas de la herramienta antes de presentarlas. La inteligencia artificial puede equivocarse, por lo que no asumiré que una respuesta es correcta solamente porque está bien redactada. El objetivo es que tutelaapp sea una herramienta de orientación académica responsable, no un sustituto del análisis jurídico profesional.

---

## 🔍 Parte 7 — Análisis crítico

### 7.1 ¿Dónde falla mi herramienta?

**Situación 1: el caso contiene información que no está en el corpus.**

La herramienta puede recibir una situación relacionada con un medicamento o una barrera de acceso que no esté suficientemente desarrollada en las fuentes incorporadas. En ese caso, podría no tener elementos suficientes para identificar todos los fundamentos jurídicos relevantes. Por eso, deberá reconocer cuando no encuentre información suficiente y no inventar una respuesta.

**Situación 2: el caso requiere un análisis jurídico más amplio.**

La herramienta puede orientar sobre posibles derechos y normas, pero no necesariamente podrá valorar todas las circunstancias de un caso real. Por ejemplo, puede no tener información suficiente sobre los hechos, las pruebas, las actuaciones de la entidad responsable o las condiciones particulares del usuario. Por eso, su respuesta será una orientación inicial y no una decisión sobre la procedencia o el resultado de una tutela.

### 7.2 ¿Qué datos procesa?

| **Elemento** | **Descripción** |
|---|---|
| **Qué entra** | Una descripción ficticia de una situación relacionada con una barrera de acceso a medicamentos. |
| **Qué se guarda** | El corpus jurídico y los archivos necesarios para el funcionamiento del proyecto. |
| **Qué no se guarda** | Nombres, números de identificación, historias clínicas ni otros datos personales reales de usuarios de prueba. |
| **Qué sale** | Una orientación jurídica basada en las fuentes incorporadas, con identificación de posibles derechos y normas relevantes. |

### 7.3 ¿Por qué no reemplaza al abogado?

tutelaapp no reemplaza al abogado porque una herramienta de inteligencia artificial no puede asumir por sí sola toda la responsabilidad del análisis jurídico. Su respuesta depende de la información que recibe y de las fuentes que tiene incorporadas. Si el caso contiene hechos incompletos o información que no está en el corpus, puede quedarse corta. Además, no puede garantizar que una tutela sea concedida ni valorar todas las circunstancias particulares de una persona. El abogado debe analizar los hechos, las pruebas, las normas y la jurisprudencia aplicable. También debe verificar que la orientación sea correcta y adecuada al caso concreto. Por eso, tutelaapp será una herramienta de apoyo académico y de comprensión inicial, no un sustituto de la consulta jurídica profesional.

---

## ✅ Parte 8 — Entregables finales

### 8.1 Definition of Done

| Requisito | Evidencia | Estado |
|---|---|---|
| **Solución funcionando** | URL pública de tutelaapp. | ⬜ Pendiente |
| **Usuario real** | Evidencia de que una persona externa al curso probó la herramienta. | ⬜ Pendiente |
| **Repositorio con historial** | Commits y bitácora semanal en GitHub. | ⬜ Pendiente |
| **Análisis crítico** | Parte 7 completada. | 🟡 En desarrollo |
| **Partes 1–7 completas** | README actualizado. | 🟡 En desarrollo |

### 8.2 Evidencia del usuario real

Cuando la herramienta esté funcionando, una persona externa al curso probará tutelaapp utilizando un caso ficticio. Se guardará evidencia de la prueba, por ejemplo, una captura de pantalla o un testimonio breve, sin incluir datos personales reales.

**Usuario de prueba:** `[Se completará cuando se realice la prueba]`  
**Fecha de prueba:** `[Se completará]`  
**Caso utilizado:** `[Descripción del caso ficticio]`  
**Resultado:** `[Qué respondió la herramienta y qué se observó]`  
**Evidencia:** `[Enlace o archivo de evidencia]`

### 8.3 Presentación final

La presentación tendrá una duración aproximada de **5 minutos** y explicará:

1. El problema jurídico que busca resolver tutelaapp.
2. Cómo funciona la herramienta.
3. Qué fuentes jurídicas utiliza.
4. Una demostración de un caso ficticio.
5. Sus límites y por qué no reemplaza al abogado.

### 8.4 Conclusión del proyecto

tutelaapp busca demostrar cómo la inteligencia artificial puede utilizarse como herramienta de apoyo para comprender problemas jurídicos relacionados con el acceso a medicamentos. El proyecto combina conocimientos de Derecho, selección de fuentes, diseño de instrucciones y evaluación crítica de resultados. Su propósito no es reemplazar el trabajo jurídico profesional, sino facilitar una primera orientación académica basada en un corpus jurídico previamente seleccionado.

---

*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖
