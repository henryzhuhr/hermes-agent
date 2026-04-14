---
sidebar_position: 7
title: "Gateway 内部实现"
description: "消息网关如何启动、授权用户、路由会话并投递消息"
---

# Gateway 内部实现

Messaging gateway 是 Hermes 接到十多个外部平台的长期运行进程。它不只是“收消息再回文本”，还负责授权、session 路由、hooks、cron 和后台维护。

:::note 中文整理版
本页是 `website/docs/developer-guide/gateway-internals.md` 的中文整理版。英文原文：[/docs/developer-guide/gateway-internals](/docs/developer-guide/gateway-internals)
:::

## 关键文件

- `gateway/run.py`
- `gateway/session.py`
- `gateway/delivery.py`
- `gateway/pairing.py`
- `gateway/hooks.py`
- `gateway/status.py`

## 消息流

典型路径：

1. 平台 adapter 收到消息
2. gateway 做授权检查
3. 解析 session key
4. 把消息投递给 `AIAgent`
5. 把回复和工具进度发回平台

## Session Key

session key 的构造决定了：

- 私聊是否隔离
- 群聊是否共享上下文
- 线程 / 频道如何映射

## 授权

gateway 内建：

- allowlist
- DM pairing
- 平台级授权控制

## Hooks 与后台维护

gateway 不只是消息通道，还承担：

- hooks 生命周期
- memory flush
- 背景进程维护
- cron ticking

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [新增平台适配器](/docs.zh/developer-guide/adding-platform-adapters)
- [Security](/docs.zh/user-guide/security)
