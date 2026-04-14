---
title: Browser Automation
description: 使用多种 provider、本地 Chrome via CDP 或云端浏览器完成网页交互、表单填写、抓取等任务。
sidebar_label: Browser
sidebar_position: 5
---

# 浏览器自动化

Hermes 内置完整 browser toolset，可接云浏览器、本地 Chrome/CDP，或本地浏览器模式，适合处理动态网页、表单、登录态页面和视觉理解场景。

:::note 中文整理版
本页是 `website/docs/user-guide/features/browser.md` 的中文整理版。英文原文：[/docs/user-guide/features/browser](/docs/user-guide/features/browser)
:::

## 支持的后端方向

- Browserbase cloud
- Browser Use cloud
- Firecrawl cloud browser
- Camofox 本地反检测浏览
- 本地 Chrome via CDP
- 本地 `agent-browser` 模式

## 常见工具

- `browser_navigate`
- `browser_snapshot`
- `browser_click`
- `browser_type`
- `browser_scroll`
- `browser_vision`
- `browser_console`

## 适合什么场景

- 填表和点击流程
- 需要 JS 渲染后的内容
- 截图+视觉分析
- 浏览器控制而非纯网页抽取

## 相关页面

- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- [Vision](/docs.zh/user-guide/features/vision)
- [Configuration](/docs.zh/user-guide/configuration)
