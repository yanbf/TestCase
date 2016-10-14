#!/usr/bin/env python
# -*- coding:utf-8 -* -

#list生成式
def list_comprehensions(n):
  
   print [x*x for x in range(1,n)]
    
list_comprehensions(12)

# 生成器generator
def generator():
    g=(x*x for x in range(2,8))
    for n in g:
        print n
generator()


