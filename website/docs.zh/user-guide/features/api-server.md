---
sidebar_position: 14
title: "API Server"
description: "把 hermes-agent 暴露成 OpenAI-compatible API，供任意前端接入"
---

# API Server

Hermes 可以暴露成兼容 OpenAI 的 HTTP API。任何会说 OpenAI 格式的前端，例如 Open WebUI、LobeChat、LibreChat、NextChat，都能把 Hermes 当后端接上。

:::note 中文整理版
本页是 `website/docs/user-guide/features/api-server.md` 的中文整理版。英文原文：[/docs/user-guide/features/api-server](/docs/user-guide/features/api-server)
:::

## 快速开始

1. 在 `.env` 中开启 API server 相关变量
2. 启动 gateway
3. 用前端或 `curl` 连到 Hermes

## 暴露的接口

主要包括：

- `POST /v1/chat/completions`
- `POST /v1/responses`
- `GET /v1/models`
- `GET /health`

## 使用场景

- 把 Hermes 接到现成 Web 聊天前端
- 多用户通过 profile 分端口接入
- 让外部系统用统一 OpenAI 接口调用 Hermes

## 注意点

- 这是网关侧 API，不是轻量 mock server
- 工具调用和流式进度会影响前端体验
- 多用户场景建议配合 profile 隔离

## 相关页面

- [Open WebUI](/docs.zh/user-guide/messaging/open-webui)
- [Web Dashboard](/docs.zh/user-guide/features/web-dashboard)
- [消息网关](/docs.zh/user-guide/messaging/index)
