# TASKS

**Versión:** 1.1

---

# Objetivo

Gestionar las tareas de desarrollo del proyecto JARVIS.

Cada tarea debe tener definido:

- Objetivo.
- Alcance.
- Restricciones.
- Decisiones asociadas cuando corresponda.

Solo una TASK puede encontrarse en estado "Pendiente" al mismo tiempo.

---

# TASK-001

## Estado

Completada.

## Nombre

Crear la estructura inicial del proyecto.

## Objetivo

Construir la base inicial del proyecto sin implementar funcionalidades.

## Alcance

- Crear la estructura de carpetas.
- Crear los archivos principales.
- Crear README.md.
- Crear main.py.
- Crear requirements.txt.
- Preparar los paquetes principales del sistema.

## Restricciones

- No implementar funcionalidades.
- No agregar dependencias innecesarias.
- No crear lógica de negocio.
- No modificar la arquitectura definida.

## Decisiones asociadas

- ADR-005: Estructura de código fuente con directorio src.

---

# TASK-002

## Estado

Completada.

## Nombre

Crear la ventana principal.

## Objetivo

Crear la base inicial de la interfaz gráfica de JARVIS sin lógica de negocio ni estados visuales.

## Alcance

- Crear la ventana principal de la aplicación.
- Configurar el punto inicial de la interfaz gráfica.
- Preparar la UI para futuras capas visuales.
- Integrar el arranque básico desde main.py.

## Restricciones

- No implementar estados visuales.
- No implementar animaciones.
- No implementar lógica de negocio.
- No conectar con Voice, Orchestrator, Brain o Modules.

## Decisiones asociadas

- ADR-007: Framework de interfaz gráfica PySide6.

---

# TASK-003

## Estado

Completada.

## Nombre

Implementar los estados visuales.

## Objetivo

Crear el sistema visual que represente el estado actual de JARVIS.

## Alcance

- Implementar los estados visuales oficiales:
  - Inicializando.
  - Reposo.
  - Escuchando.
  - Procesando.
  - Hablando.
  - Error.
- Mostrar visualmente el estado actual.
- Preparar la interfaz para futuras integraciones.

## Restricciones

- No implementar reconocimiento de voz.
- No implementar respuestas de voz.
- No implementar lógica del Orchestrator.
- No integrar Claude.
- No crear funcionalidades fuera de la interfaz visual.

## Decisiones asociadas

- ADR-006: Identidad visual híbrida JARVIS.

---

# TASK-004

## Estado

Completada.

## Nombre

Implementar el motor de voz.

## Objetivo

Crear la capa encargada de recibir y emitir audio.

## Alcance

- Implementar la captura de audio desde el micrófono.
- Implementar Speech To Text mediante Whisper.
- Implementar Text To Speech mediante Piper.
- Crear VoiceEngine como interfaz pública de la capa Voice.
- Preparar la capa para futuras estrategias de captura de audio.

## Restricciones

- No modificar el Orchestrator.
- No implementar lógica de decisiones.
- No implementar la detección de palabra de activación.
- No integrar Claude.
- No modificar componentes fuera de la capa Voice.

## Decisiones asociadas

- ADR-009: Whisper como motor de Speech To Text.
- ADR-010: Piper como motor de Text To Speech.

---

# TASK-005

## Estado

Completada.

## Nombre

Implementar el Orchestrator.

## Objetivo

Construir el componente central encargado de coordinar la comunicación entre los distintos componentes del sistema.

## Alcance

- Crear la estructura del Orchestrator.
- Definir su interfaz pública.
- Preparar la comunicación con UI.
- Preparar la comunicación con Voice.
- Preparar la comunicación con Brain.
- Preparar la comunicación con Modules.
- Mantener un único punto de coordinación del sistema.

## Restricciones

- No integrar Claude.
- No implementar módulos.
- No implementar lógica de conversación.
- No ejecutar acciones del sistema.
- No modificar otros componentes fuera del alcance de la tarea.

## Decisiones asociadas

- ADR-001: Arquitectura modular.
- ADR-004: Desarrollo incremental.

---

# TASK-006

## Estado

Pendiente.

## Nombre

Integrar Brain (Claude).

## Objetivo

Implementar la comunicación entre el Brain y Claude como motor principal de razonamiento.

## Alcance

Pendiente de definición al habilitar la tarea.

## Restricciones

- El Brain no debe comunicarse directamente con la UI.
- El Brain no debe comunicarse directamente con Voice.
- Toda comunicación debe realizarse a través del Orchestrator.

## Decisiones asociadas

- ADR-002: Claude como motor principal de razonamiento.

---

# TASK-007

## Estado

Bloqueada.

## Nombre

Implementar el primer módulo del sistema.

## Objetivo

Crear el primer módulo funcional integrado al Orchestrator para validar la arquitectura modular.

## Alcance

Pendiente de definición al habilitar la tarea.

## Restricciones

- Toda comunicación debe pasar por el Orchestrator.
- No acceder directamente a Brain, UI o Voice.

## Decisiones asociadas

Pendiente.

---

# TASK-008

## Estado

Bloqueada.

## Nombre

Implementar módulos adicionales.

## Objetivo

Incorporar nuevas capacidades al sistema respetando la arquitectura modular.

## Alcance

Pendiente de definición al habilitar la tarea.

## Restricciones

- Todos los módulos deben ser independientes.
- No comunicarse entre sí.
- Toda coordinación debe realizarse mediante el Orchestrator.

## Decisiones asociadas

Pendiente.

---

# Regla de desarrollo

Una tarea debe:

1. Tener alcance definido antes de comenzar.
2. Tener restricciones claras.
3. Respetar la arquitectura existente.
4. No agregar funcionalidades futuras.
5. Ser revisada antes de marcarse como completada.
6. Solo puede existir una TASK en estado **Pendiente** al mismo tiempo.