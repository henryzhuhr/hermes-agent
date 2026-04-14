---
sidebar_position: 6
title: "Signal"
description: "通过 signal-cli daemon 把 Hermes Agent 配置成 Signal Bot"
---

# Signal 配置

Hermes 通过 `signal-cli` daemon 接入 Signal，适合更重视隐私和端到端加密的消息工作流。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/signal.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/signal](/docs/user-guide/messaging/signal)
:::

## 基本流程

1. 安装 `signal-cli`
2. 绑定或链接账号
3. 启动 daemon
4. 把相关配置写入 Hermes
5. 启动 gateway

## 特点

- 默认更隐私
- 支持附件
- 支持 typing indicators
- 适合安全敏感场景

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [Security](/docs.zh/user-guide/security)
