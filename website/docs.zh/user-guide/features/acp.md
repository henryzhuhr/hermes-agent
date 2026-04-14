---
sidebar_position: 11
title: "ACP 编辑器集成"
description: "在 VS Code、Zed 和 JetBrains 等 ACP 兼容编辑器中使用 Hermes Agent"
---

# ACP 编辑器集成

Hermes 可以作为 ACP server 运行，让支持 ACP 的编辑器通过 stdio 接入 Hermes，并显示聊天、工具活动、审批请求以及会话上下文。

:::note 中文整理版
本页是 `website/docs/user-guide/features/acp.md` 的中文整理版。英文原文：[/docs/user-guide/features/acp](/docs/user-guide/features/acp)
:::

## ACP 模式能暴露什么

编辑器里通常可以看到：

- chat 消息
- 工具执行进度
- 审批与确认请求
- 会话级上下文

也就是说，ACP 不是“把网页嵌进 IDE”，而是让编辑器真正成为 Hermes 的前端。

## 安装与启动

```bash
pip install -e '.[acp]'
hermes acp
```

然后在编辑器里把 Hermes 注册为 ACP server。

## 支持场景

当前文档重点覆盖：

- VS Code
- Zed
- JetBrains 系列

不同编辑器接入方式略有不同，但核心都是配置一个能启动 `hermes acp` 的 command。

## 凭据与配置

Hermes ACP 复用你现有的 `~/.hermes/` 配置，因此：

- model / provider 不需要重配
- `.env` 与 `config.yaml` 仍然是单一真源
- memory、skills、session 也能沿用

## Working Directory 与会话

ACP 模式下，工作目录和编辑器打开的项目密切相关。它的价值在于：代码上下文、工作目录和 agent 操作界面终于在一个地方闭环。

## 适合谁

- 想在 IDE 内保留 Hermes 的完整工具能力
- 不想被某个单一编辑器插件锁死
- 需要和 CLI / gateway 共享同一个实例配置

## 进一步阅读

- [Context Files](/docs.zh/user-guide/features/context-files)
- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- [AI Providers](/docs.zh/integrations/providers)
