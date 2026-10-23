# humanize-en

**An open-source editorial skill for English writing that still sounds like you.**

Humanize-en reviews AI-style writing patterns without erasing the author's intent. It is designed for founders, builders, and professionals who write LinkedIn posts, Substack essays, Notes, comments, and professional messages, including people writing in a second language.

It is **not** an AI detector, an engagement-growth promise, or a generator of made-up first-person anecdotes.

## What makes it different

- Checks **structure**, not just overused words: binary contrasts, staged hooks, slogan endings, repeated post templates.
- Uses a **truth gate**: preserve numbers, dates, direct quotes, uncertainty, and the difference between firsthand work and third-party research.
- Has **10 optional founder-post structures** grounded in linked public case examples. They are editorial illustrations, **not** representative research or evidence of causality.
- Adapts to the writer: the optional [Korean founder profile](profiles/korean-founder.md) is not activated by default.
- Supports channel-specific editing and a 50-point editorial rubric, with factual accuracy as a separate hard requirement.

## Quick start

1. Download or clone the repository.
2. Supply `SKILL.md` to an assistant or agent that supports instruction files, along with the referenced `references/` directory.
3. If you want a specific voice, add a profile in `profiles/`, or provide 2–3 samples of your writing.
4. Try: **"Use humanize-en to edit this LinkedIn post. Preserve every claim, make it less formulaic, and show changes."**

For ChatGPT Projects, upload `SKILL.md` and reference files to project files and add an instruction to follow the skill. This is a *project instruction workflow*, not the same as installing a native skill. Native skill installation depends on your workspace's available features.

## Examples

- [LinkedIn: from generic advice to grounded observation](examples/linkedin-before-after.md)
- [Substack: from broad claim to careful argument](examples/substack-before-after.md)
- [DM: shorter without faking familiarity](examples/dm-before-after.md)

Examples are **fictional editing demonstrations**, not client cases, endorsements, or measured performance tests.

## How it works

1. Confirm author intent, evidence and target channel.
2. Audit language, rhythm and structure for formulaic patterns.
3. Rewrite using the author's actual voice, with a profile only when selected.
4. Run the [Founder Trust Audit](references/founder-trust-audit.md) and check claim provenance.
5. Apply the editorial rubric; revise once if needed. Do not claim the resulting score predicts AI detection or engagement.

## Scope and limits

- No API keys, external dependencies, or model execution are included. This repository supplies instructions and examples.
- The ten linked LinkedIn cases are non-exhaustive. Some writers are not US-based. Linking to third-party posts does not imply endorsement or verification of their claims.
- You must review potentially private client information before publishing an edited draft.
- Public post availability and details may change; verify external factual claims before publishing.

## Repository contents

- `SKILL.md`: primary instructions
- `references/`: pattern audits, channels, scoring, founder evidence and structural atlas
- `profiles/`: optional voice profiles
- `examples/`: fictional before/after edits
- `scripts/validate_repo.py`: structural and link checks (offline)
- `THIRD_PARTY_NOTICES.md`: upstream copyrights and license texts
- `REFERENCES.md`: attribution and research limitations
- `CHANGELOG.md`: version history

## Credits and license

Inspired by [blader/humanizer](https://github.com/blader/humanizer) and [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop). This is an independent adaptation, not endorsed by either project. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for upstream copyright notices and licenses.

The project content is shared under [MIT](LICENSE). **Before publishing under your own account, replace the project copyright holder placeholder with the correct legal name or organization.** Preserve third-party notices.

Contributions: see [CONTRIBUTING.md](CONTRIBUTING.md).
