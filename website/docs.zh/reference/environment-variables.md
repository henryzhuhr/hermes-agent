---
sidebar_position: 2
title: "环境变量"
description: "Hermes Agent 使用的环境变量参考"
---

# 环境变量参考

Hermes 的环境变量通常放在 `~/.hermes/.env`。你也可以通过 `hermes config set VAR value` 来写入。

:::note 中文速查版
本页是 `website/docs/reference/environment-variables.md` 的中文速查版。原英文页是完整清单，覆盖所有 provider、消息平台与行为开关。英文原文：[/docs/reference/environment-variables](/docs/reference/environment-variables)
:::

## LLM Providers

常见变量：

| 变量 | 说明 |
|---|---|
| `OPENROUTER_API_KEY` | OpenRouter API key |
| `OPENAI_API_KEY` / `OPENAI_BASE_URL` | 自定义 OpenAI-compatible 端点 |
| `ANTHROPIC_API_KEY` | Anthropic 兼容或相关直连配置 |
| `GLM_API_KEY` | z.ai / ZhipuAI |
| `KIMI_API_KEY` | Moonshot / Kimi |
| `MINIMAX_API_KEY` | MiniMax |
| `DASHSCOPE_API_KEY` | DashScope |
| `HF_TOKEN` | Hugging Face |

## Provider Auth / Copilot

| 变量 | 说明 |
|---|---|
| `COPILOT_GITHUB_TOKEN` | Copilot 认证主入口 |
| `GH_TOKEN` / `GITHUB_TOKEN` | GitHub token 备用入口 |
| `HERMES_COPILOT_ACP_COMMAND` | 覆盖 Copilot ACP CLI 路径 |

## Tool APIs

| 变量 | 说明 |
|---|---|
| 各类 `*_API_KEY` | Web 搜索、浏览器、TTS、图像等工具凭据 |
| MCP server 自定义 env | 由 `config.yaml` 中 `mcp_servers.*.env` 提供 |

## 终端与容器后端

| 变量 | 说明 |
|---|---|
| `MESSAGING_CWD` | 消息网关默认工作目录 |
| SSH / Docker / Modal / Daytona 相关变量 | 远程执行与容器资源控制 |
| 持久 shell 相关变量 | 控制 backend shell 生命周期 |

## Messaging

不同平台会有各自 token / secret，例如：

- Telegram bot token
- Discord bot token
- Slack app / socket mode token
- WhatsApp 桥接相关配置

这些变量往往决定 gateway 是否能正常启动。

## Agent Behavior

行为类变量和 `config.yaml` 通常搭配使用，常见包括：

- 背景通知
- 审批与安全模式
- 流式输出
- 语音相关 provider

## 建议

- secrets 全部放 `.env`
- 非敏感结构化配置放 `config.yaml`
- 不同 profile 使用独立 `.env`

## 相关页面

- [配置](/docs.zh/user-guide/configuration)
- [AI Providers](/docs.zh/integrations/providers)
- [消息网关](/docs.zh/user-guide/messaging/index)
