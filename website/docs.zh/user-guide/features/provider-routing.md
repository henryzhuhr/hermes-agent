---
title: Provider Routing
description: 配置 OpenRouter provider 偏好，以在成本、速度和质量之间做取舍。
sidebar_label: Provider Routing
sidebar_position: 7
---

# Provider 路由

当你通过 OpenRouter 使用 Hermes 时，可以进一步控制底层实际由哪家 provider 来处理请求。这个能力叫 provider routing。

:::note 中文整理版
本页是 `website/docs/user-guide/features/provider-routing.md` 的中文整理版。英文原文：[/docs/user-guide/features/provider-routing](/docs/user-guide/features/provider-routing)
:::

## 解决什么问题

同一个模型名在 OpenRouter 背后可能由多个底层 provider 提供。Routing 允许你：

- 优先低成本 provider
- 优先更稳定或更快的 provider
- 排除不想用的 provider
- 强制需要某些参数特性

## 常见策略

- `sort`：按成本、延迟等排序
- `only`：只允许某些 provider
- `ignore`：排除某些 provider
- `order`：给 provider 固定优先顺序
- `require_parameters`：要求支持某些参数能力
- `data_collection`：约束数据收集策略

## 什么时候值得配

- 你明确关注成本或延迟
- 某些 provider 在你的地区更稳定
- 某些模型在不同 provider 上工具调用表现差异明显

## 实践建议

- 没有稳定需求时先保持默认
- 有观测数据后再逐步收紧 provider 偏好
- 与 fallback 配合，而不是只靠单一路由

## 相关页面

- [Fallback Providers](/docs.zh/user-guide/features/fallback-providers)
- [AI Providers](/docs.zh/integrations/providers)
- [Configuration](/docs.zh/user-guide/configuration)
