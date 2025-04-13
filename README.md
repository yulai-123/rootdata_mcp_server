# Rootdata MCP Server

基于 Model Context Protocol (MCP) 实现的服务器，提供查询「[Rootdata](https://www.rootdata.com/zh)每日新增热点项目」的功能，让 AI 助手可以获取最新的区块链和 Web3 项目信息。

## 项目简介

Rootdata MCP Server 使用 Model Context Protocol 技术，为 AI 助手提供了查询 Rootdata 平台热门项目数据的能力。通过该服务器，AI 可以实时获取区块链和 Web3 领域的最新热点项目信息，帮助用户了解行业动态。

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

### 与 AI 助手集成

要将此 MCP 服务器与 AI 助手集成，可以参考以下资源：

- [VS Code Copilot Chat MCP 插件](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat-mcp)
- [OpenAI Function Calling API](https://platform.openai.com/docs/guides/function-calling)

## 参考资料

- [MCP 终极指南](https://guangzhengli.com/blog/zh/model-context-protocol)
- [MCP 官方组织](https://github.com/modelcontextprotocol)
- [MCP 官方文档](https://modelcontextprotocol.io/introduction)
- [Vscode + MCP](https://hackmd.io/@ohQEG7SsQoeXVwVP2-v06A/SkQpE8STJg)
- [Rootdata 官网](https://www.rootdata.com/zh)
