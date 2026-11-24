# AutoSoft Connector

## Overview

The `autosoft-connector` repository contains the vendor-specific integration responsible for extracting dealership data from the AutoSoft DMS and preparing it for migration into Tekion ARC.

This connector owns its AutoSoft-specific authentication, navigation, extraction workflows, data handling, transformation and migration behaviour.

It operates independently from the other DMS connectors.

## Responsibilities

- Connect to the authorized AutoSoft DMS environment.
- Authenticate using the existing supported authentication mechanism.
- Navigate AutoSoft-specific workflows.
- Extract supported dealership data.
- Handle vendor-specific extraction failures.
- Transform extracted data into the required ARC-compatible format.
- Preserve migration data integrity.
- Report extraction and processing errors.

## Vendor Identity

| Property | Value |
|---|---|
| Vendor | AUTOSOFT |
| Repository | autosoft-connector |
| Target platform | Tekion ARC |
| Connector type | Vendor-specific DMS connector |

## Architecture

Document the actual implementation here:

- Authentication mechanism: To be documented
- Navigation mechanism: To be documented
- Extraction workflow: To be documented
- Supported data entities: To be documented
- Transformation and mapping: To be documented
- Error-handling strategy: To be documented

## Vendor-Specific Workflow

Document the actual AutoSoft extraction sequence.

| Workflow | Extraction steps | Status |
|---|---|---|
| Customer data | To be documented | Pending |
| Vehicle data | To be documented | Pending |
| Deal data | To be documented | Pending |
| Service data | To be documented | Pending |

AutoSoft workflow steps must be documented independently. Never assume they match Automate, CDK or Reynolds.

## Repository Development Guidelines

1. Preserve existing AutoSoft extraction behaviour.
2. Make targeted changes based on the reported issue.
3. Avoid unrelated refactoring.
4. Follow existing project conventions.
5. Add or update relevant tests.
6. Preserve existing data transformations unless explicitly required.
7. Do not modify other vendor connectors.

## AI Migration Agent Integration

This repository is registered under the logical vendor identifier `AUTOSOFT`.

The central repository registry must resolve `AUTOSOFT` to `autosoft-connector`.

The AI Migration Agent may:

- Analyze AutoSoft-specific source code.
- Investigate extraction and mapping failures.
- Identify affected functions and dependencies.
- Prepare an implementation plan.
- Modify relevant code in an isolated Docker workspace.
- Execute available tests.
- Produce a Git diff for validation.

Repository selection and authorization remain backend responsibilities.

The AI agent must not independently select a different repository.

## Testing and Validation

Before creating a pull request:

- Run relevant unit tests.
- Run relevant integration tests where available.
- Run configured lint and type checks.
- Inspect the complete Git diff.
- Verify that unrelated files have not changed.
- Check for unintended changes to existing extraction behaviour.

Document actual commands after inspecting the repository.

## Security

- Never commit dealership credentials or authentication tokens.
- Avoid logging passwords, cookies or sensitive customer information.
- Use approved secure credential handling.
- Preserve existing access controls.

## Documentation Maintenance

Update this README when extraction workflows, supported entities, architecture or development commands change.

**Note:** Actual AutoSoft implementation details must be verified against the repository before this documentation is considered complete.
