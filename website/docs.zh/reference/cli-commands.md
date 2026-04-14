---
sidebar_position: 1
title: "CLI 命令参考"
description: "Hermes 终端命令与命令族的权威参考"
---

# CLI 命令参考

本页整理你在 shell 里直接运行的 `hermes ...` 命令。聊天内的 `/xxx` 命令见 [Slash Commands Reference](/docs.zh/reference/slash-commands)。

:::note 中文整理版
本页是 `website/docs/reference/cli-commands.md` 的中文整理版。原文更完整，覆盖每个子命令的全部选项与示例。英文原文：[/docs/reference/cli-commands](/docs/reference/cli-commands)
:::

## 全局入口

```bash
hermes [global-options] <command> [subcommand/options]
```

### 常用全局参数

| 参数 | 作用 |
|---|---|
| `--version`, `-V` | 显示版本 |
| `--profile <name>`, `-p <name>` | 选择 profile |
| `--resume <session>`, `-r <session>` | 恢复指定会话 |
| `--continue [name]`, `-c [name]` | 恢复最近会话 |
| `--worktree`, `-w` | 在独立 git worktree 中启动 |
| `--yolo` | 跳过危险命令审批 |

## 高频顶层命令

| 命令 | 作用 |
|---|---|
| `hermes` / `hermes chat` | 启动交互式或单次聊天 |
| `hermes model` | 选择或切换模型 |
| `hermes setup` | 初始化配置 |
| `hermes gateway` | 启动或管理消息网关 |
| `hermes status` | 查看实例状态 |
| `hermes doctor` | 诊断安装与环境问题 |
| `hermes config` | 查看和修改配置 |
| `hermes tools` | 管理 toolsets / tools |
| `hermes skills` | 搜索、安装、启用 skills |
| `hermes sessions` | 管理会话 |
| `hermes profile` | 管理 profiles |

## 其他命令族

| 命令 | 作用 |
|---|---|
| `hermes auth` | provider 认证相关 |
| `hermes cron` | 定时任务 |
| `hermes webhook` | webhook 订阅与回调 |
| `hermes dump` | 导出调试信息 |
| `hermes debug` | 调试入口 |
| `hermes backup` / `import` | 备份与导入 |
| `hermes logs` | 查看日志 |
| `hermes pairing` | pairing / 授权管理 |
| `hermes memory` | 记忆管理 |
| `hermes acp` | 启动 ACP server |
| `hermes mcp` | MCP 相关命令 |
| `hermes plugins` | 插件管理 |
| `hermes insights` | 统计与观察 |
| `hermes dashboard` | Web dashboard |
| `hermes completion` | shell 补全 |

## 实用示例

```bash
hermes
hermes chat -q "summarize the repo"
hermes --continue
hermes -p coder chat
hermes config edit
hermes logs -f
hermes sessions list
```

## 相关页面

- [Slash Commands Reference](/docs.zh/reference/slash-commands)
- [Profile Commands Reference](/docs.zh/reference/profile-commands)
- [Environment Variables](/docs.zh/reference/environment-variables)
