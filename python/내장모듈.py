import urllib.request

response =urllib.request.urlopen("http://www.naver.com")

print(response.read())