# Arquitectura

**Versión:** 1.0

---

# Filosofía

JARVIS está construido mediante una arquitectura modular.

Cada componente tiene una única responsabilidad.

Ningún módulo debe conocer el funcionamiento interno de otro módulo.

Toda comunicación pasa por el Orchestrator.

---

# Componentes

## UI

Responsabilidad:

Interfaz gráfica.

Estados visuales.

Animaciones.

Interacción del usuario.

La UI nunca debe contener lógica de negocio.

---

## Voice

Responsabilidad:

Captura de audio.

Speech To Text.

Text To Speech.

Detección de palabra de activación.

La capa de voz nunca decide qué hacer con una solicitud.

---

## Orchestrator

Responsabilidad:

Es el corazón del sistema.

Recibe todas las solicitudes.

Decide qué módulo utilizar.

Controla el flujo completo.

Controla el estado de JARVIS.

Toda solicitud debe pasar por el Orchestrator.

---

## Brain

Responsabilidad:

Comunicación con Claude.

Construcción del contexto.

Recepción de respuestas.

Nunca interactúa directamente con la interfaz.

Nunca ejecuta acciones del sistema.

---

## Modules

Responsabilidad:

Implementar capacidades independientes.

Ejemplos:

- Hora
- Clima
- Calendario
- WhatsApp
- Spotify
- Navegador
- Archivos
- Python

Cada módulo debe ser independiente.

Agregar un módulo nuevo nunca debe requerir modificar otro módulo.

---

# Flujo

Usuario

↓

Voice

↓

Orchestrator

↓

Brain o Module

↓

Orchestrator

↓

Voice

↓

Usuario

---

# Reglas

La UI nunca habla con Claude.

Voice nunca habla con Claude.

Los módulos nunca hablan entre sí.

Solo el Orchestrator puede decidir el flujo.

El Orchestrator nunca debe contener lógica específica de un módulo.

---

# Objetivo

La arquitectura debe permitir agregar nuevas capacidades sin modificar el núcleo del sistema.