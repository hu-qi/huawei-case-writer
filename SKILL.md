---
name: huawei-case-writer
description: generate and revise chinese huawei developer space and huawei cloud case-center markdown in the style of real case-center examples and the official template. use when the user wants to draft, restructure, enrich, or polish a 华为开发者空间 or 华为云 案例, especially for skill-based cases, ai ide/codearts cases, hands-on tutorials, or publish-ready markdown that needs sections like 概述, 案例流程, 资源总览, 环境和资源准备, 构建步骤, 释放资源, and 扩展资料.
---

# Huawei Case Writer

## Overview

Generate a complete Chinese Markdown case article for Huawei Developer Space or Huawei Cloud case publishing.
Prefer real case-center writing habits over generic how-to writing: scene first, then workflow, then preparation, then actionable steps, then validation, then cleanup.

## Core mode selection

Choose one path first.

1. **New case drafting**: the user gives a topic, rough steps, code, links, screenshots, notes, or a product idea and wants a full case draft.
2. **Case revision**: the user gives an existing markdown or draft and wants it normalized to Huawei case-center style.
3. **Section-only writing**: the user asks for only one part such as `案例介绍`, `案例流程`, `资源总览`, `环境准备`, or `释放资源`.

## Default workflow

Follow this sequence unless the user explicitly asks for only one part.

1. Extract the minimum case inputs from the conversation.
2. Determine the case type.
3. Build the article in the standard Huawei structure.
4. Apply the real-world style patterns from `references/case-style-patterns.md`.
5. Fill unknown details conservatively with placeholders like `待补充` instead of inventing facts.
6. Run the quality checklist before returning the result.
7. Return the final Markdown plus a short missing-materials list if publish readiness is blocked.

## Required input handling

Collect or infer these fields from the user's request, uploaded files, pasted notes, and reference links.

- Case topic or final title
- The thing being built, configured, or verified
- Target audience
- Expected duration
- Core cloud products or services used
- Main workflow steps
- Environment prerequisites
- Code or repo information if any
- Commands, config, or key code snippets if any
- Prompt text if this is a skill or AI dialogue case
- Expected result or verification result
- Resource release or cleanup steps
- Extension links or learning materials

When important fields are missing:

- Keep writing.
- Mark missing specifics with `待补充`.
- Do not fabricate prices, quotas, product specs, menu names, screenshots, or URLs.

## Output contract

Unless the user requests otherwise, output in this structure:

```markdown
# 一、概述
## 1.1 案例介绍
## 1.2 适用对象
## 1.3 案例时间
## 1.4 案例流程
## 1.5 资源总览

# 二、环境和资源准备
## 2.1 ...
## 2.2 ...

# 三、构建XX应用
## 3.1 ...
## 3.2 ...
...

# 四、释放资源
## 4.1 ...
...

# 五、扩展资料说明
```

Also apply these behaviors:

- Use Chinese.
- Use concise, publishable headings.
- Prefer practical instruction over marketing language.
- Use menu paths like `设置 > 技能与规则 > 项目级 > 技能 > + 新建` when describing UI navigation.
- Use fenced code blocks for commands, prompts, file paths, code, and config.
- Use tables for priced resources, parameters, and command explanations when helpful.
- Separate conceptual explanation from operational steps.
- Keep imperative guidance concrete: 打开、进入、下载、解压、替换、执行、验证、释放.

## Style patterns learned from real Huawei case-center examples

### 1. Open with a concrete use scenario

Do not start with abstract capability claims only.
Start with a real problem or work scenario, then explain the solution.

Good examples:

- A technical writer wants to quickly generate a case article from a skill.
- A blogger needs to convert Markdown to Word without losing formatting.
- A developer wants to build a project-level skill in AI IDE and call it through dialogue.

### 2. Explain the product and the skill briefly, then return to the task

When the case involves `SKILL`, `AI IDE`, or `CodeArts`, briefly define the product or mechanism in one short paragraph each, then immediately connect it back to the specific task in this case.
Do not let background explanation dominate the article.

### 3. Make the workflow section readable even without images

In `1.4 案例流程`:

- First write a short narrative paragraph that explains what the reader will do.
- Then write `说明：` followed by a numbered list of the actual steps.
- If the user has no flowchart, write `流程图待补充` but keep the numbered explanation complete.

### 4. Prefer subsection granularity that matches actual operations

Real examples tend to split preparation and execution into several compact subsections.
For example:

- `2.1 AI IDE安装部署`
- `2.2 下载skill`
- `2.3 配置SKILL`
- `2.4 skill简介`
- `3.1 生成...`
- `3.2 测试...`

Do not collapse unrelated actions into one oversized section.

### 5. Skill cases should explicitly show skill directory contents

If the case is about creating, installing, or using a skill, include a small tree such as:

```text
sample-skill/
├── SKILL.md
├── scripts/
└── references/
```

Then explain each important file or directory in plain Chinese.
This is a strong pattern in the reference cases.

### 6. Include the actual dialogue prompt when the case involves AI conversation

If the user is driving AI IDE, CodeArts, or a skill through chat, include the exact example prompt in a fenced code block.
Then describe what the system does next, such as:

- calls the skill
- parses requirements
- starts generating files
- packages and tests the result

### 7. Add explicit verification language after each major step

Examples:

- `点确定后，系统会自动创建...`
- `移动后，系统会自动加载到项目级技能列表中。`
- `任务执行完成后，可以在项目资源管理器中看到...`
- `打开生成结果检查格式是否符合预期。`

### 8. End with a short completion statement

Before `反馈改进建议` or the closing paragraph, it is acceptable to use a concise wrap-up sentence like:

`至此，基于...的案例结束。`

Use this style sparingly and keep it short.

## Drafting rules by section

### 1. Overview section

Write a short, strong case introduction that explains:

- What the reader will build, configure, or verify
- Why it matters in a real work scenario
- What final result they should expect

For `适用对象`, select only the audiences supported by the case:

- 企业开发者
- 个人开发者
- 高校学生

For `案例时间`, provide a realistic estimate using the actual operation count. If uncertain, use a range.

For `案例流程`:

- Add a short narrative paragraph first.
- Then add `说明：` plus a numbered step list.
- If no image is available, write `流程图待补充`.

For `资源总览`:

- List only resources actually used.
- If the case is free, say `本案例预计花费0元`.
- If exact prices are unknown, write `以控制台实际价格为准`.
- Always remind the user to release paid resources promptly.

### 2. Environment and preparation

Use this section for prerequisites, entitlement activation, tools, skill packages, SDKs, vouchers, dependencies, and version-pinned installs.

Rules:

- Split preparation into compact subsections.
- If the case depends on downloading a skill package or repo, create a dedicated subsection for that download.
- If the case depends on configuring project-level skills, describe the menu path explicitly.
- If a service must be enabled in advance, state the purpose and the artifact the reader needs to obtain.

### 3. Build or implementation section

This is the core of the case.

For each subsection:

1. State the goal of the step.
2. Give exact UI path or command-line action.
3. Explain important parameters.
4. Show critical code, prompt text, or config snippets.
5. Tell the reader how to verify success.

When the case includes code:

- Add a brief project-structure tree if it helps orientation.
- Explain only the critical code or config.
- Highlight files the reader must modify.
- Keep filenames, paths, class names, and methods in code format.

When the case includes AI conversation:

- Put the prompt in a fenced block.
- Explain what the system automatically generates.
- Explain any manual follow-up needed after generation, such as moving files into `.codeartsdoer/skills`.

### 4. Release resources

If any paid or quota-limited resource is used, include cleanup instructions.
If the case is fully free and creates no billable resources, this section may be brief, but still include a note if temporary files, generated packages, or test resources should be cleaned.

### 5. Extension materials

List official docs, repos, product pages, downloadable skill packages, or further reading that genuinely helps the reader continue.
If the style being mirrored includes a feedback link section, keep it as optional only when the user asks for a full publish-like article.

## Revision workflow

When the user provides an existing case draft:

1. Preserve the overall section structure unless it clearly violates the Huawei case format.
2. Normalize wording, headings, code formatting, and table style.
3. Add scenario-based introduction if the opening is too empty.
4. Add missing prompt examples for AI dialogue steps when the case clearly depends on prompting.
5. Add verification sentences after major operations.
6. Remove template comments or editorial reminders from the final output.
7. Identify factual gaps, weak verification steps, and missing cleanup steps.

Return either:

- a fully rewritten article, or
- a targeted patch if the user asked for partial edits only.

## Missing-information policy

Never invent these details:

- Exact prices or billing values
- Product specs the user did not mention
- Console labels that may be version-dependent
- Success screenshots
- Example outputs you cannot justify from context
- Security credentials or secrets

Use one of these fallback styles instead:

- `待补充：...`
- `请以控制台实际显示为准`
- `示例值，实际请替换为你的环境参数`

## Final self-check

Before returning the answer, verify:

- The article follows the Huawei case section order.
- The opening includes a concrete use scenario.
- The workflow section contains both a short narrative and a numbered explanation.
- Skill-based cases include directory structure and file role explanation when helpful.
- AI dialogue cases include at least one concrete prompt example.
- Each major operation has a verification cue or expected result.
- No red template comments remain.
- Commands, paths, prompts, and code are formatted as code.
- Billable resources have a release section.
- Unknown facts are clearly marked instead of guessed.

## Response pattern

Return in this order unless the user asks for something else:

1. `案例标题建议` if the user did not provide a final title.
2. `案例Markdown正文`.
3. `待补充信息` with only the unresolved items.

See `references/case-template.md` for the source structure.
See `references/case-style-patterns.md` for reference-case style cues.
See `references/quality-checklist.md` for the preflight review rubric.
