import hashlib
import requests
import base64
import platform 
import sys
from bs4 import BeautifulSoup
def script():
    try:
        if platform.system().startswith("Linux") :
            red , green , yellow , blue , endc = '\033[91m' , '\033[92m' ,'\033[93m' , '\033[94m' , '\033[0m'
        else :
            red = green = yellow = blue = endc = ""
        Banner = """\n
        #                       _              _               _   
        #  ___ _ __ _   _ _ __ | |_ ___   __ _| |__   ___  ___| |_ 
        # / __| '__| | | | '_ \| __/ _ \ / _` | '_ \ / _ \/ __| __|
        #| (__| |  | |_| | |_) | || (_) | (_| | | | | (_) \__ \ |_ 
        # \___|_|   \__, | .__/ \__\___/ \__, |_| |_|\___/|___/\__|
        #           |___/|_|             |___/                     
        #
        #                By:\033[91mAbdelkarim Mouchquelita \n\n"""
        text = sys.argv[2].encode("utf-8")
        if sys.argv[1] == "-e":
            print(Banner)
            try:
                print(green + '''
                    1-  MD5
                    2-  SHA1
                    3-  BLAKE2B
                    4-  SHA3_256
                    5-  SHA3_512
                    6-  BLAKE2S
                    7-  SHA256
                    8-  SHA512
                    9-  SHA3_224
                    10- SHA3_384
                    11- BASE64
                    12- BASE32
                    13- BASE16
                ''' + endc)

                choice = input("Enter You Choice: ")

                vars = {1  : lambda : hashlib.md5(text).hexdigest(),
                        2  : lambda : hashlib.sha1(text).hexdigest(), 
                        3  : lambda : hashlib.blake2b(text).hexdigest(), 
                        4  : lambda : hashlib.sha3_256(text).hexdigest(), 
                        5  : lambda : hashlib.sha3_512(text).hexdigest(), 
                        6  : lambda : hashlib.blake2s(text).hexdigest(), 
                        7  : lambda : hashlib.sha256(text).hexdigest(), 
                        8  : lambda : hashlib.sha512(text).hexdigest() ,
                        9  : lambda : hashlib.sha3_224(text).hexdigest(), 
                        10 : lambda : hashlib.sha3_384(text).hexdigest(), 
                        11 : lambda : base64.b64encode(text).decode(), 
                        12 : lambda : base64.b32encode(text).decode(), 
                        13 : lambda : base64.b16encode(text).decode()}
                print("\n" + yellow + "[+] Your Hash is : " + endc + green + vars[int(choice)]() + "\n\n")
            except ValueError:
                print(red + "You not chose anything !!")
        if sys.argv[1] == "-d":
            print(Banner)
            hashtxt = sys.argv[2]
            if len(hashtxt) == int(32):
                url = 'https://gist.githubusercontent.com/mchklt/891807e44bb0f97fb5dcf9131bad0a36/raw/2cffc0ceaeaa2ce1a9334b7931d2b3ef9e450728/mchklt_Words.txt'
                def hash(txt):
                    return hashlib.md5(txt.encode("utf-8")).hexdigest()
                lis_t = requests.get(url).text.split("\n")
                for text in lis_t:
                    if hash(text) == hashtxt :
                        print(green + "[+] Hash Found: " + red + text + "\n\n")
                        break
                    elif hash(text) != hashtxt:
                        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                        url = 'https://hashtoolkit.com/decrypt-md5-hash/'
                        es = requests.get(url + hashtxt, headers = headers).text
                        soup = BeautifulSoup(es, 'html.parser')
                        s = soup.find_all('code')
                        print(green + "[+] Hash Found: " + red + s[1].text + "\n\n")
                        break
                    else:
                        print("Hash Not Found !")
            elif len(hashtxt) == int(40):
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                url = 'https://hashtoolkit.com/decrypt-hash/?hash='
                es = requests.get(url + hashtxt, headers = headers).text
                soup = BeautifulSoup(es, 'html.parser')
                s = soup.find_all('code')
                print(green + "[+] Hash Found: " + red + s[1].text + "\n\n")
            elif len(hashtxt) == int(64):
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                url = 'https://hashtoolkit.com/decrypt-sha256-hash/'
                es = requests.get(url + hashtxt, headers = headers).text
                soup = BeautifulSoup(es, 'html.parser')
                s = soup.find_all('code')
                print(green + "[+] Hash Found: " + red + s[1].text + "\n\n")
            elif len(hashtxt) == int(96):
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                url = 'https://hashtoolkit.com/decrypt-sha384-hash/'
                es = requests.get(url + hashtxt, headers = headers).text
                soup = BeautifulSoup(es, 'html.parser')
                s = soup.find_all('code')
                print(green + "[+] Hash Found: " + red + s[1].text + "\n\n")
            elif len(hashtxt) == int(128):
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                url = 'https://hashtoolkit.com/decrypt-sha512-hash/'
                es = requests.get(url + hashtxt, headers = headers).text
                soup = BeautifulSoup(es, 'html.parser')
                s = soup.find_all('code')
                print(green + "[+] Hash Found: " + red + s[1].text + "\n\n")
            else:
                try:
                    print(green + "\n[+]Found : " + red + base64.b64decode(hashtxt).decode('ascii') + "\n\n")
                except:
                    print(green + "\n[+]Found : " + red+ base64.b32decode(hashtxt).decode('ascii') + "\n\n")
    except IndexError:
        print(Banner + "\n python3 cryptoghost.py -e [text]\n python3 cryptoghost.py -d [hash]\n\n")
script()
