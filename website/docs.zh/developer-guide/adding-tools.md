---
sidebar_position: 2
title: "新增工具"
description: "如何为 Hermes Agent 新增工具：schema、handler、注册与 toolset 接入"
---

# 新增工具

在写工具前，先问自己一句：这到底应该是工具，还是 [Skill](/docs.zh/developer-guide/creating-skills)？

:::note 中文整理版
本页是 `website/docs/developer-guide/adding-tools.md` 的中文整理版。英文原文：[/docs/developer-guide/adding-tools](/docs/developer-guide/adding-tools)
:::

## 什么时候该做 Tool

适合做 Tool：

- 需要 API key / auth 集成
- 需要稳定且精确的 Python 逻辑
- 要处理二进制、流式数据或实时事件

适合做 Skill：

- 可以靠说明 + shell 命令 + 现有工具完成

## 增加一个工具要改哪三处

1. `tools/your_tool.py`
2. `toolsets.py`
3. `model_tools.py`

这三处缺一不可：实现、分组、发现。

## 文件结构

一个标准工具文件通常包括：

- `check_requirements()`：可用性检查
- handler：真正执行逻辑
- schema：给模型看的工具描述
- `registry.register(...)`：注册入口

## 关键规则

- handler 必须返回 JSON 字符串
- schema 描述要让模型知道“何时用、如何用、别在哪些场景滥用”
- 如果需要 `task_id`，显式接受它

## Toolset 接入

你要决定：

- 加到核心 toolset
- 还是单独做新 toolset

这是能力边界问题，不只是“放哪看着顺眼”。

## 发现机制

`model_tools._discover_tools()` 会导入工具模块。没加这里，工具不会被发现。

## 什么时候需要额外改 Setup

如果工具依赖新的 API key、provider 或初始化向导流程，通常还要补 `hermes setup` 和配置文档。

## 相关页面

- [Tools Runtime](/docs.zh/developer-guide/tools-runtime)
- [Toolsets Reference](/docs.zh/reference/toolsets-reference)
- [Creating Skills](/docs.zh/developer-guide/creating-skills)
