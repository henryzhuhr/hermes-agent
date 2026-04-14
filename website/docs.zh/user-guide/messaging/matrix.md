---
sidebar_position: 9
title: "Matrix"
description: "把 Hermes Agent 配置成 Matrix Bot"
---

# Matrix 配置

Hermes 支持 Matrix，这是一套开放、联邦化的消息协议。你可以跑在自建 homeserver 或公共服务上，并把 Hermes 作为 bot 接进来。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/matrix.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/matrix](/docs/user-guide/messaging/matrix)
:::

## 行为特点

- 私聊与群聊都支持
- 支持附件和媒体
- 可选端到端加密

## 基本流程

1. 创建 bot 账户
2. 获取 access token
3. 配置 homeserver 与用户 ID
4. 启动 gateway

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [Security](/docs.zh/user-guide/security)
