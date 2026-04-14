---
sidebar_position: 9
---

# 新增平台适配器

这页讲的是如何把一个新的消息平台接入 Hermes gateway。难点不在单个 adapter 文件，而在 20 多处代码、配置、工具和文档的联动。

:::note 中文整理版
本页是 `website/docs/developer-guide/adding-platform-adapters.md` 的中文整理版。英文原文：[/docs/developer-guide/adding-platform-adapters](/docs/developer-guide/adding-platform-adapters)
:::

## 架构位置

```text
User ↔ Messaging Platform ↔ Platform Adapter ↔ Gateway Runner ↔ AIAgent
```

每个 adapter 都要继承 `BasePlatformAdapter`，并实现连接、断连、发送消息等核心方法。

## Checklist

不仅要写 adapter，还通常要改：

- platform enum
- `gateway/config.py`
- `gateway/run.py`
- cross-platform delivery
- CLI integration
- tools / toolsets
- tests
- docs

## 常见模式

- 长轮询型平台
- callback / webhook 型平台
- 使用 token lock 的平台

## 做完后怎么查漏

很实用的方法是拿一个现成平台做 parity audit：搜索参考平台出现的文件，再搜索你新平台出现的文件，对比差集。

## 参考实现

不同平台的接入风格不同，最好的学习方式是挑一个跟你目标平台最接近的现有 adapter。

## 相关页面

- [Gateway Internals](/docs.zh/developer-guide/gateway-internals)
- [消息网关](/docs.zh/user-guide/messaging/index)
- [Security](/docs.zh/user-guide/security)
