from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<─────────────── v.1.2 ───────────────>')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m  786 => lakhan-meena-sniper-king
')")
           print("\033[1;93m")
           print("  <───────[ lakhan meena ]───────>")
           print("")
           try:
                x = str(input('\033[1;92mUsername \lakhanmeena[1;93m: '))
                print("")
                e = getpass('\880[1;92mPassword \880[1;93m: ')
                print ("")
                if x=="lakhan" and e=="46495":
                   print('wait...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\880[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\880[1;91m     Wrong Password")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\880[1;91m     Wrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\880[1;91m     Wrong Password")
                      time.sleep(2)
menu()
