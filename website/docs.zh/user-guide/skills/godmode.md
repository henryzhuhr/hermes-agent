---
sidebar_position: 1
sidebar_label: "G0DM0D3（Godmode）"
title: "G0DM0D3：Godmode Jailbreaking Skill"
description: "基于 G0DM0D3 技术的自动化越狱研究 skill，用于安全研究与红队评估"
---

# G0DM0D3：Godmode Jailbreaking Skill

这是一项面向安全研究与红队评估的 skill，目标是研究 API 提供的 LLM 在提示层面的防护边界，而不是普通生产使用场景。

:::warning 安全研究用途
本页仅提供高层中文说明，不展开可操作的越狱步骤、模板或规避细节。若你在做合法授权的安全研究，请对照英文原文、项目源码和你自己的合规边界审阅使用。
:::

:::note 中文整理版
本页是 `website/docs/user-guide/skills/godmode.md` 的中文整理版。英文原文：[/docs/user-guide/skills/godmode](/docs/user-guide/skills/godmode)
:::

## 它是什么

`G0DM0D3` 是一个 red-teaming skill，基于公开安全研究项目整理，用于评估不同模型和 provider 的防护表现。

## 适用场景

- 合法授权的安全研究
- 模型防护评估
- 红队测试与对照实验

## 与其他路径的区别

它偏 prompt / API 层研究，不是模型权重层改造工具。

## Hermes 中的角色

它以 skill 形式存在，意味着：

- 不是默认启用功能
- 需要明确使用场景
- 应在受控环境中使用

## 建议

- 仅在明确授权的测试环境中使用
- 不要把这类 skill 暴露给普通用户或公网 bot
- 配合隔离执行环境和严格审计

## 相关页面

- [内置 Skills 目录](/docs.zh/reference/skills-catalog)
- [Security](/docs.zh/user-guide/security)
