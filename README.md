# Rootdata MCP Server

一个很小的 MCP server 实验，用来把 [Rootdata](https://www.rootdata.com/zh) 上的 Web3 项目信息暴露给支持 MCP 的 AI 助手。

它适合用来理解：

- 如何写一个最小 MCP tool
- 如何把外部 Web3 数据源接入 AI 助手
- AI 研究工作流里如何补充结构化数据入口

## 项目简介

当前工具提供一个 MCP 方法：

```text
get_rootdata_hot_projects
```

它会抓取 Rootdata 页面，解析项目名称、描述和链接，并返回给 MCP 客户端。

这个项目是 MCP / Web3 research workflow 的小实验，不是 Rootdata 官方 API，也不保证页面结构变更后的稳定性。

## 安装

### 环境要求

- Python 3.11+
- pip 或 uv 包管理器

### 安装步骤

1. 克隆仓库到本地：

```bash
git clone https://github.com/yulai-123/rootdata_mcp_server.git
cd rootdata_mcp_server
```

2. 安装依赖：

```bash
pip install -e .
# 或使用 uv
uv pip install -e .
```

## 使用方法

### 启动 MCP 服务器

```bash
python main.py
```

服务器将以标准输入/输出（stdio）模式运行，可以被 MCP 客户端连接。

### Tool

```python
get_rootdata_hot_projects() -> list[dict[str, str]]
```

返回字段：

- `name`
- `description`
- `link`

### 与 MCP 客户端集成

不同客户端的配置格式不完全相同。核心是让客户端通过 stdio 启动：

```bash
python /path/to/rootdata_mcp_server/main.py
```

可以参考：

- [VS Code Copilot Chat MCP 插件](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat-mcp)
- [MCP 官方组织](https://github.com/modelcontextprotocol)

## 参考资料

- [MCP 终极指南](https://guangzhengli.com/blog/zh/model-context-protocol)
- [MCP 官方组织](https://github.com/modelcontextprotocol)
- [MCP 官方文档](https://modelcontextprotocol.io/introduction)
- [Vscode + MCP](https://hackmd.io/@ohQEG7SsQoeXVwVP2-v06A/SkQpE8STJg)
- [Rootdata 官网](https://www.rootdata.com/zh)
