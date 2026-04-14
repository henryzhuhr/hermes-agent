---
sidebar_position: 8
title: "Memory Provider 插件"
description: "如何为 Hermes Agent 构建一个 memory provider 插件"
---

# 构建 Memory Provider 插件

Memory provider 插件让 Hermes 拥有超出内建 `MEMORY.md` / `USER.md` 的跨会话持久知识后端。

:::note 中文整理版
本页是 `website/docs/developer-guide/memory-provider-plugin.md` 的中文整理版。英文原文：[/docs/developer-guide/memory-provider-plugin](/docs/developer-guide/memory-provider-plugin)
:::

## 插件目录

每个 memory provider 通常位于：

```text
plugins/memory/<name>/
```

## 你要实现什么

围绕 `MemoryProvider` 抽象，你需要实现：

- 生命周期方法
- 配置读取
- 保存 / 检索逻辑
- 可选 hook

## 重要约束

- 同一时刻只允许一个 memory provider 生效
- 必须遵守 profile 隔离
- 线程模型要清楚，避免共享状态污染不同实例

## CLI 集成

memory provider 还可以附带 CLI 命令，方便配置和调试。

## 相关页面

- [持久记忆](/docs.zh/user-guide/features/memory)
- [上下文引擎插件](/docs.zh/developer-guide/context-engine-plugin)
