# 贡献指南

感谢你对 Huawei Case Writer 的关注！欢迎提交 Issue 和 Pull Request。

## 提交 Issue

- **Bug 报告**：请使用 Bug Report 模板，描述复现步骤和期望行为
- **功能建议**：请使用 Feature Request 模板，说明使用场景和期望效果
- **案例风格改进**：请在 Issue 中附上真实案例链接或片段，说明当前风格与目标的差距

## 提交 Pull Request

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/your-feature`
3. 提交变更：`git commit -m "描述你的变更"`
4. 推送分支：`git push origin feature/your-feature`
5. 创建 Pull Request

### PR 规范

- 标题使用中文，简洁描述变更内容
- 正文说明变更原因和影响范围
- 涉及 `references/` 或 `SKILL.md` 的变更，请在 PR 中附上生成效果对比
- 确保 Markdown 格式正确，无语法错误

## 项目结构说明

| 目录/文件 | 用途 |
|---|---|
| `SKILL.md` | Skill 主文件，定义工作流、输入输出规范和风格规则 |
| `agents/openai.yaml` | Agent 接口描述 |
| `assets/case-template-source.md` | 华为官方模板源文件 |
| `references/case-template.md` | 标准结构参考 |
| `references/case-style-patterns.md` | 真实案例风格模式 |
| `references/quality-checklist.md` | 发布前质量检查清单 |

## 许可证

提交的贡献将按照 [Apache License 2.0](LICENSE) 授权。
