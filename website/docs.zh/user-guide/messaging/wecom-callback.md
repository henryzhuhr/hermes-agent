---
sidebar_position: 15
---

# WeCom Callback（自建应用）

这条路径把 Hermes 接到企业微信自建应用的 callback / webhook 模式。它和普通 WeCom bot 路径不同，更像“企业应用接入”而不是“群聊机器人”。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/wecom-callback.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/wecom-callback](/docs/user-guide/messaging/wecom-callback)
:::

## 基本流程

1. 创建企业微信自建应用
2. 配环境变量
3. 启动 gateway
4. 配 callback endpoint

## 特点

- 支持多企业路由
- 有加密 XML callback
- 更适合“第一方企业应用”集成

## 相关页面

- [WeCom](/docs.zh/user-guide/messaging/wecom)
- [Webhooks](/docs.zh/user-guide/messaging/webhooks)
