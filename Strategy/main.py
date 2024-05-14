import requests


def main():
	"""
	Fear and greed is generally a lagging indicator. When it is high, a reversal may occur.
	"""
	url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"

	headers = {
		"X-RapidAPI-Key": "ea61c8ffe8msh2682f5953875300p179641jsn9e0b502fc2c7",
		"X-RapidAPI-Host": "fear-and-greed-index.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)

	if response.status_code == 200:
		print(response.json())
	else:
		print("Fear & Greed API call failed")

main()

#maybe send me notification if the indicator is really high or low