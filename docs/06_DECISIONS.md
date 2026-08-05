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