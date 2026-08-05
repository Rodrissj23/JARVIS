# Decisiones del Proyecto

**Versión:** 1.0

---

# Objetivo

Registrar decisiones importantes de arquitectura y desarrollo.

Una decisión registrada no debe modificarse sin documentar el motivo del cambio.

---

# ADR-001

## Nombre

Arquitectura modular.

## Estado

Aceptada.

## Fecha

Inicio del proyecto.

## Decisión

JARVIS será construido mediante módulos independientes conectados por un Orchestrator.

## Motivo

Permitir agregar nuevas capacidades sin modificar el núcleo del sistema.

---

# ADR-002

## Nombre

Claude como motor principal de razonamiento.

## Estado

Aceptada.

## Fecha

Inicio del proyecto.

## Decisión

Claude será utilizado como cerebro principal para tareas que requieran razonamiento.

## Motivo

Proporciona capacidades avanzadas de comprensión y generación de respuestas.

---

# ADR-003

## Nombre

Interacción principal mediante voz.

## Estado

Aceptada.

## Fecha

Inicio del proyecto.

## Decisión

La voz será la interfaz principal de interacción.

## Motivo

La experiencia buscada es la de un asistente personal, no un chatbot tradicional.

---

# ADR-004

## Nombre

Desarrollo incremental.

## Estado

Aceptada.

## Fecha

Inicio del proyecto.

## Decisión

JARVIS será construido desde un núcleo mínimo hacia funcionalidades más avanzadas.

## Motivo

Reducir complejidad y permitir validación constante.

---

# ADR-005

## Nombre

Estructura de código fuente con directorio src.

## Estado

Aceptada.

## Fecha

Después de TASK-001.

## Decisión

El código fuente de JARVIS estará contenido dentro del directorio src.

## Motivo

Separar el código de la configuración, documentación y archivos externos del proyecto.

---

# ADR-006

## Nombre

Identidad visual híbrida JARVIS.

## Estado

Aceptada.

## Fecha

Después de TASK-001.

## Decisión

JARVIS utilizará una interfaz visual híbrida entre el estilo J.A.R.V.I.S. de Iron Man y un asistente moderno minimalista.

La interfaz tendrá:

- Un núcleo visual central inspirado en un reactor.
- Estados visuales claros.
- Diseño limpio.
- Sensación de asistente personal avanzado.
- Evitar una interfaz cargada de elementos innecesarios.

## Motivo

Buscar una experiencia futurista e inmersiva sin convertir la aplicación en una simple demostración visual.

JARVIS debe sentirse como un producto funcional.

---

# ADR-007

## Nombre

Framework de interfaz gráfica.

## Estado

Aceptada.

## Fecha

Después de TASK-002.

## Decisión

JARVIS utilizará PySide6 como framework principal para la interfaz gráfica.

## Motivo

Permite crear una interfaz moderna, escalable y compatible con la experiencia visual buscada para JARVIS.

Su sistema de componentes facilita futuras animaciones, estados visuales y elementos interactivos.

---

# ADR-008

## Nombre

Representación visual mediante núcleo central.

## Estado

Aceptada.

## Fecha

Después de TASK-002.

## Decisión

JARVIS utilizará un núcleo visual central inspirado en un reactor como elemento principal para representar sus estados.

La interfaz priorizará el núcleo como punto de interacción visual, evitando paneles cargados de información.

## Motivo

Crear una experiencia inmersiva y simple, donde el usuario perciba a JARVIS como un asistente activo y no como una aplicación tradicional.

# ADR-009

## Nombre

Motor de reconocimiento de voz.

## Estado

Aceptada.

## Fecha

Antes de TASK-004.

## Decisión

JARVIS utilizará Whisper como motor principal de reconocimiento de voz (STT).

La ejecución inicial será local para mantener independencia de servicios externos y permitir evolución futura del sistema.

## Motivo

Whisper ofrece alta precisión de reconocimiento, soporte multilenguaje y una arquitectura compatible con un asistente personal de escritorio.

---

# ADR-010

## Nombre

Motor de síntesis de voz.

## Estado

Aceptada.

## Fecha

Antes de TASK-004.

## Decisión

JARVIS utilizará Piper TTS como motor principal de síntesis de voz (TTS).

La ejecución inicial será local para mantener independencia de servicios externos y permitir una evolución progresiva del sistema.

## Motivo

Piper TTS ofrece una solución ligera, rápida y compatible con ejecución local, permitiendo que JARVIS genere respuestas habladas sin depender de servicios externos.

# ADR-011: Configuración externa mediante archivo .env

## Estado

Aceptada.

## Contexto

Durante la integración del flujo principal del sistema (TASK-009), fue necesario definir cómo se gestionaría la configuración de componentes que requieren valores externos.

El componente VoiceEngine necesita recibir la ruta del modelo de voz de Piper TTS. Mantener esta ruta directamente en el código generaría un acoplamiento innecesario y dificultaría cambiar configuraciones sin modificar la implementación.

## Decisión

La configuración local del sistema se gestionará mediante un archivo `.env`.

Las variables de configuración serán cargadas desde el entorno de ejecución utilizando `python-dotenv`.

La ruta del modelo Piper será definida mediante:

JARVIS_TTS_MODEL_PATH

## Consecuencias

### Positivas

- Permite modificar configuraciones sin cambiar código.
- Evita valores sensibles o dependientes del entorno dentro del repositorio.
- Facilita futuras configuraciones adicionales del sistema.
- Mantiene los componentes desacoplados de su configuración específica.

### Negativas

- Requiere configurar correctamente el archivo `.env` antes de ejecutar la aplicación.
- Agrega una dependencia adicional (`python-dotenv`).

## Alcance

Esta decisión aplica inicialmente a la configuración del modelo Piper TTS, pero establece el mecanismo base para futuras configuraciones externas del sistema.