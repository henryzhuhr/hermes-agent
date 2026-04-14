---
title: "功能总览"
sidebar_label: "总览"
sidebar_position: 1
---

# 功能总览

Hermes 的能力远不止“聊天 + 工具调用”。它把长期记忆、上下文文件、技能、MCP、语音、编辑器接入和自动化编排组合在一起，形成一个可长期运行的 agent 平台。

:::note 中文整理版
本页是 `website/docs/user-guide/features/overview.md` 的中文整理版。英文原文：[/docs/user-guide/features/overview](/docs/user-guide/features/overview)
:::

## 核心能力

- [Tools & Toolsets](/docs.zh/user-guide/features/tools)：决定 agent 能做什么
- [Skills 系统](/docs.zh/user-guide/features/skills)：按需加载知识和工作流
- [Persistent Memory](/docs.zh/user-guide/features/memory)：跨会话保留稳定事实
- [Context Files](/docs.zh/user-guide/features/context-files)：从 `SOUL.md`、`AGENTS.md` 等文件注入上下文
- [Checkpoints](/docs.zh/user-guide/checkpoints-and-rollback)：文件修改前自动快照

## 自动化

- [Subagent Delegation](/docs.zh/user-guide/features/delegation)：把任务拆给子代理并行执行
- [Code Execution](/docs.zh/user-guide/features/code-execution)：通过脚本程序化调用 Hermes 工具
- 定时任务 Cron：见英文原文 [/docs/user-guide/features/cron](/docs/user-guide/features/cron)
- Hooks / Batch Processing：见英文原文

## 媒体与 Web

- [Voice Mode](/docs.zh/user-guide/features/voice-mode)
- 浏览器自动化：[/docs/user-guide/features/browser](/docs/user-guide/features/browser)
- 图像生成、视觉分析、TTS：本阶段仍保留英文

## 集成

- [MCP](/docs.zh/user-guide/features/mcp)
- [ACP 编辑器集成](/docs.zh/user-guide/features/acp)
- [AI Providers](/docs.zh/integrations/providers)
- Plugins：[/docs/user-guide/features/plugins](/docs/user-guide/features/plugins)

## 个性化

- [Personality & SOUL.md](/docs.zh/user-guide/features/personality)
- [Provider Routing](/docs.zh/user-guide/features/provider-routing)
- [Fallback Providers](/docs.zh/user-guide/features/fallback-providers)

## 推荐阅读顺序

1. [Tools & Toolsets](/docs.zh/user-guide/features/tools)
2. [Skills 系统](/docs.zh/user-guide/features/skills)
3. [Persistent Memory](/docs.zh/user-guide/features/memory)
4. [MCP](/docs.zh/user-guide/features/mcp)
5. [Delegation](/docs.zh/user-guide/features/delegation)
