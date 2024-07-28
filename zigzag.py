#zizag program 
import time
indent = 0
IndentIncrese =True
try:
    while(True):
        print(' '*indent,end='')
        print('******')
        time.sleep(0.2)
        if(IndentIncrese):
            indent = indent + 1
            if(indent == 20):
                IndentIncrese  = False
        else:
            indent = indent - 1
            if(indent == 0):
                IndentIncrese = True        
except KeyboardInterrupt:
    print("program finish") 