---
sidebar_position: 4
title: "MCP（Model Context Protocol）"
description: "通过 MCP 把 Hermes Agent 连接到外部工具服务器，并精确控制加载哪些 MCP 工具"
---

# MCP（Model Context Protocol）

MCP 让 Hermes 能接入外部工具服务器，把 GitHub、数据库、文件系统、内部 API 或任意现成工具暴露给 agent。对 Hermes 来说，MCP 是扩展工具能力的第一等公民，而不是外围插件。

:::note 中文整理版
本页是 `website/docs/user-guide/features/mcp.md` 的中文整理版。英文原文：[/docs/user-guide/features/mcp](/docs/user-guide/features/mcp)
:::

## MCP 能带来什么

- 复用现有工具，而不是重写成本地 tool
- 给特定业务系统快速加能力
- 让工具面按 server 拆分，更好管理权限

## 两种接入方式

- `stdio`：Hermes 拉起本地子进程型 MCP server
- `http`：Hermes 连接远程 MCP server

前者部署简单，后者更适合共享服务或远程基础设施。

## 最小示例

```yaml
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxx"
```

## 你可以控制什么

Hermes 不只是“连上就全收”。你可以控制：

- server 是否启用
- timeout
- 只包含哪些 tools
- 排除哪些 tools
- 是否注册 resources / prompts

这能显著降低无关工具噪音和安全暴露面。

## Runtime 行为

连接成功后，MCP tools 会像内置工具一样进入工具面，名称通常带 server 前缀，例如 `github_create_issue`。

## 与 Toolset 的关系

MCP tools 也会形成动态 toolset。这样你可以把外部能力像原生能力一样按平台启用或禁用。

## 安全建议

- 只给 MCP server 最小必要凭据
- 对外部 server 做 allowlist
- 不需要的 resources / prompts 默认关闭
- 在公网 bot 场景严格过滤工具

## 常见用途

- GitHub issue / PR 流程
- 数据库查询
- 内部知识库访问
- 第三方 SaaS 操作

## 进一步阅读

- [MCP Config Reference](/docs.zh/reference/mcp-config-reference)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- 英文实践指南：[/docs/guides/use-mcp-with-hermes](/docs/guides/use-mcp-with-hermes)
