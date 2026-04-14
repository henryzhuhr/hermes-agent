---
sidebar_position: 6
title: "事件 Hooks"
description: "在关键生命周期点运行自定义代码：记录活动、发送告警、推送到 webhook"
---

# 事件 Hooks

Hermes 有两套 hook 系统，分别面向 gateway 和 plugin。它们都允许你在关键生命周期点运行自定义代码。

:::note 中文整理版
本页是 `website/docs/user-guide/features/hooks.md` 的中文整理版。英文原文：[/docs/user-guide/features/hooks](/docs/user-guide/features/hooks)
:::

## 两类 Hooks

| 类型 | 注册方式 | 运行位置 |
|---|---|---|
| Gateway hooks | `HOOK.yaml` + `handler.py` | Gateway only |
| Plugin hooks | `ctx.register_hook()` | CLI + Gateway |

## 常见用途

- 日志
- 告警
- Webhook 通知
- 工具拦截
- 指标上报
- Guardrails

## 实践建议

Hook 应该尽量非阻塞，并把失败限制在自己内部，不影响主 agent 流程。

## 相关页面

- [Plugins](/docs.zh/user-guide/features/plugins)
- [Gateway Internals](/docs.zh/developer-guide/gateway-internals)
