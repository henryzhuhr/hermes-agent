---
sidebar_position: 2
---

# Profiles：在一台机器上运行多个 Hermes

Profile 是 Hermes 的多实例隔离机制。每个 profile 都有自己独立的 `config.yaml`、`.env`、`SOUL.md`、记忆、技能、会话、cron 和 gateway 状态。

:::note 中文整理版
本页是 `website/docs/user-guide/profiles.md` 的中文整理版。英文原文：[/docs/user-guide/profiles](/docs/user-guide/profiles)
:::

## Profile 是什么

你可以把 profile 理解成“同一套程序里的多个 Hermes 人格和运行环境”。它适合：

- 一个 coder agent
- 一个个人助手 bot
- 一个研究或自动化 agent

它们互不污染，不共享会话、记忆和 token 配置。

## 快速开始

```bash
hermes profile create coder
coder setup
coder chat
```

创建后，`coder` 会自动成为一个可调用的命令别名。

## 创建方式

常见模式：

- 空白创建：从零开始配置
- `--clone`：只复制配置
- `--clone-all`：复制配置、记忆、技能和更多状态

如果你只是想基于主实例快速派生一个“同配置不同用途”的 bot，`--clone` 往往最合适。

## 使用方式

你有三种高频入口：

- 命令别名：`coder chat`
- 显式 profile 参数：`hermes -p coder chat`
- sticky default：`hermes profile use coder`

如果你经常在多个 profile 间来回切，推荐保留 `-p` 的显式用法，减少误操作。

## Gateway 与 Bot Token

Profiles 非常适合多机器人部署。典型做法：

- `coder` 绑定一个 Telegram bot
- `assistant` 绑定另一个 Discord / Slack bot
- 每个实例使用自己的 token、allowlist 和工作目录

项目内还有 token locks 机制，防止两个 profile 误用同一组凭据。

## 配置与更新

Profile 的配置文件仍在各自的 `HERMES_HOME` 下。更新代码时，所有 profile 共用同一份程序代码，但用户态数据彼此隔离。

## 管理命令

常用命令：

- `hermes profile list`
- `hermes profile show <name>`
- `hermes profile rename <old> <new>`
- `hermes profile delete <name>`
- `hermes profile export <name>`
- `hermes profile import <archive>`

完整语法见 [Profile Commands Reference](/docs.zh/reference/profile-commands)。

## 适合什么时候用 Profile

建议优先用 profile，而不是手工改 `HERMES_HOME`，当你需要：

- 长期维护多个独立 agent
- 给不同平台分配不同 bot token
- 让家庭、工作、研究场景完全分离

## 下一步

- [Messaging Gateway](/docs.zh/user-guide/messaging/index)
- [Profile Commands Reference](/docs.zh/reference/profile-commands)
- [Security](/docs.zh/user-guide/security)
