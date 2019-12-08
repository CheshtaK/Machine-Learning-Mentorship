#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return int(abs((datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)).total_seconds()))

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        if(delta != None):
            print(delta)


# In[ ]:





# In[ ]:




