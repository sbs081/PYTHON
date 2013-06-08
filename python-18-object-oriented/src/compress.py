'''
Created on 2009-9-29

@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
'''

def compress(data1, data2):
    if len(data1) != len(data2):
        raise RuntimeError, 'Please give me two datas of same length'
    i = 0
    while i < len(data1):
        while i + 1 < len(data1) and data2[i] + 1 == data1[i + 1]:
            data2[i] = data2[i + 1]
            del data1[i + 1]
            del data2[i + 1]
        i += 1
    return data1, data2

if __name__ == '__main__':
    data1 = [0, 5, 7, 9, 11, 13, 18, 30]
    data2 = [2, 6, 8, 10, 12, 14, 20, 50]
    print compress(data1, data2)
    