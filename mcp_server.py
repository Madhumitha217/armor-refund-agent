from fastmcp import FastMCP

mcp = FastMCP("Refund Server")

# Fake sandbox data (no real customers!)
ORDERS = {
    "ORD-1001": {"customer": "Test User A", "total": 45.00, "refunded": False},
    "ORD-1002": {"customer": "Test User B", "total": 480.00, "refunded": False},
    "ORD-1003": {"customer": "Test User C", "total": 120.00, "refunded": False},
}

@mcp.tool()
def get_order(order_id: str) -> dict:
    """Look up a sandbox order."""
    return ORDERS.get(order_id, {"error": "Order not found"})

@mcp.tool()
def issue_refund(order_id: str, amount: float, reason: str = "") -> dict:
    """Issue a refund for an order (sandbox only)."""
    order = ORDERS.get(order_id)
    if not order:
        return {"error": "Order not found"}
    order["refunded"] = True
    return {"status": "refunded", "order_id": order_id,
            "amount": amount, "reason": reason}
            @mcp.tool()
def delete_order(order_id: str) -> dict:
    """Delete an order (dangerous, sandbox only)."""
    return {"status": "deleted", "order_id": order_id}

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000, stateless_http=True)