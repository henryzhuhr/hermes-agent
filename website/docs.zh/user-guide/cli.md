---
sidebar_position: 1
title: "CLI 界面"
description: "掌握 Hermes Agent 的终端界面：命令、快捷键、个性与会话管理"
---

# CLI 界面

Hermes Agent 的 CLI 是完整的终端交互界面，不是网页壳。它提供多行编辑、Slash 命令补全、会话恢复、工具流式输出，以及“打断当前任务并重定向”的工作流，适合把 agent 当成长期终端搭档来用。

:::note 中文整理版
本页是 `website/docs/user-guide/cli.md` 的中文整理版，保留日常使用最关键的操作方式。英文原文：[/docs/user-guide/cli](/docs/user-guide/cli)
:::

## 启动方式

```bash
hermes
hermes chat -q "Hello"
hermes chat --model "anthropic/claude-sonnet-4"
hermes chat --provider openrouter
hermes chat --toolsets "web,terminal,skills"
hermes --continue
hermes -w
```

常见场景：

- `hermes`：进入交互式 CLI
- `hermes chat -q`：单次提问，适合脚本或快速查询
- `hermes --continue`：恢复最近一次会话
- `hermes -w`：在独立 git worktree 中启动，适合并行多 agent

## 界面构成

CLI 的高频区域主要有三块：

- 输入区：支持多行输入、历史记录和 Slash 命令补全
- 响应区：显示模型回复、工具输出和状态信息
- 状态栏：展示模型、provider、toolsets、会话信息等

当你恢复旧会话时，CLI 会显示当前会话标题和简短回顾，帮助你快速接上上下文。

## 常用快捷键

- `Alt+Enter` / `Ctrl+J`：插入换行
- `Ctrl+C`：中断当前执行
- 方向键：浏览输入历史
- 输入 `/`：打开 Slash 命令补全

如果你经常粘贴长日志、代码块或计划文本，多行输入会比单行 prompt 更高效。

## Slash 命令

CLI 内置大量命令，常见的有：

- `/help`
- `/model`
- `/tools`
- `/personality`
- `/save`
- `/compress`
- `/history`
- `/title`
- `/rollback`

完整列表见 [Slash 命令参考](/docs.zh/reference/slash-commands)。

## Quick Commands

你可以在 `~/.hermes/config.yaml` 里配置 quick commands，把常用 prompt 模板做成短命令。它适合：

- 固定的代码审查提示
- 每日总结模板
- 一键调用某个技能或常用工作流

## Skills 与动态 Slash 命令

Hermes 安装或创建的 Skills 会自动暴露为动态 Slash 命令。常见用法：

- 直接输入技能命令名加载技能
- 在会话中让 agent 按需读取 `SKILL.md`
- 通过 `hermes skills search/install` 从 Skills Hub 安装

更多内容见 [Skills 系统](/docs.zh/user-guide/features/skills)。

## 个性与人格

CLI 支持两层人格控制：

- `SOUL.md`：全局、长期的人格与行为边界
- `/personality`：当前会话级的人格预设覆盖层

如果你想改的是“这个实例长期怎么说话、如何做决策”，优先改 `SOUL.md`。详见 [Personality & SOUL.md](/docs.zh/user-guide/features/personality)。

## 打断、重定向与后台会话

Hermes 的 CLI 支持在 agent 忙碌时继续输入新消息：

- 直接发新消息，可以打断当前任务并改做新任务
- 长任务可以挂到后台，稍后再回来查看结果
- 会话状态会被保存，适合长链路任务

这和传统“一次问答结束再继续”的聊天模式不同，更接近真实终端协作。

## 会话管理

CLI 会自动保存每次会话。高频操作包括：

- `hermes --continue`
- `hermes --resume <session>`
- `/title`
- `/save`
- `/compress`

会话的搜索、导出、删除和命名规则见 [Sessions](/docs.zh/user-guide/sessions)。

## Quiet Mode

如果你想减少视觉噪音，可以启用 quiet mode，压缩 banner、状态信息或工具进度展示。是否要这么做取决于你更看重“信息密度”还是“过程可见性”。

## 推荐搭配

- 想更安全地执行命令：看 [配置](/docs.zh/user-guide/configuration) 里的 terminal backend
- 想在同仓库并行跑多个 agent：看 [Git Worktrees](/docs.zh/user-guide/git-worktrees)
- 想随时回滚破坏性改动：看 [Checkpoints and /rollback](/docs.zh/user-guide/checkpoints-and-rollback)

## 下一步

- [配置](/docs.zh/user-guide/configuration)
- [Sessions](/docs.zh/user-guide/sessions)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- [Skills 系统](/docs.zh/user-guide/features/skills)
