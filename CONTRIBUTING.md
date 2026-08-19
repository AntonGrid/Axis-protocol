# Contributing to Axis Protocol

Thank you for your interest in Axis Protocol.

Axis Protocol is an **open standard** — an overlay trust standard between the
physical and digital worlds. Contributions that improve the specification,
architecture, documentation, and security are welcome.

---

## Principles

Every contribution should follow these principles:

- Keep the protocol open.
- Do not break backward compatibility without discussion.
- Security first.
- Architecture before implementation.
- Documentation is part of the standard.
- The specification (`spec/`) is **normative**; `docs/` are informative.

---

## Normative vs informative

- **`spec/`** is the **normative** source of truth for the protocol. Changes to
  it MUST go through the ADR process and MUST NOT silently break compatibility.
- **`docs/`** is **informative** (overviews, guides). See
  [docs/README.md](docs/README.md), section “How to Contribute”.
- **`adr/`** records accepted architecture decisions. Substantial changes SHOULD
  be proposed as a new ADR first.

---

## Workflow

1. Open an issue describing the problem or proposal.
2. For substantial changes, draft an ADR under `adr/`
   (Context → Decision → Consequences).
3. Make small, isolated changes in a feature branch.
4. Update the specification and/or documentation as needed.
5. Submit a Pull Request.
6. Participate in review.

---

## Pull Requests

Good pull requests:

- solve one problem;
- include documentation;
- keep commits clean;
- explain the architectural impact;
- reference related ADRs and spec sections.

---

## Architecture decisions

Before changing the protocol, read:

- [Core specification](spec/protocol/README.md)
- [Architecture Decision Records (ADR)](adr/)
- [Architecture Book](docs/philosophy/architecture/00_Prologue.md)

Architecture decisions should always be documented as ADRs.

---

## Security

Never submit:

- private keys;
- passwords;
- API secrets;
- production credentials.

See [SECURITY.md](SECURITY.md) for reporting guidelines.

---

## Questions

Open a GitHub Issue or start a Discussion before making major changes.

---

Thank you for helping build Axis Protocol.
