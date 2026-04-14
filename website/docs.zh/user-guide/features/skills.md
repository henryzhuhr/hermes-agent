---
sidebar_position: 2
title: "Skills 系统"
description: "按需加载的知识文档：渐进披露、agent 管理技能与 Skills Hub"
---

# Skills 系统

Skill 是 Hermes 的可复用知识与流程封装。它不是把所有说明都塞进系统提示词，而是按需加载，尽量只在真正需要时读取 `SKILL.md` 的相关片段。

:::note 中文整理版
本页是 `website/docs/user-guide/features/skills.md` 的中文整理版。英文原文：[/docs/user-guide/features/skills](/docs/user-guide/features/skills)
:::

## Skills 的核心价值

- 把重复工作流沉淀下来
- 减少每轮都重复解释背景的 token 开销
- 让 agent 在特定领域更稳定

典型例子：

- Kubernetes 运维技能
- 某个内部 API 的调用流程
- 发布 checklist
- 固定格式的代码 review 流程

## Progressive Disclosure

Hermes 的 Skill 设计强调渐进披露：

- 默认只知道有哪些技能可用
- 真正需要时再读具体 `SKILL.md`
- 必要时再展开引用文件或脚本

这样可以控制上下文大小，避免所有技能常驻 prompt。

## 存放位置

所有 skills 的主目录都是：

```text
~/.hermes/skills/
```

来源可能包括：

- 仓库自带 bundled skills
- Skills Hub 安装
- agent 自己创建

## 使用方式

高频命令：

```bash
hermes skills search kubernetes
hermes skills install openai/skills/k8s
```

CLI / gateway 中，已安装技能也会作为动态 Slash 命令出现。

## `SKILL.md` 应该写什么

好的 skill 通常包含：

- 适用场景
- 触发条件
- 必要前置条件
- 标准步骤
- 关键命令或脚本
- 输出格式约定

它更像“高质量操作手册”，而不是空泛的背景介绍。

## 平台与安全

Skill 可以按平台启用或禁用，也可以在加载时做安全检查。对于会执行命令、接触凭据或操作外部系统的 skill，这一点尤其重要。

## Skills Hub

Skills Hub 让你搜索、安装和更新外部技能。使用它时要注意：

- 来源是否可信
- 是否需要联网或额外凭据
- 是否会扩大 agent 的执行面

## 什么时候该用 Skill，什么时候该写进 Memory

- 稳定偏好、长期事实：放 [Memory](/docs.zh/user-guide/features/memory)
- 某类任务的操作套路：写成 Skill

## 下一步

- [Persistent Memory](/docs.zh/user-guide/features/memory)
- [MCP](/docs.zh/user-guide/features/mcp)
- [Slash Commands Reference](/docs.zh/reference/slash-commands)
