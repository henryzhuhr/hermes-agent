---
sidebar_position: 7
title: "在 Hermes 中使用 SOUL.md"
description: "如何用 SOUL.md 定义 Hermes 的默认风格，以及它和 AGENTS.md、/personality 的区别"
---

# 在 Hermes 中使用 SOUL.md

`SOUL.md` 是 Hermes 实例的主身份文件。你想让 Hermes 每次都像同一个助手、用稳定风格交流、坚持某种行为边界，就应该改它。

:::note 中文整理版
本页是 `website/docs/guides/use-soul-with-hermes.md` 的中文整理版。英文原文：[/docs/guides/use-soul-with-hermes](/docs/guides/use-soul-with-hermes)
:::

## `SOUL.md` 适合写什么

- 语气和表达风格
- 直接还是温和
- 面对不确定性时的态度
- 应该避免的说话方式

一句话概括：它定义“Hermes 是谁、怎么说话”。

## 不适合写什么

- 项目局部开发规则
- 一次性任务说明
- 太具体的命令流程

这些更适合放 `AGENTS.md` 或 skill。

## 它放在哪

`SOUL.md` 是全局文件，位于 `HERMES_HOME`，而不是某个项目目录里。

## 好的第一版应该长什么样

通常包括：

- Identity
- Style
- Avoid
- Defaults

关键不是写得长，而是写得稳、清晰、长期有效。

## `SOUL.md` 与 `/personality`

- `SOUL.md`：长期主身份
- `/personality`：会话级快速切换

## `SOUL.md` 与 `AGENTS.md`

- `SOUL.md`：你是谁
- `AGENTS.md`：在这个仓库里怎么工作

## 实用工作流

1. 先写一个短版本
2. 实际使用一段时间
3. 根据真实对话问题微调，而不是一次写成巨型宣言

## 相关页面

- [人格与 SOUL.md](/docs.zh/user-guide/features/personality)
- [上下文文件](/docs.zh/user-guide/features/context-files)
- [技巧与最佳实践](/docs.zh/guides/tips)
