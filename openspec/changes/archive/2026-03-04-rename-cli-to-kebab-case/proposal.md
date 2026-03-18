# Change: Rename CLI command from port_scanner to port-scanner

## Why
The current CLI command uses underscore (`port_scanner`) which is inconsistent with common CLI convention where commands typically use kebab-case (`port-scanner`). This improves usability and follows POSIX guideline recommendations.

## What Changes
- Rename CLI entry point from `port_scanner` to `port-scanner`
- Update package metadata in `pyproject.toml`
- Update documentation references

## Impact
- Affected specs: CLI interface
- Affected code: `pyproject.toml`, CLI invocation
- Breaking: Existing users must use new command name
