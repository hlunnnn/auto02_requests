import requests

session = requests.session()
print(session.get("http://www.baidu.com").status_code)
print(session.get("http://www.baidu.com").text)
session2 = requests.Session()
print(session2.get("http://www.baidu.com").status_code)
print(session2.get("http://www.baidu.com").text)