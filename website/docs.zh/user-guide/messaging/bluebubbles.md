---
sidebar_position: 8
title: "BlueBubbles（iMessage）"
description: "通过 BlueBubbles 和私有 API 辅助连接 Hermes 到 iMessage"
---

# BlueBubbles（iMessage）集成

这条路径允许你通过 BlueBubbles 把 Hermes 接到 iMessage。它依赖 macOS 端桥接和私有 API 辅助，比普通 Webhook / Bot 平台更偏个人设备生态。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/bluebubbles.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/bluebubbles](/docs/user-guide/messaging/bluebubbles)
:::

## 适合谁

- 深度使用 Apple 生态
- 想在 iMessage 中调用 Hermes
- 能接受私有 API 辅助带来的环境要求

## 基本思路

1. 配 BlueBubbles server
2. 让 Hermes 连到对应服务
3. 完成授权
4. 启动 gateway

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [Telegram](/docs.zh/user-guide/messaging/telegram)
