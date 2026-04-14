---
sidebar_position: 2
title: "配置"
description: "配置 Hermes Agent：config.yaml、provider、模型、API Key 等"
---

# 配置

Hermes 的核心配置集中在 `~/.hermes/`。绝大多数日常修改只会落在 `config.yaml`、`.env`、`SOUL.md` 和 `memories/` 这几个位置。

:::note 中文整理版
本页是 `website/docs/user-guide/configuration.md` 的中文整理版。原文覆盖所有后端、流式输出、语音、安全和实验性选项；这里优先保留高频配置项与决策路径。英文原文：[/docs/user-guide/configuration](/docs/user-guide/configuration)
:::

## 目录结构

```text
~/.hermes/
├── config.yaml
├── .env
├── auth.json
├── SOUL.md
├── memories/
├── skills/
├── cron/
├── sessions/
└── logs/
```

可以把它理解为 Hermes 实例的“用户态系统盘”：

- `config.yaml`：运行设置、平台配置、toolsets、显示行为
- `.env`：API keys、bot tokens、私密凭据
- `SOUL.md`：全局人格和行为基线
- `memories/`：长期记忆
- `skills/`：已安装或 agent 生成的 skills

## 常用配置命令

```bash
hermes config
hermes config edit
hermes config check
hermes config set terminal.backend docker
hermes config get model
```

如果你只改少量键值，`hermes config set/get` 很方便；如果要整体调整，直接编辑 `config.yaml` 更高效。

## 配置优先级

从高到低通常是：

1. 当前命令行参数
2. `config.yaml`
3. `.env`
4. 默认值

这意味着你可以把稳定设置写入文件，把临时实验放到 CLI 参数里。

## 环境变量替换

`config.yaml` 支持从 `.env` 读取值。实践上建议：

- 所有 secrets 放 `.env`
- `config.yaml` 只保留结构化配置和非敏感开关

## 终端后端

Hermes 最重要的配置之一是 `terminal.backend`。可选方向包括：

- `local`：直接在当前主机执行
- `docker`：命令在容器中执行
- `ssh`：命令在远程机器执行
- `modal` / `daytona`：更偏云端运行
- `singularity` / `apptainer`：研究和 HPC 场景

如何选：

- 本地开发最快：`local`
- 希望默认更安全：`docker`
- 远程算力或远程环境：`ssh`

## 持久 Shell 与工作目录

Hermes 支持持久 shell，会影响：

- 环境变量是否延续
- `cd` 后目录是否保留
- 长任务与后台任务体验

CLI 默认使用你启动 `hermes` 的当前目录。消息网关默认使用 `MESSAGING_CWD`。

## Memory、Context Files 与 Compression

这三块决定了 agent 长会话是否稳定：

- `memory`：跨会话记住稳定事实
- context files：把 `SOUL.md`、`AGENTS.md`、`.cursorrules` 等注入提示词
- context compression：上下文过长时自动压缩旧消息

大模型可放宽压缩阈值；小上下文本地模型则要更积极压缩。

## Auxiliary Models

Hermes 允许为不同辅助任务单独指定模型或 provider，例如：

- 视觉分析
- 上下文压缩
- 文本摘要
- 语音 STT / TTS

推荐做法是主模型负责推理和工具决策，便宜或更擅长专项任务的模型负责辅助环节。

## Provider Routing 与 Fallback

如果你通过 OpenRouter 或多 provider 使用 Hermes，可以配置：

- provider routing：偏好速度、成本或特定厂商
- fallback providers：主 provider 失败时自动切换

详见：

- [Provider Routing](/docs.zh/user-guide/features/provider-routing)
- [Fallback Providers](/docs.zh/user-guide/features/fallback-providers)

## 安全相关高频项

重点关注：

- `approvals.mode`
- `security.*`
- website blocklist
- smart approvals
- checkpoints

如果 Hermes 要接 Telegram、Discord、Slack 等外部入口，安全配置应该先于“体验优化”。

## 语音、流式输出与展示

配置页还覆盖：

- CLI / gateway streaming
- STT / TTS
- Discord 语音频道
- tool progress 展示
- 背景任务通知

如果你主要通过文本终端使用 Hermes，这些项大多保持默认即可。

## 推荐最小检查清单

新实例至少确认这几项：

- 已设置一个可用 provider 和模型
- `terminal.backend` 符合你的风险偏好
- `approvals.mode` 没有过度放开
- `MESSAGING_CWD` 或当前工作目录正确
- `.env` 权限和内容安全

## 下一步

- [CLI 界面](/docs.zh/user-guide/cli)
- [Security](/docs.zh/user-guide/security)
- [AI Providers](/docs.zh/integrations/providers)
- [Environment Variables](/docs.zh/reference/environment-variables)
