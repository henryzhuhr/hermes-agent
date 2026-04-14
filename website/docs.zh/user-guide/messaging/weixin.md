---
sidebar_position: 15
title: "Weixin（微信）"
description: "通过 iLink Bot API 把 Hermes Agent 接到个人微信账号"
---

# Weixin（微信）

Hermes 可以通过 iLink Bot API 接到个人微信账号。这和企业微信是两条不同路线。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/weixin.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/weixin](/docs/user-guide/messaging/weixin)
:::

## 基本流程

1. 运行 setup wizard
2. 完成登录和 token 保存
3. 按需配置访问策略
4. 启动 gateway

## 特点

- 长轮询连接
- 支持媒体收发
- 有 markdown 和消息分片策略
- 带 token 持久化与去重

## 相关页面

- [WeCom](/docs.zh/user-guide/messaging/wecom)
- [消息网关](/docs.zh/user-guide/messaging/index)
