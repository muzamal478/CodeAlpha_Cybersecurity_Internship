# Parameterized Query
query = "SELECT * FROM users WHERE username = %s"
Cursor.execute(query, (input(),)) # type: ignore