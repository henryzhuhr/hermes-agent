---
sidebar_position: 8
title: "Open WebUI"
description: "通过 OpenAI-compatible API server 把 Open WebUI 接到 Hermes Agent"
---

# Open WebUI 集成

Open WebUI 是最常见的自托管聊天前端之一。配合 Hermes 的 API server，你可以获得一个更像成熟聊天产品的浏览器界面，而底层仍然是 Hermes agent。

:::note 中文整理版
本页是 `website/docs/user-guide/messaging/open-webui.md` 的中文整理版。英文原文：[/docs/user-guide/messaging/open-webui](/docs/user-guide/messaging/open-webui)
:::

## 基本架构

Open WebUI 前端通过 `POST /v1/chat/completions` 或 `Responses API` 调 Hermes。

## 快速步骤

1. 开启 Hermes API server
2. 启动 Hermes gateway
3. 启动 Open WebUI
4. 在管理界面添加 Hermes 连接

## 适合什么

- 想要多用户 Web 前端
- 想保留 Hermes 工具能力，但不用 CLI

## 相关页面

- [API Server](/docs.zh/user-guide/features/api-server)
- [Web Dashboard](/docs.zh/user-guide/features/web-dashboard)
