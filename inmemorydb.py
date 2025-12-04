class TransactionError(Exception):
    pass

class InMemoryDB:
    def __init__(self):
        self._db = {}
        self._in_transaction = False
        # staged changes during the current transaction
        self._tx_changes = {}

    def get(self, key: str):
        return self._db.get(key)

    def put(self, key: str, val: int):
        if not self._in_transaction:
            raise TransactionError("No active transaction")
        self._tx_changes[key] = val

    def begin_transaction(self):
        if self._in_transaction:
            raise TransactionError("Transaction already in progress")
        self._in_transaction = True
        self._tx_changes = {}

    def commit(self):
        if not self._in_transaction:
            raise TransactionError("No active transaction to commit")
        # apply staged changes to committed db
        for key, val in self._tx_changes.items():
            self._db[key] = val
        self._tx_changes = {}
        self._in_transaction = False

    def rollback(self):
        if not self._in_transaction:
            raise TransactionError("No active transaction to rollback")
        self._tx_changes = {}
        self._in_transaction = False


# test
if __name__ == "__main__":
    db = InMemoryDB()

    # should return None because A doesn’t exist
    print("get(A):", db.get("A"))

    # should throw an error because a transaction is not in progress
    try:
        db.put("A", 5)
    except TransactionError as e:
        print("put(A,5) error:", e)

    # starts a new transaction
    db.begin_transaction()

    # sets value of A to 5 but it's not committed yet
    db.put("A", 5)

    # should return None because updates to A are not committed yet
    print("get(A) inside tx (after put 5):", db.get("A"))

    # update A’s value to 6 within the transaction
    db.put("A", 6)

    # commits the open transaction
    db.commit()

    # should return 6
    print("get(A) after commit:", db.get("A"))

    # throws an error because there is no open transaction
    try:
        db.commit()
    except TransactionError as e:
        print("commit() error:", e)

    # throws an error because there is no ongoing transaction
    try:
        db.rollback()
    except TransactionError as e:
        print("rollback() error:", e)

    # should return None because B does not exist in the database
    print("get(B):", db.get("B"))

    # starts a new transaction
    db.begin_transaction()

    # key B’s value to 10 within the transaction
    db.put("B", 10)

    # rollback the transaction
    db.rollback()

    # should return None
    print("get(B) after rollback:", db.get("B"))
