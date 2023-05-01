from hashlib import sha256
import time

def apply_sha256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine_btc(block_number, transactions, previous_hash, zero_qty):
    nonce = 0
    while True:
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = apply_sha256(text)
        if new_hash[:zero_qty] != "0" * zero_qty:
            nonce += 1
            text = str(block_number) + transactions + previous_hash + str(nonce)
            new_hash = apply_sha256(text)