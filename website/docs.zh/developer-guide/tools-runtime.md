---
sidebar_position: 9
title: "工具运行时"
description: "工具注册表、toolsets、dispatch 和终端执行环境的运行时行为"
---

# 工具运行时

Hermes 的工具系统是“自注册工具 + toolset 分组 + 中央 registry/dispatch”的组合。理解它，基本就理解了 Hermes 为什么能同时支持内置工具、MCP 工具和不同 terminal backend。

:::note 中文整理版
本页是 `website/docs/developer-guide/tools-runtime.md` 的中文整理版。英文原文：[/docs/developer-guide/tools-runtime](/docs/developer-guide/tools-runtime)
:::

## 注册模型

每个工具模块在导入时调用 `registry.register(...)`。也就是说，工具不是手工汇总成一个大表，而是通过导入副作用完成注册。

## 发现机制

`model_tools._discover_tools()` 负责触发导入。一个工具即便实现对了，只要没被 discover，就等于不存在。

## 可用性检查

`check_fn` 用来决定工具当前是否应该暴露。例如某些工具缺 API key 时，不应该让模型看见。

## Toolset 解析

`get_tool_definitions()` 会根据当前平台、配置和动态能力过滤工具。这里决定了模型最终能看见的工具面。

## Dispatch

典型链路是：

1. 模型产出 tool call
2. registry 找到 handler
3. handler 执行
4. 结果包装成结构化响应写回对话

## Terminal 环境

`terminal` 工具底下还有多种执行环境：

- local
- docker
- ssh
- modal
- daytona
- singularity / apptainer

所以“terminal 工具能做什么”不只由工具自身决定，还由 backend 决定。

## 审批流

危险命令会进入 `DANGEROUS_PATTERNS` 审批路径，这也是工具系统和安全系统的交汇点。

## 相关页面

- [Adding Tools](/docs.zh/developer-guide/adding-tools)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- [Security](/docs.zh/user-guide/security)
