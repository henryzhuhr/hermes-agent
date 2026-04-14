---
sidebar_position: 5
title: "新增 Provider"
description: "如何为 Hermes Agent 新增推理 provider：认证、运行时解析、CLI 流程、适配器、测试与文档"
---

# 新增 Provider

Hermes 已经能接任意 OpenAI-compatible endpoint。除非你需要一等公民级体验，否则不要轻易加内建 provider。

:::note 中文整理版
本页是 `website/docs/developer-guide/adding-providers.md` 的中文整理版。英文原文：[/docs/developer-guide/adding-providers](/docs/developer-guide/adding-providers)
:::

## 先判断该走哪条路径

### 路径 A：OpenAI-compatible provider

如果只是 base URL + API key 的变化，通常不需要新增内建 provider，命名 custom provider 就够了。

### 路径 B：原生 provider

只有在这些场景才值得做：

- 需要专门 auth / token refresh
- 需要 curated model catalog
- 需要 `hermes model` / setup 的一等接入
- API 形态不兼容 OpenAI

## 实现涉及哪些层

一个 provider 往往要同时打通：

- `hermes_cli/auth.py`
- `hermes_cli/models.py`
- `hermes_cli/runtime_provider.py`
- `hermes_cli/main.py`
- `agent/auxiliary_client.py`
- 原生 provider 还可能涉及 `run_agent.py` 和新 adapter

## 常见坑

- auth 加了，但模型解析没加
- 忘了 `config["model"]` 有多种形态
- 只改主路径，忘了 auxiliary
- 把 OpenRouter 专属参数错误传给其他 provider

## 测试与验证

这类改动很容易“CLI 能配，运行时报错”。需要同时验证：

- `hermes model`
- setup 流程
- 主对话模型
- auxiliary 模型
- fallback / routing 兼容性

## 相关页面

- [Provider Runtime Resolution](/docs.zh/developer-guide/provider-runtime)
- [AI Providers](/docs.zh/integrations/providers)
- [Configuration](/docs.zh/user-guide/configuration)
