from lxml.html import parse
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlparse, urljoin
import argparse

argparser = argparse.ArgumentParser(description='Download images from a Wikipedia article.')
argparser.add_argument('url', help='The article\'s URL')
argparser.add_argument('-f', dest='href_filter', default='', help='Filter image file names with specified ending.')
args = argparser.parse_args()

purl = urlparse(args.url)

with urlopen(args.url) as response:
    root = parse(response).getroot()
    anchors = root.cssselect('a.image')

links = [a.get('href') for a in anchors]
links = [f'{purl.scheme}://{purl.netloc}{link}' for link in links if link.endswith(args.href_filter)]
    
for link in links:
    with urlopen(link) as response:
        original = parse(response).getroot().cssselect('a.internal')[0].get('href')
        filename = original.split('/')[-1]
        print(filename)
        urlretrieve(urljoin('https://', original), filename=filename)
