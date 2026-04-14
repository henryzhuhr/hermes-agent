# 上下文压缩与缓存

Hermes 用“双层压缩 + Anthropic prompt caching”的方式处理长会话上下文。目标不是简单裁剪，而是在尽量保留有效历史的同时控制上下文窗口和成本。

:::note 中文整理版
本页是 `website/docs/developer-guide/context-compression-and-caching.md` 的中文整理版。英文原文：[/docs/developer-guide/context-compression-and-caching](/docs/developer-guide/context-compression-and-caching)
:::

## 可插拔 Context Engine

上下文管理建立在 `ContextEngine` 抽象之上。内建实现是 `ContextCompressor`，但插件可以替换成其他策略，例如无损上下文管理。

## 双层压缩

### 1. Gateway Session Hygiene

网关层会先做一层会话卫生处理，避免消息平台长线程把上下文拖爆。

### 2. Agent ContextCompressor

agent 层再做真正的压缩，包括：

- 清理旧工具输出
- 保头尾
- 摘要中间段
- 必要时重复压缩

## 压缩算法要点

Hermes 不是“全量摘要一遍完事”，而是分阶段：

1. 先剪便宜的部分，例如旧 tool results
2. 再决定保留边界
3. 生成结构化摘要
4. 组装压缩后的新消息列表

## Prompt Caching

Anthropic prompt caching 依赖 prompt 稳定性。Hermes 的很多设计，包括冻结系统层、尽量不重建 memory、避免会话中途改 toolset，都是在服务这个目标。

## 为什么这块很敏感

改这部分最容易引发：

- token 成本回归
- 会话行为漂移
- 历史语义丢失

## 相关页面

- [Prompt Assembly](/docs.zh/developer-guide/prompt-assembly)
- [Agent Loop Internals](/docs.zh/developer-guide/agent-loop)
- [Configuration](/docs.zh/user-guide/configuration)
