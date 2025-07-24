from dotenv import load_dotenv
import os
import json
from web3 import Web3


load_dotenv()
RPC_URL = os.getenv("RPC_URL")
DIAMOND_ADDRESS = os.getenv("DIAMOND_ADDRESS")


abi_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "abi", "symmio.json"))
with open(abi_path, "r") as abi_file:
    ABI = json.load(abi_file)


w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(
    address=Web3.to_checksum_address(DIAMOND_ADDRESS),
    abi=ABI
)


SYMBOL_ID = 1

def main():
    try:
        penalty = contract.functions.forceCloseGapRatio(SYMBOL_ID).call()
        print(f"Force close gap ratio for symbolId {SYMBOL_ID}: {penalty}")
    except Exception as e:
        print("Error calling forceCloseGapRatio:", e)

if __name__ == "__main__":
    main()