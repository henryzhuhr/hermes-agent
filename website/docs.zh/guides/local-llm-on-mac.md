---
sidebar_position: 2
title: "在 Mac 上运行本地 LLM"
description: "在 macOS 上用 llama.cpp 或 MLX 搭建 OpenAI-compatible 本地模型服务"
---

# 在 Mac 上运行本地 LLM

这份指南讲的是如何在 Apple Silicon Mac 上本地跑一个兼容 OpenAI API 的推理服务，再把 Hermes 接过去使用。

:::note 中文整理版
本页是 `website/docs/guides/local-llm-on-mac.md` 的中文整理版。英文原文：[/docs/guides/local-llm-on-mac](/docs/guides/local-llm-on-mac)
:::

## 两条主路径

| 后端 | 适合场景 |
|---|---|
| `llama.cpp` | 安装简单、首 token 更快、GGUF 生态成熟 |
| MLX / `omlx` | Apple Silicon 原生优化、更偏高吞吐 |

两者都能暴露 OpenAI-compatible `/v1/chat/completions` 接口。

## 先选模型

最关键的不是“参数越大越好”，而是：

- 你机器的内存
- 工具调用稳定性
- 实际上下文长度

Hermes 更需要足够上下文和稳健工具调用，而不是单纯聊天跑分。

## 方案 A：`llama.cpp`

核心步骤：

1. `brew install llama.cpp`
2. 下载 GGUF 模型
3. 启动 `llama-server`
4. 用 `curl` 测试接口
5. 记录模型名和端口

如果机器内存紧张，可以优先用更激进的量化和更保守的上下文设置。

## 方案 B：MLX / `omlx`

核心步骤：

1. 安装 MLX 路径工具
2. 下载 MLX / safetensors 格式模型
3. 启动本地服务
4. 测试 OpenAI-compatible API

这条路径在 Apple Silicon 上通常更“原生”，但模型与工具生态和 `llama.cpp` 不完全一样。

## 接到 Hermes

最简单的方式是走自定义 provider：

- `OPENAI_BASE_URL=http://localhost:.../v1`
- `OPENAI_API_KEY=<任意占位或按服务要求>`
- 模型名填你本地服务实际暴露的名字

也可以直接用 `hermes model` 走交互配置。

## 重要提醒：上下文长度

本地模型最常见的问题不是“连不上”，而是 Hermes 以为你有大上下文，但服务端实际只给了很小的 `context length`。这会直接影响工具调用、压缩频率和稳定性。

## 什么时候适合本地模型

- 隐私优先
- 长期成本敏感
- 你愿意接受一些模型能力折中

## 进一步阅读

- [AI Providers](/docs.zh/integrations/providers)
- [Configuration](/docs.zh/user-guide/configuration)
- [FAQ](/docs.zh/reference/faq)
