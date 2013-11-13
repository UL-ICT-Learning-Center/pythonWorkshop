#!/usr/bin/python2

# Get the username of the user ID 0, calling C functions from Python using cffi.

# checkout this link for an example that uses a library: https://gist.github.com/grejppi/7428112

from cffi import FFI

ffi = FFI()

ffi.cdef("""     // some declarations from the man page
    struct passwd {
        char *pw_name;
        ...;
    };
    struct passwd *getpwuid(int uid);
""")

C = ffi.verify("""   // passed to the real C compiler
#include <sys/types.h>
#include <pwd.h>
""", libraries=[])   # or a list of libraries to link with

p = C.getpwuid(0)

print( "" + ffi.string(p.pw_name) )
