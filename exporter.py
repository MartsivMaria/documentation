from strategies import StorageStrategy

class DataExporter:
    def __init__(self, strategy: StorageStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: StorageStrategy):
        self._strategy = strategy

    def export(self, data_list):
        for row in data_list:
            self._strategy.send(row)