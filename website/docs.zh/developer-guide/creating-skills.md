---
sidebar_position: 3
title: "创建 Skills"
description: "如何为 Hermes Agent 创建 skills：SKILL.md 格式、编写规范与发布方式"
---

# 创建 Skills

Skill 是给 Hermes 增能力的首选方式。它比 tool 更轻、更快，也更适合社区共享。

:::note 中文整理版
本页是 `website/docs/developer-guide/creating-skills.md` 的中文整理版。英文原文：[/docs/developer-guide/creating-skills](/docs/developer-guide/creating-skills)
:::

## Skill 还是 Tool

优先做 Skill，当：

- 能用指令 + shell + 现有工具表达
- 只是包装现有 CLI 或 Web/API
- 不需要把复杂集成硬编码进 agent

## Skill 目录结构

核心就是一个目录和一个 `SKILL.md`。复杂一点时可以再带脚本和引用文件。

## `SKILL.md` 应该包含什么

高质量结构通常是：

- 什么时候用
- 快速参考
- 步骤
- 常见坑
- 验证方式

## 写作原则

- Progressive disclosure
- 避免外部依赖
- 必要时附 helper scripts
- 用真实任务测试

## 放在哪里

可以是：

- 本地 `~/.hermes/skills/`
- 通过 Skills Hub 发布
- 自定义仓库

## 安全扫描

Skill 会被扫描。对于会触发命令、访问凭据或执行敏感流程的技能，这一步尤其重要。

## 相关页面

- [Skills 系统](/docs.zh/user-guide/features/skills)
- [Working with Skills](/docs.zh/guides/work-with-skills)
- [Adding Tools](/docs.zh/developer-guide/adding-tools)
