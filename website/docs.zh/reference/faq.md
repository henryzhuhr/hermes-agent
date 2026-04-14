---
sidebar_position: 3
title: "FAQ 与故障排查"
description: "Hermes Agent 的常见问题与排查方案"
---

# FAQ 与故障排查

这里汇总最常见的问题和修复路径。

:::note 中文整理版
本页是 `website/docs/reference/faq.md` 的中文整理版。英文原文：[/docs/reference/faq](/docs/reference/faq)
:::

## 常见问题

### 支持哪些 LLM provider？

基本上，任何 OpenAI-compatible endpoint 都能接。高频选择包括 OpenRouter、Anthropic、OpenAI 兼容端点、GitHub Copilot，以及 Ollama / vLLM / SGLang 等本地或自建服务。

### 支持 Windows 吗？

官方推荐路径是 WSL2，而不是原生 Windows shell。

### 支持 Android / Termux 吗？

支持，但推荐使用专门的 Termux 依赖路径，而不是直接安装所有 extras。见 [Termux 指南](/docs.zh/getting-started/termux)。

### 能离线用吗？

能，但前提是你有本地模型或自托管推理端点，并正确设置 base URL、模型名和上下文长度。

### Memory 和 Skills 有什么区别？

- Memory：保存长期稳定事实
- Skills：保存可复用流程与知识

## 安装问题

### `hermes: command not found`

- 重新加载 shell
- 检查 PATH
- 确认虚拟环境或安装目录已正确暴露

### Python 版本过低

升级到 3.11+。

### `uv: command not found`

重新安装 `uv`，或对照 [安装](/docs.zh/getting-started/installation) 页的手动步骤。

## Provider 与模型问题

### API key 无效 / 模型找不到

- 用 `hermes model` 重新配置
- 检查 `.env`
- 确认模型名与 provider 支持情况一致

### 上下文长度不够

- 压缩当前会话
- 换更大 context 的模型
- 如果是本地模型，检查服务端真实 context length

## 终端与执行问题

### 命令被判定为危险

这是审批系统在工作。看 [Security](/docs.zh/user-guide/security)。

### Docker backend 连不上

- 确认 Docker 正在运行
- 检查用户权限
- 检查 volume 与工作目录配置

## 消息平台问题

### Bot 不回复

- 确认 gateway 已启动
- 检查平台 token
- 检查 allowlist / pairing
- 查看 `hermes logs`

### 网关老是掉线

优先检查网络、systemd/launchd 配置、工作目录和平台侧 token 权限。

## MCP 问题

### MCP server 连不上

- 检查依赖是否安装
- 手工测试 server 命令
- 检查 timeout 和 env

### 工具没出现

- 检查 `mcp_servers` 配置
- 检查 include / exclude 过滤
- 重启或重载 Hermes

## 仍然卡住？

优先执行：

```bash
hermes doctor
hermes status
hermes logs
```

然后再对照英文完整 FAQ。
