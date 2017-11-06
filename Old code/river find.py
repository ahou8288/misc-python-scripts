import re
import urllib

url = 'http://www.kayakcanberra.com/heights/'
html = urllib.urlopen(url).read()
print html
matches = re.findall('href="\.\./rivers/.*?', x, re.DOTALL)
print matches
