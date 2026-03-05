# Port Scanner

A professional-grade, multithreaded TCP port scanner written in Python.

## Features

- **Multithreaded Scanning**: Uses a worker-thread model with `queue.Queue` for efficient port scanning
- **Service Detection**: Identifies standard services using `socket.getservbyport()`
- **Banner Grabbing**: Captures initial response strings from open ports to identify specific software versions
- **Thread-Safe Output**: Uses `threading.Lock()` to ensure clean, non-overlapping console output
- **Configurable Timeouts**: Granular timeout settings to prevent hanging
  - Connection timeout: 1.0s
  - Banner retrieval timeout: 2.0s

## Tech Stack

- **Language**: Python 3.8+
- **Libraries**: Standard library only (`socket`, `threading`, `queue`, `argparse`)
- **Code Formatting**: Black
- **Testing**: pytest
- **Package Management**: pyproject.toml

## How It Was Made

This project was built following a specification-driven development approach using OpenSpec and OpenCode.

### Development Process

1. **Project Setup**: Created `pyproject.toml` with Black and pytest configuration
2. **Core Implementation**: Built the scanner module (`scanner.py`) with:
   - `get_service_name()` - Service detection using `socket.getservbyport()`
   - `banner_grab()` - Banner grabbing with configurable timeout
   - `scan_port()` - Single port scanning with connection detection
   - `thread_worker()` - Worker thread for processing port queue
   - `scan_ports()` - Main scanning function using thread pool
3. **CLI Interface**: Created `__main__.py` with argparse for command-line argument parsing
4. **Testing**: Wrote unit tests using pytest with mocking for socket operations
5. **Documentation**: Created comprehensive README with usage examples

### Architecture

```
port_scanner/
├── scanner.py       # Core scanning logic
│   ├── get_service_name()   # Service detection
│   ├── banner_grab()        # Banner grabbing
│   ├── scan_port()          # Single port scan
│   ├── thread_worker()      # Thread worker
│   └── scan_ports()         # Main scan function
└── __main__.py      # CLI interface
```

### Design Decisions

- **Worker-thread model**: Uses `queue.Queue` for thread-safe port distribution
- **Thread safety**: `threading.Lock()` prevents console output race conditions
- **Modular design**: Separate functions for clear separation of concerns
- **No external dependencies**: Uses only Python standard library for portability

## Requirements

- Python 3.8+

No external dependencies required - uses only Python standard library.

## Installation

### Development Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner

# Install in editable mode
pip install -e .
```

### Running Without Installation

```bash
PYTHONPATH=src python3 -m port_scanner <arguments>
```

## Usage

### Basic Usage

Scan the default port range (1-1024) on a target host:

```bash
port-scanner 192.168.1.1
```

Or without installation:

```bash
PYTHONPATH=src python3 -m port_scanner 192.168.1.1
```

### Command-Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--start-port` | `-s` | Starting port number | 1 |
| `--end-port` | `-e` | Ending port number | 1024 |
| `--threads` | `-t` | Number of worker threads | 100 |
| `--help` | `-h` | Show help message | - |

### Examples

#### Scan common ports (1-1024)

```bash
port-scanner 192.168.1.1
```

#### Scan a specific port

```bash
port-scanner 192.168.1.1 -s 80 -e 80
```

#### Scan a custom range

```bash
port-scanner 192.168.1.1 -s 1 -e 10000
```

#### Adjust number of threads

```bash
port-scanner 192.168.1.1 -t 50     # Fewer threads (slower but more polite)
port-scanner 192.168.1.1 -t 200    # More threads (faster but more aggressive)
```

#### Combine options

```bash
port-scanner 192.168.1.1 -s 1 -e 5000 -t 150
```

#### Scan localhost

```bash
port-scanner 127.0.0.1 -s 1 -e 1024
```

## Output Format

The scanner displays results in a table format:

```
Port       Status     Service             Banner
----------------------------------------------------------------------
22         open       ssh                 SSH-2.0-OpenSSH_8.0
80         open       http
443        open       https
```

### Output Columns

| Column | Description |
|--------|-------------|
| Port | The port number that was scanned |
| Status | Whether the port is `open` or `closed` (closed ports are not shown) |
| Service | Standard service name (e.g., `http`, `ssh`, `ftp`) or `unknown` |
| Banner | Response string from the service (if available) |

## Technical Details

### Architecture

The scanner uses a producer-consumer pattern:

1. **Main Thread**: Creates a queue of ports to scan
2. **Worker Threads**: Pull ports from the queue and scan them
3. **Results Collection**: Thread-safe storage of scan results

### Thread Safety

- `threading.Lock()` prevents race conditions when writing results
- Each worker thread processes one port at a time
- Results are sorted by port number before display

### Timeouts

| Operation | Timeout | Purpose |
|-----------|---------|---------|
| Connection | 1.0s | Prevents hanging on closed ports |
| Banner Grab | 2.0s | Allows time for slow services to respond |

### Performance Considerations

- Default 100 threads provides good balance for most networks
- Increase threads for faster scanning on local networks
- Decrease threads to be more polite to remote targets
- Very high thread counts may cause socket exhaustion

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=src/port_scanner --cov-report=html
```

## Development

### Code Style

This project uses:
- **Black** for formatting (line length: 100)
- **isort** for import sorting
- **PEP 8** compliance

Format code:

```bash
black src/ tests/
isort src/ tests/
```

### Project Structure

```
port-scanner/
├── src/
│   └── port_scanner/
│       ├── __init__.py      # Package exports
│       ├── __main__.py      # CLI entry point
│       └── scanner.py       # Core scanning logic
├── tests/
│   └── test_scanner.py      # Unit tests
├── pyproject.toml           # Project configuration
└── README.md                # This file
```

## License

MIT License

## Disclaimer

This tool is intended for legitimate network administration and security testing purposes only. Always ensure you have permission to scan the target network. Unauthorized port scanning may be illegal in your jurisdiction.

## AI Disclosure

This project was built with the assistance of [OpenCode](https://opencode.ai),
an AI coding agent. and [OpenSpec](https://openspec.dev/), a spec-driven development framework. All AI-generated code has been reviewed by a human developer.

# AI-Assisted Code

This module was initially generated by OpenCode using MiniMax-M2.5-Free.
Reviewed and tested by: markam303
Date: 04-03-2026

