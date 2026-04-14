# 轨迹格式

Hermes 会把对话轨迹保存成兼容 ShareGPT 的 JSONL，用于训练数据、调试产物和 RL 数据集。

:::note 中文整理版
本页是 `website/docs/developer-guide/trajectory-format.md` 的中文整理版。英文原文：[/docs/developer-guide/trajectory-format](/docs/developer-guide/trajectory-format)
:::

## 默认文件

常见输出包括：

- `trajectory_samples.jsonl`
- `failed_trajectories.jsonl`

批处理路径还会写自己的批次输出文件。

## 每条记录包含什么

- conversations 数组
- tool calls / tool responses 归一化结果
- reasoning 标记
- 完成状态
- 批处理额外元数据

## 用途

- 训练数据
- 错误复盘
- 评测输出

## 相关页面

- [Session 存储](/docs.zh/developer-guide/session-storage)
- [环境、基准与数据生成](/docs.zh/developer-guide/environments)
