---
sidebar_position: 7
title: "会话"
description: "会话持久化、恢复、搜索、管理，以及按平台隔离的会话追踪"
---

# 会话

Hermes 会自动把每次对话保存成 session。会话系统不仅是“聊天历史”，也是恢复上下文、跨会话搜索、平台隔离和压缩续写的基础。

:::note 中文整理版
本页是 `website/docs/user-guide/sessions.md` 的中文整理版。英文原文：[/docs/user-guide/sessions](/docs/user-guide/sessions)
:::

## 会话如何存储

Hermes 使用两套互补存储：

1. `~/.hermes/state.db`：SQLite，保存结构化元数据和全文检索索引
2. `~/.hermes/sessions/`：JSONL transcript，保存原始消息和工具调用轨迹

数据库里会记录：

- session ID
- 来源平台
- 会话标题
- 模型与配置快照
- 完整消息历史
- token 统计
- 时间戳
- 父会话 ID

## 恢复会话

常见方式：

```bash
hermes --continue
hermes --resume <session-id>
hermes --resume "My Session"
```

恢复时，CLI 会给你一个简短 recap，帮助你快速接回前文。

## 会话标题

Hermes 会自动生成标题，也支持你手动设置：

```text
/title 我的重构会话
```

标题的价值不只是“好看”，更重要的是：

- 恢复更快
- 导出更清晰
- 压缩后 lineage 更容易追踪

## 会话管理命令

常用命令包括：

- `hermes sessions list`
- `hermes sessions export`
- `hermes sessions delete`
- `hermes sessions rename`
- `hermes sessions prune`
- `hermes sessions stats`

如果你经常在不同平台之间切换，这套命令能帮你把 CLI、Telegram、Discord 等来源的历史统一管理。

## Session Search

`session_search` 工具允许 agent 在旧会话中检索相关内容。适合：

- 找回以前讨论过的方案
- 追踪某个 bug 的历史处理过程
- 跨天续接复杂任务

它和持久记忆不同：记忆保存稳定事实，会话搜索保留历史过程。

## 按平台隔离

Hermes 会给会话打来源标签，例如 CLI、Telegram、Discord、Slack、WhatsApp。这样可以：

- 防止不同渠道混到同一上下文
- 支持每个平台的恢复和清理策略
- 在群聊里区分共享会话和隔离会话

## 压缩后的 lineage

当上下文过长触发压缩时，Hermes 不只是“删掉旧消息”，而是会保留会话继承关系。这样你后续仍然可以追踪：

- 当前会话来自哪个旧会话
- 哪个节点触发了压缩
- 如何回溯完整历史

## 清理与归档

如果历史很多，可以定期做：

```bash
hermes sessions prune
hermes sessions export
```

推荐策略：

- 活跃项目保留
- 低价值旧会话定期清理
- 大项目在清理前先导出归档

## 什么时候该用新会话

这些情况建议新开 session：

- 任务目标已明显变化
- 当前上下文污染严重
- 需要切换人格、平台或不同代码库
- 旧会话太长，压缩后仍然噪声大

## 下一步

- [CLI 界面](/docs.zh/user-guide/cli)
- [Profiles](/docs.zh/user-guide/profiles)
- [Persistent Memory](/docs.zh/user-guide/features/memory)
