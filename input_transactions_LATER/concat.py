from inputTransactions.inputDate import setDate
from inputTransactions.inputAction import setMovement

def get_transaction():
    """
    Union information to save a transaction
    """
    date = setDate()
    movement = setMovement()