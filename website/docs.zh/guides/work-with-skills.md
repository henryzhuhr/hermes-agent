---
sidebar_position: 12
title: "使用 Skills"
description: "查找、安装、使用并创建 skills：让 Hermes 学会新工作流的按需知识文档"
---

# 使用 Skills

Skill 是 Hermes 的按需知识文档，用来教它处理特定任务。这页讲的是日常怎么找、装、用、配，以及什么时候值得自己写一个。

:::note 中文整理版
本页是 `website/docs/guides/work-with-skills.md` 的中文整理版。英文原文：[/docs/guides/work-with-skills](/docs/guides/work-with-skills)
:::

## 查找 Skills

Hermes 自带 bundled skills。高频入口：

```bash
/skills
hermes skills list
hermes skills search <keyword>
```

## Skills Hub

你也可以从 Skills Hub 浏览和安装：

```bash
hermes skills search kubernetes
hermes skills install <skill>
```

## 使用方式

两种常见姿势：

- 直接加载 skill 并附带任务
- 只加载 skill，再在后续消息中补任务

Skill 的核心机制仍然是 progressive disclosure，不会把所有内容一次塞进上下文。

## 验证是否安装成功

```bash
hermes skills list
```

或在聊天里看动态 Slash 命令是否出现。

## 配置 Skill

某些 skill 带有独立配置项，可以通过 `hermes skills` 相关命令查看和修改。

## 自己创建 Skill

最小流程：

1. 创建目录
2. 写 `SKILL.md`
3. 可选地加引用文件
4. 在真实任务里测试

## Skills vs Memory

- Skill：工作方法
- Memory：长期事实

## 使用建议

- 重复三次以上的流程就考虑沉淀成 skill
- 内容写步骤、条件和边界，不要写空话
- 不要把项目全量文档硬塞进单个 skill

## 下一步

- [Skills 系统](/docs.zh/user-guide/features/skills)
- [技巧与最佳实践](/docs.zh/guides/tips)
- [在 Hermes 中使用 MCP](/docs.zh/guides/use-mcp-with-hermes)
