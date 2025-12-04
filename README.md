# Bonus: Data Processing and Storage

This code creates simple transactional behavior.

**Operations**
- begin_transaction(): starts a new transaction
- put(key, value): inserts or updates a key inside transaction
- get(key): returns committed value, or None if key doesn't exist
- commit(): applies all changes in the transaction to the main db
- rollback(): cancels all transactional changes

**User Guide**
1. Clone the repo by using command git clone <url>
2. Run program by using command python3 inmemorydb.py

**Official Assignment**

This assignment can be modified to become an official assignment by adding more requirements. The code could require several classes and a UI. Additionally, additions like more implementation ideas and functionality like transaction history. In reference to testing, students could implement automated unit tests to test their functionality. 
