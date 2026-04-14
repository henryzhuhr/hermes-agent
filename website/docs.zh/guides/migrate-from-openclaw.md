---
sidebar_position: 10
title: "从 OpenClaw 迁移"
description: "把 OpenClaw / Clawdbot 配置迁移到 Hermes Agent 的完整指南"
---

# 从 OpenClaw 迁移

`hermes claw migrate` 可以把 OpenClaw（以及更早的 Clawdbot / Moldbot）配置导入 Hermes。这页讲的是迁什么、怎么迁，以及迁完该检查什么。

:::note 中文整理版
本页是 `website/docs/guides/migrate-from-openclaw.md` 的中文整理版。英文原文：[/docs/guides/migrate-from-openclaw](/docs/guides/migrate-from-openclaw)
:::

## 快速开始

```bash
hermes claw migrate
hermes claw migrate --dry-run
hermes claw migrate --preset full --yes
```

迁移前会先给你完整预览，建议先看清楚再确认。

## 会迁移哪些内容

主要包括：

- persona、memory、instructions
- skills
- model / provider 配置
- agent 行为参数
- session reset 规则
- MCP servers
- TTS
- 各类消息平台配置

也有一些旧配置在 Hermes 中没有一一对应项，文档里会列出归档项。

## API Key 与 SecretRef

这部分是迁移风险最高的内容之一。迁完后务必检查：

- `.env` 是否完整
- provider 是否可正常认证
- 某些 voice / platform token 是否被正确映射

## 迁移后要检查什么

- `hermes status`
- `hermes model`
- `hermes skills list`
- gateway 是否能启动
- TTS / MCP / 消息平台是否还工作

## 常见问题

- 找不到 OpenClaw 目录
- 没发现 provider API key
- skills 没出现
- TTS voice 没迁过来

## 下一步

- [Configuration](/docs.zh/user-guide/configuration)
- [AI Providers](/docs.zh/integrations/providers)
- [FAQ](/docs.zh/reference/faq)
