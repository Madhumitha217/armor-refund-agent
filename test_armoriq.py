import os
from dotenv import load_dotenv
from armoriq_sdk import ArmorIQClient

load_dotenv()

client = ArmorIQClient(
    api_key=os.environ["ARMORIQ_API_KEY"],
    user_id=os.environ["ARMORIQ_USER_ID"],
    agent_id=os.environ["ARMORIQ_AGENT_ID"],
)

def try_refund(order_id, amount):
    inputs = {"order_id": order_id, "amount": amount, "reason": "customer request"}
    plan = {
        "goal": f"Refund ${amount} for {order_id}",
        "steps": [{"action": "issue_refund", "tool": "refund-mcp", "inputs": inputs}],
    }
    capture = client.capture_plan(
        llm="gemini", prompt=f"Refund ${amount} for {order_id}", plan=plan
    )
    token = client.get_intent_token(capture)
    return client.invoke(
        mcp_name="refund-mcp",
        action="issue_refund",
        intent_token=token,
        inputs=inputs,
    )

for order_id, amount in [("ORD-1001", 45), ("ORD-1002", 480)]:
    print(f"\n--- Refund ${amount} for {order_id} ---")
    try:
        print("RESULT:", try_refund(order_id, amount))
    except Exception as e:
        print("BLOCKED or ERROR:", e)