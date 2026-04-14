---
title: Credential Pools
description: 为同一 provider 配置多个 API key 或 OAuth token，自动轮换并恢复限流。
sidebar_label: Credential Pools
sidebar_position: 9
---

# Credential Pools

Credential pools 允许你为同一 provider 配多个 key 或 token。当一个凭据限流或配额耗尽时，Hermes 会自动切下一个。

:::note 中文整理版
本页是 `website/docs/user-guide/features/credential-pools.md` 的中文整理版。英文原文：[/docs/user-guide/features/credential-pools](/docs/user-guide/features/credential-pools)
:::

## 它和 Fallback 的区别

- credential pool：同 provider 内轮换
- fallback providers：换到另一个 provider

顺序上通常是先试 pool，再试 fallback。

## 适合什么

- 高频使用单一 provider
- 容易打到速率限制
- 团队共用多组同 provider 凭据

## 关键点

- 支持不同轮换策略
- 子代理也会共享这套恢复能力
- 需要注意线程安全和存储行为

## 相关页面

- [Fallback Providers](/docs.zh/user-guide/features/fallback-providers)
- [Provider Routing](/docs.zh/user-guide/features/provider-routing)
