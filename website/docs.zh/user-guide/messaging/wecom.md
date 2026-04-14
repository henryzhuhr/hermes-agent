---
sidebar_position: 14
title: "WeCom（企业微信）"
description: "通过 AI Bot WebSocket gateway 把 Hermes Agent 接到企业微信"
---

# WeCom（企业微信）

Hermes 可以通过 WeCom 的 AI Bot WebSocket gateway 接入企业微信，实现实时双向通信，不需要公网 webhook。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/wecom.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/wecom](/docs/user-guide/messaging/wecom)
:::

## 前置条件

- 企业微信组织
- AI Bot
- Bot ID 和 Secret

## 基本流程

1. 创建 AI Bot
2. 配置 Hermes
3. 启动 gateway

## 特点

- 支持群和私聊策略
- 支持媒体收发
- 有重连与去重逻辑

## 相关页面

- [Feishu / Lark](/docs.zh/user-guide/messaging/feishu)
- [WeCom Callback](/docs.zh/user-guide/messaging/wecom-callback)
