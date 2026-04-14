---
sidebar_position: 12
title: "Cron 故障排查"
description: "排查 Hermes cron 常见问题：任务不触发、投递失败、skill 加载异常与性能问题"
---

# Cron 故障排查

当 cron 任务表现不对时，最有效的方式不是乱改配置，而是按顺序排查：任务状态、时间配置、gateway、投递目标、skills、日志。

:::note 中文整理版
本页是 `website/docs/guides/cron-troubleshooting.md` 的中文整理版。英文原文：[/docs/guides/cron-troubleshooting](/docs/guides/cron-troubleshooting)
:::

## 任务不触发

优先检查：

1. 任务是否真的存在且处于 active
2. schedule 是否写对
3. gateway / scheduler 是否在运行
4. 系统时钟和 timezone 是否正确

## 投递失败

常见原因：

- deliver target 写错
- 平台 token 权限不够
- `[SILENT]` 或消息包装逻辑影响了可见输出

## Skill 加载失败

先检查：

- skill 是否真的安装了
- 使用的是 skill 名还是目录名
- skill 是否依赖交互式工具
- 多 skill 顺序是否不合理

## 任务报错

最重要的是看最近执行输出和日志。高频问题包括：

- 配置错误
- 权限问题
- 重复进程导致锁冲突
- `jobs.json` 权限异常

## 性能问题

几个常见症状：

- 启动慢
- 任务重叠太多
- `script` 输出过大

Cron 越像批处理系统，就越要控制输入规模。

## 常用诊断命令

```bash
hermes cron list
hermes status
hermes logs
```

## 下一步

- [Automate Anything with Cron](/docs.zh/guides/automate-with-cron)
- [Daily Briefing Bot](/docs.zh/guides/daily-briefing-bot)
- [FAQ](/docs.zh/reference/faq)
