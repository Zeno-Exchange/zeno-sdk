import os
import asyncio
from zeno.zeno_client import Client
from zeno.constants.tokens import COLLATERAL_mUSDC, COLLATERAL_WETH
from dotenv import load_dotenv
from time import sleep

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")
ACCOUNT = os.getenv("ACCOUNT")


async def main():
  client = Client(
     eth_private_key=PRIVATE_KEY,
     rpc_url=RPC_URL,
   )

  # Get Collateral
  client.public.get_collaterals(ACCOUNT, sub_account_id=0)

  # Deposit ETH as collateral
  client.private.deposit_eth_collateral(sub_account_id=0, amount=0.1)
  sleep(5)

  # Deposit ERC20 as collateral. This function will automatically
  # approve CrossMarginHandler if needed.
  client.private.deposit_erc20_collateral(
    sub_account_id=0, token_address=COLLATERAL_mUSDC, amount=100.10)

  sleep(5)

  # Withdraw ETH as collateral
  # Can wrap if wanted
  client.private.withdraw_collateral(
    sub_account_id=0, token_address=COLLATERAL_WETH, amount=0.1, wrap=False)

  sleep(5)

  # Withdraw ERC20 as collateral. This function will automatically
  client.private.withdraw_collateral(
    sub_account_id=0, token_address=COLLATERAL_mUSDC, amount=100.10)

if __name__ == '__main__':
  asyncio.run(main())
