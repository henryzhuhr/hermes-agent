---
sidebar_position: 11
title: "Feishu / Lark"
description: "把 Hermes Agent 配置成飞书 / Lark 机器人"
---

# Feishu / Lark 配置

Hermes 可以作为飞书 / Lark 机器人接入，支持私聊、群聊、home chat，以及文本、图片、音频和文件附件。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/feishu.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/feishu](/docs/user-guide/messaging/feishu)
:::

## 两种连接模式

- `websocket`：推荐，不需要公网 webhook
- `webhook`：适合你希望平台主动推送事件

## 基本流程

1. 创建应用
2. 选择连接模式
3. 写入配置
4. 启动 gateway

## 能力特点

- home chat
- 交互卡片动作
- 多媒体收发
- 批量与去重处理

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [WeCom](/docs.zh/user-guide/messaging/wecom)
