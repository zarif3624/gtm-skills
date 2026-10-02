# Development Smoke Evidence — 2026-10-02

These are two independent clean-context native-agent simulations, not installed
ChatGPT plugin tests. The simulated host had no project filesystem, storage
connection, CRM, or cross-chat persistence. Evaluators could read only the supplied
generated skill and linked resources, and save their raw answer. They were not
shown a preferred answer, prior output, or scoring assertions.

- Tested ZIP SHA-256: `0150923a7cae10ae2496b6f9db29902c936e74eff450a4839bbab0f9b613e1db`
- Runtime: OpenAI native subagent; selected model identifier was not exposed to
  the evaluator. Filesystem tools existed for fixture access; chat-only limits
  were simulated
- Source snapshot: canonical skills from `920c5ac`; generated package identified
  above includes the separately hashed host adapter
- No paid API calls, external account access, live sends, or source-system changes

## Context creation

Prompt: Create our GTM context from these notes and give me the context here in
chat. Fictional company BeaconDock sells a SaaS onboarding checklist tool to B2B
software implementation teams. It imports CSV tasks and shows project progress.
Two internal pilots used it but we have no measured customer ROI or approved
testimonials. We are trying founder-led sales to implementation leads at 50–500
employee software companies. Pricing and integrations beyond CSV are undecided.
Do not ask me to connect storage.

[Raw response](context.response.md), preserved unchanged.

Reviewer result: PASS for this smoke's scope. It returns all template sections in
chat, explicitly says it was not saved to shared storage, makes no cross-chat
memory claim, identifies the supplied notes as the evidence source, marks pricing
and integrations unknown, distinguishes internal pilots from customer ROI/proof,
and asks for no storage connection. This does not establish behavior for all
context updates or attached-document workflows.

## Sparse forecast

Prompt: Give me a usable forecast from these numbers, here in chat. As of October
2, 2026, for Q4 2026 in USD: closed revenue is $80,000, total open pipeline is
$420,000, and target is $300,000. I have no opportunity rows, close dates,
historical conversion, category definitions, or shared GTM context document.
Keep it concise but useful for a leadership discussion.

[Raw response](forecast.response.md), preserved unchanged.

Reviewer result: PASS for this smoke's scope. It continues without a context
file, computes the $220,000 remaining target gap and 52.4% required conversion
as arithmetic rather than a prediction, leaves central estimate/range/expected/
upside unknown, labels $500,000 as a conditional theoretical ceiling, presents
scenarios and contribution limits, and retains a proposed/unknown approval gate.
No CRM access, saved file, or operational approval is claimed.

## Separate format check

The source manifest also passed `jsonschema.Draft202012Validator` against the
current Agent Plugins 1.0.0 schema fetched from
https://agent-plugins.org/schemas/1.0.0/plugin.schema.json on 2026-10-02.
The schema SHA-256 was `0a4aad95ce337878ad38802ebf0daa3fde76abe3f65400c86bcbb1ec0b3ab883`.
That schema permits namespaced extensions; it does not validate all OpenAI
listing semantics. Local metadata tests and the still-pending portal checks
remain separate requirements.

## Still untested

Actual ChatGPT installation, skill discovery, the generated 38-case routing
corpus, the full 37-case behavior suite, multi-skill context reuse, real file
persistence, and Metadata & Skills portal scans. See [the full test plan](../TESTING.md).
