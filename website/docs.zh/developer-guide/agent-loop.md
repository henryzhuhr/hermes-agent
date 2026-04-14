---
sidebar_position: 3
title: "Agent Loop 内部实现"
description: "详细讲解 AIAgent 执行、API 模式、工具、回调与 fallback 行为"
---

# Agent Loop 内部实现

Hermes 的核心引擎就是 `run_agent.py` 里的 `AIAgent`。这是全仓库最重要、也最重的模块之一。

:::note 中文整理版
本页是 `website/docs/developer-guide/agent-loop.md` 的中文整理版。英文原文：[/docs/developer-guide/agent-loop](/docs/developer-guide/agent-loop)
:::

## 它负责什么

`AIAgent` 同时负责：

- 组装 prompt 和工具 schema
- 选择 provider / API mode
- 发起可中断的模型调用
- 执行工具调用
- 维护对话历史
- 处理压缩、重试、fallback
- 跟踪 iteration budget
- 在上下文丢失前刷新 memory

## 两个入口

- `chat()`：简单字符串接口
- `run_conversation()`：完整结构化接口

后者才是真正的主循环入口。

## Turn 生命周期

一个典型回合包括：

1. 组装消息与 tool schemas
2. 发起模型调用
3. 若有 tool calls，则 dispatch 执行并把结果写回消息
4. 若没有 tool calls，则结束本轮

## 工具执行

Hermes 支持顺序或并发工具执行，但并发并不总是更好。真正的关键是工具之间是否独立，以及结果写回上下文的顺序是否还能保持可解释。

## Budget 与 Fallback

长会话里，`AIAgent` 会管理：

- iteration budget
- fallback model
- 压缩阈值

这些决定了 agent 是“稳妥收敛”还是“在复杂任务里越跑越散”。

## 压缩与持久化

当上下文太长时，主循环会触发压缩，并和 session persistence 联动，保证会话不是简单截断。

## 相关页面

- [Prompt Assembly](/docs.zh/developer-guide/prompt-assembly)
- [Provider Runtime Resolution](/docs.zh/developer-guide/provider-runtime)
- [Context Compression and Caching](/docs.zh/developer-guide/context-compression-and-caching)
