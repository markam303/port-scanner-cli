# Project Context

## Purpose
Professional-grade, multithreaded TCP port scanner CLI tool for network reconnaissance. Scans TCP ports, identifies standard services, and performs banner grabbing to detect software versions.

## Tech Stack
- Python 3.x (CLI)
- Standard libraries: `socket`, `threading`, `queue`

## Project Conventions

### Code Style
- **Formatting**: Black + isort (PEP 8 compliant)
- **Naming**: snake_case for functions/variables, SCREAMING_SNAKE for constants
- **Documentation**: Docstrings for all public functions

### Architecture Patterns
- **Worker-thread model**: queue.Queue for port management
- **Modular design**: Separate functions for scan_port, thread_worker, banner_grab, main
- **Thread safety**: threading.Lock() for console output synchronization

### Testing Strategy
- Any Python testing framework (unittest/pytest)
- Unit tests for individual functions (scan_port, banner_grab)
- Integration tests for full scan workflow

### Git Workflow
- Feature branches: `feature/<description>`
- Commit messages: Clear, descriptive (imperative mood)

## Domain Context

### Core Features
- TCP port scanning (1-1024 ports or user-defined range)
- Service detection via socket.getservbyport()
- Banner grabbing with configurable timeouts
- Thread-safe console output
- Table-formatted output (Port, Status, Service Name, Banner)

### Technical Parameters
- Connection timeout: 1.0s
- Banner retrieval timeout: 2.0s
- Default port range: 1-1024

## Important Constraints
- Must handle connection timeouts gracefully
- Must handle connection refused errors
- Must prevent thread race conditions on stdout

## External Dependencies
- None (uses only Python standard library)
