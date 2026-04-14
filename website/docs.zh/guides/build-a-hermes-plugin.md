---
sidebar_position: 9
sidebar_label: "构建插件"
title: "构建一个 Hermes 插件"
description: "一步步实现一个完整 Hermes 插件：工具、hooks、数据文件与技能打包"
---

# 构建一个 Hermes 插件

这份指南从零开始做一个完整插件，包含工具、hooks、随插件分发的数据文件和 bundled skill。

:::note 中文整理版
本页是 `website/docs/guides/build-a-hermes-plugin.md` 的中文整理版。英文原文：[/docs/guides/build-a-hermes-plugin](/docs/guides/build-a-hermes-plugin)
:::

## 示例目标

官方示例做的是一个 calculator 插件，包含：

- `calculate`：数学表达式求值
- `unit_convert`：单位换算
- 一个记录工具调用的 hook
- 一个随插件分发的 skill

## 基本步骤

1. 创建插件目录
2. 编写 manifest
3. 定义 tool schemas
4. 实现 tool handlers
5. 完成注册逻辑
6. 测试插件

## 设计要点

### Tool handler 必须返回 JSON 字符串

这是最容易犯错的地方之一。不要直接返回 Python dict。

### 处理异常

插件内异常不能随意向外冒，否则会让工具调用整体失败。应捕获并返回结构化错误 JSON。

### Schema 写清楚

模型是否能正确使用你的工具，很大程度取决于 schema 描述是否具体、边界是否清晰。

## 插件还能做什么

- 附带数据文件
- 附带 skill
- 按环境变量启用
- 做条件性工具可用性判断
- 注册多个 hooks
- 注册 CLI 命令
- 通过 pip 分发

## 什么时候该写插件

适合：

- 你要扩展 Hermes 核心能力
- 多个工具、hook 和资源需要一起发布
- 这个能力值得长期维护

如果只是接一个现成外部系统，先评估 [MCP](/docs.zh/user-guide/features/mcp) 是否更简单。

## 下一步

- [MCP](/docs.zh/user-guide/features/mcp)
- [Skills 系统](/docs.zh/user-guide/features/skills)
- 开发者文档目前仍以英文为主：[/docs/developer-guide](/docs/developer-guide)
