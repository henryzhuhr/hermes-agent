---
sidebar_position: 5
title: "WhatsApp"
description: "通过内置 Baileys 桥把 Hermes Agent 配置成 WhatsApp Bot"
---

# WhatsApp 配置

Hermes 使用基于 Baileys 的内置桥接连接 WhatsApp Web，会话体验接近“给一个常驻的 WhatsApp 客户端挂上 Hermes 大脑”，而不是官方 Business API 集成。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/whatsapp.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/whatsapp](/docs/user-guide/messaging/whatsapp)
:::

:::warning 非官方接口
这条路径不是 Meta 官方 Business API，存在一定账号限制风险。正式商用前请先评估风险与合规性。
:::

## 两种理解方式

- 对个人或小团队来说，它很方便，因为不需要 Meta 开发者流程
- 对正式企业场景来说，它不是最稳妥的官方接入方式

## 基本流程

1. 配置 WhatsApp 相关桥接
2. 启动 Hermes gateway
3. 扫码配对
4. 验证文本和语音收发

## 适合的使用场景

- 个人号码上的远程助理
- 小团队内部实验
- 需要移动端即时访问 Hermes 的场景

## 常见注意点

- 重新配对时要关注 session 持久化
- 大段 Markdown、工具进度和消息分片会影响聊天体验
- 语音消息可转写，但依赖对应语音配置

## 下一步

- [消息网关](/docs.zh/user-guide/messaging/index)
- [语音模式](/docs.zh/user-guide/features/voice-mode)
- [安全](/docs.zh/user-guide/security)
