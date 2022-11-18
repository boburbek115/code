import requests
from bs4 import BeautifulSoup

while True:
    try:
        try:
          x = requests.get('http://atomi.tk/selenium/')
        except Exception as e: 
          print("http error")
          print(f"[ERROR] register(): {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}") 
          try:
            x = requests.get('https://atomi.tk/selenium/')
          except Exception as e: 
            print("https error")
            print(f"[ERROR] register(): {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}") 
        
        try:
          # print(x.text)
          soup = BeautifulSoup(x.text , 'lxml')
          atomic_code_all = soup.find('pre')
          atomic_code = "main = 2"+atomic_code_all.text
          # 1 = login
          # 2 = register
          
          # print(atomic_code.text)
          exec(atomic_code)
        #   print(atomic_code)
        
        except Exception as e: 
          print("atomic_code error")
          print(f"[ERROR] register(): {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}") 
    except Exception as e: 
        print("code error")
        print(f"[ERROR] register(): {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
