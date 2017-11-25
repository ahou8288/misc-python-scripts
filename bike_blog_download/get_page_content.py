with open('url_list.txt','r') as f:
	url_list = f.readlines()
	url_list = [i.rstrip('\n') for i in url_list]

print(url_list)
