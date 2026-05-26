@router.post("/creator/profile")
@router.post("/creator/{creator_id}/subscribe")
@router.post("/creator/{creator_id}/tip")
@router.post("/creator/post")
@router.get("/creator/{creator_id}/posts")

wallet = db.query(models.Wallet).filter(
    models.Wallet.user_id == creator_id
).first()

wallet.balance += amount
wallet.creator_earnings += amount

create_transaction(
    db,
    sender_id=current_user.id,
    receiver_id=creator_id,
    amount=amount,
    transaction_type="tip",
    provider="internal_wallet"
)