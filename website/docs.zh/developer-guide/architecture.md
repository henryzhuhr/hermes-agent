---
sidebar_position: 1
title: "架构"
description: "Hermes Agent 内部总览：主要子系统、执行路径、数据流与阅读顺序"
---

# 架构

这页是 Hermes 内部结构的总地图。先用它建立方向感，再分别深入 agent loop、gateway、tools、prompt、session 等子系统。

:::note 中文整理版
本页是 `website/docs/developer-guide/architecture.md` 的中文整理版。英文原文：[/docs/developer-guide/architecture](/docs/developer-guide/architecture)
:::

## 主要入口

Hermes 有多个并行入口：

- CLI
- Messaging gateway
- ACP
- Batch runner
- Python library

这些入口最终都会落回核心 `AIAgent` 执行链路。

## 核心子系统

- Agent Loop：对话主循环、模型调用、工具执行、压缩与 fallback
- Prompt System：系统提示组装、cache 稳定性、上下文文件
- Provider Runtime：provider、凭据、api mode 与 auxiliary 路由
- Tool System：tool registry、toolsets、dispatch、terminal backend
- Session Persistence：SQLite + transcript
- Gateway：平台消息接入、授权、投递、后台维护
- Plugins / MCP / Skills：扩展层
- Cron / RL Environments：自动化与训练评估层

## 推荐阅读顺序

1. [Agent Loop Internals](/docs.zh/developer-guide/agent-loop)
2. [Prompt Assembly](/docs.zh/developer-guide/prompt-assembly)
3. [Provider Runtime Resolution](/docs.zh/developer-guide/provider-runtime)
4. [Tools Runtime](/docs.zh/developer-guide/tools-runtime)
5. [Session Storage](/docs.zh/developer-guide/session-storage)
6. [Gateway Internals](/docs.zh/developer-guide/gateway-internals)

## 设计原则

从仓库结构看，Hermes 有几个明显原则：

- 单一核心 agent，多个前端
- 工具注册集中化，但实现分散
- prompt cache 不轻易被破坏
- 配置尽量统一到 `~/.hermes/`
- 长期运行场景优先于一次性 demo

## 下一步

- [Agent Loop Internals](/docs.zh/developer-guide/agent-loop)
- [Adding Tools](/docs.zh/developer-guide/adding-tools)
- [Gateway Internals](/docs.zh/developer-guide/gateway-internals)
