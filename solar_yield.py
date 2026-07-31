"""Transparent preliminary photovoltaic energy-yield calculations."""

from math import isfinite


def annual_energy(
    area_m2: float,
    efficiency: float,
    irradiance_kwh_m2: float,
    performance_ratio: float = 0.8,
    years: int = 0,
    degradation_rate: float = 0.005,
) -> float:
    values = (area_m2, efficiency, irradiance_kwh_m2, performance_ratio)
    if not all(isfinite(v) and v > 0 for v in values):
        raise ValueError("area, efficiency, irradiance and performance ratio must be positive")
    if efficiency > 1 or performance_ratio > 1:
        raise ValueError("efficiency and performance ratio cannot exceed 1")
    if years < 0 or not 0 <= degradation_rate < 1:
        raise ValueError("invalid degradation inputs")
    first_year = area_m2 * efficiency * irradiance_kwh_m2 * performance_ratio
    return first_year * (1 - degradation_rate) ** years


def capacity_factor(annual_kwh: float, rated_kw: float) -> float:
    if annual_kwh < 0 or rated_kw <= 0:
        raise ValueError("annual energy must be non-negative and rated power positive")
    return annual_kwh / (rated_kw * 8760)
