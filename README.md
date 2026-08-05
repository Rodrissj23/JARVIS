# JARVIS

Asistente inteligente para Windows 11 inspirado en J.A.R.V.I.S. de Iron Man.

JARVIS ofrece una experiencia de interacción natural mediante voz, permitiendo
conversar, obtener información y ejecutar acciones desde un único asistente.

## Estado del proyecto

En desarrollo — Fase 0 (Fundación).

## Arquitectura

El proyecto está construido mediante una arquitectura modular, coordinada por
un Orchestrator central. Cada componente tiene una única responsabilidad:

- **UI** — Interfaz gráfica y estados visuales.
- **Voice** — Captura de audio, Speech To Text y Text To Speech.
- **Orchestrator** — Coordina el flujo completo del sistema.
- **Brain** — Comunicación con Claude.
- **Modules** — Capacidades independientes (Hora, Clima, Spotify, etc.).

Ver `docs/01_ARCHITECTURE.md` para el detalle completo.

## Estructura del proyecto

```
jarvis/
├── main.py              # Punto de entrada
├── requirements.txt      # Dependencias
├── docs/                 # Documentación del proyecto
└── src/
    ├── ui/
    ├── voice/
    ├── orchestrator/
    ├── brain/
    └── modules/
```

## Documentación

Toda la documentación del proyecto se encuentra en la carpeta `docs/`:

- `00_PROJECT.md` — Objetivo y alcance.
- `01_ARCHITECTURE.md` — Arquitectura del sistema.
- `02_CORE_FLOW.md` — Flujo principal.
- `03_ROADMAP.md` — Fases del proyecto.
- `04_RULES.md` — Reglas obligatorias de desarrollo.
- `05_TASKS.md` — Tareas y su estado.
- `06_DECISIONS.md` — Decisiones de arquitectura registradas.
