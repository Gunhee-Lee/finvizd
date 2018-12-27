from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def list_accounts() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'finvizd_db'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM accounts')
    results = [{username: realname} for (username, realname, password) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'ids and names': list_accounts()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
