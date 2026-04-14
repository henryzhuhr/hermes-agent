---
sidebar_position: 5
title: "学习路径"
description: "按经验和目标选择最合适的 Hermes Agent 文档阅读顺序"
---

# 学习路径

:::note 中文整理版
本页是 `website/docs/getting-started/learning-path.md` 的中文整理版，用来帮你按目标选文档。英文原文：[/docs/getting-started/learning-path](/docs/getting-started/learning-path)
:::

## 如何使用这页

如果你不确定该从哪看起，不要顺着整站从头读到尾。最有效的方式是：

1. 先按自己的经验水平定位
2. 再按具体使用场景选择入口
3. 最后再补参考文档和高级主题

## 按经验水平

### 新用户

先读：

- [安装](/docs.zh/getting-started/installation)
- [快速开始](/docs.zh/getting-started/quickstart)
- [CLI](/docs.zh/user-guide/cli)
- [配置](/docs.zh/user-guide/configuration)

### 已经用过 CLI agent / coding agent

重点读：

- [工具与 Toolset](/docs.zh/user-guide/features/tools)
- [会话](/docs.zh/user-guide/sessions)
- [Skills](/docs.zh/user-guide/features/skills)
- [MCP](/docs.zh/user-guide/features/mcp)

### 想做系统化部署

重点读：

- [消息网关](/docs.zh/user-guide/messaging/index)
- [安全](/docs.zh/user-guide/security)
- [Profiles](/docs.zh/user-guide/profiles)
- [AI Provider 集成](/docs.zh/integrations/providers)

## 按使用场景

### “我想要一个 CLI 编码助手”

推荐顺序：

1. [快速开始](/docs.zh/getting-started/quickstart)
2. [CLI](/docs.zh/user-guide/cli)
3. [工具与 Toolset](/docs.zh/user-guide/features/tools)
4. [上下文文件](/docs.zh/user-guide/features/context-files)
5. [Git Worktrees](/docs.zh/user-guide/git-worktrees)

### “我想把它做成 Telegram / Discord Bot”

推荐顺序：

1. [消息网关总览](/docs.zh/user-guide/messaging/index)
2. [Telegram](/docs.zh/user-guide/messaging/telegram)
3. [Discord](/docs.zh/user-guide/messaging/discord)
4. [Slack](/docs.zh/user-guide/messaging/slack)
5. [安全](/docs.zh/user-guide/security)

### “我想做自动化和定时任务”

推荐顺序：

1. [消息网关](/docs.zh/user-guide/messaging/index)
2. [子代理委派](/docs.zh/user-guide/features/delegation)
3. [程序化工具调用](/docs.zh/user-guide/features/code-execution)
4. [Provider 路由](/docs.zh/user-guide/features/provider-routing)

### “我想接自定义工具 / 技能 / MCP”

推荐顺序：

1. [Skills](/docs.zh/user-guide/features/skills)
2. [MCP](/docs.zh/user-guide/features/mcp)
3. [MCP 配置参考](/docs.zh/reference/mcp-config-reference)
4. [内置工具参考](/docs.zh/reference/tools-reference)

### “我想使用本地模型”

重点看：

- [AI Provider 集成](/docs.zh/integrations/providers)
- [配置](/docs.zh/user-guide/configuration)
- [常见问题](/docs.zh/reference/faq)

## 功能总览

Hermes 的高频能力可以粗分为：

- 交互：CLI、聊天平台、ACP 编辑器
- 执行：终端、文件、浏览器、Web、语音
- 组织：会话、Profiles、记忆、Skills
- 扩展：MCP、Plugins、Provider Routing
- 自动化：后台会话、定时任务、子代理、程序化工具调用

## 下一步阅读

- 要快速上手：看 [快速开始](/docs.zh/getting-started/quickstart)
- 要稳定长期使用：看 [配置](/docs.zh/user-guide/configuration)
- 要接平台和自动化：看 [消息网关](/docs.zh/user-guide/messaging/index)
- 要排错：看 [FAQ](/docs.zh/reference/faq)

