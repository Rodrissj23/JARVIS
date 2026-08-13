# Roadmap

**Versión:** 2.0  
**Actualizado:** 12/08/2026

---

# Estado actual

JARVIS queda como proyecto de asistente general de escritorio. Parte de la experimentación de voz pasó temporalmente a WORK AGENT, donde ya se validaron parser por entidades, respuesta hablada, selección de micrófono y arquitectura STT separada del cerebro.

Estado: **Pausado / investigación reutilizable en WORK AGENT**

---

# Fase 0 — Fundación ✅

- [x] Definir proyecto.
- [x] Definir arquitectura.
- [x] Definir flujo principal.
- [x] Crear estructura inicial.
- [x] Validar entorno Python y audio.
- [x] Separar UI, Voice, Orchestrator, Brain y Modules.

---

# Fase 1 — Núcleo

- [x] UI PySide6 inicial.
- [x] Estados visuales base.
- [ ] Orchestrator estable.
- [ ] STT local definitivo.
- [ ] TTS natural definitivo.
- [ ] Wake word.

Decisión actual: priorizar STT local con Whisper/faster-whisper y reutilizar lo aprendido en WORK AGENT.

---

# Fase 2 — Asistente funcional

- Conversación continua.
- Hora y fecha.
- Clima.
- Comandos locales.
- Memoria corta de contexto.

---

# Fase 3 — Sistema modular

- WhatsApp.
- Navegador.
- Archivos.
- Spotify.
- Python.
- Integración opcional con WORK AGENT para tareas laborales.

---

# Fase 4 — Experiencia JARVIS

- Voz natural estable.
- Wake word.
- Ejecución en segundo plano.
- Inicio automático.
- UI reactiva al estado de voz.
- Acciones encadenadas.

---

# Regla

JARVIS no debe duplicar motores ya resueltos en WORK AGENT: la lógica reutilizable de voz, parser y skills se comparte o se porta conscientemente.
