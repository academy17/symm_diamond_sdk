### README for SYMM Diamond SDK

---

## **SYMM Diamond SDK**

The SYMM Diamond SDK is a Python-based toolkit for interacting with the Symmio smart contracts. It provides code examples for things like managing sub-accounts, sending quotes, depositing and allocating funds, and requesting to close positions, simplifying integration with your own platform.

---

## **Installation**

### **Prerequisites**
1. **Python**: Ensure you have Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/).
2. **Pip**: Ensure `pip` is installed for managing Python packages.

### **Clone the Repository**
```bash
git clone https://github.com/your-repo/symm_diamond_sdk.git
cd symm_diamond_sdk
```

### **Set Up a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Install Dependencies**
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

---

## **Environment Configuration**

### **Create a .env File**
Copy the .env.example file to .env and populate it with your configuration details.

```bash
cp .env.example .env
```

### **Environment Variables**
Below is a description of the environment variables you need to populate in the .env file:

| Variable               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `RPC_URL`              | The RPC URL for interacting with the blockchain (e.g., Polygon).           |
| `PRIVATE_KEY`          | Your private key for signing transactions. **Keep this secure!**           |
| `DIAMOND_ADDRESS`      | The address of the Symmio Diamond contract.                                |
| `MUON_BASE_URL`        | The base URL for the Muon API.                                             |
| `HEDGER_URL`           | The base URL for the Hedger API.                                           |
| `MULTIACCOUNT_ADDRESS` | The address of the MultiAccount contract.                                  |
| `SUB_ACCOUNT_ADDRESS`  | The sub-account address for multi-account operations.                      |
| `COLLATERAL_ADDRESS`   | The ERC20 token address used for collateral.                               |
| `PARTY_B_ADDRESS`      | The Party B address for certain operations.                                |

---

## **Usage**

### **1. Deposit and Allocate for Account**

This script allows you to deposit ERC20 tokens into the MultiAccount contract and allocate them to a specific sub-account.

#### **Example**
```bash
python multiaccount/deposit_and_allocate_for_account.py
```

#### **Parameters**
- **Sub-account Address**: The address of the sub-account to allocate funds to.
- **Deposit Amount**: The amount of ERC20 tokens to deposit (in wei).

#### **Code Example**
```python
sub_account_address = "0x4921a5fC974d5132b4eba7F8697236fc5851a3fA"  # Replace with your sub-account address
deposit_amount = Web3.to_wei(100, "ether")  # Replace with the amount to deposit

print("Approving ERC20 tokens...")
client.approve_erc20(CONFIG["multiaccount_address"], deposit_amount)

print("Depositing and allocating for account...")
client.deposit_and_allocate_for_account(sub_account_address, deposit_amount)
```

---

### **2. Send Quote with Affiliate**

This script sends a quote using the `sendQuoteWithAffiliate` function via the MultiAccount `_call` method.

#### **Example**
```bash
python multiaccount/account_actions/send_quote_with_affiliate.py
```

#### **Parameters**
- **Symbol ID**: The ID of the trading pair (e.g., XRP/USDT).
- **Quantity**: The quantity to trade (in ether).
- **Leverage**: The leverage to use for the trade.
- **Position Type**: `0` for LONG, `1` for SHORT.
- **Order Type**: `0` for LIMIT, `1` for MARKET.
- **Slippage**: The acceptable slippage percentage.
- **Affiliate Address**: The affiliate address for the trade.

#### **Code Example**
```python
client = MultiAccountTradeClient(CONFIG)

# Example parameters
CONFIG["symbol_id"] = 4  # XRP/USDT
CONFIG["quantity"] = "6"  # 6 XRP
CONFIG["leverage"] = 1  # 1x leverage
CONFIG["position_type"] = 0  # LONG
CONFIG["order_type"] = 1  # MARKET
CONFIG["slippage"] = "2"  # 2% slippage
CONFIG["affiliate"] = "0xffE2C25404525D2D4351D75177B92F18D9DaF4Af"

client.send_quote_with_affiliate_via_multiaccount()
```

---

### **3. Request to Close Position**

This script requests to close an open position using the `requestToClosePosition` function via the MultiAccount `_call` method.

#### **Example**
```bash
python multiaccount/account_actions/request_to_close_position.py
```

#### **Parameters**
- **Quote ID**: The ID of the quote to close.
- **Close Price**: The price at which to close the position (in wei).
- **Quantity to Close**: The quantity to close (in wei).
- **Order Type**: `0` for LIMIT, `1` for MARKET.
- **Deadline**: The deadline for the transaction (in seconds from now).

#### **Code Example**
```python
client = MultiAccountRequestToClosePositionClient(CONFIG)

# Example parameters
quote_id = 2213  # Replace with the actual quote ID
close_price = Web3.to_wei(3.3, "ether")  # Replace with the desired close price
quantity_to_close = Web3.to_wei(6, "ether")  # Replace with the quantity to close
order_type = 1  # MARKET
deadline = int(time.time()) + 3600  # 1 hour from now

receipt = client.request_to_close_position_via_multiaccount(
    quote_id, close_price, quantity_to_close, order_type, deadline
)
print(f"Request to close position transaction receipt: {receipt}")
```

---


### **4. View Functions**

The SDK also includes scripts for querying on-chain data, such as allocated balances, open positions, and quotes.

#### **Get Allocated Balance of Party A**
This script retrieves the allocated balance of a specific Party A.

```bash
python view/account/allocated_balance_of_party_a.py
```

#### **Code Example**
```python
PARTY_A = "0xEb42F3b1aC3b1552138C7D30E9f4e0eF43229542"  # Replace with Party A's address
allocated_balance = contract.functions.allocatedBalanceOfPartyA(PARTY_A).call()
print(f"Allocated balance of Party A {PARTY_A}: {allocated_balance}")
```

---

#### **Get Party A Open Positions**
This script retrieves the open positions for a specific Party A.

```bash
python view/positions/party_a_open_positions.py
```

#### **Code Example**
```python
PARTY_A = "0xEb42F3b1aC3b1552138C7D30E9f4e0eF43229542"  # Replace with Party A's address
START = 0
SIZE = 10
open_positions = contract.functions.getPartyAOpenPositions(PARTY_A, START, SIZE).call()
print(f"Open positions for Party A {PARTY_A}:", open_positions)
```

---

#### **Get Quote**
This script retrieves details of a specific quote by its ID.

```bash
python view/quotes/get_quote.py
```

#### **Code Example**
```python
QUOTE_ID = 137887  # Replace with the actual quote ID
quote = contract.functions.getQuote(QUOTE_ID).call()
print(f"Details of Quote ID {QUOTE_ID}:", quote)
```

---


## **Troubleshooting**

### **Common Errors**
1. **"LibMuon: TSS not verified"**:
   - Ensure you are passing the correct `partyA` and `partyB` addresses when fetching Muon signatures.
   - Verify that the `PairUpnlAndPriceSig` or `SingleUpnlSig` is formatted correctly as a dictionary.

2. **"Gas limit too low"**:
   - Increase the gas limit in the transaction. For complex transactions, use at least `300,000` gas.

---

