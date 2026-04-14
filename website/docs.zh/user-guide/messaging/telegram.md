---
sidebar_position: 1
title: "Telegram"
description: "把 Hermes Agent 配置成 Telegram Bot"
---

# Telegram 配置

Telegram 是 Hermes 最成熟的消息入口之一。接入后，你可以从任意设备与 agent 聊天、发送语音、接收定时任务结果，并在群聊中使用 bot。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/telegram.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/telegram](/docs/user-guide/messaging/telegram)
:::

## 1. 创建 Bot

通过 BotFather 创建 bot，拿到 bot token。

## 2. 配置 Hermes

把 Telegram 相关 token 和配置写入 `~/.hermes/.env` / `config.yaml`。如果你打算只允许部分人使用，记得同时配置 allowlist 或 pairing。

## 3. 启动 Gateway

```bash
hermes gateway
```

首次上线后，先在私聊里验证：

- 基本文本收发
- 工具进度是否显示
- 语音消息是否能转写

## Telegram 上的典型能力

- 私聊对话
- 群聊机器人
- 语音消息转写
- 定时任务结果投递
- home channel / topic 等定向投递

## Webhook 与轮询

文档还提供 webhook 模式与更多高级配置。如果你要做公网稳定部署或高并发，再回头对照英文完整页。

## 常见注意点

- Telegram 隐私模式会影响群聊行为
- group/forum topics 会影响会话映射
- 生产环境务必检查授权策略

## 下一步

- [消息网关](/docs.zh/user-guide/messaging/index)
- [语音模式](/docs.zh/user-guide/features/voice-mode)
- [安全](/docs.zh/user-guide/security)
