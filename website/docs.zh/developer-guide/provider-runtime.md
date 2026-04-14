---
sidebar_position: 4
title: "Provider 运行时解析"
description: "Hermes 如何在运行时解析 provider、凭据、API mode 与 auxiliary 模型"
---

# Provider 运行时解析

Hermes 有一套共享的 provider 运行时解析逻辑，CLI、gateway、cron、ACP 和 auxiliary calls 都依赖它。

:::note 中文整理版
本页是 `website/docs/developer-guide/provider-runtime.md` 的中文整理版。英文原文：[/docs/developer-guide/provider-runtime](/docs/developer-guide/provider-runtime)
:::

## 它解决什么问题

运行时解析决定：

- 当前到底走哪个 provider
- 从哪里拿凭据
- 使用哪种 API mode
- auxiliary 任务是否走不同 provider

## 为什么重要

如果这层不统一，就会出现：

- CLI 能跑，gateway 不能
- 主模型能跑，压缩或视觉模型不能
- `hermes model` 选择了一个 provider，但底层解析成另一个

## 关键文件

- `hermes_cli/runtime_provider.py`
- `hermes_cli/auth.py`
- `hermes_cli/model_switch.py`
- `agent/auxiliary_client.py`

## 高风险点

- OpenRouter、AI Gateway、自定义 OpenAI-compatible base URL 的混用
- 原生 Anthropic 路径
- Codex / GPT 特殊 API mode
- fallback 与 auxiliary 的交叉行为

## 相关页面

- [Adding Providers](/docs.zh/developer-guide/adding-providers)
- [AI Providers](/docs.zh/integrations/providers)
- [Configuration](/docs.zh/user-guide/configuration)
