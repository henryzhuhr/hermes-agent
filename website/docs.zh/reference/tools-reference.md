---
sidebar_position: 3
title: "内置工具参考"
description: "按 toolset 分组的 Hermes 内置工具参考"
---

# 内置工具参考

Hermes 内置了数十个工具，并且还能动态加载 MCP tools。理解工具面，首先要看 toolset，而不是死记每个函数名。

:::note 中文速查版
本页是 `website/docs/reference/tools-reference.md` 的中文速查版。英文原文包含按工具逐项展开的完整表格：[/docs/reference/tools-reference](/docs/reference/tools-reference)
:::

## 主要 toolsets

| Toolset | 代表工具 | 作用 |
|---|---|---|
| `browser` | `browser_navigate`, `browser_snapshot` | 浏览器自动化 |
| `file` | `read_file`, `write_file`, `patch`, `search_files` | 文件读写与检索 |
| `terminal` | `terminal`, `process` | 命令执行与进程管理 |
| `web` | `web_search`, `web_extract` | Web 搜索与抽取 |
| `memory` | `memory` | 长期记忆 |
| `session_search` | `session_search` | 历史会话检索 |
| `delegation` | `delegate_task` | 子代理委派 |
| `code_execution` | `execute_code` | 脚本化工具调用 |
| `skills` | skill 相关工具 | 技能管理与使用 |
| `cronjob` | `cronjob` | 定时任务 |
| `messaging` | `send_message` | 主动向消息平台投递结果 |
| `vision` / `image_gen` / `tts` | 多模态工具 | 图像、语音与生成 |

## 动态工具

除了内置工具，Hermes 还会从 MCP servers 动态注册工具，名称一般会带 server 前缀，例如：

- `github_create_issue`
- `stripe_list_customers`

## 使用建议

- 需要稳定性时优先缩小 toolset
- 需要扩展能力时优先看 MCP，而不是直接写新内置工具
- 公网 bot 默认不要暴露过宽工具面

## 相关页面

- [Tools & Toolsets](/docs.zh/user-guide/features/tools)
- [Toolsets Reference](/docs.zh/reference/toolsets-reference)
- [MCP](/docs.zh/user-guide/features/mcp)
