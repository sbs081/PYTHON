#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2009-10-23

@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@copyright: keep all copyright
'''

##########################
# 转载请声明出处.
# http://blog.csdn.net/lgg201
##########################

import re, time

datas = ['Thu Jul 22 19:21:19 2004::izsp@dicqdhytvhv.edu::1090549279-4-11', 
         'Sun Jul 13 22:42:11 2008::zqeu@dxaibjgkniy.com::1216014131-4-11', 
         'Sat May 5 16:36:23 1990::fclihw@alwdbzpsdg.edu::641950583-6-10', 
         'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8', 
         'Thu Jun 26 19:08:59 2036::ugxfugt@jkhuqhs.net::2098145339-7-7', 
         'Tue Apr 10 01:04:45 2012::zkwaq@rpxwmtikse.com::1334045085-5-10']

pattern = re.compile(r'''(?x)
        ^(?P<week>Mon|Tue|Wed|Thu|Fri|Sat|Sun)\   #匹配星期
        (?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Seq|Oct|Nov|Dec)\   #匹配月份
        (?P<day>  #匹配天数, 限定字符串范围: 1-9, 01-29, 30-31
            (
                (?P<day_tens_digit_one_two>[12])
                |(?P<day_tens_digit_three>3)
                |0?
            )
            (?(day_tens_digit_one_two)[0-9]|(?(day_tens_digit_three)[01]|[1-9]))
        )\ 
        (?P<hour>  #匹配小时, 限定字符串范围: 1-9, 01-19, 20-24
            ((?P<hour_tens_digit_one>1)|(?P<hour_tens_digit_two>2)|0?)
            (?(hour_tens_digit_one)[0-9]|(?(hour_tens_digit_two)[0-4]|[1-9]))
        ):
        (?P<minute>  #匹配分钟, 限定字符串范围: 0-9, 00-59
            ([1-5]|0?)[0-9]
        ):
        (?P<second>  #匹配秒钟, 限定字符串范围: 0-9, 00-59
            ([1-5]|0?)[0-9]
        )\ 
        (?P<year>  #匹配年份, 年份比较简单, 不再做复杂匹配
            \d{4}
        )::
        (?P<mail>  #匹配邮箱, 整个邮箱取出为新组mail, 然后分别把邮箱登录名和邮箱的服务提供商域名解析为mail_name和mail_domain
            (?P<mail_name>[a-zA-Z_]\w+)@(?P<mail_domain>(\w+\.)+(edu|com|gov|net|cn))
        )::
        (?P<timestamp>  #匹配时间戳
            \d{9,10}
        )\-
        (?P<other1>  #匹配倒数第二个数字
            \d
        )\-
        (?P<other2>   #匹配倒数第一个数字
            ([1-9]|0?)\d
        )
        ''')

def getdata(strdata, need_group_names = ('week', 'month', 
                     'day', 'hour', 'minute', 'second', 
                     'year', 'mail', 'mail_name', 
                     'mail_domain', 'timestamp', 'other1', 'other2')):
    if not isinstance(strdata, str):
        raise TypeError, 'please give me a string'
    match = pattern.search(strdata)
    result = {}
    for need_group_name in need_group_names:
        result[need_group_name] = match.group(need_group_name)
    return result

if __name__ == '__main__':
    for data in datas:
        match = pattern.search(data)
        print getdata(data)
    