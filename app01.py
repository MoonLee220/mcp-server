from fastmcp import FastMCP
import uvicorn

app = FastMCP("My MCP Server")

# 提供一個加法工具
@app.tool()
def add(n1: int, n2: int) -> int:
    """Add Two Number"""
    return n1 + n2

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081) 