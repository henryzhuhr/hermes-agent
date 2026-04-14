---
sidebar_position: 3
sidebar_label: "Git Worktrees"
title: "Git Worktrees"
description: "使用 git worktree 为同一仓库安全并行运行多个 Hermes Agent"
---

# Git Worktrees

如果你想在同一个仓库里同时跑多个 Hermes，最稳妥的方式不是让它们共用一个 checkout，而是给每个 agent 一个独立 worktree。

:::note 中文整理版
本页是 `website/docs/user-guide/git-worktrees.md` 的中文整理版。英文原文：[/docs/user-guide/git-worktrees](/docs/user-guide/git-worktrees)
:::

## 为什么要配合 Hermes 使用 worktree

Hermes 把当前工作目录视为项目根。多个 agent 共用一个 checkout 时，常见问题包括：

- 一个 agent 改掉另一个 agent 正在读的文件
- 很难追踪“哪一组改动属于哪个实验”
- 回滚和 review 成本上升

worktree 的好处是：每个 agent 都拿到同一仓库的独立工作副本，但不会重复克隆整个 repo。

## 快速开始

```bash
git worktree add ../repo-feature -b feature/hermes-experiment
cd ../repo-feature
hermes
```

再开一个 worktree：

```bash
git worktree add ../repo-review -b review/refactor
cd ../repo-review
hermes
```

## `hermes -w`

Hermes 自带自动 worktree 模式：

```bash
hermes -w
```

它会在隔离 worktree 中启动，适合并行 agent 场景。这个模式比手工共用一个目录安全得多。

## 适用场景

- 同时做两个重构方向
- 一个 agent 写代码，另一个 agent 做 review
- 一个 agent 跑实验，另一个 agent 保持主线稳定

## 清理

任务结束后：

```bash
git worktree remove ../repo-feature
```

如果分支不再需要，也可以再手动删掉对应分支引用。

## 最佳实践

- 每个长任务一个独立 worktree
- 给 worktree 命名时体现任务目的
- 把最终改动合并回主分支前先 review
- 不要让多个 agent 在同一 checkout 里抢写文件

## 下一步

- [CLI 界面](/docs.zh/user-guide/cli)
- [Checkpoints and /rollback](/docs.zh/user-guide/checkpoints-and-rollback)
- [Security](/docs.zh/user-guide/security)
