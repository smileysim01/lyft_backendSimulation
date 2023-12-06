from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_on):
        self.warning_light_on = warning_light_on

    def engine_should_be_serviced(self):
        return self.warning_light_on
