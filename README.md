# cryptoghost

Cryptoghost is a python script created by three important librarys (requests, hashlib, beautifulsoup from bs4) 
cryptoghost supports decryption / encryption / encoding / decoding .
The decryption is important in cryptoghost i make tow methods for decryption :
Methode 1 , bruteforce i give 100k words and passwords list for script and he try line by line he take a word word, he encrypted the word after he comparing if the ecnrypted word == the user hash . input 
Methode 2, he tak a userhash input and decrypted in site named hashtoolkit .
Thats all
keep cracking <3

## Installation
```bash
git clone https://github.com/mchklt/cryptoghost.git

cd cryptoghost

python3 cryptoghost.py
```
## Usage 
**For ENCRYPTION && ENCODING**

#### ==> python3 cryptoghost.py -e [TEXT]

**For DECRYPTION && DECODING**

#### ==> python3 cryptoghost.py -d [HASH]

**For Decryption with url of wordlist**

#### ==> python3 cryptoghost.py -d [HASH] -u [WORDLIST_URL]

## Examples
  python3 cryptoghost.py -d ddcdfbdd755fe5fec76466e4f881d0b6 -u https://example.com/wordlist.txt 
  
  python3 cryptoghost.py -d ddcdfbdd755fe5fec76466e4f881d0b6 -w /usr/share/wordlists/MoroccanRockyou.txt 
  
  python3 cryptoghost.py -e MCHKLT
## Wordlists
  [MoroccanRockyou](https://raw.githubusercontent.com/Edd13Mora/MoroccanRockyou/main/MoroccanRockyou.txt) 
  
  [10-million-pass](https://raw.githubusercontent.com/mchklt/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt) 
  
  [bt4-pass](https://raw.githubusercontent.com/mchklt/SecLists/master/Passwords/bt4-password.txt) 
