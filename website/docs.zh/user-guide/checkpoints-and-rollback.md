---
sidebar_position: 8
sidebar_label: "Checkpoints & Rollback"
title: "Checkpoints 和 /rollback"
description: "使用影子 git 仓库和自动快照，为破坏性操作提供文件系统级安全网"
---

# Checkpoints 和 `/rollback`

Hermes 会在执行破坏性操作前自动给项目做快照，让你在出错时用一条命令恢复。这个机制默认开启，而且只在真正发生文件修改时工作。

:::note 中文整理版
本页是 `website/docs/user-guide/checkpoints-and-rollback.md` 的中文整理版。英文原文：[/docs/user-guide/checkpoints-and-rollback](/docs/user-guide/checkpoints-and-rollback)
:::

## 什么操作会触发 checkpoint

典型触发源：

- 文件工具：`write_file`、`patch`
- 破坏性终端命令：`rm`、`mv`、`sed -i`、`truncate`
- 部分危险 git 操作：`git reset`、`git clean`、`git checkout`

Hermes 会控制频率，避免长会话里无限堆积快照。

## 常用命令

| 命令 | 作用 |
|---|---|
| `/rollback` | 列出 checkpoints |
| `/rollback <N>` | 恢复到第 N 个 checkpoint |
| `/rollback diff <N>` | 预览与当前状态的差异 |
| `/rollback <N> <file>` | 只恢复某个文件 |

## 它是如何实现的

Hermes 不会直接篡改你真实项目的 `.git`。它会在 `~/.hermes/checkpoints/` 下维护一个独立的影子 git 仓库，用来保存快照和差异信息。

这意味着：

- 你的主仓库历史不受污染
- checkpoint 机制可以独立于项目 git 工作流存在
- 恢复速度通常比手工回滚更快

## 适合什么时候依赖它

尤其适合这些场景：

- 让 agent 大批量改文件
- 重构未知旧代码
- 用终端工具跑潜在破坏性命令
- 并行实验多个方案

## 最佳实践

- 在大改动前确认 checkpoint 已开启
- 恢复前先用 `/rollback diff` 看差异
- 对特别重要的任务，仍建议保留正常 git commit

checkpoint 不是 git 的替代品，更像 agent 时代的“最后一道保险”。

## 下一步

- [CLI 界面](/docs.zh/user-guide/cli)
- [Git Worktrees](/docs.zh/user-guide/git-worktrees)
- [Security](/docs.zh/user-guide/security)
