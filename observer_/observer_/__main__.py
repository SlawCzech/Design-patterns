from observer_.observer_.current_kpis import CurrentKPIs
from observer_.observer_.forecast_kpis import ForecastKPIs
from observer_.observer_.kpis import KPIs

kpis = KPIs()

current_kpis = CurrentKPIs(kpis)
forecast_kpis = ForecastKPIs(kpis)


kpis.set_kpis(21, 37, 42)
kpis.set_kpis(54, 89, 24)
kpis.set_kpis(77, 32, 90)

print(f'\nDetaching the current KPIs observer\n\n')
kpis.detach(current_kpis)

kpis.set_kpis(6, 6, 6)
