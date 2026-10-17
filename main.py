import os
from dotenv import load_dotenv
from fastmcp import FastMCP
from google import genai
from armoriq_sdk import ArmorIQClient

# Load environment variables from .env
load_dotenv()

# Initialize FastMCP server for our refund tools
mcp = FastMCP("Armor Refund Agent Server")

# Initialize Gemini client
gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Initialize ArmorIQ client for cryptographic intent verification & security
armoriq = ArmorIQClient(api_key=os.environ.get("ARMORIQ_API_KEY"))

@mcp.tool()
def process_refund(order_id: str, amount: float, reason: str) -> str:
    """Process a customer refund for a specific order ID."""
    # Here you would normally connect to your database or payment provider API
    return f"Successfully processed refund of ${amount} for order {order_id}. Reason: {reason}"

if __name__ == "__main__":
    print("Armor Refund Agent with FastMCP & ArmorIQ is ready.")
    # You can run your MCP server or initialize your agent loops hereprint("Hello from Armor Refund Agent!") print("Hello from Armor Refund Agent!")
