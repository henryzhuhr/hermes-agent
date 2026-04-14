---
sidebar_position: 3
title: "教程：每日简报 Bot"
description: "构建一个每天自动研究、总结并把结果发到 Telegram 或 Discord 的简报机器人"
---

# 教程：每日简报 Bot

这个教程带你做一个“每天早上自动醒来、搜索你关心的话题、整理摘要并发给你”的 Hermes bot，不需要自己写业务代码。

:::note 中文整理版
本页是 `website/docs/guides/daily-briefing-bot.md` 的中文整理版。英文原文：[/docs/guides/daily-briefing-bot](/docs/guides/daily-briefing-bot)
:::

## 最终效果

流程大致是：

1. 设定时间触发 cron
2. Hermes 启动一个全新会话执行任务
3. Web 搜索抓取最新信息
4. 模型做摘要与结构整理
5. 通过 Telegram 或 Discord 投递结果

## 前置条件

至少先保证这些功能单独可用：

- Hermes 已安装并能正常聊天
- Web / browser 相关工具可用
- Telegram 或 Discord gateway 可正常发消息
- 你能创建和管理 cron 任务

## 第一步：先手动跑通

不要一上来就定时。先在普通会话里手工测试 prompt，确认：

- 搜索范围合适
- 输出格式符合预期
- 结果长度适中

## 第二步：创建 cron 任务

两种常见方式：

- 在聊天中用自然语言让 Hermes 创建
- 用 CLI / Slash 命令显式创建

### 黄金规则：prompt 必须自包含

Cron 任务运行在全新 session 里，不知道你现在聊天上下文里说过什么。所以 prompt 必须把它需要知道的信息写全。

## 第三步：定制简报

常见增强：

- 多主题简报
- 工作日才发送
- 早晚两次
- 用 [Delegation](/docs.zh/user-guide/features/delegation) 并行调研多个主题
- 加入你的长期偏好和格式要求

## 第四步：管理任务

高频操作：

```bash
hermes cron list
hermes cron remove <job>
```

同时别忘了检查 gateway 是否真的在运行，否则任务可能生成了但投递不出去。

## 适合扩展到什么场景

- 行业新闻晨报
- 代码仓库变更摘要
- 团队 standup 前置情报
- 个人关注领域的每日跟踪

## 下一步

- [Automate Anything with Cron](/docs.zh/guides/automate-with-cron)
- [消息网关](/docs.zh/user-guide/messaging/index)
- [Cron 功能参考（英文）](/docs/user-guide/features/cron)
