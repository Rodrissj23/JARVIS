# TASKS

**Versión:** 1.0

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

Pendiente de definición al habilitar la tarea.

## Restricciones

- No modificar Orchestrator.
- No implementar lógica de decisiones.
- No integrar módulos externos sin autorización.

## Decisiones asociadas

Pendiente.

---

# TASK-005

## Estado

Pendiente.

## Nombre

Integrar Claude.

## Objetivo

Conectar el sistema Brain con Claude como motor de razonamiento.

## Alcance

Pendiente de definición al habilitar la tarea.

## Restricciones

- Claude no controla directamente UI.
- Claude no ejecuta acciones del sistema.
- La comunicación debe pasar por Brain.

## Decisiones asociadas

- ADR-002: Claude como motor principal de razonamiento.

---

# Regla de desarrollo

Una tarea debe:

1. Tener alcance definido antes de comenzar.
2. Tener restricciones claras.
3. Respetar la arquitectura existente.
4. No agregar funcionalidades futuras.
5. Ser revisada antes de marcarse como completada.