# cli Specification

## Purpose
TBD - created by archiving change rename-cli-to-kebab-case. Update Purpose after archive.
## Requirements
### Requirement: CLI Command Name
The port scanner CLI SHALL be invoked using kebab-case command name.

#### Scenario: CLI invocation with kebab-case
- **WHEN** user runs `port-scanner --help`
- **THEN** help message is displayed

#### Scenario: CLI invocation with old underscore name
- **WHEN** user runs `port_scanner --help`
- **THEN** command not found error is returned

