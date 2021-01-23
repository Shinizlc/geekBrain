import subprocess as sb
import os
os.environ['DYLD_LIBRARY_PATH']='/usr/local/Oracle/product/instantclient//lib'
with sb.Popen(['sqlplus', '/nolog'],stdout=sb.PIPE,stdin=sb.PIPE,stderr=sb.PIPE) as f:
    #f.stdin.write('select 1 from dual;'.encode())
    f.communicate('select 1 from dual;'.encode())
    #data=f.stdout.readline()
    data,err=f.communicate()
    print(data.decode())


