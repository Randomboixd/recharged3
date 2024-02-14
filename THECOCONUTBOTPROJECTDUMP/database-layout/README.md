# database-layout

Here's how the database (electricity.db) is layed out.

Generally, as of testroll #3 of Coconutbot Recharged, this repo also contains an empty electricity.db itself, so you can download that and drop it in. boom.

# cardcfg

Stores card ownership data.

```sql
CREATE TABLE cardcfg(id INTEGER, totalcards INTEGER, cards BLOB);
```

# chargecfg

Stores coins (Charges) for each user. also keeps a record of the 25 latest transactions in a json format

```sql
CREATE TABLE chargecfg(id INTEGER, coins INTEGER, transactions BLOB);
```

## `transactions` JSON Layout

```json
[
    {"tid": "Reference to id in transactions table", "date": 1706443035, "item": "card squeeze", "currency": {"curr": "+35", "type": "charges"}}
]
```

# transactions

Stores TIDs (Transaction IDs), and their date, and the purchased item, albeit this is also referenced in chargecfg's transactions row.

```sql
CREATE TABLE transactions(tid INTEGER, date INTEGER, item TEXT, currencytype TEXT, amount TEXT);
```

# polls

The /polls command, using sqlite now.

```sql
CREATE TABLE polls(id INTEGER, data BLOB);
```

data is the JSON Structure of the submission.

# achievementd

Achievement Database. Basically if a user earns a valid achievement from the achievement registry `achievement.registry` it will be recorded here.

```sql
CREATE TABLE achievementd(userid INTEGER, achievementid TEXT, earnedat INTEGER);
```

In this case, userid is the user's discord id, achievementid is the key in `achievement.registry`, and earnedat is the UNIX Timestamp at when the achievement was earned.




