---
sidebar_position: 3
title: "持久记忆"
description: "Hermes Agent 如何跨会话记忆：MEMORY.md、USER.md 与 session search"
---

# 持久记忆

Hermes 的 memory 是“有限、经过筛选的长期记忆”，不是把所有聊天记录无限堆进 prompt。它用于保存稳定事实、偏好和长期约束。

:::note 中文整理版
本页是 `website/docs/user-guide/features/memory.md` 的中文整理版。英文原文：[/docs/user-guide/features/memory](/docs/user-guide/features/memory)
:::

## 它如何工作

内建记忆主要依赖两类内容：

- `MEMORY.md`：更偏项目、环境、工作流
- `USER.md`：更偏用户偏好和长期要求

Hermes 会在合适时机读取、更新并控制容量，而不是把记忆无限膨胀。

## 记忆适合保存什么

应该保存：

- 你长期偏好的写作和编码风格
- 常用环境信息
- 正在持续推进的项目背景
- 经常重复说明的固定要求

不该保存：

- 一次性的临时任务
- 当轮对话里的短期细节
- 可从代码库或会话搜索轻松找回的内容

## 记忆与会话搜索的区别

- memory：保存“稳定事实”
- session search：找回“历史过程”

如果你想让 Hermes 下次继续遵守某个长期偏好，用 memory；如果只是想找回上周讨论过的方案，用会话搜索。

## 去重与容量

Hermes 会尽量避免重复写入，并控制记忆规模。记忆越精炼，长期效果越好；记成流水账反而会污染后续推理。

## 外部 Memory Provider

项目支持外部 memory provider 插件。如果你需要更复杂的跨会话记忆后端，可以接插件，而不是把内建文件记忆硬改成数据库怪兽。

## 使用建议

- 每次只保存真正长期有价值的内容
- 定期审查记忆内容，删掉过时事实
- 对团队共享实例尤其要谨慎，避免把个人偏好写成全局约束

## 下一步

- [Skills 系统](/docs.zh/user-guide/features/skills)
- [Sessions](/docs.zh/user-guide/sessions)
- [Personality & SOUL.md](/docs.zh/user-guide/features/personality)
