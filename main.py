from typing import Any, List, Dict
from mcp.server.fastmcp import FastMCP
from rootdata import fetch_rootdata_projects

mcp = FastMCP("rootdata")

@mcp.tool()
async def get_rootdata_hot_projects() -> List[Dict[str, str]]:
    """
    Get the hot projects from rootdata.
    
    Returns:
        A list of hot projects from Rootdata with name, description and link.
    """
    projects = fetch_rootdata_projects()
    return projects

if __name__ == "__main__":
    mcp.run(transport="stdio")