---
sidebar_position: 7
title: "Email"
description: "通过 IMAP/SMTP 把 Hermes Agent 配置成邮件助手"
---

# Email 配置

Hermes 可以通过标准 IMAP / SMTP 收邮件并在线程中回复，不依赖专门 bot API。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/email.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/email](/docs/user-guide/messaging/email)
:::

## 适合什么

- 把 Hermes 当邮件助手
- 用邮件触发异步任务
- 和传统组织协作工具对接

## 前置条件

- 可用邮箱
- IMAP / SMTP 已开启
- 对 Gmail / Outlook 等供应商做好应用密码或等效授权

## 基本流程

1. 配 IMAP / SMTP 参数
2. 配允许访问的用户
3. 启动 gateway

## 相关页面

- [消息网关](/docs.zh/user-guide/messaging/index)
- [Security](/docs.zh/user-guide/security)
