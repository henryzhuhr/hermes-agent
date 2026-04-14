---
sidebar_position: 8
title: "扩展 CLI"
description: "构建包装型 CLI，在不重写 Hermes TUI 主循环的前提下加入自定义组件、快捷键和布局"
---

# 扩展 CLI

Hermes 暴露了一组受保护的扩展点，允许你在不重写大段 `run()` 主循环的情况下，为 CLI 加自定义 widget、快捷键和布局。

:::note 中文整理版
本页是 `website/docs/developer-guide/extending-the-cli.md` 的中文整理版。英文原文：[/docs/developer-guide/extending-the-cli](/docs/developer-guide/extending-the-cli)
:::

## 可用扩展点

- `_get_extra_tui_widgets()`
- `_register_extra_tui_keybindings(...)`
- `_build_tui_layout_children(...)`
- `process_command()`
- `_build_tui_style_dict()`

## 适合做什么

- 加常驻面板
- 自定义热键
- 调整布局
- 新增 Slash 命令
- 改样式

## 为什么不要直接覆写大主循环

因为 CLI 主循环很长，而且内部变化频繁。扩展点的意义就是让你的包装层尽量和 Hermes 内部实现解耦。

## 相关页面

- [CLI 界面](/docs.zh/user-guide/cli)
- [Architecture](/docs.zh/developer-guide/architecture)
