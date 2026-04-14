---
title: Home Assistant
description: 通过 Home Assistant 集成让 Hermes 控制智能家居。
sidebar_label: Home Assistant
sidebar_position: 5
---

# Home Assistant 集成

Hermes 和 Home Assistant 有两层集成：

1. gateway 平台，订阅实时状态事件
2. 一组可由 LLM 调用的智能家居工具

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/homeassistant.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/homeassistant](/docs/user-guide/messaging/homeassistant)
:::

## 基本流程

1. 创建 Long-Lived Access Token
2. 写入 `HA_ACCESS_TOKEN` 等配置
3. 启动 gateway

## 常见工具

- `ha_list_entities`
- `ha_get_state`
- `ha_list_services`
- `ha_call_service`

## 相关页面

- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- [消息网关](/docs.zh/user-guide/messaging/index)
