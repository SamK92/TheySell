#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TheySell.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
def final_is_delivered(order_id):
    nonce = web.eth.get_transaction_count(web.toChecksumAddress(web.eth.default_account))
    deliver_tx = operations_contract.functions.idDelivered(order_id).buildTransaction({
            'chainId': 4,
            'gas': 700000,
            'maxFeePerGas': web.toWei('2', 'gwei'),
            'maxPriorityFeePerGas': web.toWei('1', 'gwei'),
            'nonce': nonce,
            })
    signed_tx = web.eth.account.sign_transaction(deliver_tx, private_key=os.getenv("PRIVATE_KEY"))
    receipt = web.eth.send_raw_transaction(signed_tx.rawTransaction)
    web.eth.wait_for_transaction_receipt(receipt)
    is_already_payed = operations_contract.functions.id_to_order(order_id).call()[-1]
    if not is_already_payed:
        nonce = web.eth.get_transaction_count(web.toChecksumAddress(web.eth.default_account))
        deliver_tx = operations_contract.functions.idDelivered(order_id).buildTransaction({
                'chainId': 4,
                'gas': 700000,
                'maxFeePerGas': web.toWei('2', 'gwei'),
                'maxPriorityFeePerGas': web.toWei('1', 'gwei'),
                'nonce': nonce,
                })
        signed_tx = web.eth.account.sign_transaction(deliver_tx, private_key=os.getenv("PRIVATE_KEY"))
        receipt = web.eth.send_raw_transaction(signed_tx.rawTransaction)
        web.eth.wait_for_transaction_receipt(receipt)
    print("Order marked as delivered!")

if __name__ == '__main__':
    main()
