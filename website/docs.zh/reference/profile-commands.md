---
sidebar_position: 7
---

# Profile 命令参考

本页整理和 [Profiles](/docs.zh/user-guide/profiles) 相关的全部命令。

:::note 中文整理版
本页是 `website/docs/reference/profile-commands.md` 的中文整理版。英文原文：[/docs/reference/profile-commands](/docs/reference/profile-commands)
:::

## `hermes profile`

```bash
hermes profile <subcommand>
```

顶层子命令：

| 子命令 | 作用 |
|---|---|
| `list` | 列出所有 profiles |
| `use` | 设为默认 profile |
| `create` | 创建新 profile |
| `delete` | 删除 profile |
| `show` | 查看详情 |
| `alias` | 重新生成别名脚本 |
| `rename` | 重命名 profile |
| `export` | 导出为 tar.gz |
| `import` | 从 tar.gz 导入 |

## 常见示例

```bash
hermes profile list
hermes profile create coder
hermes profile create ops --clone
hermes profile use coder
hermes profile rename mybot assistant
hermes profile export coder
hermes profile import coder.tar.gz
hermes -p coder chat
```

## 何时用 `-p`

如果你频繁在多个实例之间切换，`hermes -p <name>` 往往比设置 sticky default 更安全，因为它能显式表达当前命令到底落在哪个 profile 上。

## 相关页面

- [Profiles](/docs.zh/user-guide/profiles)
- [CLI 命令参考](/docs.zh/reference/cli-commands)
