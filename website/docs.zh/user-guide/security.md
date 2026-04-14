---
sidebar_position: 8
title: "安全"
description: "安全模型、危险命令审批、用户授权、容器隔离，以及生产部署最佳实践"
---

# 安全

Hermes 的安全设计不是单点防护，而是分层防御。你可以把它理解成“让 agent 有能力做事，但默认不要轻易越权”。

:::note 中文整理版
本页是 `website/docs/user-guide/security.md` 的中文整理版，保留最关键的边界与部署建议。英文原文：[/docs/user-guide/security](/docs/user-guide/security)
:::

## 七层安全模型

Hermes 官方文档把安全边界概括为七层：

1. 用户授权
2. 危险命令审批
3. 容器或沙箱隔离
4. MCP 凭据过滤
5. 上下文文件注入扫描
6. 跨会话隔离
7. 输入参数与工作目录校验

如果你在消息平台对外开放 Hermes，至少要把前四层配置好。

## 危险命令审批

Hermes 会在执行命令前检查危险模式，例如：

- `rm`
- `git reset`
- 覆盖重定向 `>`
- `sed -i`
- 其他潜在破坏性操作

命中后需要人工批准，除非你显式开启更激进的模式。

### 审批模式

核心思路：

- 默认模式：高风险命令需要确认
- 更保守模式：更多命令触发审批
- `yolo`：跳过审批，不建议用于高风险环境

如果这是公网 bot，尽量不要开 `yolo`。

## 用户授权

消息网关场景下，要先解决“谁能和 agent 说话”：

- allowlist
- 平台级授权
- DM pairing
- 群聊或频道访问控制

这一步优先级高于 prompt 设计或模型选型。

## 容器隔离

Hermes 支持多种后端隔离：

- Docker
- Singularity / Apptainer
- Modal
- 远程 SSH

不同后端的安全性和便捷性不同。通用原则是：如果 agent 会运行不完全可信的命令，尽量不要直接给宿主机裸权限。

## MCP 与凭据暴露

MCP server 可能是本地子进程，也可能是远程服务。你需要控制：

- 传给它哪些环境变量
- 是否允许资源和 prompts 注册
- 工具白名单 / 黑名单

详见 [MCP](/docs.zh/user-guide/features/mcp) 和 [MCP Config Reference](/docs.zh/reference/mcp-config-reference)。

## 上下文文件注入防护

Hermes 会读取 `AGENTS.md`、`SOUL.md`、`.cursorrules` 等上下文文件，因此也会做注入扫描。原则很简单：

- 允许项目自定义 agent 行为
- 不把任意项目文本当成无条件可信系统提示

## Website 与网络访问

如果启用了 web / browser 工具，应额外注意：

- 网站访问白名单或黑名单
- SSRF 风险
- 凭据泄露风险

公网部署时，建议单独检查网络出口策略。

## 生产部署建议

最小清单：

- 关闭不必要的 toolsets
- 明确 allowlist
- 不在公网 bot 上开 `yolo`
- 让执行后端跑在容器或远程隔离环境
- 分离不同用途的 API keys 与 bot tokens
- 检查 `.env` 权限和日志脱敏

## 下一步

- [配置](/docs.zh/user-guide/configuration)
- [Docker](/docs.zh/user-guide/docker)
- [Messaging Gateway](/docs.zh/user-guide/messaging/index)
