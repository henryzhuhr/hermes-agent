---
title: "AI Providers"
sidebar_label: "AI Providers"
sidebar_position: 1
---

# AI Provider 集成

Hermes 至少需要一个可用的推理 provider 才能工作。它支持从云端 API 到本地推理端点的广泛选择，也支持 routing、fallback 和多模型分工。

:::note 中文整理版
本页是 `website/docs/integrations/providers.md` 的中文整理版。原文非常长，覆盖各类 provider、上下文窗口、自托管与 WSL2 网络问题；这里保留最常用配置路径。英文原文：[/docs/integrations/providers](/docs/integrations/providers)
:::

## 常见选择

- OpenRouter：最灵活，适合快速试多模型
- Anthropic / OpenAI 兼容端点：直连单 provider
- GitHub Copilot / Copilot ACP
- 中文模型平台：z.ai、Kimi、MiniMax、DashScope 等
- 本地 / 自托管：Ollama、vLLM、SGLang、llama.cpp、LM Studio

## 最常用配置入口

```bash
hermes model
```

如果你不想走交互向导，也可以直接编辑：

- `~/.hermes/.env`
- `~/.hermes/config.yaml`

## 本地模型

Hermes 支持任意 OpenAI-compatible endpoint。实践上最常见的是：

- Ollama：本地最省事
- vLLM：GPU 服务性能更强
- SGLang / llama.cpp / LM Studio：按场景选

重点不是“能不能连上”，而是要给 Hermes 正确的模型名、base URL 和上下文长度。

## 上下文长度

Hermes 对上下文窗口有实际要求。多步工具调用场景下，64K 以下通常很快捉襟见肘；如果你走本地模型，一定要核对服务端真实 `context length`。

## 高级能力

Provider 层还支持：

- [Provider Routing](/docs.zh/user-guide/features/provider-routing)
- [Fallback Providers](/docs.zh/user-guide/features/fallback-providers)
- Auxiliary models
- 自定义 base URL 与自托管兼容端点

## 选择建议

- 想最快跑通：OpenRouter
- 想走自建推理：Ollama 或 vLLM
- 想让 IDE / CLI / gateway 共用同一套 provider：统一写入 `~/.hermes/`

## 进一步阅读

- [Configuration](/docs.zh/user-guide/configuration)
- [Environment Variables](/docs.zh/reference/environment-variables)
- [FAQ](/docs.zh/reference/faq)
