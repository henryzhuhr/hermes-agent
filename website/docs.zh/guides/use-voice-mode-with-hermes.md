---
sidebar_position: 8
title: "在 Hermes 中使用语音模式"
description: "在 CLI、Telegram、Discord 以及 Discord 语音频道里设置和使用 Hermes 语音模式"
---

# 在 Hermes 中使用语音模式

这是一份实战指南，重点不是“语音模式能做什么”，而是“怎样把它配好并真的顺手地用起来”。

:::note 中文整理版
本页是 `website/docs/guides/use-voice-mode-with-hermes.md` 的中文整理版。英文原文：[/docs/guides/use-voice-mode-with-hermes](/docs/guides/use-voice-mode-with-hermes)
:::

## 语音模式最适合什么

- 免手操作 CLI
- 在 Telegram / Discord 收发语音
- 让 Hermes 常驻 Discord 语音频道
- 散步、排查问题、头脑风暴时快速来回交流

## 三种主要体验

1. CLI 麦克风输入 + 语音播放
2. 消息平台中的语音消息 / 语音回复
3. Discord voice channels 实时对话

## 上线顺序

推荐按这个顺序排障：

1. 先确认普通 Hermes 文本模式可用
2. 安装对应 extras
3. 安装系统音频依赖
4. 选 STT / TTS provider
5. 再调静音阈值、延迟和模式

## 配置建议

常见最小需求：

- `ffmpeg`
- STT provider
- TTS provider
- 必要的 Python extras

如果你先把文本模式没跑稳就上语音，排错会变得很乱。

## 场景 1：CLI 语音

适合：

- 边走边记想法
- 不方便键盘输入
- 可访问性场景

进入 CLI 后：

```text
/voice on
```

## 场景 2：Telegram / Discord 语音回复

适合移动端远程使用 Hermes，把文字 bot 变成“能听能说”的助手。

## 场景 3：Discord 语音频道

这是最重的语音形态。要特别注意：

- 权限
- 回声与误触发
- 频道环境噪音

## 常见故障

- 找不到音频设备
- 能转写但不说话
- 只在 DM 工作，频道里不工作
- Whisper 结果很差

## 相关页面

- [语音模式](/docs.zh/user-guide/features/voice-mode)
- [Discord](/docs.zh/user-guide/messaging/discord)
- [Configuration](/docs.zh/user-guide/configuration)
