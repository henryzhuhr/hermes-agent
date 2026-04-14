---
sidebar_position: 7
title: "子代理委派"
description: "使用 delegate_task 启动隔离的子代理，并行处理多个工作流"
---

# 子代理委派

`delegate_task` 会启动子代理实例，让它们在隔离上下文、受限工具面和独立终端会话中执行任务。父代理只接收最终摘要，从而避免上下文被每个中间步骤塞满。

:::note 中文整理版
本页是 `website/docs/user-guide/features/delegation.md` 的中文整理版。英文原文：[/docs/user-guide/features/delegation](/docs/user-guide/features/delegation)
:::

## 适合什么任务

- 可并行的独立子任务
- 读很多文件但只需要摘要的探索工作
- 需要临时缩小 toolset 的高风险任务

## 单任务委派

父代理把一个明确目标交给子代理，子代理做完后返回简短结论。适合：

- 代码库侦查
- 日志分析
- 某个目录的局部修改

## 并行批处理

Hermes 支持同时运行多个子代理。只有当任务真正互不依赖时，这种方式才值得用；否则只是增加协调成本。

## 与 `execute_code` 的区别

- delegation：适合“再开一个 agent”
- code execution：适合“写一段程序把工具串起来”

前者偏认知分工，后者偏程序化流水线。

## Toolset 策略

委派时最好显式缩小工具面。子代理看到的工具越少，越容易稳定，越不容易做出不必要的尝试。

## 风险与边界

- 子代理不是无限深递归
- 并发过多会增加模型成本和上下文管理难度
- 最终仍然需要父代理整合结果

## 何时不要委派

- 下一步立刻依赖子任务结果
- 子任务边界模糊
- 问题本身很小，委派开销比收益更高

## 下一步

- [Code Execution](/docs.zh/user-guide/features/code-execution)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- 英文进阶指南：[/docs/guides/delegation-patterns](/docs/guides/delegation-patterns)
