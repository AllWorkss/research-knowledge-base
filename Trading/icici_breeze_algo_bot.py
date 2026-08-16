"""
=============================================================================
ZenithAlgo Pro - Official ICICI Direct Breeze API Python Execution Script
=============================================================================
Requirements:
    pip install breeze-connect pandas numpy

Setup Instructions:
    1. Register on ICICI Direct Breeze API Portal: https://api.icicidirect.com/
    2. Obtain App Key and Secret Key.
    3. Generate Daily Session Token after customer login.
"""

from breeze_connect import BreezeConnect
import time

class ICICIBreezeBot:
    def __init__(self, app_key, secret_key, session_token):
        self.app_key = app_key
        self.secret_key = secret_key
        self.session_token = session_token
        
        self.breeze = BreezeConnect(api_key=self.app_key)
        self.authenticate()

    def authenticate(self):
        """
        Establishes daily session with ICICI Direct Breeze API.
        """
        try:
            self.breeze.generate_session(api_secret=self.secret_key, session_token=self.session_token)
            print("[SUCCESS] Connected to ICICI Direct Breeze API!")
        except Exception as e:
            print(f"[ERROR] Authentication failed: {e}")

    def place_order(self, stock_code, qty, price, transaction_type="BUY", stoploss_price=0):
        """
        Places an Intraday / Margin order on ICICI Direct.
        """
        try:
            response = self.breeze.place_order(
                stock_code=stock_code,       # e.g., 'NIFTY' or 'RELIANCE'
                exchange_code="NSE",
                product="margin",            # 'margin' for intraday, 'cash' for delivery
                action=transaction_type.lower(),
                order_type="limit",
                stoploss=str(stoploss_price),
                quantity=str(qty),
                price=str(price),
                validity="day"
            )
            print(f"[SUCCESS] Order Placed! Response: {response}")
            return response
        except Exception as e:
            print(f"[ERROR] Failed to place Breeze order: {e}")
            return None

if __name__ == "__main__":
    print("==================================================")
    print("   ZenithAlgo - ICICI Breeze API Bot Running     ")
    print("==================================================")
    
    # Example Execution (Uncomment after filling daily credentials)
    # bot = ICICIBreezeBot("YOUR_APP_KEY", "YOUR_SECRET_KEY", "YOUR_SESSION_TOKEN")
    # bot.place_order("RELIANCE", 50, 2980.0, "BUY", 2930.0)
