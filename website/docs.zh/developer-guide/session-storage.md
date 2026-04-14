# Session 存储

Hermes 使用 SQLite 数据库 `~/.hermes/state.db` 持久化 session 元数据、完整消息历史和模型配置。CLI 和 gateway 都依赖这套存储。

:::note 中文整理版
本页是 `website/docs/developer-guide/session-storage.md` 的中文整理版。英文原文：[/docs/developer-guide/session-storage](/docs/developer-guide/session-storage)
:::

## 架构

核心表包括：

- `sessions`
- `messages`
- `messages_fts`
- `schema_version`

同时使用 WAL 模式和 FTS5，以兼顾并发读写和全文检索。

## 为什么不是纯 JSONL

JSONL 适合轨迹落盘，但不适合：

- 高效按标题 / 平台 /时间查询
- 全文检索
- 统计 token 与 lineage

所以 Hermes 采用 SQLite 作为主索引层。

## 常见操作

这套存储支持：

- 新建 / 结束 / 重新打开 session
- 保存消息
- 按 OpenAI conversation format 回放
- 按标题解析 session
- 自动 lineage 命名
- 导出与清理

## FTS5 的意义

`session_search` 之所以能用，核心就是这层全文检索索引，而不是把旧消息全塞回当前 prompt。

## 相关页面

- [Sessions](/docs.zh/user-guide/sessions)
- [Trajectory Format](/docs.zh/developer-guide/trajectory-format)
- [Gateway Internals](/docs.zh/developer-guide/gateway-internals)
