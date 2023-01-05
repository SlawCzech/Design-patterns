from observer_.context_observer.current_kpis import CurrentKPIs
from observer_.context_observer.forecast_kpis import ForecastKPIs
from observer_.context_observer.kpis import KPIs

with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(21, 37, 42)
        kpis.set_kpis(54, 89, 24)
        kpis.set_kpis(77, 32, 90)

print(f'\nExited context managers\n\n')
kpis.set_kpis(6, 6, 6)
