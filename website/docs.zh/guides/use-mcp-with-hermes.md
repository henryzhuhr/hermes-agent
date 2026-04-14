---
sidebar_position: 6
title: "在 Hermes 中使用 MCP"
description: "把 MCP server 接到 Hermes、过滤工具并在真实工作流中安全使用的实战指南"
---

# 在 Hermes 中使用 MCP

如果功能页解释的是“什么是 MCP”，这份指南讲的是“怎样在日常工作里真的把它用起来，而且别把自己坑到”。

:::note 中文整理版
本页是 `website/docs/guides/use-mcp-with-hermes.md` 的中文整理版。英文原文：[/docs/guides/use-mcp-with-hermes](/docs/guides/use-mcp-with-hermes)
:::

## 什么时候该用 MCP

适合用 MCP 的情况：

- 现成工具已经有 MCP server
- 你想通过清晰 RPC 边界接内部系统
- 你需要按 server 精细控制工具暴露面

不适合用 MCP 的情况：

- Hermes 内置工具已经足够
- 目标 server 暴露面太大，你却不准备做过滤
- 只是一个很窄的小集成，原生 tool 更简单

## 心智模型

把 MCP 想成“外接工具总线”：

- Hermes 负责对话、会话、工具编排
- MCP server 负责对接外部能力
- 你负责控制哪些能力真正让模型看见

## 最佳落地路径

### 第一步：一次只加一个 server

别一上来接五个 server。先接一个、跑通、验证工具名和行为，再扩张。

### 第二步：立刻做过滤

优先白名单，而不是“先全开，之后再看”。尤其是 GitHub、数据库、内部 API 这类有破坏力的系统。

### 第三步：验证已加载内容

确认 Hermes 实际注册了哪些工具，而不是只看 MCP server 广告自己支持什么。

## 常见模式

- 本地项目助手
- GitHub triage 助手
- 内部 API 助手
- 文档 / 知识库读取 server

## 安全建议

- 危险系统优先 allowlist
- 不用的 utility wrappers 关掉
- 每个 server 范围尽量收窄
- 改配置后及时重载或重启

## 相关页面

- [MCP](/docs.zh/user-guide/features/mcp)
- [MCP 配置参考](/docs.zh/reference/mcp-config-reference)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
