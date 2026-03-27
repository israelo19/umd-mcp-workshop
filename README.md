# 🛠️ CBC x Notion — MCP Workshop
### UMD Claude Builder Club | March 27, 2026

Welcome! This repo contains everything from the MCP Workshop.  
Follow along live, or set it up at home after the session.

---

## What's in here

| File | What it is |
|------|------------|
| `server.py` | The full MCP server we built together |
| `workshop.ipynb` | Google Colab notebook — run the tools without any setup |
| `claude_desktop_config.json` | Template config for connecting to Claude Desktop |
| `requirements.txt` | Python dependencies |

---

## Option A — Follow along in Google Colab (no setup needed)

**[Open in Colab →](https://colab.research.google.com)**  
*(Replace this link with your actual Colab link before the workshop)*

Just open it, click **Runtime → Run all**, and you're good.

---

## Option B — Run the full MCP server locally

### Prerequisites
- Python 3.10+
- Claude Desktop (free): [claude.ai/download](https://claude.ai/download)

### Steps

**1. Clone this repo**
```bash
git clone https://github.com/YOUR_USERNAME/umd-mcp-workshop.git
cd umd-mcp-workshop
```

**2. Install dependencies**
```bash
pip install mcp
```

**3. Find your Claude Desktop config file**

| OS | Path |
|----|------|
| Mac | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |

**4. Add this to your config** (replace the path with your actual path)
```json
{
  "mcpServers": {
    "umd-survival": {
      "command": "python",
      "args": ["/FULL/PATH/TO/umd-mcp-workshop/server.py"]
    }
  }
}
```

**5. Restart Claude Desktop**

You'll see a 🔨 hammer icon in the chat box — that means your tools are connected.

**6. Try it out**
```
"Hey Claude, I have a segmentation fault and I don't know why"
"Hey Claude, my project is 20% done with 2 days left and I slept 3 hours"
```

---

## The 3-step structure of any MCP server

```python
from mcp.server.fastmcp import FastMCP

# Step 1: Create the server
mcp = FastMCP("My Server")

# Step 2: Decorate functions with @mcp.tool()
@mcp.tool()
def my_tool(input: str) -> str:
    """Claude reads this docstring to know what the tool does."""
    return f"You said: {input}"

# Step 3: Run it
mcp.run()
```

That's the whole protocol. Everything else is just Python.

---

## Resources
- [MCP Docs](https://modelcontextprotocol.io)
- [FastMCP on PyPI](https://pypi.org/project/mcp/)
- [Claude Desktop Download](https://claude.ai/download)
- [CBC Discord](#) ← add your Discord link

## Built by
University of Maryland | Claude Builder Club
