"""
=============================================================================
ZenithAlgo Pro - Official Upstox API v2 Python Automated Execution Script
=============================================================================
Requirements:
    pip install upstox-python-sdk pandas numpy

Setup Instructions:
    1. Create a developer account at https://developer.upstox.com/
    2. Obtain API Key and API Secret.
    3. Generate Daily Access Token via OAuth login.
"""

import upstox_client
from upstox_client.rest import ApiException
import time

class UpstoxBot:
    def __init__(self, access_token):
        self.configuration = upstox_client.Configuration()
        self.configuration.access_token = access_token
        self.api_client = upstox_client.ApiClient(self.configuration)
        
        self.order_api = upstox_client.OrderApi(self.api_client)
        self.portfolio_api = upstox_client.PortfolioApi(self.api_client)

    def place_order(self, symbol, quantity, limit_price, transaction_type="BUY"):
        """
        Places an Intraday order on Upstox API v2.
        """
        body = upstox_client.PlaceOrderRequest(
            quantity=quantity,
            product='I',              # 'I' = Intraday (MIS), 'D' = Delivery (CNC)
            validity='DAY',
            price=float(limit_price),
            tag=f'ZENITH_ALGO_{transaction_type}',
            instrument_token=symbol, # e.g. 'NSE_EQ|INE002A01018'
            order_type='LIMIT',
            transaction_type=transaction_type.upper(),
            disclosed_quantity=0,
            trigger_price=0.0,
            is_amo=False
        )
        try:
            response = self.order_api.place_order(body, api_version='2.0')
            print(f"[SUCCESS] {transaction_type} Order Executed! Order ID: {response.data.order_id}")
            return response.data.order_id
        except ApiException as e:
            print(f"[ERROR] Failed to place Upstox order: {e}")
            return None

    def get_positions(self):
        """
        Fetches active positions to enforce Dad's Safety Guard Rules.
        """
        try:
            response = self.portfolio_api.get_positions(api_version='2.0')
            print("[INFO] Active Positions Fetched Successfully.")
            return response.data
        except ApiException as e:
            print(f"[ERROR] Could not fetch positions: {e}")
            return None

if __name__ == "__main__":
    print("==================================================")
    print("      ZenithAlgo - Upstox API Bot Running         ")
    print("==================================================")
    
    # Demonstration Call
    # bot = UpstoxBot("YOUR_DAILY_UPSTOX_ACCESS_TOKEN")
    # print("Simulating Upstox Strategy Trigger...")
    # bot.place_order('NSE_EQ|INE002A01018', 50, 2980.0, "BUY")
