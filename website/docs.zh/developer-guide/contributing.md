---
sidebar_position: 4
title: "贡献指南"
description: "如何为 Hermes Agent 做贡献：开发环境、代码风格与 PR 流程"
---

# 贡献指南

这页讲的是怎样以项目期望的方式给 Hermes 提交修改，而不是单纯“能跑起来就行”。

:::note 中文整理版
本页是 `website/docs/developer-guide/contributing.md` 的中文整理版。英文原文：[/docs/developer-guide/contributing](/docs/developer-guide/contributing)
:::

## 优先级

官方优先顺序大致是：

1. Bug 修复
2. 跨平台兼容性
3. 安全加固
4. 性能与健壮性
5. 新 skills
6. 新 tools
7. 文档

这说明 Hermes 更鼓励“把现有系统做稳”，而不是无限扩功能。

## 开发环境

核心步骤：

- 准备 Python 3.11
- 安装项目依赖和开发工具
- 至少配置一个可用 provider
- 运行 CLI 和测试确认环境正常

## 代码风格

重点不是某个 formatter，而是：

- 跨平台安全
- 明确错误处理
- 不破坏 prompt cache、profiles 和 session 语义

## 安全敏感区域

提交以下改动时要格外小心：

- shell / terminal 执行
- prompt / 上下文注入
- 路径处理
- 凭据传递
- messaging 授权

## PR 前检查

- 变更范围尽量聚焦
- 相关测试补齐
- 文档同步更新
- 不引入 profile 或 prompt cache 回归

## 相关页面

- [Architecture](/docs.zh/developer-guide/architecture)
- [Adding Tools](/docs.zh/developer-guide/adding-tools)
- [Creating Skills](/docs.zh/developer-guide/creating-skills)
