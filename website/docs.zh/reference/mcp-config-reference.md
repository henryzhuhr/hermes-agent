---
sidebar_position: 8
title: "MCP 配置参考"
description: "Hermes Agent 的 MCP 配置键、过滤语义与 utility tool 策略参考"
---

# MCP 配置参考

本页是主 [MCP](/docs.zh/user-guide/features/mcp) 文档的紧凑参考版，专注 `config.yaml` 里的配置形状与过滤规则。

:::note 中文整理版
本页是 `website/docs/reference/mcp-config-reference.md` 的中文整理版。英文原文：[/docs/reference/mcp-config-reference](/docs/reference/mcp-config-reference)
:::

## 根配置结构

```yaml
mcp_servers:
  <server_name>:
    command: "..."
    args: []
    env: {}

    # 或
    url: "..."
    headers: {}

    enabled: true
    timeout: 120
    connect_timeout: 60
```

## 常见键

- `command` / `args`：本地 `stdio` server
- `url` / `headers`：远程 HTTP server
- `enabled`：是否启用
- `timeout` / `connect_timeout`：请求和连接超时
- `env`：传给 server 的环境变量

## `tools` 过滤

你可以对每个 server 做工具过滤：

- `include`
- `exclude`

语义上通常是先定义范围，再用排除项收紧。这样可以只开放少数可信工具，而不是把整个 server 暴露给 agent。

## Utility tools

Hermes 还可以控制是否注册 resources 和 prompts 相关 utility tools。若你只想要工具，不想让 agent 读资源或 prompt，可以明确关闭。

## 示例

### 只允许 GitHub 少量工具

```yaml
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    tools:
      include: ["create_issue", "list_issues"]
```

### 资源型文档 server

适合只暴露 resources，不暴露可执行工具。

## 命名与重载

- 配置更新后通常需要重载或重启 Hermes
- 工具名会做规范化处理，避免非法字符

## 相关页面

- [MCP](/docs.zh/user-guide/features/mcp)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
