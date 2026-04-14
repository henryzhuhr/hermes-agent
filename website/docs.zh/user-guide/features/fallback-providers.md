---
title: Fallback Providers
description: 当主 LLM provider 不可用时，配置自动故障转移到备用 provider。
sidebar_label: Fallback Providers
sidebar_position: 8
---

# Fallback Provider 故障切换

Hermes 有多层容错机制，用来在 provider 出问题时尽量不中断会话。Fallback providers 解决的是“主 provider 不可用时切到备用 provider”。

:::note 中文整理版
本页是 `website/docs/user-guide/features/fallback-providers.md` 的中文整理版。英文原文：[/docs/user-guide/features/fallback-providers](/docs/user-guide/features/fallback-providers)
:::

## 三层韧性

官方文档把可靠性分成三层：

1. credential pools：同一 provider 下轮换多个 key
2. fallback providers：跨 provider 失败切换
3. 模型或任务级单独 provider 解析

这意味着 fallback 不是唯一手段，而是中间那层保险。

## 适合什么时候配置

- 生产 bot 需要高可用
- 单个 provider 经常限流或偶发故障
- 主模型和辅助模型走不同线路

## 你可以为哪些场景配置 fallback

- 主对话模型
- 辅助任务，例如压缩、摘要、视觉
- 某些独立工作流，如 delegation 或 cron

## 与 Provider Routing 的关系

- routing：在一个聚合 provider 内部做偏好控制
- fallback：主 provider 整体失败时换另一条链路

这两者可以叠加使用。

## 实践建议

- 主 provider 选你最稳定的
- 备用 provider 选不同供应链的，不要只换皮
- 对辅助模型也做独立 fallback，避免“主对话没挂，压缩先挂了”

## 相关页面

- [Provider Routing](/docs.zh/user-guide/features/provider-routing)
- [AI Providers](/docs.zh/integrations/providers)
- 英文参考：[/docs/user-guide/features/credential-pools](/docs/user-guide/features/credential-pools)
