from __future__ import annotations

from datetime import datetime, timedelta, timezone

from ibm_watsonx_orchestrate.agent_builder.tools import tool


# Fuso horário fixo UTC
FUSO_PORTUGAL = timezone.utc
INICIO_VERAO = datetime(2026, 6, 21, 0, 0, 0, tzinfo=FUSO_PORTUGAL)


@tool(
    name="hours_until_portugal_summer_2026",
    display_name="Horas Até ao Verão em Portugal 2026",
    description=(
        "Calcula o número total de horas restantes até ao início do verão em Portugal "
        "(21 de Junho de 2026, 00:00, Europe/Lisbon)."
    ),
)
def hours_until_portugal_summer_2026() -> dict:
    """Devolve as horas restantes até 21 de Junho de 2026 em Portugal (Europe/Lisbon)."""
    agora = datetime.now(tz=FUSO_PORTUGAL)
    diferenca = INICIO_VERAO - agora
    horas_restantes = diferenca.total_seconds() / 3600

    return {
        "agora_portugal": agora.isoformat(),
        "inicio_verao_portugal": INICIO_VERAO.isoformat(),
        "horas_restantes": horas_restantes,
        "ja_passou": horas_restantes < 0,
    }
