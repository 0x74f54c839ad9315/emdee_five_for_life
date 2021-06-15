import requests
import hashlib
from bs4 import BeautifulSoup

URL = input("URL: ")

def main():
	SESSION = requests.session()

	REQ = SESSION.get(URL)
	SOUP = BeautifulSoup(REQ.content, "html.parser")
	H3 = SOUP.find("h3")

	S = H3.string.encode()
	H = hashlib.md5(S).hexdigest()

	DATA = {'hash': H}
	RESP = SESSION.post(URL, data=DATA)
	print(RESP.text)

main()