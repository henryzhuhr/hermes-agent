---
sidebar_position: 4
title: "Slack"
description: "使用 Socket Mode 把 Hermes Agent 配置为 Slack Bot"
---

# Slack 配置

Slack 集成基于 Socket Mode，因此 Hermes 不需要公开 HTTP webhook 端口，也能在本机、内网或受防火墙保护的服务器上工作。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/slack.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/slack](/docs/user-guide/messaging/slack)
:::

## 基本流程

1. 创建 Slack App
2. 配置 bot scopes 和 events
3. 开启 Socket Mode
4. 安装到 workspace
5. 把 token 写入 Hermes 配置
6. 启动 gateway

## Slack 上的高频行为

- 频道消息与线程回复
- @mention 触发
- 私聊 bot
- 语音消息转写

## 为什么 Slack 路径值得单独看

Slack 的线程、mention、workspace 安装和 OAuth token 管理和 Telegram / Discord 不一样，尤其适合团队内部协作。

## 常见注意点

- 漏配 scope 会导致 bot 无法收消息或回消息
- workspace 内邀请 bot 到频道前，bot 可能不会响应
- 多工作区场景需要额外注意 token 与安装范围

## 下一步

- [消息网关](/docs.zh/user-guide/messaging/index)
- [安全](/docs.zh/user-guide/security)
- [语音模式](/docs.zh/user-guide/features/voice-mode)
