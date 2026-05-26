from backend import models

def create_transaction(
    db,
    sender_id,
    receiver_id,
    amount,
    transaction_type,
    provider
):

    transaction = models.Transaction(
        sender_id=sender_id,
        receiver_id=receiver_id,
        amount=amount,
        transaction_type=transaction_type,
        payment_provider=provider,
        status="completed"
    )

    db.add(transaction)

    db.commit()

    return transaction