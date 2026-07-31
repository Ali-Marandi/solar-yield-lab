# Solar Yield Lab

A dependency-free Python calculator for transparent preliminary photovoltaic
yield estimates.

```python
from solar_yield import annual_energy

kwh = annual_energy(area_m2=10, efficiency=0.20,
                    irradiance_kwh_m2=1800, performance_ratio=0.8)
```

Features: performance-ratio losses, annual module degradation, capacity-factor
calculation, input validation, tests, and CI.

```bash
python -m unittest -v
```

This is a screening and education tool, not a bankable PV simulation.
