---
sidebar_position: 12
title: "批处理"
description: "大规模生成 agent 轨迹：并行处理、断点续跑与 toolset 分布"
---

# 批处理

Batch processing 允许你让 Hermes 并行跑上百上千条 prompt，并输出结构化轨迹数据。它主要面向训练数据生成、评测和大规模实验，不是普通日常聊天功能。

:::note 中文整理版
本页是 `website/docs/user-guide/features/batch-processing.md` 的中文整理版。英文原文：[/docs/user-guide/features/batch-processing](/docs/user-guide/features/batch-processing)
:::

## 核心思路

- 输入：JSONL prompt 数据集
- 执行：每条样本一个独立 agent session
- 输出：带工具调用和统计信息的 trajectory 数据

## 适合什么

- 训练数据生成
- 模型评测
- 对比不同 toolset / provider / reasoning 配置

## 能力点

- 并行执行
- checkpoint / resume
- toolset distributions
- 质量过滤和统计汇总

## 相关页面

- [环境、基准与数据生成](/docs.zh/developer-guide/environments)
- [轨迹格式](/docs.zh/developer-guide/trajectory-format)
