---
sidebar_position: 2
title: "Slash Commands Reference"
description: "交互式 CLI 与消息平台 Slash 命令的完整参考"
---

# Slash 命令参考

Hermes 的 Slash 命令有两套表面：

- 交互式 CLI 内的 `/xxx`
- 消息平台中的 `/xxx`

它们都来自同一个中央命令注册表，因此帮助信息、别名和菜单通常是统一派生的。

:::note 中文整理版
本页是 `website/docs/reference/slash-commands.md` 的中文整理版。英文原文：[/docs/reference/slash-commands](/docs/reference/slash-commands)
:::

## 交互式 CLI Slash 命令

输入 `/` 就可以看到补全菜单。内置命令大小写不敏感。

### Session

| 命令 | 作用 |
|---|---|
| `/new` / `/reset` | 新建会话 |
| `/clear` | 清屏并新建会话 |
| `/history` | 查看会话历史 |
| `/save` | 保存当前会话 |
| `/retry` | 重试上一轮 |
| `/undo` | 撤销上一轮 user/assistant 交换 |
| `/title` | 给会话命名 |

### Configuration

| 命令 | 作用 |
|---|---|
| `/model` | 切换模型 |
| `/tools` | 查看或切换工具 |
| `/personality` | 切换人格 |
| `/compress` | 压缩上下文 |
| `/voice` | 控制语音模式 |

### Tools & Skills

| 命令 | 作用 |
|---|---|
| `/skills` | 浏览 skills |
| `/rollback` | 查看或恢复 checkpoint |
| 动态技能命令 | 已安装 skill 会暴露为 Slash 命令 |

### Info / Exit

| 命令 | 作用 |
|---|---|
| `/help` | 显示帮助 |
| `/status` | 查看当前状态 |
| `/quit` / `/exit` | 退出 |

## Dynamic Slash Commands

安装好的 skills 也会成为动态 Slash 命令。Hermes 内置技能如 `/plan` 也属于这类能力。

## Messaging Slash Commands

消息平台侧的命令集合会受平台限制、配置开关和菜单能力影响，但大体复用同一套注册表。常见命令包括：

- `/help`
- `/model`
- `/tools`
- `/personality`
- `/title`

## Quick Commands 与别名

除了标准 Slash 命令，你还可以配置 quick commands，并为命令设置别名。这样能把高频提示词或操作收缩成更短的入口。

## 相关页面

- [CLI 命令参考](/docs.zh/reference/cli-commands)
- [CLI 界面](/docs.zh/user-guide/cli)
- [Skills 系统](/docs.zh/user-guide/features/skills)
