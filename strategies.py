import json
import redis
from kafka import KafkaProducer
from abc import ABC, abstractmethod

class StorageStrategy(ABC):
    @abstractmethod
    def send(self, data):
        pass

class ConsoleStrategy(StorageStrategy):
    def send(self, data):
        print(f"--- [CONSOLE] ---\n{data}\n")

class RedisStrategy(StorageStrategy):
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def send(self, data):
        self.client.lpush('budget_data', json.dumps(data))
        print(f"Data sent to Docker REDIS")

class KafkaStrategy(StorageStrategy):
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send(self, data):
        self.producer.send('budget_topic', data)
        print(f"Message sent to Docker KAFKA")