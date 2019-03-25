import sys
import mechanize

def crawler(link):
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41')]
    response = br.open(link)
    for link in br.links():
        linkBrowser = mechangize.Browser()
        linkBrowser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41')]
        try:
            linkBrowser.open(link.url)
            for lf in linkBrowser.links():
                print(lf.url)
        except:
            pass

crawler(sys.argv[1])
