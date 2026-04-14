---
sidebar_position: 5
title: "环境、基准与数据生成"
description: "构建 RL 训练环境、运行评测基准，以及用 Hermes-Agent 与 Atropos 生成 SFT 数据"
---

# 环境、基准与数据生成

Hermes 不只是用户代理，也带一套环境框架，把工具调用能力接到 Atropos RL 训练与评测体系。

:::note 中文整理版
本页是 `website/docs/developer-guide/environments.md` 的中文整理版。英文原文：[/docs/developer-guide/environments](/docs/developer-guide/environments)
:::

## 三类工作流

1. RL Training
2. Benchmarks
3. Data Generation

它们共享同一个核心：环境类负责定义任务、运行 agent loop 并给结果打分。

## 架构层次

- `BaseEnv`
- `HermesAgentBaseEnv`
- 各类具体环境实现

## 典型能力

- 跑 TerminalBench2、TBLite、YC-Bench 等基准
- 生成 SFT 数据
- 连接 Atropos API 做训练

## 适合谁看

如果你只是把 Hermes 当用户工具，这页可以跳过。它主要面向做评测、训练或研究集成的人。

## 相关页面

- [Trajectory Format](/docs.zh/developer-guide/trajectory-format)
- [Architecture](/docs.zh/developer-guide/architecture)
