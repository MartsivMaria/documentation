import json
from reader import read_dataset
from exporter import DataExporter
from strategies import ConsoleStrategy, RedisStrategy, KafkaStrategy

STRATEGIES_MAP = {
    "console": ConsoleStrategy(),
    "redis": RedisStrategy(),
    "kafka": KafkaStrategy()
}

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    storage_type = config.get("storage_type", "console")
    strategy = STRATEGIES_MAP.get(storage_type, ConsoleStrategy())
    
    dataset = read_dataset('expenses.csv')
    
    exporter = DataExporter(strategy)
    print(f"Running export using: {storage_type.upper()}")
    exporter.export(dataset)

if __name__ == "__main__":
    main()