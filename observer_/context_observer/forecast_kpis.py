from observer_.context_observer.observer.abs_observer import AbsObserver


class ForecastKPIs(AbsObserver):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        self._kpis.attach(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)

    def update(self, value=None):
        type(self)._open_tickets = self._kpis.open_tickets
        type(self)._closed_tickets = self._kpis.closed_tickets
        type(self)._new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(f'Forecast current open tickets: {type(self)._open_tickets}')
        print(f'New tickets in last hour: {type(self)._closed_tickets}')
        print(f'Tickets closed in last hour: {type(self)._new_tickets}')
        print('*****\n')
