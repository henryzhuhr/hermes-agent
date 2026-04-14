---
sidebar_position: 5
title: "把 Hermes 当作 Python 库使用"
description: "在你自己的 Python 脚本、Web 应用或自动化流水线中嵌入 AIAgent"
---

# 把 Hermes 当作 Python 库使用

Hermes 不只是 CLI。你也可以直接导入 `AIAgent`，在自己的脚本、服务或自动化管道里程序化使用。

:::note 中文整理版
本页是 `website/docs/guides/python-library.md` 的中文整理版。英文原文：[/docs/guides/python-library](/docs/guides/python-library)
:::

## 安装

```bash
pip install git+https://github.com/NousResearch/hermes-agent.git
```

或者：

```bash
uv pip install git+https://github.com/NousResearch/hermes-agent.git
```

## 最基本用法

核心对象是 `AIAgent`：

```python
from run_agent import AIAgent

agent = AIAgent()
reply = agent.chat("Hello")
print(reply)
```

## 更完整的控制

如果你需要完整消息历史和结构化结果，可以使用 `run_conversation()`，而不是只拿最终字符串。

## 工具配置

可以在构造时控制 toolsets，例如：

- 只开 Web
- 禁用 terminal
- 针对某类自动化任务只保留最小工具面

这对嵌入 Web 服务或 CI 步骤时很重要。

## 多轮对话

`AIAgent` 可以维持会话上下文，所以不仅能做一次性问答，也能做持续多轮代理任务。

## 轨迹保存

Hermes 支持把执行轨迹导出成 ShareGPT 风格数据，适合训练、评估或离线分析。

## 典型集成场景

- FastAPI 接口
- 自己写的 Discord / Telegram bot
- CI/CD 步骤中的自动代码分析
- 离线批处理任务

## 什么时候用库，什么时候用 CLI

- 你需要嵌入到自己程序里：用 Python 库
- 你主要是手工交互和调试：用 CLI

## 下一步

- [CLI 界面](/docs.zh/user-guide/cli)
- [Code Execution](/docs.zh/user-guide/features/code-execution)
- [AI Providers](/docs.zh/integrations/providers)
