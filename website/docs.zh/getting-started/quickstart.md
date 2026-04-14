---
sidebar_position: 2
title: "快速开始"
description: "从安装到第一次对话，2 分钟跑通 Hermes Agent"
---

# 快速开始

:::note 中文整理版
本页是 `website/docs/getting-started/quickstart.md` 的中文整理版，保留首次上手所需的最短路径。英文原文：[/docs/getting-started/quickstart](/docs/getting-started/quickstart)
:::

## 1. 安装 Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
```

Android 用户请改看 [Termux 指南](/docs.zh/getting-started/termux)。Windows 用户请先在 WSL2 中安装。

## 2. 配置模型提供方

最常用的入口：

```bash
hermes model
hermes tools
hermes setup
```

常见提供方包括：

- Nous Portal
- OpenRouter
- Anthropic
- GitHub Copilot / Copilot ACP
- OpenAI 兼容自建端点
- Ollama / vLLM / SGLang / llama.cpp / LM Studio
- 多个中文模型平台，如 z.ai、Kimi、MiniMax、DashScope

Hermes 要求模型上下文窗口至少 **64K**，否则不适合多步工具调用。

## 3. 开始聊天

```bash
hermes
```

然后直接输入问题，例如：

```text
❯ 帮我看看当前目录里最大的 5 个文件夹
```

## 4. 先试几个关键能力

### 让它使用终端

```text
❯ 查看我的磁盘占用，并列出最大的 5 个目录
```

### 使用 Slash 命令

输入 `/` 可以看到命令补全。常用命令：

- `/help`
- `/model`
- `/tools`
- `/personality`
- `/save`
- `/compress`

### 多行输入

- `Alt+Enter` 或 `Ctrl+J` 插入换行
- 适合粘贴代码、日志或长提示词

### 中断当前任务

- 直接发送新消息即可打断当前流程
- 或使用 `Ctrl+C`

### 恢复上次会话

```bash
hermes --continue
# 或
hermes -c
```

## 5. 继续探索

### 配置更安全的终端后端

```bash
hermes config set terminal.backend docker
# 或
hermes config set terminal.backend ssh
```

### 连接聊天平台

```bash
hermes gateway setup
```

### 开启语音模式

```bash
pip install "hermes-agent[voice]"
```

进入 CLI 后：

```text
/voice on
```

### 安排自动任务

你可以直接让 Hermes 创建 cron 任务，例如每天汇总新闻并发到 Telegram。

### 搜索和安装 Skills

```bash
hermes skills search kubernetes
hermes skills install openai/skills/k8s
```

### 在编辑器中通过 ACP 使用 Hermes

```bash
pip install -e '.[acp]'
hermes acp
```

### 尝试 MCP Server

在 `~/.hermes/config.yaml` 中配置：

```yaml
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxx"
```

## 快速参考

| 动作 | 命令 |
|---|---|
| 启动 CLI | `hermes` |
| 选择模型 | `hermes model` |
| 配置工具 | `hermes tools` |
| 完整初始化 | `hermes setup` |
| 启动网关 | `hermes gateway` |
| 健康检查 | `hermes doctor` |

## 下一步

- [CLI 界面](/docs.zh/user-guide/cli)
- [配置](/docs.zh/user-guide/configuration)
- [消息网关](/docs.zh/user-guide/messaging/index)
- [AI Provider 集成](/docs.zh/integrations/providers)

