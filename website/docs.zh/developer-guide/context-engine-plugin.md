---
sidebar_position: 9
title: "上下文引擎插件"
description: "如何构建一个替换内建 ContextCompressor 的上下文引擎插件"
---

# 构建上下文引擎插件

上下文引擎插件允许你用自定义策略替换内建 `ContextCompressor`。典型动机是做“不是摘要压缩”的上下文管理，例如 knowledge DAG 或其他无损方案。

:::note 中文整理版
本页是 `website/docs/developer-guide/context-engine-plugin.md` 的中文整理版。英文原文：[/docs/developer-guide/context-engine-plugin](/docs/developer-guide/context-engine-plugin)
:::

## 工作方式

Hermes 的上下文管理围绕 `ContextEngine` 抽象。插件实现只要遵守同一接口，就能在配置中被选为当前引擎。

## 关键约束

- 同一时刻只能有一个 context engine 生效
- 插件要兼容现有 agent loop 生命周期
- 要承担何时压缩、如何压缩的完整责任

## 你需要实现什么

- 必要的 class attributes
- `should_compress()`
- `compress()`
- 可选生命周期方法

## 工具与注册

可以通过目录式插件或通用插件系统注册。目录式通常更直接。

## 测试重点

不要只测“能不能加载”，还要测：

- 长会话行为
- session lineage
- prompt cache 兼容性
- gateway 和 CLI 一致性

## 相关页面

- [Context Compression and Caching](/docs.zh/developer-guide/context-compression-and-caching)
- [Memory Provider Plugins](/docs.zh/developer-guide/memory-provider-plugin)
