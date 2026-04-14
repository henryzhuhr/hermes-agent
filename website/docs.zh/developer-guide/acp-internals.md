---
sidebar_position: 2
title: "ACP 内部实现"
description: "ACP adapter 如何工作：生命周期、sessions、事件桥、审批与工具渲染"
---

# ACP 内部实现

ACP adapter 本质上是把同步的 `AIAgent` 包进一个异步 JSON-RPC stdio server，让编辑器前端能把 Hermes 当作 ACP server 使用。

:::note 中文整理版
本页是 `website/docs/developer-guide/acp-internals.md` 的中文整理版。英文原文：[/docs/developer-guide/acp-internals](/docs/developer-guide/acp-internals)
:::

## 启动流程

核心涉及：

- `acp_adapter/entry.py`
- `acp_adapter/server.py`
- `acp_adapter/session.py`
- `acp_adapter/events.py`

## 主要组件

- `HermesACPAgent`
- `SessionManager`
- 事件桥
- 权限桥
- 工具渲染辅助层

## Session 生命周期

ACP 也有自己的 session 管理，包括取消、分叉、工作目录绑定和工具调用呈现。

## 权限与审批

编辑器里的审批请求不是 gateway 的样子，但底层仍要桥接 Hermes 现有审批模型。

## 当前限制

ACP 很强，但仍受编辑器实现、stdio 生命周期和工具渲染方式约束。不要假设它和 CLI / gateway 是完全同构体验。

## 相关页面

- [ACP 编辑器集成](/docs.zh/user-guide/features/acp)
- [Architecture](/docs.zh/developer-guide/architecture)
