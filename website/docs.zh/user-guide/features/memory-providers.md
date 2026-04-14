---
sidebar_position: 4
title: "Memory Providers"
description: "外部记忆 provider 插件：Honcho、OpenViking、Mem0、Hindsight、Holographic、RetainDB、ByteRover、Supermemory"
---

# Memory Providers

Hermes 提供多种外部 memory provider 插件，用于在内建 `MEMORY.md` / `USER.md` 之外增加更强的跨会话记忆能力。同一时刻只能启用一个外部 provider，但内建记忆始终存在。

:::note 中文整理版
本页是 `website/docs/user-guide/features/memory-providers.md` 的中文整理版。英文原文：[/docs/user-guide/features/memory-providers](/docs/user-guide/features/memory-providers)
:::

## 快速开始

```bash
hermes memory setup
hermes memory status
hermes memory off
```

## 已提供的 provider

包括：

- Honcho
- OpenViking
- Mem0
- Hindsight
- Holographic
- RetainDB
- ByteRover
- Supermemory

## 选择思路

- 想要更强用户建模：看 Honcho
- 想接已有外部记忆服务：看对应 provider
- 想自己做：看 [Memory Provider 插件](/docs.zh/developer-guide/memory-provider-plugin)

## 相关页面

- [持久记忆](/docs.zh/user-guide/features/memory)
- [Honcho 记忆](/docs.zh/user-guide/features/honcho)
