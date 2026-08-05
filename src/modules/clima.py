"""
Módulo Clima.

Según docs/01_ARCHITECTURE.md, cada módulo implementa una capacidad
independiente y no se comunica directamente con Brain, UI ni Voice,
ni con otros módulos (docs/05_TASKS.md - TASK-008). Su interfaz
pública es `can_handle` y `handle`, invocadas por el Orchestrator,
que es quien decide si esta solicitud le corresponde a este módulo o
debe derivarse a Brain.

Consulta el clima actual mediante Open-Meteo, que no requiere API key
(decisión tomada durante TASK-008). La ciudad es fija pero
configurable mediante el parámetro `city` del constructor.
"""

import requests

_KEYWORDS = ("clima", "temperatura")

_GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

DEFAULT_CITY = "Buenos Aires"


class ClimaModule:
    """Responde solicitudes relacionadas con el clima actual de una ciudad configurable."""

    def __init__(self, city: str = DEFAULT_CITY) -> None:
        self._city = city
        self._coordinates = None

    def can_handle(self, text: str) -> bool:
        """Indica si este módulo puede resolver `text`."""
        return any(keyword in text.lower() for keyword in _KEYWORDS)

    def handle(self, text: str) -> str:
        """Devuelve la temperatura actual de la ciudad configurada.

        Debe llamarse únicamente cuando `can_handle(text)` es `True`.
        """
        latitude, longitude = self._get_coordinates()
        temperature = self._get_current_temperature(latitude, longitude)
        return f"En {self._city} hay {temperature}°C."

    def _get_coordinates(self) -> tuple:
        """Resuelve latitud/longitud de la ciudad configurada.

        Se resuelve una única vez y se guarda en caché, ya que la
        ciudad es fija durante la vida de la instancia.
        """
        if self._coordinates is None:
            response = requests.get(
                _GEOCODING_URL,
                params={"name": self._city, "count": 1},
                timeout=5,
            )
            response.raise_for_status()
            results = response.json().get("results")
            if not results:
                raise RuntimeError(f"No se encontró la ciudad configurada: {self._city}")
            self._coordinates = (results[0]["latitude"], results[0]["longitude"])
        return self._coordinates

    def _get_current_temperature(self, latitude: float, longitude: float) -> float:
        """Consulta la temperatura actual para unas coordenadas dadas."""
        response = requests.get(
            _FORECAST_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": True,
            },
            timeout=5,
        )
        response.raise_for_status()
        return response.json()["current_weather"]["temperature"]
