---
sidebar_position: 13
title: "Webhooks"
description: "接收 GitHub、GitLab 等外部服务事件并触发 Hermes agent 运行"
---

# Webhooks

Webhook adapter 允许 Hermes 接收外部服务事件，例如 GitHub、GitLab、JIRA、Stripe，再把事件转成 agent prompt 自动处理。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/webhooks.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/webhooks](/docs/user-guide/messaging/webhooks)
:::

## 典型用途

- PR 评论与审查
- 代码仓库事件触发
- 业务系统通知转 agent 处理
- 再把结果投递到 Telegram / Discord 等平台

## 基本流程

1. 启用 webhook server
2. 配路由规则
3. 配签名校验
4. 让外部服务指向你的 endpoint

## 风险点

- HMAC 校验
- 速率限制
- Prompt injection
- 去重和幂等

## 相关页面

- [API Server](/docs.zh/user-guide/features/api-server)
- [消息网关](/docs.zh/user-guide/messaging/index)
- [Security](/docs.zh/user-guide/security)
