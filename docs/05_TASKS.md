# TASK-006

## Estado

Completada.

## Nombre

Integrar Brain (Claude).

## Objetivo

Implementar la comunicación entre el Brain y Claude como motor principal de razonamiento.

## Alcance

- Implementar la comunicación con Claude mediante el SDK oficial de Anthropic.
- Mantener el historial de conversación en memoria.
- Construir el contexto de conversación.
- Preparar el Brain para su integración con el Orchestrator.
- Mantener el modelo configurable.

## Restricciones

- El Brain no debe comunicarse directamente con la UI.
- El Brain no debe comunicarse directamente con Voice.
- Toda comunicación debe realizarse a través del Orchestrator.
- No ejecutar acciones del sistema.
- No modificar componentes fuera del alcance de la tarea.

## Decisiones asociadas

- ADR-002: Claude como motor principal de razonamiento.

---

# TASK-007

## Estado

Completada.

## Nombre

Implementar el primer módulo del sistema.

## Objetivo

Crear el primer módulo funcional integrado al Orchestrator para validar la arquitectura modular.

## Alcance

- Implementar el primer módulo funcional del sistema.
- Integrar el módulo con el Orchestrator.
- Definir la interfaz pública de los módulos mediante `can_handle()` y `handle()`.
- Permitir que el Orchestrator decida entre módulos y Brain.
- Validar la arquitectura modular.

## Restricciones

- Toda comunicación debe pasar por el Orchestrator.
- Los módulos no deben acceder directamente a Brain, UI o Voice.
- No implementar funcionalidades fuera del primer módulo.

## Decisiones asociadas

- ADR-001: Arquitectura modular.

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

# TASK-009

## Estado

Pendiente.

## Nombre

Integrar el flujo principal del sistema.

## Objetivo

Conectar los componentes principales de JARVIS respetando la arquitectura definida, preparando el flujo completo de comunicación entre UI, Voice, Orchestrator, Brain y Modules.

## Alcance

- Instanciar los componentes principales del sistema.
- Conectar UI, Voice, Brain y Orchestrator.
- Registrar los módulos iniciales en el Orchestrator.
- Preparar el punto de entrada de la aplicación para la integración de los componentes.
- Mantener un único flujo de comunicación a través del Orchestrator.

## Restricciones

- No implementar ejecución continua.
- No implementar palabra de activación.
- No agregar nuevos módulos.
- No modificar la arquitectura existente.
- No implementar funcionalidades fuera del flujo principal.

## Decisiones asociadas

- ADR-001: Arquitectura modular.
- ADR-002: Claude como motor principal de razonamiento.
- ADR-007: Framework de interfaz gráfica PySide6.
- ADR-009: Motor de reconocimiento de voz Whisper.
- ADR-010: Motor de síntesis de voz Piper TTS.

---

# Regla de desarrollo

Una tarea debe:

1. Tener alcance definido antes de comenzar.
2. Tener restricciones claras.
3. Respetar la arquitectura existente.
4. No agregar funcionalidades futuras.
5. Ser revisada antes de marcarse como completada.
6. Solo puede existir una TASK en estado **Pendiente** al mismo tiempo.