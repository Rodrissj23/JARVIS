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