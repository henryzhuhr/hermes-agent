---
sidebar_position: 8
title: "代码执行"
description: "带 RPC 工具访问的沙箱 Python 执行，把多步工作流压缩为单轮"
---

# 代码执行（程序化工具调用）

`execute_code` 工具允许 agent 编写 Python 脚本，并在沙箱子进程中通过 RPC 调用 Hermes 工具。它适合把多步、机械、结构化的工作折叠成一次执行。

:::note 中文整理版
本页是 `website/docs/user-guide/features/code-execution.md` 的中文整理版。英文原文：[/docs/user-guide/features/code-execution](/docs/user-guide/features/code-execution)
:::

## 它解决什么问题

普通工具调用适合一两步推理后立刻执行。`execute_code` 更适合：

- 要循环处理很多输入
- 需要稳定结构化输出
- 一次脚本中连续调用多个工具

## 典型例子

- 批量读取文件并提取指标
- 多次调用 Web / 文件 / MCP 工具后汇总成表格
- 运行固定流程而不想让模型逐步“手搓”每一步

## 资源与安全

脚本运行在受控子进程中，不是直接把任意 Python 丢进宿主环境无限执行。即便如此，你仍然应该把它视作高能力工具，必要时配合容器后端和审批策略。

## 与 Terminal 的区别

- terminal：更接近 shell
- execute_code：更接近“写一个小程序调用工具 API”

如果目标是结构化数据处理、循环、条件分支和聚合，`execute_code` 通常更合适。

## 与 Delegation 的区别

- execute_code：让程序执行
- delegation：让另一个 agent 思考

## 适合的平台

最适合 CLI 或受控服务器环境。公网消息 bot 若开放这项能力，必须先想清楚 toolset、backend 和权限边界。

## 下一步

- [Subagent Delegation](/docs.zh/user-guide/features/delegation)
- [Security](/docs.zh/user-guide/security)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
