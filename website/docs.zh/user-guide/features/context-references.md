---
sidebar_position: 9
sidebar_label: "Context References"
title: "上下文引用"
description: "用内联 @ 语法把文件、目录、git diff 和 URL 直接附加到消息中"
---

# 上下文引用

在 Hermes 里，你可以输入 `@...` 直接把文件、目录、git diff 或 URL 内容附加到消息中。它比手工复制粘贴更稳定，也更适合长内容注入。

:::note 中文整理版
本页是 `website/docs/user-guide/features/context-references.md` 的中文整理版。英文原文：[/docs/user-guide/features/context-references](/docs/user-guide/features/context-references)
:::

## 支持的引用

- `@file:...`
- `@folder:...`
- `@git:...`
- `@url:...`

还支持行号范围。

## 适合什么

- 代码 review
- 指定日志片段
- 让 agent 看目录树
- 把网页上下文直接附上

## 安全限制

Hermes 会做路径穿越、敏感路径和二进制文件检测，不是任何内容都能无条件注入。

## 相关页面

- [Context Files](/docs.zh/user-guide/features/context-files)
- [CLI 界面](/docs.zh/user-guide/cli)
