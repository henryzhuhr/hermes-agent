---
slug: /
sidebar_position: 0
title: "Hermes Agent 文档"
description: "Nous Research 构建的自我改进代理。内置学习闭环，能从经验中生成技能、在使用中持续改进，并跨会话保留记忆。"
hide_table_of_contents: true
---

# Hermes Agent

Nous Research 打造的自我改进 AI Agent。它不仅能聊天和执行工具，还会在长期使用中沉淀记忆、生成技能、复用经验，并逐步形成对用户和工作方式的稳定理解。

:::note 中文整理版
本页是 `website/docs/index.md` 的中文整理版，优先保留核心能力、常用入口与导航信息。更细的背景说明可对照英文原文：[/docs/](/docs/)
:::

<div style={{display: 'flex', gap: '1rem', marginBottom: '2rem', flexWrap: 'wrap'}}>
  <a href="/docs.zh/getting-started/installation" style={{display: 'inline-block', padding: '0.6rem 1.2rem', backgroundColor: '#FFD700', color: '#07070d', borderRadius: '8px', fontWeight: 600, textDecoration: 'none'}}>开始使用 →</a>
  <a href="https://github.com/NousResearch/hermes-agent" style={{display: 'inline-block', padding: '0.6rem 1.2rem', border: '1px solid rgba(255,215,0,0.2)', borderRadius: '8px', textDecoration: 'none'}}>查看 GitHub</a>
</div>

## Hermes Agent 是什么？

Hermes 不是“只能在 IDE 里工作的 Copilot”，也不是“套了一层外壳的聊天机器人”。它是一个长期运行的自治代理：

- 可以在 CLI、Telegram、Discord、Slack、WhatsApp 等多种界面中工作
- 能调用终端、文件、Web、浏览器、MCP、语音等工具
- 会把稳定偏好和关键信息写入持久记忆
- 会把复杂流程沉淀为可复用的 Skills
- 能通过子代理、计划、批处理和定时任务完成更长链路的工作

你可以把它跑在本机，也可以放在 VPS、GPU 机器、Daytona 或 Modal 这类接近“闲时零成本”的云环境里。

## 快速入口

| 入口 | 用途 |
|---|---|
| [安装](/docs.zh/getting-started/installation) | 在 Linux、macOS、WSL2 或 Termux 上完成安装 |
| [快速开始](/docs.zh/getting-started/quickstart) | 2 分钟完成首次对话和基本体验 |
| [学习路径](/docs.zh/getting-started/learning-path) | 按经验和使用场景选择阅读顺序 |
| [配置](/docs.zh/user-guide/configuration) | `config.yaml`、`.env`、模型与工具设置 |
| [CLI 界面](/docs.zh/user-guide/cli) | 终端交互、快捷键、Slash 命令、会话管理 |
| [消息网关](/docs.zh/user-guide/messaging/index) | 配置 Telegram、Discord、Slack、WhatsApp 等 |
| [工具与 Toolset](/docs.zh/user-guide/features/tools) | 了解内置工具、后端与权限边界 |
| [持久记忆](/docs.zh/user-guide/features/memory) | 让代理跨会话记住稳定事实 |
| [Skills 系统](/docs.zh/user-guide/features/skills) | 复用操作流程和领域知识 |
| [MCP](/docs.zh/user-guide/features/mcp) | 挂接任意 MCP Server 扩展工具能力 |
| [ACP 编辑器集成](/docs.zh/user-guide/features/acp) | 在 VS Code、Zed、JetBrains 中运行 Hermes |
| [AI Provider 集成](/docs.zh/integrations/providers) | 配置 OpenRouter、Anthropic、Copilot、本地模型等 |
| [常见问题](/docs.zh/reference/faq) | 常见报错、安装问题与排查路径 |

## 关键能力

- **学习闭环**：通过记忆、技能、自我修补和跨会话检索，越用越懂你
- **多运行环境**：支持本地、Docker、SSH、Singularity、Modal、Daytona 六类终端后端
- **多交互面**：CLI、聊天平台、编辑器 ACP、Web Dashboard 并存
- **自动化能力**：定时任务、后台会话、子代理委派、程序化工具调用
- **开放扩展**：MCP、Plugins、Skills Hub、外部记忆后端
- **研究友好**：批处理、轨迹导出、RL 训练、环境模拟

## 推荐阅读顺序

1. 先看 [安装](/docs.zh/getting-started/installation) 和 [快速开始](/docs.zh/getting-started/quickstart)
2. 日常使用重点看 [CLI](/docs.zh/user-guide/cli)、[配置](/docs.zh/user-guide/configuration)、[会话](/docs.zh/user-guide/sessions)
3. 要接聊天平台就看 [消息网关](/docs.zh/user-guide/messaging/index)
4. 要接入模型、MCP、编辑器或本地推理服务，就看 [Integrations](/docs.zh/integrations/index)
5. 需要完整命令与环境变量清单，再看 [Reference](/docs.zh/reference/cli-commands)

