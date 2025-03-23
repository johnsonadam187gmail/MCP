from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def usd_to_gbp(amount: float) -> float:
  """Convert USD to GBP"""
  EXCHANGE_RATE = 0.79
  return round(amount * EXCHANGE_RATE, 2)




if __name__ == "__main__":
  mcp.run()