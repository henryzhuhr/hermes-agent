---
sidebar_position: 1
title: "Tools 与 Toolsets"
description: "Hermes Agent 工具体系总览：可用能力、toolset 机制与终端后端"
---

# Tools 与 Toolsets

Tools 是 Hermes 真正“能动手做事”的来源。Toolset 则是这些工具的分组与权限边界，决定某个平台、某个会话或某个任务里，agent 可以看到和调用哪些能力。

:::note 中文整理版
本页是 `website/docs/user-guide/features/tools.md` 的中文整理版。英文原文：[/docs/user-guide/features/tools](/docs/user-guide/features/tools)
:::

## 常见工具类别

| 类别 | 例子 | 作用 |
|---|---|---|
| Web | `web_search`, `web_extract` | 搜索网页与抽取内容 |
| Terminal / Files | `terminal`, `read_file`, `patch` | 执行命令、读写文件 |
| Browser | `browser_navigate`, `browser_snapshot` | 交互式浏览器自动化 |
| Agent 编排 | `todo`, `clarify`, `execute_code`, `delegate_task` | 计划、澄清、脚本化调用、子代理委派 |
| 记忆与检索 | `memory`, `session_search` | 长期记忆与历史会话检索 |
| 自动化与投递 | `cronjob`, `send_message` | 定时任务与结果投递 |
| 扩展集成 | MCP tools、`ha_*`、`rl_*` | 第三方系统、家庭自动化或训练环境 |

## Toolset 为什么重要

Toolset 不是“文档分类”，而是运行时权限模型：

- 哪些工具能暴露给模型
- 不同平台默认启用哪些能力
- 子任务是否要缩小工具面

这对安全、稳定性和成本都有直接影响。

## 高层配置方式

常见入口：

```bash
hermes tools
hermes chat --toolsets web,file,terminal
```

也可以在 `config.yaml` 里按平台控制默认 toolsets。

## 终端后端

`terminal` 工具的真正风险边界取决于 backend：

- `local`：最快，但直接碰宿主机
- `docker`：默认更安全
- `ssh`：适合远程算力或隔离执行
- `modal` / `daytona`：偏云端
- `singularity` / `apptainer`：HPC / 研究环境

如果你打算让消息平台用户触发终端命令，先配 backend，再谈“开放哪些平台”。

## 后台进程与 `sudo`

Hermes 支持：

- 后台进程管理
- 过程输出跟踪
- 完成后通知
- `sudo` 审批与交互

但这类能力也意味着更高风险，所以常常应配合 [Security](/docs.zh/user-guide/security) 和 checkpoints 一起使用。

## 什么时候该缩小 Toolset

建议收紧 toolsets 的场景：

- 公网 bot
- 群聊多人共享实例
- 自动化任务只需要固定能力
- 子代理只负责一小段明确工作

## 参考

- 完整工具清单： [Built-in Tools Reference](/docs.zh/reference/tools-reference)
- Toolset 机制： [Toolsets Reference](/docs.zh/reference/toolsets-reference)
- 扩展工具： [MCP](/docs.zh/user-guide/features/mcp)
