
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

QUOTE_ID = 137887

def main():
    try:
        quote = contract.functions.getQuote(QUOTE_ID).call()
        print(quote)
    except Exception as e:
        print("Error calling getQuote:", e)

if __name__ == "__main__":
    main()
