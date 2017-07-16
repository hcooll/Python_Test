import os

print(os.name)

# 工作目录
print(os.getcwd())

# 获取目录下的所有文件
print(os.listdir('../'))

# 关机
# os.system('shutdown -s -t 3600 -c "haha"')
# os.system('shutdown -r -t 3600')

# os.system('shutdown -a')

# 计算器
# os.system('calc')

# 删除文件/文件夹
# os.remove('../jike.txt')

# 判断是文件或者文件夹
# print(os.path.isfile('../'))
# print(os.path.isdir('../'))

# 路径拆分
print(os.path.split('../'))

