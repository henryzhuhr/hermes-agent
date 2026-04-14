---
sidebar_position: 3
title: "Discord"
description: "把 Hermes Agent 配置成 Discord Bot"
---

# Discord 配置

Discord 适合把 Hermes 放进团队服务器或私聊环境中使用。它支持文本、附件、语音消息，以及更进一步的语音频道对话。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/discord.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/discord](/docs/user-guide/messaging/discord)
:::

## 1. 创建应用与 Bot

在 Discord Developer Portal 中：

- 创建应用
- 添加 bot
- 开启必要 intents
- 复制 bot token

## 2. 邀请到服务器

生成带权限的 invite URL，把 bot 拉进你的 server。

## 3. 配置 Hermes

把 Discord token 和相关配置写入 `.env` / `config.yaml`，再启动 gateway。

## Discord 上的行为特点

- 可以在 DM 中单独和 bot 对话
- 也可以在 server channel 里使用
- 会话映射与线程/频道上下文相关
- 支持语音消息，扩展后还能进语音频道

## 语音与 Slash 命令

Discord 是 Hermes 语音体验最完整的平台之一。若你要做实时语音频道对话，额外看 [语音模式](/docs.zh/user-guide/features/voice-mode)。

## 常见注意点

- 没开 intents，bot 可能看不到消息
- 权限不够，bot 无法读写频道
- 公开 server 一定要配授权策略

## 下一步

- [消息网关](/docs.zh/user-guide/messaging/index)
- [语音模式](/docs.zh/user-guide/features/voice-mode)
- [安全](/docs.zh/user-guide/security)
