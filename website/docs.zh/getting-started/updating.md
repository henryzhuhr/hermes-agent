---
sidebar_position: 6
title: "更新与卸载"
description: "升级 Hermes Agent、检查版本、回滚，以及完整卸载"
---

# 更新与卸载

:::note 中文整理版
本页是 `website/docs/getting-started/updating.md` 的中文整理版。英文原文：[/docs/getting-started/updating](/docs/getting-started/updating)
:::

## 更新

最常用的更新方式：

```bash
hermes update
```

如果你通过消息平台使用 Hermes，部分平台也支持在聊天内触发更新，但推荐优先在终端中执行。

## 更新时会发生什么

典型更新流程包括：

- 拉取最新代码
- 更新 Python / Node 依赖
- 保留 `~/.hermes/` 下的配置、记忆、技能和会话数据
- 必要时提示你补齐新配置项

## 更新后的推荐检查

```bash
hermes doctor
hermes config check
hermes status
```

如果你在运行 gateway，也要确认服务已成功重启。

## 查看当前版本

```bash
hermes version
```

## 手动更新

如果你是从源码安装：

```bash
git pull --recurse-submodules
source venv/bin/activate
uv pip install -e ".[all]"
hermes config check
```

## 回滚

如果新版本出现问题，可以回退到某个历史提交：

```bash
git log --oneline -n 20
git checkout <commit>
source venv/bin/activate
uv pip install -e ".[all]"
```

如果 gateway 正在跑，记得重启对应服务。

## Nix 用户

Nix / NixOS 用户应该遵循自己的更新路径，例如更新 flake input 后重建系统，而不是直接用源码方式覆盖。

## 卸载

如果你想彻底卸载 Hermes：

- 删除安装目录
- 删除 PATH 中的 `hermes` 入口
- 停止并移除 gateway/systemd/launchd 服务
- 视情况删除 `~/.hermes/`

## 手动卸载提示

卸载前建议先备份：

- `~/.hermes/config.yaml`
- `~/.hermes/.env`
- `~/.hermes/memories/`
- `~/.hermes/skills/`
- `~/.hermes/state.db`

如果你只是暂时不用，通常没必要删除 `~/.hermes/`。

