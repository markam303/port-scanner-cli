# Contributing to Port Scanner

Thank you for your interest in contributing to Port Scanner!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/port-scanner.git`
3. Create a branch: `git checkout -b feature/your-feature-name`

## Development Setup

```bash
# Install in editable mode
pip install -e .

# Run tests
pytest tests/ -v

# Format code
black src/ tests/
```

## Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting (line length: 100)
- Write tests for new functionality
- Keep functions focused and small

## Submitting Changes

1. Ensure all tests pass: `pytest tests/ -v`
2. Update documentation if needed
3. Commit your changes with clear messages
4. Push to your fork
5. Open a Pull Request

## Reporting Issues

Please report bugs via GitHub Issues with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS

## Security Disclosure

If you discover a security vulnerability, please do NOT open a public issue.
Instead, contact the maintainers privately.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
