# Case style patterns from the provided Huawei reference cases

These patterns are derived from the two pasted reference articles about:

- `content-research-writer` in AI IDE / CodeArts
- `skill-creator` generating `md-to-word`

Use these cues when drafting or revising Huawei case articles.

## 1. Narrative setup before action

The better reference article opens with a concrete content publishing problem before introducing the solution.
Use this especially when the case solves an obvious workflow pain point.

Recommended pattern:

1. Describe the user's real problem.
2. Explain why the current manual process is inefficient.
3. Introduce the Huawei product plus skill as the solution.
4. State what the user will complete in this case.

## 2. Short product and mechanism explanation

When the case involves `SKILL`, `AI IDE`, or `CodeArts`, add a short explanation paragraph for each only if it helps understanding.
Keep these paragraphs short and task-linked.

## 3. Workflow section shape

A strong `案例流程` subsection often looks like this:

- one short explanatory paragraph
- optional flowchart image
- `说明：`
- a numbered list of operations

Even without an image, preserve the paragraph plus numbered-step shape.

## 4. Preparation section shape

Real examples often separate preparation into these kinds of units:

- installation or deployment of AI IDE
- download of the skill package or repo
- configuration of project-level skill in the IDE
- brief introduction of the downloaded skill contents

This pattern works well for skill-related cases.

## 5. Skill structure explanation pattern

When a skill is central to the case, include a simple tree and explain the role of important files.

Example pattern:

```text
sample-skill/
├── SKILL.md
├── scripts/
└── references/
```

Then explain what `SKILL.md`, `scripts`, and `references` do in the context of the case.

## 6. Prompt-driven execution pattern

If the workflow depends on chatting with AI IDE or CodeArts, include the exact prompt.
After the prompt, describe the system behavior in plain language, such as:

- calls the relevant skill
- parses the requirement
- generates files
- tests or packages the result
- asks for Python plugin installation if needed

## 7. Verification sentence pattern

After each major operation, include a verification sentence.
Common patterns:

- `点确定后，系统会自动创建...`
- `系统将自动加载至项目级SKILL。`
- `任务执行完成后，可以看到...`
- `打开生成结果检查是否符合预期。`

## 8. Ending pattern

A short ending sentence such as `至此，...案例结束。` is acceptable before the final feedback or extension section.
Do not overdo it.

## 9. Tone guidance

Preferred tone:

- practical
- direct
- explanatory
- lightly guided

Avoid:

- excessive slogans
- unsupported claims
- large sections of generic theory unrelated to the task
