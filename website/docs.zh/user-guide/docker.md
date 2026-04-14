---
sidebar_position: 7
title: "Docker"
description: "在 Docker 中运行 Hermes Agent，以及把 Docker 用作终端后端"
---

# Hermes Agent 与 Docker

Docker 和 Hermes 的关系有两种，必须区分清楚：

1. Hermes 自己跑在容器里
2. Hermes 跑在宿主机上，但命令执行放进 Docker sandbox

本页主要讲第一种。第二种属于 terminal backend，见 [配置](/docs.zh/user-guide/configuration)。

:::note 中文整理版
本页是 `website/docs/user-guide/docker.md` 的中文整理版。英文原文：[/docs/user-guide/docker](/docs/user-guide/docker)
:::

## 快速开始

```sh
mkdir -p ~/.hermes
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent setup
```

这个流程会把用户数据写到宿主机的 `~/.hermes`，镜像本身保持无状态。

## Gateway 模式

如果你想让 Telegram、Discord、Slack 或 WhatsApp 持续在线，更常见的是让容器长期运行 gateway，而不是临时开个交互式 shell。

重点是确保这些内容挂载持久化：

- `config.yaml`
- `.env`
- sessions
- memories
- skills
- logs

## 交互式 CLI

除了 gateway，也可以直接以容器方式聊天：

```sh
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent
```

## 环境变量与卷

实践上建议：

- 配置和凭据走挂载目录
- 临时覆盖项用 `-e`
- 代码或工作目录按需挂载

如果 Hermes 需要看到你的项目仓库，记得额外挂载工作目录，而不是只挂 `~/.hermes`。

## 资源限制

Docker 路径适合：

- 想把运行环境与宿主机隔离
- 想更稳定地部署 gateway
- 希望更容易迁移到服务器

但如果你要做高频本地开发，容器内文件系统和路径映射会带来一点额外复杂度。

## 升级

升级通常只需要：

- 拉取新镜像
- 使用同一份持久化数据目录重新启动

只要数据目录不丢，配置、会话、记忆和技能就能保留。

## 常见问题

- 容器启动后立刻退出：通常是命令模式不对，或配置缺失
- 权限错误：检查挂载目录的属主和权限
- 浏览器工具不可用：确认镜像内依赖与宿主机能力
- gateway 断线：检查网络、token 和日志

## 什么时候该用 Docker

优先考虑 Docker，当你需要：

- 默认更强的命令执行隔离
- 稳定的服务化部署
- 一致的跨机器运行环境

## 下一步

- [配置](/docs.zh/user-guide/configuration)
- [Messaging Gateway](/docs.zh/user-guide/messaging/index)
- [Security](/docs.zh/user-guide/security)
