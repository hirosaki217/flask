import requests
from db.mysql import connect_db
import requests

def fetch_with_proxy(url: str):
  try:
    connection = connect_db()
    
    while True:
      cursor = connection.cursor()
      cursor.execute("SELECT username, password, ip, port FROM proxies WHERE valid = true LIMIT 1")
      proxy = cursor.fetchone()
      result = fetch_with_proxy_has_auth(url, proxy)
      text = result.text
      if 'Có quá nhiều truy cập' in text:
        cursor.execute("UPDATE proxies SET valid = false WHERE ip = %s and port = %s", (proxy[2], proxy[3]))
        connection.commit()
        cursor.close()
        print(cursor.rowcount, "record(s) affected")
      else:
        connection.close()
        print("dang xai proxy")
        return result
  except:
    print("dang xai bth")
    cursor.close()
    connection.close()
    result = requests.get(url, stream=True)
    text = result.text
    if 'Có quá nhiều truy cập' in text:
      raise Exception('Có quá nhiều truy cập')
    return result



def fetch_with_proxy_has_auth(url: str, proxy):
  proxies = {
    "http": "http://{}:{}@{}:{}".format(proxy[0], proxy[1], proxy[2], proxy[3]),
  }
  return requests.get(url, proxies=proxies, stream=True)