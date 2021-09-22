#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Taking a binary number input
binary = list(input("please enter a binary number: "))
d_num = 0
for i in range(len(binary)):
    digit = binary.pop()
    if digit == '1':
        d_num = d_num + pow(2,i)
print("The Decimal Number is ", d_num)


# In[ ]:




