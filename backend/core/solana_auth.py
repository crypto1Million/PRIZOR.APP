from solders.pubkey import Pubkey

def validate_wallet(address: str):

    try:
        Pubkey.from_string(address)
        return True

    except:
        return False