---
sidebar_position: 11
sidebar_label: "插件"
title: "插件"
description: "通过插件系统扩展 Hermes：自定义工具、hooks 与集成"
---

# 插件

Hermes 有插件系统，允许你在不改核心代码的前提下加入自定义工具、hooks 和集成能力。

:::note 中文整理版
本页是 `website/docs/user-guide/features/plugins.md` 的中文整理版。英文原文：[/docs/user-guide/features/plugins](/docs/user-guide/features/plugins)
:::

## 你可以用插件做什么

- 注册新工具
- 注册 hooks
- 打包数据文件
- 分发 skill
- 扩展 CLI

## 最小形式

把一个带 `plugin.yaml` 和 Python 代码的目录放进：

```text
~/.hermes/plugins/
```

## 管理方式

可以交互管理，也可以按插件粒度禁用。

## 从哪开始

最好的入口是完整示例教程：

- [构建一个 Hermes 插件](/docs.zh/guides/build-a-hermes-plugin)

## 相关页面

- [事件 Hooks](/docs.zh/user-guide/features/hooks)
- [MCP](/docs.zh/user-guide/features/mcp)
