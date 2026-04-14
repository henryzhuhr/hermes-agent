---
sidebar_position: 9
title: "人格与 SOUL.md"
description: "通过全局 SOUL.md、内置人格和自定义 persona 定义 Hermes Agent 的行为风格"
---

# 人格与 SOUL.md

`SOUL.md` 是 Hermes 人格系统的第一层，也是系统提示中的最前位置。它决定这个实例“是什么样的 agent”，而 `/personality` 则更像会话级的临时人格覆盖。

:::note 中文整理版
本页是 `website/docs/user-guide/features/personality.md` 的中文整理版。英文原文：[/docs/user-guide/features/personality](/docs/user-guide/features/personality)
:::

## 现在的人格结构

可以简单理解为两层：

- `SOUL.md`：实例级、长期、稳定
- `/personality`：会话级、可切换

如果你在改全局行为基线，优先改 `SOUL.md`，不要把所有长期约束都堆到某次聊天里。

## `SOUL.md` 适合写什么

- 沟通风格
- 价值取向
- 决策边界
- 长期遵循的工作原则

不建议写：

- 仓库局部规则
- 一次性任务说明
- 具体命令步骤清单

这些更适合放 `AGENTS.md` 或 skill。

## 内置人格与自定义人格

Hermes 支持：

- 内置 personality preset
- 自定义 persona
- 会话中切换人格

适合做不同使用场景的快速切换，例如“代码审查模式”“研究助手模式”“简短回复模式”。

## 与 Context Files 的关系

- `SOUL.md`：定义“你是谁”
- `AGENTS.md`：定义“在这个项目里怎么干活”

两者不能混成一个万能大文件，否则长期会变得难维护。

## 安全与扫描

因为 `SOUL.md` 会进入系统提示，Hermes 也会对相关上下文文件做注入扫描。你仍应把人格文件视为高信任配置入口。

## 推荐做法

- `SOUL.md` 保持稳定、简洁、长期有效
- 项目规则交给 `AGENTS.md`
- 会话风格切换交给 `/personality`

## 下一步

- [Context Files](/docs.zh/user-guide/features/context-files)
- [Persistent Memory](/docs.zh/user-guide/features/memory)
- [CLI 界面](/docs.zh/user-guide/cli)
