---
sidebar_position: 10
title: "语音模式"
description: "与 Hermes Agent 进行实时语音对话：CLI、Telegram、Discord（私聊、文字频道与语音频道）"
---

# 语音模式

Hermes 支持完整语音交互：CLI 里可以开麦讲话并听语音回复，消息平台可以转写语音消息，Discord 还支持语音频道实时对话。

:::note 中文整理版
本页是 `website/docs/user-guide/features/voice-mode.md` 的中文整理版。英文原文：[/docs/user-guide/features/voice-mode](/docs/user-guide/features/voice-mode)
:::

## 适用范围

语音能力覆盖：

- CLI 麦克风输入
- 文字平台中的语音消息转写
- Telegram / Discord 等平台的语音回复
- Discord voice channels

## 基本前提

通常需要：

- 安装语音相关 extras
- 配置 STT / TTS provider
- 系统级音频依赖，例如 `ffmpeg`

CLI 场景常见入口：

```bash
pip install "hermes-agent[voice]"
```

进入会话后：

```text
/voice on
```

## CLI 语音模式

CLI 语音模式适合“边说边让 agent 干活”。重点体验包括：

- 自动静音检测
- 流式语音回复
- 幻听过滤

## Messaging 语音

如果你主要在 Telegram 或 Discord 用 Hermes，语音模式更像“对已有文字 bot 的能力扩展”，包括：

- 上传语音消息自动转写
- 文本理解后返回语音或文本
- 在 Discord 语音频道持续对话

## 什么时候值得用

适合：

- 移动设备远程操控
- 手不方便敲键盘时的快速指令
- 要在 Discord 频道里做实时问答

不适合：

- 需要精确粘贴代码和长日志
- 环境噪音很大
- 部署环境缺失音频依赖

## 进一步阅读

- [Messaging Gateway](/docs.zh/user-guide/messaging/index)
- 英文实战指南：[/docs/guides/use-voice-mode-with-hermes](/docs/guides/use-voice-mode-with-hermes)
- [Configuration](/docs.zh/user-guide/configuration)
