---
sidebar_position: 10
title: "DingTalk"
description: "把 Hermes Agent 配置成钉钉聊天机器人"
---

# DingTalk 配置

Hermes 可以作为钉钉机器人接入，支持私聊和群聊，并通过 Stream Mode 长连接工作，无需公网 webhook。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/dingtalk.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/dingtalk](/docs/user-guide/messaging/dingtalk)
:::

## 行为模型

- 私聊：默认每条消息都响应
- 群聊：通常需要 `@mention`
- 每个对话有独立 session

## 基本流程

1. 创建钉钉应用
2. 开启机器人能力
3. 获取用户 ID
4. 把 client id / secret 等写入配置
5. 启动 gateway

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [Security](/docs.zh/user-guide/security)
