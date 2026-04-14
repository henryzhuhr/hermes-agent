---
sidebar_position: 4
title: "Toolsets Reference"
description: "Hermes 核心、组合、平台与动态 toolsets 参考"
---

# Toolsets 参考

Toolset 是 Hermes 的工具权限模型。每个工具都属于一个 toolset，启用或禁用 toolset，等于在控制 agent 的能力边界。

:::note 中文整理版
本页是 `website/docs/reference/toolsets-reference.md` 的中文整理版。英文原文：[/docs/reference/toolsets-reference](/docs/reference/toolsets-reference)
:::

## Toolset 如何工作

Hermes 中常见的 toolset 类型包括：

- Core：一组相关工具，例如 `file`
- Composite：面向常见场景的组合
- Platform：某个平台默认启用的一整套工具
- Dynamic：运行时从 MCP 或插件生成

## 配置方式

### 会话级

```bash
hermes chat --toolsets web,file,terminal
hermes chat --toolsets debugging
hermes chat --toolsets all
```

### 平台级

通过 `config.yaml` 控制不同平台默认启用哪些 toolsets。

### 交互式管理

```bash
hermes tools
```

## Dynamic Toolsets

这部分最重要：

- MCP server 会生成动态 toolsets
- 插件也可以扩展 toolsets
- 这样外部能力可以像原生能力一样被管理

## 与 `hermes tools` 的关系

`hermes tools` 是用户界面的管理入口；toolset 本身是底层能力抽象。前者是操作方式，后者是运行模型。

## 相关页面

- [内置工具参考](/docs.zh/reference/tools-reference)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- [MCP](/docs.zh/user-guide/features/mcp)
