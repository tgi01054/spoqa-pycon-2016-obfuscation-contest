import sys
import os
import shlex, subprocess
from subprocess import call
from subprocess import PIPE

expr = sys.argv[1]

#if( expr.startswith("+") == True ):
#        expr = expr[1:]
#expr = "scale=4; %s" % (expr)	
#
#p1 = subprocess.Popen(['echo', expr ],
#                         stdout=subprocess.PIPE)
#p2 = subprocess.Popen(['bc'], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
#
#stdout, stderr = p2.communicate()
#stdout=stdout.decode()
#stderr=stderr.decode()

code = "print(%s)" % (expr)

p = subprocess.Popen(['python','-c',code], stdout=PIPE, stderr=PIPE)

stdout, stderr = p.communicate()
stdout=stdout.decode()
stderr=stderr.decode()

if( not stderr ):
	print(stdout)
	sys.exit(0)	
sys.exit(-1)	
