---
sidebar_position: 8
sidebar_label: "SMS（Twilio）"
title: "SMS（Twilio）"
description: "通过 Twilio 把 Hermes Agent 配置成 SMS 聊天机器人"
---

# SMS 配置（Twilio）

Hermes 可以通过 Twilio 接入普通短信。用户给 Twilio 号码发短信，Hermes 再回短信。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/sms.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/sms](/docs/user-guide/messaging/sms)
:::

## 基本流程

1. 获取 Twilio 凭据
2. 配 Hermes 的 Twilio 配置
3. 配好 webhook
4. 启动 gateway

## 注意点

- 公开短信入口风险更高，建议严格 allowlist
- 依赖外部 webhook 可达性

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [Webhooks](/docs.zh/user-guide/messaging/webhooks)
