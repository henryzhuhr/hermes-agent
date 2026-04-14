---
sidebar_position: 13
title: "委派与并行工作"
description: "什么时候该用子代理委派，以及并行调研、代码审查和多文件工作的模式"
---

# 委派与并行工作

Hermes 可以启动隔离子代理并行干活，但不是任何任务都值得开子代理。关键不在“能不能委派”，而在“是否真有并行收益”。

:::note 中文整理版
本页是 `website/docs/guides/delegation-patterns.md` 的中文整理版。英文原文：[/docs/guides/delegation-patterns](/docs/guides/delegation-patterns)
:::

## 什么时候该委派

适合委派：

- 推理量大的子问题
- 中间数据很多、会污染主上下文
- 多条相互独立的工作流
- 你希望子代理用全新视角切入

不适合委派：

- 只差一个工具调用
- 主流程下一步立刻依赖结果
- 子任务边界模糊

## 模式：并行调研

把多个主题拆给不同子代理，各自汇总后再由主代理收敛。

## 模式：代码审查

子代理很适合读一个明确模块、产出问题清单，而不是在主上下文里灌满所有文件细节。

## 模式：比较多个方案

让不同子代理各自站在一个备选方案上做论证，最后主代理统一比较。

## 模式：多文件重构

前提是边界清晰、写入面尽量不重叠，否则并行会变成冲突制造机。

## Gather Then Analyze

机械收集通常更适合 [Code Execution](/docs.zh/user-guide/features/code-execution)，需要判断和综合的部分再交给 delegation。

## Toolset 选择

给子代理的工具越聚焦越好。不要把全量工具面无脑复制给每个子代理。

## 相关页面

- [子代理委派](/docs.zh/user-guide/features/delegation)
- [Code Execution](/docs.zh/user-guide/features/code-execution)
- [Git Worktrees](/docs.zh/user-guide/git-worktrees)
