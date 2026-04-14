---
sidebar_position: 1
title: "消息网关"
description: "从 Telegram、Discord、Slack、WhatsApp 等平台与 Hermes 对话：架构与配置总览"
---

# 消息网关

Hermes 的 messaging gateway 是一个统一后台进程，负责连接多个聊天平台、处理会话、执行 cron，并把结果投递回相应入口。它不是“每个平台各写一套 bot”，而是“一个 agent 平台，多种前端”。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/index.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/index](/docs/user-guide/messaging/index)
:::

## 支持的平台

本阶段中文页覆盖：

- [Telegram](/docs.zh/user-guide/messaging/telegram)
- [Discord](/docs.zh/user-guide/messaging/discord)
- [Slack](/docs.zh/user-guide/messaging/slack)
- [WhatsApp](/docs.zh/user-guide/messaging/whatsapp)

其余平台目前仍保留英文，例如 Signal、Email、Matrix、Home Assistant、Feishu、WeCom、Webhooks 等。

## Gateway 架构

网关统一处理这些事情：

- 平台消息接入
- 会话映射与恢复
- 工具执行与进度回传
- 语音消息转写与投递
- 定时任务与后台完成通知

这意味着你只需要维护一套 Hermes 配置，而不是给每个平台单独拼接不同 agent 行为。

## 基本启动流程

```bash
hermes gateway setup
hermes gateway
```

或者根据你的部署方式，用 systemd、launchd、Docker 等方式常驻运行。

## 配置重点

上线任一平台前，建议先确认：

- 平台 token / secret 已写入 `.env`
- allowlist 或授权策略已配置
- `MESSAGING_CWD` 正确
- terminal backend 和 approvals.mode 符合风险预期

## 会话模型

网关不会简单地把所有消息塞进一个大对话。它会按平台、用户、群组或线程映射到独立 session，避免上下文串台。

## 工具进度与后台任务

消息平台里通常还会显示：

- 工具进度
- 长任务状态
- 后台进程完成通知

这让 Hermes 不只是“回复一段文本”，而是能远程操作一个持续运行的 agent。

## 生产部署建议

- 先配 [Security](/docs.zh/user-guide/security)
- 对公网平台尽量使用隔离 backend
- 给不同 bot 分配不同 profile
- 把 gateway 当作长期服务管理

## 下一步

- [Telegram](/docs.zh/user-guide/messaging/telegram)
- [Discord](/docs.zh/user-guide/messaging/discord)
- [Slack](/docs.zh/user-guide/messaging/slack)
- [WhatsApp](/docs.zh/user-guide/messaging/whatsapp)
