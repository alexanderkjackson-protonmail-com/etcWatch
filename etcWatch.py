import threading
from typing import Dict, Any, List
import queue

# ------------------ Event/Message Class ------------------ #

class Message:
    def __init__(self, event_type: str, data: Dict[str, Any]):
        self.event_type = event_type
        self.data = data


# ------------------ Core Interfaces ------------------ #

class EventProcessor:
    def process_event(self, event: Message):
        raise NotImplementedError

class EventPersister:
    def persist_event(self, event: Message):
        raise NotImplementedError

class Subscriber:
    def handle_event(self, event: Message):
        raise NotImplementedError


# ------------------ Concrete Implementations ------------------ #

class BatchingEventProcessor(EventProcessor):
    def process_event(self, event: Message):
        # Batching logic
        pass

class DatabaseEventPersister(EventPersister):
    def persist_event(self, event: Message):
        # Database persistence logic
        pass

class RealTimeEventProcessor(EventProcessor):
    def process_event(self, event: Message):
        # Real-time processing logic
        pass

class EmailNotifierSubscriber(Subscriber):
    def handle_event(self, event: Message):
        # Handle and send email based on event data
        pass


# ------------------ Pub-Sub Mechanism ------------------ #

class PubSub:
    def __init__(self):
        self.subscribers: Dict[str, List[Subscriber]] = {}

    def subscribe(self, event_type: str, subscriber: Subscriber):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    def publish(self, event: Message):
        if event.event_type in self.subscribers:
            for subscriber in self.subscribers[event.event_type]:
                # Using threading to handle events concurrently
                threading.Thread(target=subscriber.handle_event, args=(event,)).start()


# ------------------ Sample Usage ------------------ #

def main():
    # Configurations (could come from a file or other sources)
    config = {
        "processor_type": "batching",
        "persister_type": "database"
    }

    # Instantiate PubSub mechanism
    pubsub = PubSub()

    # Factory method for event processors based on config
    if config["processor_type"] == "batching":
        processor = BatchingEventProcessor()
    elif config["processor_type"] == "real_time":
        processor = RealTimeEventProcessor()
    else:
        raise ValueError(f"Unsupported processor_type: {config['processor_type']}")

    # Example: Subscribing to an event type for notifications
    pubsub.subscribe("file_changed", EmailNotifierSubscriber())

    # Example: Publishing an event
    message = Message(event_type="file_changed", data={"file_name": "sample.txt", "action": "updated"})
    pubsub.publish(message)

if __name__ == "__main__":
    main()
