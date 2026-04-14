---
sidebar_position: 4
title: "教程：团队 Telegram 助手"
description: "逐步搭建一个供整个团队使用的 Telegram Hermes Bot，用于代码帮助、调研、运维等场景"
---

# 搭建团队 Telegram 助手

这份教程讲的是如何把 Hermes 接成一个团队可共用的 Telegram bot，并且在多人使用下仍保持会话隔离和安全控制。

:::note 中文整理版
本页是 `website/docs/guides/team-telegram-assistant.md` 的中文整理版。英文原文：[/docs/guides/team-telegram-assistant](/docs/guides/team-telegram-assistant)
:::

## 目标效果

这个 bot 具备：

- 授权团队成员可私聊求助
- 后端运行在你的服务器上
- 具备终端、文件、Web、执行等工具能力
- 每个用户拥有独立 session
- 支持定时任务和频道投递

## 第一步：创建 Telegram Bot

通过 BotFather 创建 bot 并拿到 token。

## 第二步：配置 Gateway

推荐先用交互式方式：

```bash
hermes gateway setup
```

如果走手动配置，也至少要准备：

- bot token
- 你的 Telegram user ID
- 授权策略

## 第三步：启动 Gateway

```bash
hermes gateway
```

生产环境建议作为 systemd、launchd、Docker 或 tmux 常驻服务来跑。

## 第四步：团队授权

两种常用方式：

- 静态 allowlist
- DM pairing

团队场景通常更推荐 pairing，因为它比手工维护 ID 列表更灵活。

## 第五步：配置 Bot 行为

建议尽早确定这些内容：

- home channel
- 工具进度显示
- `SOUL.md` 的团队人格
- 项目上下文文件

## 第六步：加定时任务

这个 bot 很适合承担：

- 每日 standup 汇总
- 健康检查
- 项目提醒

## 生产建议

- 对外开放前先收紧 toolsets
- 尽量用 Docker 或隔离 backend
- 严格配置授权和日志审查

## 下一步

- [Telegram](/docs.zh/user-guide/messaging/telegram)
- [Security](/docs.zh/user-guide/security)
- [Daily Briefing Bot](/docs.zh/guides/daily-briefing-bot)
