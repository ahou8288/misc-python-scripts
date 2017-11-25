with open('url_list.txt','r') as f:
	url_list = f.readlines()
	url_list = [i.rstrip('\n') for i in url_list]

def get_page_content(url):
	import requests

	r = requests.get(url)
	html = r.text

	web_lines = html.split('\n')
	# print(web_lines)

	for i in web_lines:
		if 'click here' in i.lower():
			print(i)

print('URL list loaded.')
get_page_content(url_list[0])

# print(url_list[0])