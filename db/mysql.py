import os
from urllib.parse import urlparse
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

mysql_url = os.environ.get("PSCALE_DATABASE_URL")
url_parsed = urlparse(mysql_url)

def connect_db():
  return mysql.connector.connect(
    host=url_parsed.hostname,
    user=url_parsed.username,
    password=url_parsed.password,
    database=url_parsed.path[1:],
  )
  

