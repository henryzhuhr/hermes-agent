---
sidebar_position: 4
title: "Nix / NixOS 安装与部署"
description: "在 Nix 与 NixOS 上以声明式方式安装、运行和管理 Hermes Agent"
---

# Nix / NixOS 安装与部署

:::note 中文整理版
本页是 `website/docs/getting-started/nix-setup.md` 的中文整理版。原文非常长，覆盖模块选项、容器模式、密钥管理与开发壳；这里优先保留部署决策和最常用配置。英文原文：[/docs/getting-started/nix-setup](/docs/getting-started/nix-setup)
:::

## 适用场景

如果你想要：

- 声明式安装 Hermes
- 通过 NixOS module 统一管理配置
- 用 systemd / 容器方式稳定运行 gateway
- 结合 `sops-nix` / `agenix` 管理 secrets

那么 Nix 路径非常合适。

## 前置条件

- 已安装 Nix 或 NixOS
- 熟悉 flake / module 的基本用法
- 愿意把 Hermes 配置放入声明式系统配置中

## 任意 Nix 用户的快速开始

可以直接运行：

```bash
nix run github:NousResearch/hermes-agent
```

或持久安装到 profile。

## NixOS Module

### 1. 在 flake 中引入 Hermes

把 `hermes-agent` 作为 flake input 加入系统配置。

### 2. 启用最小配置

核心思路：

- 启用 `services.hermes-agent`
- 指定模型和基础设置
- 按需启用 gateway、web dashboard、cron、容器模式

### 3. 验证

```bash
systemctl status hermes-agent
journalctl -u hermes-agent -f
```

## 部署模式选择

### 原生模式

Hermes 直接在主机上运行。

适合：

- 机器就是你要工作的地方
- 不需要额外容器隔离
- 希望调试更直接

### 容器模式

Hermes 在容器中运行，CLI 通过容器感知逻辑路由进去。

适合：

- 希望把运行环境和宿主机隔离
- 系统服务和交互式命令共用同一容器
- 想更稳定地管理依赖和权限

## 配置建议

### 声明式设置

建议把这些项放到 Nix 配置中：

- 模型与 provider
- toolsets / 平台设置
- gateway 开关
- dashboard / cron / MCP
- 文档和记忆文件的初始内容

### 自带配置逃生口

如果你不想把所有内容都放进 Nix，可以只声明基础运行方式，把更频繁变动的内容留给 `~/.hermes/config.yaml`。

## Secrets 管理

推荐：

- `sops-nix`
- `agenix`

重点是把 `.env`、OAuth 种子、Bot Token、MCP 凭据以安全方式注入，而不是硬编码进公开仓库。

## 文档与上下文文件

Nix 路径也支持：

- `SOUL.md`
- `AGENTS.md`
- 记忆目录
- 技能目录

这些都可以作为声明式资源注入。

## MCP Server

支持两类：

- `stdio` 本地子进程型
- `http` 远程服务型

如果远程服务启用 OAuth，也可以在 Nix 配置里声明对应认证方式。

## Managed Mode 与容器架构

NixOS 集成中有两个很关键的概念：

- **Managed mode**：Hermes 感知自己正被包管理器/系统模块接管，某些命令会转而提示使用 Nix 方式更新
- **Container mode**：CLI 不再直接本地运行，而是自动进入容器内执行 Hermes

## 开发者工作流

### Dev Shell

项目提供 Nix dev shell，可拉起包含 Python、Node、ripgrep、git、ssh、ffmpeg 等工具的开发环境。

### direnv

如果你常驻仓库开发，推荐配合 `direnv` 自动进入 dev shell。

## 常用排查路径

- 看服务日志：`journalctl -u hermes-agent -f`
- 容器模式下同时检查容器状态与挂载是否正确
- 验证 secrets 是否注入成功
- 验证 GC root 是否保护当前构建不被回收

## 什么时候应该读英文原文

如果你要做下面这些事，建议直接对照英文完整页：

- 精细调整所有 NixOS module 选项
- 自定义容器模式行为
- 配置复杂 MCP / OAuth
- 管理文档注入、GC root、开发壳细节

