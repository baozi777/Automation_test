user_file = open('user_info','r')
lines = user_file.readline()
#readline()读取一行
#readlines（）读取所有行
user_file.close()
#for line in lines:#所有行集合
username = lines.split(',')[0]
password = lines.split(',')[1]
print(username,password)