---
sidebar_position: 8
title: "Mattermost"
description: "把 Hermes Agent 配置成 Mattermost Bot"
---

# Mattermost 配置

Hermes 可以作为 Mattermost bot 工作，支持私聊、团队频道和 slash commands，适合自托管团队协作环境。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/mattermost.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/mattermost](/docs/user-guide/messaging/mattermost)
:::

## 基本流程

1. 开启 bot accounts
2. 创建 bot
3. 把 bot 加入频道
4. 配置 token、用户和回复模式
5. 启动 gateway

## 常见能力

- 线程回复
- mention 控制
- 指定频道自由回复

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [Slack](/docs.zh/user-guide/messaging/slack)
