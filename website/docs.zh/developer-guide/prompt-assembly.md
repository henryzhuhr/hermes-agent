---
sidebar_position: 5
title: "Prompt 组装"
description: "Hermes 如何构建 system prompt、保持缓存稳定，并注入临时层"
---

# Prompt 组装

Hermes 有意把 prompt 分成两类：

- 可缓存、尽量稳定的系统提示状态
- 仅在当前 API 调用时注入的临时层

这是整个项目最关键的设计之一，因为它直接影响 token 成本、缓存命中率、会话连续性和 memory 正确性。

:::note 中文整理版
本页是 `website/docs/developer-guide/prompt-assembly.md` 的中文整理版。英文原文：[/docs/developer-guide/prompt-assembly](/docs/developer-guide/prompt-assembly)
:::

## 缓存层通常包含什么

高频层包括：

- `SOUL.md`
- 工具感知行为说明
- 可选的系统消息
- 冻结的 memory / user 快照
- skills 索引
- context files
- 时间戳 / session 信息
- 平台提示

## 为什么要拆开

因为如果每次都重建所有内容：

- prompt cache 很容易失效
- 会话成本飙升
- 跨轮行为更不稳定

## Context Files 与 Skills

Hermes 并不是简单把所有项目内容塞进 system prompt。它有选择地发现、加载和冻结特定层，尽量在“有足够上下文”和“别把缓存打碎”之间平衡。

## API 调用时临时层

一些内容只应在当前调用注入，而不是变成冻结层。这样可以减少不必要的 cache invalidation。

## 实践含义

如果你改动了 prompt 组装逻辑，一定要同时思考：

- cache 是否被破坏
- memory 是否仍然正确
- gateway / CLI / ACP 是否行为一致

## 相关页面

- [Context Compression and Caching](/docs.zh/developer-guide/context-compression-and-caching)
- [Context Files](/docs.zh/user-guide/features/context-files)
- [Personality & SOUL.md](/docs.zh/user-guide/features/personality)
