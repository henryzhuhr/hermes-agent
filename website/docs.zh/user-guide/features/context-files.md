---
sidebar_position: 8
title: "上下文文件"
description: "自动注入到对话中的项目上下文文件：.hermes.md、AGENTS.md、CLAUDE.md、全局 SOUL.md 与 .cursorrules"
---

# 上下文文件

Hermes 会自动发现并加载一组上下文文件，用来决定“这个实例是谁”“这个项目希望 agent 怎样工作”。这套机制是它比通用聊天机器人更适合长期工程协作的关键原因之一。

:::note 中文整理版
本页是 `website/docs/user-guide/features/context-files.md` 的中文整理版。英文原文：[/docs/user-guide/features/context-files](/docs/user-guide/features/context-files)
:::

## 支持的文件

高频文件包括：

- `SOUL.md`
- `AGENTS.md`
- `.hermes.md`
- `CLAUDE.md`
- `.cursorrules`

其中：

- `SOUL.md` 是全局文件，来自 `HERMES_HOME`
- 其他文件更多是项目本地上下文

## 典型分工

- `SOUL.md`：人格、原则、长期行为基线
- `AGENTS.md`：仓库级开发规范、测试要求、工作流约束
- `.cursorrules` / `.hermes.md`：项目内补充规则

## 目录发现

Hermes 会从工作目录向上查找相关上下文文件。多层目录结构下，这意味着子目录可以拥有更贴近局部模块的规则。

## 为什么这比把说明写进 prompt 更好

因为上下文文件：

- 能和代码一起版本化
- 能按目录组织
- 能让多人协作时共享约束
- 不需要每轮手工粘贴说明

## 安全与注入

上下文文件既强大也敏感。Hermes 会做注入扫描，但你仍然应该把它们视为“受信任但要审查”的配置入口，尤其是：

- 来自第三方仓库
- 通过自动化下载进来的项目
- 多人可写目录

## 编写建议

- 用简洁、明确、可执行的规则
- 把测试方式、代码风格和关键禁令写清楚
- 避免空泛口号
- 项目规则放 `AGENTS.md`，人格内容放 `SOUL.md`

## 下一步

- [Personality & SOUL.md](/docs.zh/user-guide/features/personality)
- [Configuration](/docs.zh/user-guide/configuration)
- [Security](/docs.zh/user-guide/security)
