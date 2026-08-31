# Case Thinking Coach

Case Thinking Coach is an open-source Codex skill that helps graduate students practice structured, nontechnical business case interviews for consulting, marketing, analytics, brand, PR, and corporate communications roles.

It lets the student think first. After the student submits a framework, the coach explains strengths and gaps, presents a strong reference framework, and lists the math and formulas the case will require. It performs calculations and reveals the final recommendation only when the student chooses to continue.

In a fresh conversation, the coach first asks whether the student is new to case interviews. Beginners receive a short orientation and may choose a lesson before practice. When the student is ready to begin, the coach asks for an easy, intermediate, or advanced case level.

## Independence and student comfort

This is an independent educational project. It is not sponsored, endorsed, reviewed, or approved by any university, employer, consulting firm, or other organization. The author's views and work are personal and do not represent their employer. References to public interview-preparation standards do not imply affiliation or endorsement.

The bundled case bank excludes sensitive, distressing, discriminatory, graphic, and personally intrusive scenarios. Generated cases are screened against the same policy. Students may skip, stop, replace, or soften a case immediately without explanation. See [references/safety.md](references/safety.md).

## Install

Copy the `case-thinking-coach` directory into your Codex skills directory:

```bash
cp -R case-thinking-coach "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart or reload Codex if the skill does not appear immediately. Then invoke `$case-thinking-coach`, or ask naturally for a supported case-interview activity.

## Try it

- `Use $case-thinking-coach to give me an intermediate GTM case.`
- `Use $case-thinking-coach to teach me how to build an issue tree.`
- `Use $case-thinking-coach to evaluate this framework for a pricing case: ...`
- `Use $case-thinking-coach to generate a safe PR crisis case.`

Commands include `Teach me`, `Generate a case`, `Coach me`, `Interview me`, `Let me solve it`, `Show solution`, `Evaluate my answer`, `New case`, `Skip this case`, `Stop here`, and `Help`.

## Supported scope

The skill teaches foundational Profitability, 3 Cs, Porter’s Five Forces, 4 Ps, and M&A frameworks, then helps students tailor them into case-specific issue trees. It covers GTM, pricing, brand positioning, growth, marketing ROI, customer strategy, safe crisis management, internal/external communications, profitability, and nontechnical operations/turnaround. It does not cover behavioral interviews, networking practice, engineering/science cases, sensitive scenarios, or confidential employer material.

## Repository map

- `SKILL.md`: routing and interaction contract
- `references/`: curriculum, frameworks, formulas, rubric, safety, and generator protocol
- `cases/`: separated candidate and facilitator materials
- `scripts/`: dependency-free validation
- `agents/openai.yaml`: Codex UI metadata

## Validate

```bash
python3 scripts/validate_cases.py
python3 scripts/check_skill.py
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

The first build contains six deeply reviewed representative cases. The planned `0.1.0` bank contains 20 cases across all required categories. See [cases/README.md](cases/README.md).

The evaluation rubric is synthesized from official public preparation guidance from [McKinsey](https://www.mckinsey.com/careers/interviewing/en), [BCG](https://careers.bcg.com/global/en/case-interview-preparation), and [Bain](https://www.bain.com/careers/interview-preparation/experience-interview.aspx). The project is not affiliated with any of these firms.

## Disclaimer

This tool supports practice and does not reproduce confidential interviews, represent an employer or university, guarantee recruiting outcomes, or provide business, legal, medical, financial, or mental-health advice.
