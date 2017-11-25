with open('url_list.txt', 'r') as f:
    url_list = f.readlines()
    url_list = [i.rstrip('\n') for i in url_list]


def get_image_content(image_url):
    print(image_url)


def get_page_title(html):

    return 'dog'


def get_page_content(page_number, url):
    import requests
    image_start_ind = 20
    base_webpage = "https://www.crazyguyonabike.com"

    r = requests.get(url)
    html = r.text

    web_lines = html.split('\n')
    # print(web_lines)

    print(get_page_title(web_lines))

    # for i in web_lines:
    #     if 'click here' in i.lower() and 'src' in i.lower():
    #         url_end_index = i.find('"  WIDTH')
    #         # image source is probs valid
    #         if url_end_index > 0 and len(i) > 10:
    #                 get_image_content(base_webpage+i[image_start_ind:url_end_index])

print('URL list loaded.')
get_page_content(0, url_list[0])

# print(url_list[0])
