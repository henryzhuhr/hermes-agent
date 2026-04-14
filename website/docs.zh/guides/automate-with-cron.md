---
sidebar_position: 11
title: "用 Cron 自动化任何事"
description: "基于 Hermes cron 的真实自动化模式：监控、报告、流水线与多技能工作流"
---

# 用 Cron 自动化任何事

如果说“每日简报 bot”只是在讲 cron 的基础玩法，这页讲的是更像真实生产工作流的几种模式。

:::note 中文整理版
本页是 `website/docs/guides/automate-with-cron.md` 的中文整理版。英文原文：[/docs/guides/automate-with-cron](/docs/guides/automate-with-cron)
:::

:::info 关键概念
Cron 任务运行在全新 agent session 中，不会记得你当前聊天里的上下文。Prompt 必须完全自包含。
:::

## 模式 1：网站变化监控

典型做法：

- `script` 先负责机械工作：抓页面、做 diff、保存状态
- agent 再负责判断：这次变化是否值得通知

这是 cron 很强的一种用法：脚本做重复劳动，模型做有判断性的部分。

## 模式 2：每周报告

把一周的数据、日志或外部信息先收集起来，再用 Hermes 整理成结构化周报。

## 模式 3：GitHub 仓库观察员

适合：

- issue / PR 动态汇总
- 新发布版本提醒
- 仓库活跃度跟踪

## 模式 4：数据采集流水线

例如周期性抓取价格、指标或状态，再让 Hermes 对近期变化做解读。

## 模式 5：多 Skill 工作流

一个 cron 可以按需加载多个 skill，把检索、整理、发布串起来。

## 管理任务

高频命令：

```bash
hermes cron list
hermes cron run <job>
hermes cron pause <job>
hermes cron edit <job>
hermes cron remove <job>
```

## 投递目标

任务结果可以发回：

- 当前平台
- 指定聊天入口
- 频道 / 群组
- 其他配置好的 delivery target

## 建议

- 从小任务开始，不要一开始就上超长 prompt
- 脚本做机械处理，agent 做判断和总结
- 先在前台手工跑通，再变成 cron

## 下一步

- [Daily Briefing Bot](/docs.zh/guides/daily-briefing-bot)
- [Cron 排障](/docs.zh/guides/cron-troubleshooting)
- [Cron 功能参考（英文）](/docs/user-guide/features/cron)
