# etcWatch 

A Python-based system for monitoring file changes and acting upon specific events. Utilizing a pub-sub, event-sourcing architecture, this project aims to offer a simple but extensible solution for various file event-driven requirements.

The current Python-based implementation likely will not be fast or efficient enough to monitor large portions of a production system. The main goal of this particular implementation is to be as simple as possible while still using an extensible scaffolding. If this works reasonably well, it will likely be rewritten, perhaps in a different language, likely with a different inotify library, or a library using another language and an FFI will be provided with the necessary facilities to ensure this is performant-enough to track changes to production systems.

## Features

- Event-driven architecture: Quickly act upon changes with custom handlers.
- Multi-threaded: Handle multiple events concurrently without blocking.
- Configurable: Adjust the behavior of the system based on requirements.
- Integrated with `inotify-simple` for efficient file change notifications.

## Requirements

- Python 3.10.12
- poetry (for dependency management)

## Installation

1. Clone the repository:
```
git clone https://github.com/alexanderkjackson-protonmail-com/etcWatch
```

2. Navigate to the project folder:
```
cd etcWatch 
```

3. Install dependencies using poetry:
```
poetry install
```

## Usage

Simply run the main python file:

```
poetry run python etcWatch.py 
```

## Configuration

The system's behavior can be configured by modifying the `config` dictionary in the main python file. You can select different event processors and persisters based on your requirements.

## Extending the System

### Adding a New Event Processor

1. Implement a new class that inherits from the `EventProcessor` interface.
2. Override the `process_event` method with your custom logic.
3. Adjust the configuration to use your new processor.

### Subscribing to Events

Use the `PubSub` class to subscribe to specific event types. You can create custom subscribers by implementing the `Subscriber` interface and overriding the `handle_event` method.

## Dependencies

This project utilizes the `inotify-simple` library to efficiently detect file changes.

## License

GNU GPL v3

## Contributing

Feel free to open issues, suggest improvements, or submit pull requests. When submitting pull requests, your code doesn't have to be good or tested. I'll take anything!
