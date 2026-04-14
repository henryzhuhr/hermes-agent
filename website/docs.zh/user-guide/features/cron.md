---
sidebar_position: 5
title: "定时任务（Cron）"
description: "用自然语言安排自动化任务，通过统一 cron 工具管理，并为任务附加一个或多个 skill"
---

# 定时任务（Cron）

Hermes 的 cron 功能允许你用自然语言、间隔或标准 cron expression 安排自动化任务。它不只是“到点执行一段文本”，还能附 skill、投递结果、暂停恢复和脚本预处理。

:::note 中文整理版
本页是 `website/docs/user-guide/features/cron.md` 的中文整理版。英文原文：[/docs/user-guide/features/cron](/docs/user-guide/features/cron)
:::

## 它能做什么

- 一次性任务
- 周期任务
- 暂停 / 恢复 / 编辑 / 删除
- 附加一个或多个 skill
- 把结果发回聊天、文件或指定平台目标

## 创建方式

- 聊天里用 `/cron`
- CLI 独立命令
- 直接自然语言告诉 Hermes 创建任务

## 核心注意点

任务在新 session 中运行，所以 prompt 必须自包含。

## 进阶能力

- skill-backed jobs
- script-backed jobs
- response wrapping
- provider recovery

## 相关页面

- [用 Cron 自动化任何事](/docs.zh/guides/automate-with-cron)
- [Cron 内部实现](/docs.zh/developer-guide/cron-internals)
- [消息网关](/docs.zh/user-guide/messaging/index)
