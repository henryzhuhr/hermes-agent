---
sidebar_position: 1
title: "安装"
description: "在 Linux、macOS、WSL2 或 Termux 上安装 Hermes Agent"
---

# 安装

:::note 中文整理版
本页是 `website/docs/getting-started/installation.md` 的中文整理版。命令、目录和依赖名保持原样；若你需要完整逐项说明，可查看英文原文：[/docs/getting-started/installation](/docs/getting-started/installation)
:::

## 快速安装

### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装完成后重新加载 shell：

```bash
source ~/.bashrc
# 或
source ~/.zshrc
```

### Android / Termux

Termux 有单独的推荐路径与限制说明，优先阅读 [Termux 指南](/docs.zh/getting-started/termux)。

## 安装器会做什么

官方安装脚本会完成这些事情：

- 检查系统依赖与 Python / Node / `uv`
- 克隆或更新 Hermes Agent 源码
- 创建虚拟环境
- 安装 Python 依赖和必要的 Node 依赖
- 帮你把 `hermes` 放进 PATH
- 在首次安装后引导进入配置流程

## 前置条件

- Python 3.11+
- `git`
- 能联网安装 Python/Node 依赖
- 至少准备一个可用模型提供方

Windows 原生环境不是官方推荐路径，请先装 WSL2，再在 WSL2 中执行安装。

## 手动安装

如果你不想使用一键脚本，可以按下面的显式步骤安装：

### 1. 克隆仓库

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
```

### 2. 安装 `uv` 并创建虚拟环境

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
source venv/bin/activate
```

### 3. 安装 Python 依赖

```bash
uv pip install -e ".[all]"
```

如果你只需要特定能力，也可以安装更小的 extras，例如 `.[acp]`、`.[voice]`、`.[web]`。

### 4. 可选：初始化子模块

如果你要使用 RL / 训练相关功能，需要补拉相关子模块并安装额外依赖。

### 5. 可选：安装 Node 依赖

部分浏览器与桥接功能依赖 Node.js：

```bash
npm install
```

### 6. 初始化配置目录

Hermes 的运行配置在 `~/.hermes/`：

```text
~/.hermes/
├── config.yaml
├── .env
├── SOUL.md
├── memories/
├── skills/
└── logs/
```

### 7. 填入 API Key

至少要配置一个模型提供方，例如：

```bash
OPENROUTER_API_KEY=...
# 或
ANTHROPIC_API_KEY=...
# 或配置 OPENAI_BASE_URL + OPENAI_API_KEY 指向自建兼容端点
```

### 8. 将 `hermes` 加入 PATH

如果命令不可直接调用，把虚拟环境或安装目录加入 PATH。

### 9. 配置 Provider

```bash
hermes model
```

### 10. 验证安装

```bash
hermes doctor
hermes status
hermes
```

## 手动安装速查版

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
source venv/bin/activate
uv pip install -e ".[all]"
hermes model
hermes doctor
```

## 故障排查

- `hermes` 找不到：检查 PATH 是否已刷新，或虚拟环境是否已激活
- Python 版本过低：升级到 3.11+
- 不要用 `sudo` 跑安装脚本；Hermes 默认安装到用户目录
- 构建依赖失败：优先确认 `uv`、编译工具链、Node.js 与网络环境
- 手机上安装失败：改走 [Termux 指南](/docs.zh/getting-started/termux)

## 下一步

- [快速开始](/docs.zh/getting-started/quickstart)
- [配置](/docs.zh/user-guide/configuration)
- [AI Provider 集成](/docs.zh/integrations/providers)

