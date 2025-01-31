import example_utils

from hyperliquid.utils import constants


def main():
    # Setup the exchange connection using testnet
    address, info, exchange = example_utils.setup(constants.TESTNET_API_URL, skip_ws=True)

    # Enable big blocks (30M gas limit, 1 minute duration)
    print("Enabling big blocks...")
    result = exchange.evm_user_modify(using_big_blocks=True)
    print("Result:", result)

    # # Wait for user input before switching back
    # input("\nPress Enter to switch back to small blocks...")

    # # Switch back to small blocks (1M gas limit, 2 seconds duration)
    # print("\nSwitching back to small blocks...")
    # result = exchange.evm_user_modify(using_big_blocks=True)
    # print("Result:", result)


if __name__ == "__main__":
    main() 