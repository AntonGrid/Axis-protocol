# Security Policy

## Reporting Security Issues

Security is a top priority for Axis Protocol.

If you discover a vulnerability in the specification, cryptographic rules, or a
reference implementation, please do not publish it immediately. Instead, report
it privately so it can be investigated and fixed.

**Contact:** enrg.project@gmail.com

---

## Scope

This includes:

- Protocol specification (`spec/`)
- Cryptographic schemes and signing/verification rules
- Wire format and validation rules
- Architecture Decision Records (ADR)
- Reference implementations (e.g., Axis Core)

---

## Out of Scope

- General support questions.
- Feature requests.
- Configuration problems.
- Domain-specific applications (e.g., ENRG) — report those in their own
  repositories.

---

## Responsible Disclosure

Please include:

- Description
- Steps to reproduce
- Impact
- Suggested mitigation (optional)

---

## Security Principles

Axis Protocol follows these architectural principles:

- Private keys never leave devices (ADR-0001).
- Every Proof must be cryptographically verifiable.
- Trust is minimized.
- Every component has a single responsibility.
- Security is preferred over convenience.

---

## Conformance

Implementations and deployments MUST follow the normative rules in `spec/` and
the security invariants in `adr/`. Any deviation must be documented.

---

Thank you for helping keep Axis Protocol secure.
