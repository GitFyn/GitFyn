'''
    自己编写的字典结合工具
'''
#打开第一个字典
fuzz1 = input('>>>Input Fist: ').strip()
fuzz1_list = []
with open(fuzz1,'r+') as f:
    for i in f.readlines():
        u = i.strip()
        if u:
            fuzz1_list.append(u)
#打开第二个字典
fuzz2_list = []
fuzz2 = input('>>>Input Two: ').strip()
with open(fuzz2,'r+') as f:
    for i in f.readlines():
        u = i.strip()
        if u:
            fuzz2_list.append(u)

fuzz_all = list(set(fuzz1_list+fuzz2_list))
# print(fuzz_all)
#写入文件
with open('./merge.txt','w') as f:
    for j in fuzz_all:
        f.write('{}\n'.format(j))

print('>>>Write successfully @ ~_~@ - >./merge.txt')

