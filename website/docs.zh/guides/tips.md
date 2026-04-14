---
sidebar_position: 1
title: "技巧与最佳实践"
description: "快速提升 Hermes Agent 使用效果的实用建议：提问方式、CLI 技巧、上下文文件、记忆、成本和安全"
---

# 技巧与最佳实践

这页是高频“立刻见效”的经验合集。它不讲底层原理，重点是让你少走弯路、更快拿到稳定结果。

:::note 中文整理版
本页是 `website/docs/guides/tips.md` 的中文整理版。英文原文：[/docs/guides/tips](/docs/guides/tips)
:::

## 拿到更好结果

### 说清楚你要什么

“帮我修代码”这种提示太宽。更好的说法是：

- 报错位置
- 期望行为
- 相关文件路径
- 复现方式

上下文越明确，来回澄清越少。

### 提前给足上下文

首条消息尽量一次带齐：

- 文件路径
- 错误日志
- 当前尝试过的方案
- 约束条件

一条高质量消息通常胜过三轮补充。

### 让 agent 用工具

Hermes 的价值在于终端、文件、Web、MCP 等工具，不只是文本生成。如果任务需要真实检查状态，不要把它限制成“只能猜”。

### 复杂流程写成 Skill

重复出现的工作流，不要每次手写提示词。适合沉淀成 [Skills](/docs.zh/user-guide/features/skills)。

## CLI 高阶习惯

- 多行输入适合长 prompt、日志和代码片段
- 直接发新消息可以打断当前流程
- `hermes --continue` 能快速接回上次会话
- 输入 `/` 立刻看 Slash 命令补全

## 上下文文件

把长期有效的规则写进项目文件，而不是每次手贴：

- `AGENTS.md`：项目级工作规范
- `SOUL.md`：实例级人格与风格
- `.cursorrules`：兼容已有编辑器规则

详见 [Context Files](/docs.zh/user-guide/features/context-files)。

## Memory 与 Skills

记法很简单：

- 长期稳定事实：放 [Memory](/docs.zh/user-guide/features/memory)
- 任务流程和知识套路：做成 [Skill](/docs.zh/user-guide/features/skills)

## 性能与成本

- 不要频繁打破 prompt cache
- 会话太长时及时 `/compress`
- 需要并行思考时用 [Delegation](/docs.zh/user-guide/features/delegation)
- 机械批处理优先用 [Code Execution](/docs.zh/user-guide/features/code-execution)
- 模型别只看“最强”，还要看上下文窗口和工具稳定性

## 消息平台建议

- 给 bot 配好 home channel
- 用 `/title` 管理长会话
- 团队场景优先用 pairing 或 allowlist
- 工具进度显示不要默认开到最吵

## 安全建议

- 不完全可信的代码尽量放 Docker 或隔离后端
- 审批系统不是累赘，是最后一道保险
- 公网 bot 一定做授权控制

## 下一步

- [CLI 界面](/docs.zh/user-guide/cli)
- [Security](/docs.zh/user-guide/security)
- [Working with Skills](/docs.zh/guides/work-with-skills)
