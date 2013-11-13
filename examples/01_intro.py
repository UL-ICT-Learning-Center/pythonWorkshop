#!/usr/bin/python

# The above "comment" defines what program to run the file in.
# Since python3 is the "default" python on this machine, it will run in that
# Specifying /usr/bin/python2 will use python2.x


# define a function
def add(x, y):
  return x + y


# only run if this file is being executed: allows importing of this .py file
# as a module for other scripts without running code
if __name__ == "__main__":
  print("main")
  int1 = 20
  int2 = 40
  res = add ( int1, int2 )
  print( "result = " + str(res) )
