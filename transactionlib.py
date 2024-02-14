import sqlite3
import random
import json
import time


def user_retrieval_transaction(userid: int) -> dict:
    connection = sqlite3.connect("electricity.db")
    cursor = connection.cursor()

    user_ = cursor.execute("SELECT * FROM chargecfg WHERE id = ?", (userid,)).fetchone()

    if user_ == None:
        transactions = json.dumps([{"tid": 0, "date": 0, "item": "Welcome to Coconutbot!", "currency": {"curr": "0", "type": "charges"}}]).encode()
        cursor.execute("INSERT INTO chargecfg VALUES(?,?,?)", (userid, 0, transactions, ))
        connection.commit()
        user_data = {"id": userid, "coins": 0, "transactions": json.loads(transactions.decode())}
    else:
        
        user_data = {"id": user_[0], "coins": user_[1], "transactions": json.loads(user_[2].decode())}
    
    connection.close()
    return user_data

def create_positive_transaction(userid: int, item: str, charges: int) -> None:

    user_ = user_retrieval_transaction(userid)

    coins = user_["coins"]
    transactions = user_["transactions"]

    result = coins + charges

    transaction_id = random.randint(0, 999999999999)
    current_date = int(time.time())

    transaction_definition = {"tid": transaction_id, "date": current_date, "item": item, "currency": {"curr": f"+{charges}", "type": "charges"}}
    
    transactions.append(transaction_definition)

    if len(transactions) == 26:
        transactions = transactions[:-1]

    newtransactions = json.dumps(transactions).encode()

    connection = sqlite3.connect("electricity.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE chargecfg SET coins = ? WHERE id = ?", (result, userid,))
    cursor.execute("UPDATE chargecfg SET transactions = ? WHERE id = ?", (newtransactions, userid,))
    cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?)", (transaction_id, current_date, item, "charges", f"+{charges}",))

    connection.commit()

    connection.close()

    return

def create_negative_transaction(userid: int, item: str, charges: int) -> bool:

    user_ = user_retrieval_transaction(userid)

    coins = user_["coins"]

    if charges > coins:
        return False

    transactions = user_["transactions"]

    result = coins - charges

    transaction_id = random.randint(0, 999999999999)
    current_date = int(time.time())

    transaction_definition = {"tid": transaction_id, "date": current_date, "item": item, "currency": {"curr": f"-{charges}", "type": "charges"}}
    
    transactions.append(transaction_definition)

    if len(transactions) == 26:
        transactions = transactions[:-1]

    newtransactions = json.dumps(transactions).encode()

    connection = sqlite3.connect("electricity.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE chargecfg SET coins = ? WHERE id = ?", (result, userid,))
    cursor.execute("UPDATE chargecfg SET transactions = ? WHERE id = ?", (newtransactions, userid,))
    cursor.execute("INSERT INTO transactions VALUES(?,?,?,?,?)", (transaction_id, current_date, item, "charges", f"-{charges}",))

    connection.commit()

    connection.close()

    return True
