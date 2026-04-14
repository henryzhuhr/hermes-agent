---
sidebar_position: 3
title: "在 Android / Termux 上运行 Hermes"
description: "在手机上的 Termux 环境中安装并使用 Hermes Agent"
---

# 在 Android / Termux 上运行 Hermes

:::note 中文整理版
本页是 `website/docs/getting-started/termux.md` 的中文整理版，聚焦官方测试通过的安装路径与常见坑。英文原文：[/docs/getting-started/termux](/docs/getting-started/termux)
:::

## 测试过的能力范围

官方验证路径主要覆盖：

- CLI 基本交互
- 主流模型提供方接入
- 配置、技能、记忆与基础工具
- 适合手机环境的依赖组合

## 当前不在“官方测试路径”里的内容

这些能力在手机上可能可用，但不属于首选路径：

- `.[all]` 的完整依赖集合
- 某些依赖本身需要桌面或服务器级二进制
- 重度浏览器、语音、图形、训练相关能力

## 方案一：一键安装

如果你的 Termux 环境比较新，可以先尝试官方安装器：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

如果失败，再走手动安装。

## 方案二：手动安装

### 1. 更新 Termux 并安装系统包

```bash
pkg update && pkg upgrade
pkg install git python clang make rust nodejs-lts ripgrep ffmpeg
```

### 2. 克隆 Hermes

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
```

### 3. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate
```

### 4. 安装官方推荐的 Termux 依赖包

使用专门的 Termux extra，而不是 `.[all]`：

```bash
pip install -e ".[termux]"
```

### 5. 把 `hermes` 放到 PATH

确保你能直接调用 `hermes`，必要时把虚拟环境可执行目录加入 shell PATH。

### 6. 验证安装

```bash
hermes doctor
```

### 7. 启动 Hermes

```bash
hermes
```

## 建议的后续设置

### 配置模型

```bash
hermes model
```

### 之后再运行完整初始化

```bash
hermes setup
```

### 按需安装 Node 依赖

如果你需要浏览器或桥接类功能，再额外安装对应 Node 依赖。

## 常见问题

### 安装 `.[all]` 失败

这是正常情况。Android 不适合默认拉满所有 extras，请改用：

```bash
pip install -e ".[termux]"
```

### `uv pip install` 在 Android 上失败

优先尝试 Termux 自带 Python + `venv` 路径，必要时减少 extras。

### `ANDROID_API_LEVEL` 相关构建错误

通常来自 Rust/Python 原生扩展构建，尽量使用官方推荐依赖组合，避免拉入不兼容 wheel。

### `hermes doctor` 说缺少 ripgrep 或 Node

回头检查：

```bash
pkg install ripgrep nodejs-lts
```

### Python 包编译失败

说明你拉入了超出官方手机路径的依赖，建议减少 extras，优先保证 CLI 基本可用。

## 手机上的已知限制

- 本地推理、浏览器自动化、音频录制等能力更受设备性能与系统限制影响
- 后台长任务稳定性不如桌面或服务器
- 手机环境更适合“轻量聊天 + 远程控制”，而不是重度本地执行

## 推荐用法

手机端更适合：

- 作为 CLI 轻量入口
- 连接远程模型或远程终端后端
- 结合消息网关，把重任务放到云端 Hermes 实例上执行

