from observer_.context_observer.observer.abs_subject import AbsSubject


# Key performance indicator
class KPIs(AbsSubject):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def open_tickets(self):
        return type(self)._open_tickets

    @property
    def closed_tickets(self):
        return type(self)._closed_tickets

    @property
    def new_tickets(self):
        return type(self)._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        type(self)._open_tickets = open_tickets
        type(self)._closed_tickets = closed_tickets
        type(self)._new_tickets = new_tickets
        self.notify()
