import requests
#it's going to allow us to make request
import hashlib


def request_api_data(guery_car):
	url = 'https://api.pwnedpasswords.com/range/'+ 'CBFDA'
	res = requests.get(url)
	if res.status !=200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
	return res

#check password if it exists in api response

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	return sha1password