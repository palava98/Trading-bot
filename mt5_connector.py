# mt5_connector.py

import MetaTrader5 as mt5

def initialize_mt5():
    if not mt5.initialize():
        print("Failed to initialize MT5")
        mt5.shutdown()
        return False
    print("MT5 initialized successfully")
    return True

def get_account_info():
    account_info = mt5.account_info()
    if account_info is None:
        print("Failed to retrieve account information")
        return None
    return account_info

def shutdown_mt5():
    mt5.shutdown()
