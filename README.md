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
git clone <repository-url>
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

## 技术架构

- **FastMCP**：用于构建 MCP 服务器的框架
- **BeautifulSoup**：用于解析 HTML 数据
- **Requests**：用于发送网络请求获取 Rootdata 网站数据

## 开发指南

### 添加新功能

1. 在 `rootdata.py` 中添加新的数据获取和解析函数
2. 在 `main.py` 中注册新的 MCP 工具函数
3. 更新工具函数的文档字符串，确保 AI 助手能够理解其功能

### 项目结构

- `main.py`：MCP 服务器入口和工具函数定义
- `rootdata.py`：Rootdata 网站数据获取和解析逻辑
- `pyproject.toml`：项目依赖和元数据

## 参考资料

- [MCP 终极指南](https://guangzhengli.com/blog/zh/model-context-protocol)
- [MCP 官方组织](https://github.com/modelcontextprotocol)
- [MCP 官方文档](https://modelcontextprotocol.io/introduction)
- [Vscode + MCP](https://hackmd.io/@ohQEG7SsQoeXVwVP2-v06A/SkQpE8STJg)
- [Rootdata 官网](https://www.rootdata.com/zh)
