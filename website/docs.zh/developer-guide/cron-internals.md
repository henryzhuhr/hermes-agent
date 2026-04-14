---
sidebar_position: 11
title: "Cron 内部实现"
description: "Hermes 如何存储、调度、编辑、暂停、注入 skill，并投递 cron 任务结果"
---

# Cron 内部实现

Cron 子系统负责定时任务执行，从简单延时到循环 cron expression，再到 skill 注入和跨平台结果投递。

:::note 中文整理版
本页是 `website/docs/developer-guide/cron-internals.md` 的中文整理版。英文原文：[/docs/developer-guide/cron-internals](/docs/developer-guide/cron-internals)
:::

## 关键文件

- `cron/jobs.py`
- `cron/scheduler.py`
- `tools/cronjob_tools.py`
- `gateway/run.py`
- `hermes_cli/cron.py`

## 调度模型

Cron 任务有自己的存储、状态机和 tick 循环。它们不是从当前聊天里“顺手延续”，而是以新 session 运行。

## Job 存储

存储层不仅保存 schedule，也保存：

- 生命周期状态
- 重复次数
- deliver target
- skill / script 注入信息

## Skill 与 Script

Cron 的实战能力很大程度来自这两件事：

- 用 skill 提供工作方法
- 用 script 先做机械采集，再让 agent 判断

## 相关页面

- [用 Cron 自动化任何事](/docs.zh/guides/automate-with-cron)
- [Cron 故障排查](/docs.zh/guides/cron-troubleshooting)
- [消息网关](/docs.zh/user-guide/messaging/index)
