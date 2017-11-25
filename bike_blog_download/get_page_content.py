# Constants
title_start_ind = 67
image_start_ind = 20
base_webpage = "https://www.crazyguyonabike.com"

with open('url_list.txt', 'r') as f:
    url_list = f.readlines()
    url_list = [i.rstrip('\n') for i in url_list]


def get_image_content(image_url):
    print(image_url)


def get_image_list(web_lines):
    output = []
    for j, i in enumerate(web_lines):
        if 'click here' in i.lower() and 'src' in i.lower():
            url_end_index = i.find('"  WIDTH')
            # image source is probs valid
            if url_end_index > 0 and len(i) > 10:
                image_url = base_webpage + i[image_start_ind:url_end_index]
                image_caption = web_lines[j + 5]
                image_caption = image_caption.lstrip(
                    '       <B >').rstrip('</B>').replace('.', '')
                output.append((image_url, image_caption))
    return output


def get_page_title(html):
    for i in html:
        if '<meta property = "og:title"' in i:
            return i.rstrip('">')[title_start_ind:]
    return 'Page title not found'


def get_page_text(html):
    for i, data in enumerate(html):
        if '<DIV ALIGN="LEFT" >' in data:
            content = html[i + 1]
            content = content.replace('<P>', '\n')
            return content


def write_page_info(title, body, images):
    import os
    import shutil
    import requests

    base_dir = './pages/'
    folder_path = base_dir + title + '/'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(folder_path + 'content.txt', 'w') as content_file:
        content_file.write(body)

    print('Downloading {} images.'.format(len(images)))

    for image_url, image_caption in images:
        response = requests.get(image_url, stream=True)
        with open(folder_path + image_caption + '.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    print('"{}" page written to file.'.format(title))


def get_page_content(page_number, url):
    import requests

    # Get the data
    r = requests.get(url)
    html = r.text

    # Process the data into lines
    web_lines = html.split('\n')

    # Process the page into images, title and body text
    page_title = get_page_title(web_lines)

    image_list = get_image_list(web_lines)

    page_body_text = get_page_text(web_lines)

    write_page_info(page_title,page_body_text,image_list)

print('URL list loaded.')
get_page_content(0, url_list[0])

from multiprocessing import Pool
import tqdm

pool = Pool(processes=8)
for _ in tqdm.tqdm(pool.imap_unordered(get_page_content, enumerate(url_list)), total=len(content), ncols = 160, unit='page'):
    pass