# Huawei Case Writer

基于 AI Skill 的华为云案例文章生成器，用于快速撰写符合华为开发者空间和华为云案例中心规范的中文 Markdown 案例文章。

## 功能

- **新建案例**：根据主题、步骤、代码片段等信息，生成完整案例草稿
- **案例修订**：将已有文章规范化为华为案例中心风格
- **单节撰写**：仅生成某个章节，如 `案例介绍`、`资源总览`、`释放资源` 等

## 生成的文章结构

```markdown
# 一、概述
## 1.1 案例介绍
## 1.2 适用对象
## 1.3 案例时间
## 1.4 案例流程
## 1.5 资源总览

# 二、环境和资源准备

# 三、构建XX应用

# 四、释放资源

# 五、扩展资料说明
```

## 项目结构

```text
huawei-case-writer/
├── SKILL.md                          # Skill 主文件，定义工作流与输出规范
├── agents/
│   └── openai.yaml                   # Agent 接口描述
├── assets/
│   └── case-template-source.md       # 华为官方模板源文件（含编辑注释）
├── references/
│   ├── case-template.md              # 标准结构参考
│   ├── case-style-patterns.md        # 真实案例风格模式
│   └── quality-checklist.md          # 发布前质量检查清单
├── LICENSE
└── README.md
```

## 使用方式

### 作为 AI IDE Skill 使用

将本项目作为项目级 Skill 安装到 AI IDE 或 CodeArts 中，通过对话驱动案例生成：

1. 将项目目录放入 `.codeartsdoer/skills/` 下
2. 在 AI IDE 对话中描述你的案例需求
3. Skill 自动调用，生成符合规范的案例文章

### 直接参考

也可以直接阅读 `references/` 下的参考文件，手动按规范撰写案例。

## 核心规范

- 全文中文，面向实操而非营销
- 以真实场景开篇，先问题后方案
- 菜单路径使用 `设置 > 技能与规则 > 项目级` 格式
- 代码、命令、路径使用围栏代码块
- 资源使用表格列出，付费资源必须包含释放步骤
- 未知信息标记 `待补充`，不编造事实

## 许可证

[Apache License 2.0](LICENSE)
