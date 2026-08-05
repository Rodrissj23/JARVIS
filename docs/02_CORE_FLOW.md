# Core Flow

**Versión:** 1.0

---

# Inicio

Al iniciar Windows, JARVIS debe ejecutarse automáticamente.

Al finalizar la carga, JARVIS entra en estado de reposo.

En este estado únicamente escucha la palabra de activación.

---

# Activación

JARVIS puede activarse de dos maneras:

- Mediante la palabra de activación.
- Mediante el botón del micrófono de la interfaz.

Una vez activado, comienza a escuchar la solicitud del usuario.

---

# Procesamiento

La voz del usuario se convierte en texto.

El texto es enviado al Orchestrator.

El Orchestrator decide si la solicitud debe resolverse mediante un módulo o mediante Claude.

Una vez obtenida la respuesta, el flujo continúa.

---

# Respuesta

La respuesta debe mostrarse en la interfaz.

La respuesta debe reproducirse mediante voz.

La experiencia principal de JARVIS es la conversación por voz.

---

# Conversación

Después de responder, JARVIS permanece en modo conversación.

Mientras exista actividad del usuario, la conversación continúa.

Cada nueva interacción reinicia el temporizador.

---

# Reposo

Si transcurren cuatro minutos sin interacción del usuario, JARVIS informa que vuelve al modo de espera.

Luego retorna al estado de reposo.

---

# Estados

Los estados oficiales de JARVIS son:

- Inicializando
- Reposo
- Escuchando
- Procesando
- Hablando
- Error

La interfaz debe representar visualmente el estado actual.

---

# Principios

El usuario nunca debe preocuparse por qué módulo está trabajando.

Toda la experiencia debe sentirse como una única conversación.

La transición entre estados debe ser clara y natural.