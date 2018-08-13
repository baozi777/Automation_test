import os
#定义文件目录
result_dir = r'C:\Users\Administrator\PycharmProjects\Automation_test\unittest_1\test_project'
lists = os.listdir(result_dir)
#重新按时间排序
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
print(('最新的文件为：' + lists[-2]))#[-1]是一个驱动的log
file = os.path.join(result_dir,lists[-2])
print(file)