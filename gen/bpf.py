r"""Wrapper for bpf.h

Generated with:
/home/m.bieganski/.local/bin/ctypesgen -D__signed__=signed ../libbpf//include/uapi/linux/bpf.h -l ./libbpf.so.1

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):
    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["./libbpf.so.1"] = load_library("./libbpf.so.1")

# 1 libraries
# End libraries

# No modules

__u8 = c_ubyte# /usr/include/asm-generic/int-ll64.h: 21

__s16 = c_short# /usr/include/asm-generic/int-ll64.h: 23

__u16 = c_ushort# /usr/include/asm-generic/int-ll64.h: 24

__s32 = c_int# /usr/include/asm-generic/int-ll64.h: 26

__u32 = c_uint# /usr/include/asm-generic/int-ll64.h: 27

__u64 = c_ulonglong# /usr/include/asm-generic/int-ll64.h: 34

__be16 = __u16# /usr/include/linux/types.h: 25

__be32 = __u32# /usr/include/linux/types.h: 27

enum_bpf_cond_pseudo_jmp = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 57

BPF_MAY_GOTO = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 57

enum_anon_3 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_0 = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_1 = (BPF_REG_0 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_2 = (BPF_REG_1 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_3 = (BPF_REG_2 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_4 = (BPF_REG_3 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_5 = (BPF_REG_4 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_6 = (BPF_REG_5 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_7 = (BPF_REG_6 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_8 = (BPF_REG_7 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_9 = (BPF_REG_8 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

BPF_REG_10 = (BPF_REG_9 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

__MAX_BPF_REG = (BPF_REG_10 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 62

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 80
class struct_bpf_insn(Structure):
    pass

struct_bpf_insn.__slots__ = [
    'code',
    'dst_reg',
    'src_reg',
    'off',
    'imm',
]
struct_bpf_insn._fields_ = [
    ('code', __u8),
    ('dst_reg', __u8, 4),
    ('src_reg', __u8, 4),
    ('off', __s16),
    ('imm', __s32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 92
class struct_bpf_lpm_trie_key(Structure):
    pass

struct_bpf_lpm_trie_key.__slots__ = [
    'prefixlen',
    'data',
]
struct_bpf_lpm_trie_key._fields_ = [
    ('prefixlen', __u32),
    ('data', __u8 * int(0)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 98
class struct_bpf_lpm_trie_key_hdr(Structure):
    pass

struct_bpf_lpm_trie_key_hdr.__slots__ = [
    'prefixlen',
]
struct_bpf_lpm_trie_key_hdr._fields_ = [
    ('prefixlen', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 104
class union_anon_4(Union):
    pass

union_anon_4.__slots__ = [
    'hdr',
    'prefixlen',
]
union_anon_4._fields_ = [
    ('hdr', struct_bpf_lpm_trie_key_hdr),
    ('prefixlen', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 103
class struct_bpf_lpm_trie_key_u8(Structure):
    pass

struct_bpf_lpm_trie_key_u8.__slots__ = [
    'unnamed_bpf_lpm_trie_key_u8_1',
    'data',
]
struct_bpf_lpm_trie_key_u8._anonymous_ = [
    'unnamed_bpf_lpm_trie_key_u8_1',
]
struct_bpf_lpm_trie_key_u8._fields_ = [
    ('unnamed_bpf_lpm_trie_key_u8_1', union_anon_4),
    ('data', POINTER(__u8)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 111
class struct_bpf_cgroup_storage_key(Structure):
    pass

struct_bpf_cgroup_storage_key.__slots__ = [
    'cgroup_inode_id',
    'attach_type',
]
struct_bpf_cgroup_storage_key._fields_ = [
    ('cgroup_inode_id', __u64),
    ('attach_type', __u32),
]

enum_bpf_cgroup_iter_order = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 116

BPF_CGROUP_ITER_ORDER_UNSPEC = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 116

BPF_CGROUP_ITER_SELF_ONLY = (BPF_CGROUP_ITER_ORDER_UNSPEC + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 116

BPF_CGROUP_ITER_DESCENDANTS_PRE = (BPF_CGROUP_ITER_SELF_ONLY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 116

BPF_CGROUP_ITER_DESCENDANTS_POST = (BPF_CGROUP_ITER_DESCENDANTS_PRE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 116

BPF_CGROUP_ITER_ANCESTORS_UP = (BPF_CGROUP_ITER_DESCENDANTS_POST + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 116

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 125
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'map_fd',
]
struct_anon_5._fields_ = [
    ('map_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 128
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'order',
    'cgroup_fd',
    'cgroup_id',
]
struct_anon_6._fields_ = [
    ('order', enum_bpf_cgroup_iter_order),
    ('cgroup_fd', __u32),
    ('cgroup_id', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 140
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'tid',
    'pid',
    'pid_fd',
]
struct_anon_7._fields_ = [
    ('tid', __u32),
    ('pid', __u32),
    ('pid_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 124
class union_bpf_iter_link_info(Union):
    pass

union_bpf_iter_link_info.__slots__ = [
    'map',
    'cgroup',
    'task',
]
union_bpf_iter_link_info._fields_ = [
    ('map', struct_anon_5),
    ('cgroup', struct_anon_6),
    ('task', struct_anon_7),
]

enum_bpf_cmd = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_CREATE = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_LOOKUP_ELEM = (BPF_MAP_CREATE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_UPDATE_ELEM = (BPF_MAP_LOOKUP_ELEM + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_DELETE_ELEM = (BPF_MAP_UPDATE_ELEM + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_GET_NEXT_KEY = (BPF_MAP_DELETE_ELEM + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_LOAD = (BPF_MAP_GET_NEXT_KEY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_OBJ_PIN = (BPF_PROG_LOAD + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_OBJ_GET = (BPF_OBJ_PIN + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_ATTACH = (BPF_OBJ_GET + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_DETACH = (BPF_PROG_ATTACH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_TEST_RUN = (BPF_PROG_DETACH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_RUN = BPF_PROG_TEST_RUN# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_GET_NEXT_ID = (BPF_PROG_RUN + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_GET_NEXT_ID = (BPF_PROG_GET_NEXT_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_GET_FD_BY_ID = (BPF_MAP_GET_NEXT_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_GET_FD_BY_ID = (BPF_PROG_GET_FD_BY_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_OBJ_GET_INFO_BY_FD = (BPF_MAP_GET_FD_BY_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_QUERY = (BPF_OBJ_GET_INFO_BY_FD + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_RAW_TRACEPOINT_OPEN = (BPF_PROG_QUERY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_BTF_LOAD = (BPF_RAW_TRACEPOINT_OPEN + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_BTF_GET_FD_BY_ID = (BPF_BTF_LOAD + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_TASK_FD_QUERY = (BPF_BTF_GET_FD_BY_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_LOOKUP_AND_DELETE_ELEM = (BPF_TASK_FD_QUERY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_FREEZE = (BPF_MAP_LOOKUP_AND_DELETE_ELEM + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_BTF_GET_NEXT_ID = (BPF_MAP_FREEZE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_LOOKUP_BATCH = (BPF_BTF_GET_NEXT_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_LOOKUP_AND_DELETE_BATCH = (BPF_MAP_LOOKUP_BATCH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_UPDATE_BATCH = (BPF_MAP_LOOKUP_AND_DELETE_BATCH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_MAP_DELETE_BATCH = (BPF_MAP_UPDATE_BATCH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_LINK_CREATE = (BPF_MAP_DELETE_BATCH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_LINK_UPDATE = (BPF_LINK_CREATE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_LINK_GET_FD_BY_ID = (BPF_LINK_UPDATE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_LINK_GET_NEXT_ID = (BPF_LINK_GET_FD_BY_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_ENABLE_STATS = (BPF_LINK_GET_NEXT_ID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_ITER_CREATE = (BPF_ENABLE_STATS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_LINK_DETACH = (BPF_ITER_CREATE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_BIND_MAP = (BPF_LINK_DETACH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_TOKEN_CREATE = (BPF_PROG_BIND_MAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_STREAM_READ_BY_FD = (BPF_TOKEN_CREATE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

BPF_PROG_ASSOC_STRUCT_OPS = (BPF_PROG_STREAM_READ_BY_FD + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

__MAX_BPF_CMD = (BPF_PROG_ASSOC_STRUCT_OPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 947

enum_bpf_map_type = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_UNSPEC = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_HASH = (BPF_MAP_TYPE_UNSPEC + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_ARRAY = (BPF_MAP_TYPE_HASH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_PROG_ARRAY = (BPF_MAP_TYPE_ARRAY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_PERF_EVENT_ARRAY = (BPF_MAP_TYPE_PROG_ARRAY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_PERCPU_HASH = (BPF_MAP_TYPE_PERF_EVENT_ARRAY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_PERCPU_ARRAY = (BPF_MAP_TYPE_PERCPU_HASH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_STACK_TRACE = (BPF_MAP_TYPE_PERCPU_ARRAY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_CGROUP_ARRAY = (BPF_MAP_TYPE_STACK_TRACE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_LRU_HASH = (BPF_MAP_TYPE_CGROUP_ARRAY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_LRU_PERCPU_HASH = (BPF_MAP_TYPE_LRU_HASH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_LPM_TRIE = (BPF_MAP_TYPE_LRU_PERCPU_HASH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_ARRAY_OF_MAPS = (BPF_MAP_TYPE_LPM_TRIE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_HASH_OF_MAPS = (BPF_MAP_TYPE_ARRAY_OF_MAPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_DEVMAP = (BPF_MAP_TYPE_HASH_OF_MAPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_SOCKMAP = (BPF_MAP_TYPE_DEVMAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_CPUMAP = (BPF_MAP_TYPE_SOCKMAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_XSKMAP = (BPF_MAP_TYPE_CPUMAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_SOCKHASH = (BPF_MAP_TYPE_XSKMAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_CGROUP_STORAGE_DEPRECATED = (BPF_MAP_TYPE_SOCKHASH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_CGROUP_STORAGE = BPF_MAP_TYPE_CGROUP_STORAGE_DEPRECATED# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_REUSEPORT_SOCKARRAY = (BPF_MAP_TYPE_CGROUP_STORAGE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_PERCPU_CGROUP_STORAGE_DEPRECATED = (BPF_MAP_TYPE_REUSEPORT_SOCKARRAY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_PERCPU_CGROUP_STORAGE = BPF_MAP_TYPE_PERCPU_CGROUP_STORAGE_DEPRECATED# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_QUEUE = (BPF_MAP_TYPE_PERCPU_CGROUP_STORAGE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_STACK = (BPF_MAP_TYPE_QUEUE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_SK_STORAGE = (BPF_MAP_TYPE_STACK + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_DEVMAP_HASH = (BPF_MAP_TYPE_SK_STORAGE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_STRUCT_OPS = (BPF_MAP_TYPE_DEVMAP_HASH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_RINGBUF = (BPF_MAP_TYPE_STRUCT_OPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_INODE_STORAGE = (BPF_MAP_TYPE_RINGBUF + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_TASK_STORAGE = (BPF_MAP_TYPE_INODE_STORAGE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_BLOOM_FILTER = (BPF_MAP_TYPE_TASK_STORAGE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_USER_RINGBUF = (BPF_MAP_TYPE_BLOOM_FILTER + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_CGRP_STORAGE = (BPF_MAP_TYPE_USER_RINGBUF + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_ARENA = (BPF_MAP_TYPE_CGRP_STORAGE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

BPF_MAP_TYPE_INSN_ARRAY = (BPF_MAP_TYPE_ARENA + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

__MAX_BPF_MAP_TYPE = (BPF_MAP_TYPE_INSN_ARRAY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 991

enum_bpf_prog_type = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_UNSPEC = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SOCKET_FILTER = (BPF_PROG_TYPE_UNSPEC + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_KPROBE = (BPF_PROG_TYPE_SOCKET_FILTER + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SCHED_CLS = (BPF_PROG_TYPE_KPROBE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SCHED_ACT = (BPF_PROG_TYPE_SCHED_CLS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_TRACEPOINT = (BPF_PROG_TYPE_SCHED_ACT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_XDP = (BPF_PROG_TYPE_TRACEPOINT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_PERF_EVENT = (BPF_PROG_TYPE_XDP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_CGROUP_SKB = (BPF_PROG_TYPE_PERF_EVENT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_CGROUP_SOCK = (BPF_PROG_TYPE_CGROUP_SKB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_LWT_IN = (BPF_PROG_TYPE_CGROUP_SOCK + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_LWT_OUT = (BPF_PROG_TYPE_LWT_IN + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_LWT_XMIT = (BPF_PROG_TYPE_LWT_OUT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SOCK_OPS = (BPF_PROG_TYPE_LWT_XMIT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SK_SKB = (BPF_PROG_TYPE_SOCK_OPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_CGROUP_DEVICE = (BPF_PROG_TYPE_SK_SKB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SK_MSG = (BPF_PROG_TYPE_CGROUP_DEVICE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_RAW_TRACEPOINT = (BPF_PROG_TYPE_SK_MSG + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_CGROUP_SOCK_ADDR = (BPF_PROG_TYPE_RAW_TRACEPOINT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_LWT_SEG6LOCAL = (BPF_PROG_TYPE_CGROUP_SOCK_ADDR + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_LIRC_MODE2 = (BPF_PROG_TYPE_LWT_SEG6LOCAL + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SK_REUSEPORT = (BPF_PROG_TYPE_LIRC_MODE2 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_FLOW_DISSECTOR = (BPF_PROG_TYPE_SK_REUSEPORT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_CGROUP_SYSCTL = (BPF_PROG_TYPE_FLOW_DISSECTOR + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_RAW_TRACEPOINT_WRITABLE = (BPF_PROG_TYPE_CGROUP_SYSCTL + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_CGROUP_SOCKOPT = (BPF_PROG_TYPE_RAW_TRACEPOINT_WRITABLE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_TRACING = (BPF_PROG_TYPE_CGROUP_SOCKOPT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_STRUCT_OPS = (BPF_PROG_TYPE_TRACING + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_EXT = (BPF_PROG_TYPE_STRUCT_OPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_LSM = (BPF_PROG_TYPE_EXT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SK_LOOKUP = (BPF_PROG_TYPE_LSM + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_SYSCALL = (BPF_PROG_TYPE_SK_LOOKUP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

BPF_PROG_TYPE_NETFILTER = (BPF_PROG_TYPE_SYSCALL + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

__MAX_BPF_PROG_TYPE = (BPF_PROG_TYPE_NETFILTER + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1052

enum_bpf_attach_type = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET_INGRESS = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET_EGRESS = (BPF_CGROUP_INET_INGRESS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET_SOCK_CREATE = (BPF_CGROUP_INET_EGRESS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_SOCK_OPS = (BPF_CGROUP_INET_SOCK_CREATE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_SK_SKB_STREAM_PARSER = (BPF_CGROUP_SOCK_OPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_SK_SKB_STREAM_VERDICT = (BPF_SK_SKB_STREAM_PARSER + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_DEVICE = (BPF_SK_SKB_STREAM_VERDICT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_SK_MSG_VERDICT = (BPF_CGROUP_DEVICE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET4_BIND = (BPF_SK_MSG_VERDICT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET6_BIND = (BPF_CGROUP_INET4_BIND + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET4_CONNECT = (BPF_CGROUP_INET6_BIND + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET6_CONNECT = (BPF_CGROUP_INET4_CONNECT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET4_POST_BIND = (BPF_CGROUP_INET6_CONNECT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET6_POST_BIND = (BPF_CGROUP_INET4_POST_BIND + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UDP4_SENDMSG = (BPF_CGROUP_INET6_POST_BIND + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UDP6_SENDMSG = (BPF_CGROUP_UDP4_SENDMSG + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_LIRC_MODE2 = (BPF_CGROUP_UDP6_SENDMSG + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_FLOW_DISSECTOR = (BPF_LIRC_MODE2 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_SYSCTL = (BPF_FLOW_DISSECTOR + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UDP4_RECVMSG = (BPF_CGROUP_SYSCTL + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UDP6_RECVMSG = (BPF_CGROUP_UDP4_RECVMSG + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_GETSOCKOPT = (BPF_CGROUP_UDP6_RECVMSG + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_SETSOCKOPT = (BPF_CGROUP_GETSOCKOPT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_RAW_TP = (BPF_CGROUP_SETSOCKOPT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_FENTRY = (BPF_TRACE_RAW_TP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_FEXIT = (BPF_TRACE_FENTRY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_MODIFY_RETURN = (BPF_TRACE_FEXIT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_LSM_MAC = (BPF_MODIFY_RETURN + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_ITER = (BPF_LSM_MAC + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET4_GETPEERNAME = (BPF_TRACE_ITER + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET6_GETPEERNAME = (BPF_CGROUP_INET4_GETPEERNAME + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET4_GETSOCKNAME = (BPF_CGROUP_INET6_GETPEERNAME + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET6_GETSOCKNAME = (BPF_CGROUP_INET4_GETSOCKNAME + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_XDP_DEVMAP = (BPF_CGROUP_INET6_GETSOCKNAME + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_INET_SOCK_RELEASE = (BPF_XDP_DEVMAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_XDP_CPUMAP = (BPF_CGROUP_INET_SOCK_RELEASE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_SK_LOOKUP = (BPF_XDP_CPUMAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_XDP = (BPF_SK_LOOKUP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_SK_SKB_VERDICT = (BPF_XDP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_SK_REUSEPORT_SELECT = (BPF_SK_SKB_VERDICT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_SK_REUSEPORT_SELECT_OR_MIGRATE = (BPF_SK_REUSEPORT_SELECT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_PERF_EVENT = (BPF_SK_REUSEPORT_SELECT_OR_MIGRATE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_KPROBE_MULTI = (BPF_PERF_EVENT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_LSM_CGROUP = (BPF_TRACE_KPROBE_MULTI + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_STRUCT_OPS = (BPF_LSM_CGROUP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_NETFILTER = (BPF_STRUCT_OPS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TCX_INGRESS = (BPF_NETFILTER + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TCX_EGRESS = (BPF_TCX_INGRESS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_UPROBE_MULTI = (BPF_TCX_EGRESS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UNIX_CONNECT = (BPF_TRACE_UPROBE_MULTI + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UNIX_SENDMSG = (BPF_CGROUP_UNIX_CONNECT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UNIX_RECVMSG = (BPF_CGROUP_UNIX_SENDMSG + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UNIX_GETPEERNAME = (BPF_CGROUP_UNIX_RECVMSG + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_CGROUP_UNIX_GETSOCKNAME = (BPF_CGROUP_UNIX_GETPEERNAME + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_NETKIT_PRIMARY = (BPF_CGROUP_UNIX_GETSOCKNAME + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_NETKIT_PEER = (BPF_NETKIT_PRIMARY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_KPROBE_SESSION = (BPF_NETKIT_PEER + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

BPF_TRACE_UPROBE_SESSION = (BPF_TRACE_KPROBE_SESSION + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

__MAX_BPF_ATTACH_TYPE = (BPF_TRACE_UPROBE_SESSION + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1089

enum_bpf_link_type = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_UNSPEC = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_RAW_TRACEPOINT = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_TRACING = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_CGROUP = 3# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_ITER = 4# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_NETNS = 5# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_XDP = 6# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_PERF_EVENT = 7# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_KPROBE_MULTI = 8# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_STRUCT_OPS = 9# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_NETFILTER = 10# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_TCX = 11# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_UPROBE_MULTI = 12# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_NETKIT = 13# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

BPF_LINK_TYPE_SOCKMAP = 14# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

__MAX_BPF_LINK_TYPE = (BPF_LINK_TYPE_SOCKMAP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1156

enum_bpf_perf_event_type = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

BPF_PERF_EVENT_UNSPEC = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

BPF_PERF_EVENT_UPROBE = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

BPF_PERF_EVENT_URETPROBE = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

BPF_PERF_EVENT_KPROBE = 3# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

BPF_PERF_EVENT_KRETPROBE = 4# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

BPF_PERF_EVENT_TRACEPOINT = 5# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

BPF_PERF_EVENT_EVENT = 6# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1177

enum_anon_8 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1307

BPF_F_KPROBE_MULTI_RETURN = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1307

enum_anon_9 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1314

BPF_F_UPROBE_MULTI_RETURN = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1314

enum_bpf_addr_space_cast = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1377

BPF_ADDR_SPACE_CAST = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1377

enum_anon_10 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1382

BPF_ANY = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1382

BPF_NOEXIST = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1382

BPF_EXIST = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1382

BPF_F_LOCK = 4# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1382

enum_anon_11 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_NO_PREALLOC = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_NO_COMMON_LRU = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_NUMA_NODE = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_RDONLY = (1 << 3)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_WRONLY = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_STACK_BUILD_ID = (1 << 5)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_ZERO_SEED = (1 << 6)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_RDONLY_PROG = (1 << 7)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_WRONLY_PROG = (1 << 8)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_CLONE = (1 << 9)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_MMAPABLE = (1 << 10)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_PRESERVE_ELEMS = (1 << 11)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_INNER_MAP = (1 << 12)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_LINK = (1 << 13)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_PATH_FD = (1 << 14)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_VTYPE_BTF_OBJ_FD = (1 << 15)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_TOKEN_FD = (1 << 16)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_SEGV_ON_FAULT = (1 << 17)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_NO_USER_CONV = (1 << 18)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

BPF_F_RB_OVERWRITE = (1 << 19)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1390

enum_bpf_stats_type = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1468

BPF_STATS_RUN_TIME = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1468

enum_bpf_stack_build_id_status = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1473

BPF_STACK_BUILD_ID_EMPTY = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1473

BPF_STACK_BUILD_ID_VALID = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1473

BPF_STACK_BUILD_ID_IP = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1473

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1486
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    'offset',
    'ip',
]
union_anon_12._fields_ = [
    ('offset', __u64),
    ('ip', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1483
class struct_bpf_stack_build_id(Structure):
    pass

struct_bpf_stack_build_id.__slots__ = [
    'status',
    'build_id',
    'unnamed_bpf_stack_build_id_1',
]
struct_bpf_stack_build_id._anonymous_ = [
    'unnamed_bpf_stack_build_id_1',
]
struct_bpf_stack_build_id._fields_ = [
    ('status', __s32),
    ('build_id', c_ubyte * int(20)),
    ('unnamed_bpf_stack_build_id_1', union_anon_12),
]

enum_anon_13 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1494

BPF_STREAM_STDOUT = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1494

BPF_STREAM_STDERR = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1494

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1500
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'map_type',
    'key_size',
    'value_size',
    'max_entries',
    'map_flags',
    'inner_map_fd',
    'numa_node',
    'map_name',
    'map_ifindex',
    'btf_fd',
    'btf_key_type_id',
    'btf_value_type_id',
    'btf_vmlinux_value_type_id',
    'map_extra',
    'value_type_btf_obj_fd',
    'map_token_fd',
    'excl_prog_hash',
    'excl_prog_hash_size',
]
struct_anon_14._fields_ = [
    ('map_type', __u32),
    ('key_size', __u32),
    ('value_size', __u32),
    ('max_entries', __u32),
    ('map_flags', __u32),
    ('inner_map_fd', __u32),
    ('numa_node', __u32),
    ('map_name', c_char * int(16)),
    ('map_ifindex', __u32),
    ('btf_fd', __u32),
    ('btf_key_type_id', __u32),
    ('btf_value_type_id', __u32),
    ('btf_vmlinux_value_type_id', __u32),
    ('map_extra', __u64),
    ('value_type_btf_obj_fd', __s32),
    ('map_token_fd', __s32),
    ('excl_prog_hash', __u64),
    ('excl_prog_hash_size', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1551
class union_anon_15(Union):
    pass

union_anon_15.__slots__ = [
    'value',
    'next_key',
]
union_anon_15._fields_ = [
    ('value', __u64),
    ('next_key', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1548
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'map_fd',
    'key',
    'unnamed_anon_16_1',
    'flags',
]
struct_anon_16._anonymous_ = [
    'unnamed_anon_16_1',
]
struct_anon_16._fields_ = [
    ('map_fd', __u32),
    ('key', __u64),
    ('unnamed_anon_16_1', union_anon_15),
    ('flags', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1558
class struct_anon_17(Structure):
    pass

struct_anon_17.__slots__ = [
    'in_batch',
    'out_batch',
    'keys',
    'values',
    'count',
    'map_fd',
    'elem_flags',
    'flags',
]
struct_anon_17._fields_ = [
    ('in_batch', __u64),
    ('out_batch', __u64),
    ('keys', __u64),
    ('values', __u64),
    ('count', __u32),
    ('map_fd', __u32),
    ('elem_flags', __u64),
    ('flags', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1600
class union_anon_18(Union):
    pass

union_anon_18.__slots__ = [
    'attach_prog_fd',
    'attach_btf_obj_fd',
]
union_anon_18._fields_ = [
    ('attach_prog_fd', __u32),
    ('attach_btf_obj_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1575
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'prog_type',
    'insn_cnt',
    'insns',
    'license',
    'log_level',
    'log_size',
    'log_buf',
    'kern_version',
    'prog_flags',
    'prog_name',
    'prog_ifindex',
    'expected_attach_type',
    'prog_btf_fd',
    'func_info_rec_size',
    'func_info',
    'func_info_cnt',
    'line_info_rec_size',
    'line_info',
    'line_info_cnt',
    'attach_btf_id',
    'unnamed_anon_19_1',
    'core_relo_cnt',
    'fd_array',
    'core_relos',
    'core_relo_rec_size',
    'log_true_size',
    'prog_token_fd',
    'fd_array_cnt',
    'signature',
    'signature_size',
    'keyring_id',
]
struct_anon_19._anonymous_ = [
    'unnamed_anon_19_1',
]
struct_anon_19._fields_ = [
    ('prog_type', __u32),
    ('insn_cnt', __u32),
    ('insns', __u64),
    ('license', __u64),
    ('log_level', __u32),
    ('log_size', __u32),
    ('log_buf', __u64),
    ('kern_version', __u32),
    ('prog_flags', __u32),
    ('prog_name', c_char * int(16)),
    ('prog_ifindex', __u32),
    ('expected_attach_type', __u32),
    ('prog_btf_fd', __u32),
    ('func_info_rec_size', __u32),
    ('func_info', __u64),
    ('func_info_cnt', __u32),
    ('line_info_rec_size', __u32),
    ('line_info', __u64),
    ('line_info_cnt', __u32),
    ('attach_btf_id', __u32),
    ('unnamed_anon_19_1', union_anon_18),
    ('core_relo_cnt', __u32),
    ('fd_array', __u64),
    ('core_relos', __u64),
    ('core_relo_rec_size', __u32),
    ('log_true_size', __u32),
    ('prog_token_fd', __s32),
    ('fd_array_cnt', __u32),
    ('signature', __u64),
    ('signature_size', __u32),
    ('keyring_id', __s32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1641
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'pathname',
    'bpf_fd',
    'file_flags',
    'path_fd',
]
struct_anon_20._fields_ = [
    ('pathname', __u64),
    ('bpf_fd', __u32),
    ('file_flags', __u32),
    ('path_fd', __s32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1655
class union_anon_21(Union):
    pass

union_anon_21.__slots__ = [
    'target_fd',
    'target_ifindex',
]
union_anon_21._fields_ = [
    ('target_fd', __u32),
    ('target_ifindex', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1663
class union_anon_22(Union):
    pass

union_anon_22.__slots__ = [
    'relative_fd',
    'relative_id',
]
union_anon_22._fields_ = [
    ('relative_fd', __u32),
    ('relative_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1654
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'unnamed_anon_23_1',
    'attach_bpf_fd',
    'attach_type',
    'attach_flags',
    'replace_bpf_fd',
    'unnamed_anon_23_2',
    'expected_revision',
]
struct_anon_23._anonymous_ = [
    'unnamed_anon_23_1',
    'unnamed_anon_23_2',
]
struct_anon_23._fields_ = [
    ('unnamed_anon_23_1', union_anon_21),
    ('attach_bpf_fd', __u32),
    ('attach_type', __u32),
    ('attach_flags', __u32),
    ('replace_bpf_fd', __u32),
    ('unnamed_anon_23_2', union_anon_22),
    ('expected_revision', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1670
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'prog_fd',
    'retval',
    'data_size_in',
    'data_size_out',
    'data_in',
    'data_out',
    'repeat',
    'duration',
    'ctx_size_in',
    'ctx_size_out',
    'ctx_in',
    'ctx_out',
    'flags',
    'cpu',
    'batch_size',
]
struct_anon_24._fields_ = [
    ('prog_fd', __u32),
    ('retval', __u32),
    ('data_size_in', __u32),
    ('data_size_out', __u32),
    ('data_in', __u64),
    ('data_out', __u64),
    ('repeat', __u32),
    ('duration', __u32),
    ('ctx_size_in', __u32),
    ('ctx_size_out', __u32),
    ('ctx_in', __u64),
    ('ctx_out', __u64),
    ('flags', __u32),
    ('cpu', __u32),
    ('batch_size', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1695
class union_anon_25(Union):
    pass

union_anon_25.__slots__ = [
    'start_id',
    'prog_id',
    'map_id',
    'btf_id',
    'link_id',
]
union_anon_25._fields_ = [
    ('start_id', __u32),
    ('prog_id', __u32),
    ('map_id', __u32),
    ('btf_id', __u32),
    ('link_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1694
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'unnamed_anon_26_1',
    'next_id',
    'open_flags',
    'fd_by_id_token_fd',
]
struct_anon_26._anonymous_ = [
    'unnamed_anon_26_1',
]
struct_anon_26._fields_ = [
    ('unnamed_anon_26_1', union_anon_25),
    ('next_id', __u32),
    ('open_flags', __u32),
    ('fd_by_id_token_fd', __s32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1707
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'bpf_fd',
    'info_len',
    'info',
]
struct_anon_27._fields_ = [
    ('bpf_fd', __u32),
    ('info_len', __u32),
    ('info', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1714
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'target_fd',
    'target_ifindex',
]
union_anon_28._fields_ = [
    ('target_fd', __u32),
    ('target_ifindex', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1722
class union_anon_29(Union):
    pass

union_anon_29.__slots__ = [
    'prog_cnt',
    'count',
]
union_anon_29._fields_ = [
    ('prog_cnt', __u32),
    ('count', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1713
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'unnamed_anon_30_1',
    'attach_type',
    'query_flags',
    'attach_flags',
    'prog_ids',
    'unnamed_anon_30_2',
    'unnamed_anon_30_3',
    'prog_attach_flags',
    'link_ids',
    'link_attach_flags',
    'revision',
]
struct_anon_30._anonymous_ = [
    'unnamed_anon_30_1',
    'unnamed_anon_30_2',
]
struct_anon_30._fields_ = [
    ('unnamed_anon_30_1', union_anon_28),
    ('attach_type', __u32),
    ('query_flags', __u32),
    ('attach_flags', __u32),
    ('prog_ids', __u64),
    ('unnamed_anon_30_2', union_anon_29),
    ('unnamed_anon_30_3', __u32, 32),
    ('prog_attach_flags', __u64),
    ('link_ids', __u64),
    ('link_attach_flags', __u64),
    ('revision', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1736
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'name',
    'prog_fd',
    'unnamed_anon_31_1',
    'cookie',
]
struct_anon_31._fields_ = [
    ('name', __u64),
    ('prog_fd', __u32),
    ('unnamed_anon_31_1', __u32, 32),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1743
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'btf',
    'btf_log_buf',
    'btf_size',
    'btf_log_size',
    'btf_log_level',
    'btf_log_true_size',
    'btf_flags',
    'btf_token_fd',
]
struct_anon_32._fields_ = [
    ('btf', __u64),
    ('btf_log_buf', __u64),
    ('btf_size', __u32),
    ('btf_log_size', __u32),
    ('btf_log_level', __u32),
    ('btf_log_true_size', __u32),
    ('btf_flags', __u32),
    ('btf_token_fd', __s32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1761
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'pid',
    'fd',
    'flags',
    'buf_len',
    'buf',
    'prog_id',
    'fd_type',
    'probe_offset',
    'probe_addr',
]
struct_anon_33._fields_ = [
    ('pid', __u32),
    ('fd', __u32),
    ('flags', __u32),
    ('buf_len', __u32),
    ('buf', __u64),
    ('prog_id', __u32),
    ('fd_type', __u32),
    ('probe_offset', __u64),
    ('probe_addr', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1778
class union_anon_34(Union):
    pass

union_anon_34.__slots__ = [
    'prog_fd',
    'map_fd',
]
union_anon_34._fields_ = [
    ('prog_fd', __u32),
    ('map_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1782
class union_anon_35(Union):
    pass

union_anon_35.__slots__ = [
    'target_fd',
    'target_ifindex',
]
union_anon_35._fields_ = [
    ('target_fd', __u32),
    ('target_ifindex', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1790
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'iter_info',
    'iter_info_len',
]
struct_anon_36._fields_ = [
    ('iter_info', __u64),
    ('iter_info_len', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1794
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'bpf_cookie',
]
struct_anon_37._fields_ = [
    ('bpf_cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1801
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'flags',
    'cnt',
    'syms',
    'addrs',
    'cookies',
]
struct_anon_38._fields_ = [
    ('flags', __u32),
    ('cnt', __u32),
    ('syms', __u64),
    ('addrs', __u64),
    ('cookies', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1808
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'target_btf_id',
    'cookie',
]
struct_anon_39._fields_ = [
    ('target_btf_id', __u32),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1817
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'pf',
    'hooknum',
    'priority',
    'flags',
]
struct_anon_40._fields_ = [
    ('pf', __u32),
    ('hooknum', __u32),
    ('priority', __s32),
    ('flags', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1824
class union_anon_41(Union):
    pass

union_anon_41.__slots__ = [
    'relative_fd',
    'relative_id',
]
union_anon_41._fields_ = [
    ('relative_fd', __u32),
    ('relative_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1823
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'unnamed_anon_42_1',
    'expected_revision',
]
struct_anon_42._anonymous_ = [
    'unnamed_anon_42_1',
]
struct_anon_42._fields_ = [
    ('unnamed_anon_42_1', union_anon_41),
    ('expected_revision', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1830
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'path',
    'offsets',
    'ref_ctr_offsets',
    'cookies',
    'cnt',
    'flags',
    'pid',
]
struct_anon_43._fields_ = [
    ('path', __u64),
    ('offsets', __u64),
    ('ref_ctr_offsets', __u64),
    ('cookies', __u64),
    ('cnt', __u32),
    ('flags', __u32),
    ('pid', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1840
class union_anon_44(Union):
    pass

union_anon_44.__slots__ = [
    'relative_fd',
    'relative_id',
]
union_anon_44._fields_ = [
    ('relative_fd', __u32),
    ('relative_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1839
class struct_anon_45(Structure):
    pass

struct_anon_45.__slots__ = [
    'unnamed_anon_45_1',
    'expected_revision',
]
struct_anon_45._anonymous_ = [
    'unnamed_anon_45_1',
]
struct_anon_45._fields_ = [
    ('unnamed_anon_45_1', union_anon_44),
    ('expected_revision', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1847
class union_anon_46(Union):
    pass

union_anon_46.__slots__ = [
    'relative_fd',
    'relative_id',
]
union_anon_46._fields_ = [
    ('relative_fd', __u32),
    ('relative_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1846
class struct_anon_47(Structure):
    pass

struct_anon_47.__slots__ = [
    'unnamed_anon_47_1',
    'expected_revision',
]
struct_anon_47._anonymous_ = [
    'unnamed_anon_47_1',
]
struct_anon_47._fields_ = [
    ('unnamed_anon_47_1', union_anon_46),
    ('expected_revision', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1788
class union_anon_48(Union):
    pass

union_anon_48.__slots__ = [
    'target_btf_id',
    'unnamed_anon_48_1',
    'perf_event',
    'kprobe_multi',
    'tracing',
    'netfilter',
    'tcx',
    'uprobe_multi',
    'netkit',
    'cgroup',
]
union_anon_48._anonymous_ = [
    'unnamed_anon_48_1',
]
union_anon_48._fields_ = [
    ('target_btf_id', __u32),
    ('unnamed_anon_48_1', struct_anon_36),
    ('perf_event', struct_anon_37),
    ('kprobe_multi', struct_anon_38),
    ('tracing', struct_anon_39),
    ('netfilter', struct_anon_40),
    ('tcx', struct_anon_42),
    ('uprobe_multi', struct_anon_43),
    ('netkit', struct_anon_45),
    ('cgroup', struct_anon_47),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1777
class struct_anon_49(Structure):
    pass

struct_anon_49.__slots__ = [
    'unnamed_anon_49_1',
    'unnamed_anon_49_2',
    'attach_type',
    'flags',
    'unnamed_anon_49_3',
]
struct_anon_49._anonymous_ = [
    'unnamed_anon_49_1',
    'unnamed_anon_49_2',
    'unnamed_anon_49_3',
]
struct_anon_49._fields_ = [
    ('unnamed_anon_49_1', union_anon_34),
    ('unnamed_anon_49_2', union_anon_35),
    ('attach_type', __u32),
    ('flags', __u32),
    ('unnamed_anon_49_3', union_anon_48),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1858
class union_anon_50(Union):
    pass

union_anon_50.__slots__ = [
    'new_prog_fd',
    'new_map_fd',
]
union_anon_50._fields_ = [
    ('new_prog_fd', __u32),
    ('new_map_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1865
class union_anon_51(Union):
    pass

union_anon_51.__slots__ = [
    'old_prog_fd',
    'old_map_fd',
]
union_anon_51._fields_ = [
    ('old_prog_fd', __u32),
    ('old_map_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1856
class struct_anon_52(Structure):
    pass

struct_anon_52.__slots__ = [
    'link_fd',
    'unnamed_anon_52_1',
    'flags',
    'unnamed_anon_52_2',
]
struct_anon_52._anonymous_ = [
    'unnamed_anon_52_1',
    'unnamed_anon_52_2',
]
struct_anon_52._fields_ = [
    ('link_fd', __u32),
    ('unnamed_anon_52_1', union_anon_50),
    ('flags', __u32),
    ('unnamed_anon_52_2', union_anon_51),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1877
class struct_anon_53(Structure):
    pass

struct_anon_53.__slots__ = [
    'link_fd',
]
struct_anon_53._fields_ = [
    ('link_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1881
class struct_anon_54(Structure):
    pass

struct_anon_54.__slots__ = [
    'type',
]
struct_anon_54._fields_ = [
    ('type', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1885
class struct_anon_55(Structure):
    pass

struct_anon_55.__slots__ = [
    'link_fd',
    'flags',
]
struct_anon_55._fields_ = [
    ('link_fd', __u32),
    ('flags', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1890
class struct_anon_56(Structure):
    pass

struct_anon_56.__slots__ = [
    'prog_fd',
    'map_fd',
    'flags',
]
struct_anon_56._fields_ = [
    ('prog_fd', __u32),
    ('map_fd', __u32),
    ('flags', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1896
class struct_anon_57(Structure):
    pass

struct_anon_57.__slots__ = [
    'flags',
    'bpffs_fd',
]
struct_anon_57._fields_ = [
    ('flags', __u32),
    ('bpffs_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1901
class struct_anon_58(Structure):
    pass

struct_anon_58.__slots__ = [
    'stream_buf',
    'stream_buf_len',
    'stream_id',
    'prog_fd',
]
struct_anon_58._fields_ = [
    ('stream_buf', __u64),
    ('stream_buf_len', __u32),
    ('stream_id', __u32),
    ('prog_fd', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1908
class struct_anon_59(Structure):
    pass

struct_anon_59.__slots__ = [
    'map_fd',
    'prog_fd',
    'flags',
]
struct_anon_59._fields_ = [
    ('map_fd', __u32),
    ('prog_fd', __u32),
    ('flags', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1499
class union_bpf_attr(Union):
    pass

union_bpf_attr.__slots__ = [
    'unnamed_bpf_attr_1',
    'unnamed_bpf_attr_2',
    'batch',
    'unnamed_bpf_attr_3',
    'unnamed_bpf_attr_4',
    'unnamed_bpf_attr_5',
    'test',
    'unnamed_bpf_attr_6',
    'info',
    'query',
    'raw_tracepoint',
    'unnamed_bpf_attr_7',
    'task_fd_query',
    'link_create',
    'link_update',
    'link_detach',
    'enable_stats',
    'iter_create',
    'prog_bind_map',
    'token_create',
    'prog_stream_read',
    'prog_assoc_struct_ops',
]
union_bpf_attr._anonymous_ = [
    'unnamed_bpf_attr_1',
    'unnamed_bpf_attr_2',
    'unnamed_bpf_attr_3',
    'unnamed_bpf_attr_4',
    'unnamed_bpf_attr_5',
    'unnamed_bpf_attr_6',
    'unnamed_bpf_attr_7',
]
union_bpf_attr._fields_ = [
    ('unnamed_bpf_attr_1', struct_anon_14),
    ('unnamed_bpf_attr_2', struct_anon_16),
    ('batch', struct_anon_17),
    ('unnamed_bpf_attr_3', struct_anon_19),
    ('unnamed_bpf_attr_4', struct_anon_20),
    ('unnamed_bpf_attr_5', struct_anon_23),
    ('test', struct_anon_24),
    ('unnamed_bpf_attr_6', struct_anon_26),
    ('info', struct_anon_27),
    ('query', struct_anon_30),
    ('raw_tracepoint', struct_anon_31),
    ('unnamed_bpf_attr_7', struct_anon_32),
    ('task_fd_query', struct_anon_33),
    ('link_create', struct_anon_49),
    ('link_update', struct_anon_52),
    ('link_detach', struct_anon_53),
    ('enable_stats', struct_anon_54),
    ('iter_create', struct_anon_55),
    ('prog_bind_map', struct_anon_56),
    ('token_create', struct_anon_57),
    ('prog_stream_read', struct_anon_58),
    ('prog_assoc_struct_ops', struct_anon_59),
]

enum_bpf_func_id = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_unspec = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_map_lookup_elem = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_map_update_elem = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_map_delete_elem = 3# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_probe_read = 4# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ktime_get_ns = 5# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_trace_printk = 6# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_prandom_u32 = 7# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_smp_processor_id = 8# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_store_bytes = 9# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_l3_csum_replace = 10# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_l4_csum_replace = 11# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tail_call = 12# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_clone_redirect = 13# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_current_pid_tgid = 14# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_current_uid_gid = 15# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_current_comm = 16# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_cgroup_classid = 17# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_vlan_push = 18# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_vlan_pop = 19# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_get_tunnel_key = 20# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_set_tunnel_key = 21# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_perf_event_read = 22# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_redirect = 23# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_route_realm = 24# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_perf_event_output = 25# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_load_bytes = 26# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_stackid = 27# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_csum_diff = 28# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_get_tunnel_opt = 29# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_set_tunnel_opt = 30# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_change_proto = 31# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_change_type = 32# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_under_cgroup = 33# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_hash_recalc = 34# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_current_task = 35# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_probe_write_user = 36# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_current_task_under_cgroup = 37# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_change_tail = 38# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_pull_data = 39# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_csum_update = 40# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_set_hash_invalid = 41# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_numa_node_id = 42# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_change_head = 43# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_xdp_adjust_head = 44# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_probe_read_str = 45# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_socket_cookie = 46# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_socket_uid = 47# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_set_hash = 48# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_setsockopt = 49# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_adjust_room = 50# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_redirect_map = 51# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_redirect_map = 52# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sock_map_update = 53# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_xdp_adjust_meta = 54# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_perf_event_read_value = 55# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_perf_prog_read_value = 56# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_getsockopt = 57# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_override_return = 58# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sock_ops_cb_flags_set = 59# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_msg_redirect_map = 60# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_msg_apply_bytes = 61# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_msg_cork_bytes = 62# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_msg_pull_data = 63# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_bind = 64# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_xdp_adjust_tail = 65# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_get_xfrm_state = 66# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_stack = 67# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_load_bytes_relative = 68# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_fib_lookup = 69# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sock_hash_update = 70# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_msg_redirect_hash = 71# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_redirect_hash = 72# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_lwt_push_encap = 73# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_lwt_seg6_store_bytes = 74# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_lwt_seg6_adjust_srh = 75# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_lwt_seg6_action = 76# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_rc_repeat = 77# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_rc_keydown = 78# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_cgroup_id = 79# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_current_cgroup_id = 80# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_local_storage = 81# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_select_reuseport = 82# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_ancestor_cgroup_id = 83# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_lookup_tcp = 84# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_lookup_udp = 85# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_release = 86# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_map_push_elem = 87# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_map_pop_elem = 88# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_map_peek_elem = 89# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_msg_push_data = 90# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_msg_pop_data = 91# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_rc_pointer_rel = 92# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_spin_lock = 93# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_spin_unlock = 94# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_fullsock = 95# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_sock = 96# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_ecn_set_ce = 97# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_listener_sock = 98# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_lookup_tcp = 99# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_check_syncookie = 100# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sysctl_get_name = 101# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sysctl_get_current_value = 102# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sysctl_get_new_value = 103# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sysctl_set_new_value = 104# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_strtol = 105# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_strtoul = 106# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_storage_get = 107# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_storage_delete = 108# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_send_signal = 109# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_gen_syncookie = 110# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_output = 111# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_probe_read_user = 112# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_probe_read_kernel = 113# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_probe_read_user_str = 114# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_probe_read_kernel_str = 115# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_send_ack = 116# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_send_signal_thread = 117# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_jiffies64 = 118# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_read_branch_records = 119# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_ns_current_pid_tgid = 120# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_xdp_output = 121# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_netns_cookie = 122# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_current_ancestor_cgroup_id = 123# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_assign = 124# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ktime_get_boot_ns = 125# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_seq_printf = 126# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_seq_write = 127# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_cgroup_id = 128# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sk_ancestor_cgroup_id = 129# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_output = 130# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_reserve = 131# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_submit = 132# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_discard = 133# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_query = 134# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_csum_level = 135# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_to_tcp6_sock = 136# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_to_tcp_sock = 137# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_to_tcp_timewait_sock = 138# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_to_tcp_request_sock = 139# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_to_udp6_sock = 140# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_task_stack = 141# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_load_hdr_opt = 142# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_store_hdr_opt = 143# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_reserve_hdr_opt = 144# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_inode_storage_get = 145# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_inode_storage_delete = 146# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_d_path = 147# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_copy_from_user = 148# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_snprintf_btf = 149# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_seq_printf_btf = 150# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_cgroup_classid = 151# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_redirect_neigh = 152# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_per_cpu_ptr = 153# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_this_cpu_ptr = 154# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_redirect_peer = 155# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_task_storage_get = 156# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_task_storage_delete = 157# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_current_task_btf = 158# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_bprm_opts_set = 159# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ktime_get_coarse_ns = 160# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ima_inode_hash = 161# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sock_from_file = 162# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_check_mtu = 163# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_for_each_map_elem = 164# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_snprintf = 165# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sys_bpf = 166# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_btf_find_by_name_kind = 167# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_sys_close = 168# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_timer_init = 169# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_timer_set_callback = 170# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_timer_start = 171# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_timer_cancel = 172# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_func_ip = 173# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_attach_cookie = 174# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_task_pt_regs = 175# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_branch_snapshot = 176# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_trace_vprintk = 177# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_to_unix_sock = 178# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_kallsyms_lookup_name = 179# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_find_vma = 180# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_loop = 181# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_strncmp = 182# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_func_arg = 183# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_func_ret = 184# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_func_arg_cnt = 185# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_get_retval = 186# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_set_retval = 187# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_xdp_get_buff_len = 188# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_xdp_load_bytes = 189# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_xdp_store_bytes = 190# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_copy_from_user_task = 191# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skb_set_tstamp = 192# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ima_file_hash = 193# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_kptr_xchg = 194# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_map_lookup_percpu_elem = 195# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_skc_to_mptcp_sock = 196# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_dynptr_from_mem = 197# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_reserve_dynptr = 198# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_submit_dynptr = 199# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ringbuf_discard_dynptr = 200# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_dynptr_read = 201# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_dynptr_write = 202# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_dynptr_data = 203# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_raw_gen_syncookie_ipv4 = 204# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_raw_gen_syncookie_ipv6 = 205# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_raw_check_syncookie_ipv4 = 206# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_tcp_raw_check_syncookie_ipv6 = 207# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_ktime_get_tai_ns = 208# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_user_ringbuf_drain = 209# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_cgrp_storage_get = 210# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

BPF_FUNC_cgrp_storage_delete = 211# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

__BPF_FUNC_MAX_ID = (BPF_FUNC_cgrp_storage_delete + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6119

enum_anon_60 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6128

BPF_F_RECOMPUTE_CSUM = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6128

BPF_F_INVALIDATE_HASH = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6128

enum_anon_61 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6136

BPF_F_HDR_FIELD_MASK = 0xf# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6136

enum_anon_62 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6141

BPF_F_PSEUDO_HDR = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6141

BPF_F_MARK_MANGLED_0 = (1 << 5)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6141

BPF_F_MARK_ENFORCE = (1 << 6)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6141

BPF_F_IPV6 = (1 << 7)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6141

enum_anon_63 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6149

BPF_F_TUNINFO_IPV6 = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6149

enum_anon_64 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6154

BPF_F_SKIP_FIELD_MASK = 0xff# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6154

BPF_F_USER_STACK = (1 << 8)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6154

BPF_F_FAST_STACK_CMP = (1 << 9)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6154

BPF_F_REUSE_STACKID = (1 << 10)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6154

BPF_F_USER_BUILD_ID = (1 << 11)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6154

enum_anon_65 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6165

BPF_F_ZERO_CSUM_TX = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6165

BPF_F_DONT_FRAGMENT = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6165

BPF_F_SEQ_NUMBER = (1 << 3)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6165

BPF_F_NO_TUNNEL_KEY = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6165

enum_anon_66 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6173

BPF_F_TUNINFO_FLAGS = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6173

enum_anon_67 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6180

BPF_F_INDEX_MASK = 0xffffffff# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6180

BPF_F_CURRENT_CPU = BPF_F_INDEX_MASK# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6180

BPF_F_CTXLEN_MASK = (0xfffff << 32)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6180

enum_anon_68 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6188

BPF_F_CURRENT_NETNS = (-1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6188

enum_anon_69 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6193

BPF_CSUM_LEVEL_QUERY = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6193

BPF_CSUM_LEVEL_INC = (BPF_CSUM_LEVEL_QUERY + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6193

BPF_CSUM_LEVEL_DEC = (BPF_CSUM_LEVEL_INC + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6193

BPF_CSUM_LEVEL_RESET = (BPF_CSUM_LEVEL_DEC + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6193

enum_anon_70 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_FIXED_GSO = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_ENCAP_L3_IPV4 = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_ENCAP_L3_IPV6 = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_ENCAP_L4_GRE = (1 << 3)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_ENCAP_L4_UDP = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_NO_CSUM_RESET = (1 << 5)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_ENCAP_L2_ETH = (1 << 6)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_DECAP_L3_IPV4 = (1 << 7)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

BPF_F_ADJ_ROOM_DECAP_L3_IPV6 = (1 << 8)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6201

enum_anon_71 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6213

BPF_ADJ_ROOM_ENCAP_L2_MASK = 0xff# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6213

BPF_ADJ_ROOM_ENCAP_L2_SHIFT = 56# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6213

enum_anon_72 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6223

BPF_F_SYSCTL_BASE_NAME = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6223

enum_anon_73 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6228

BPF_LOCAL_STORAGE_GET_F_CREATE = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6228

BPF_SK_STORAGE_GET_F_CREATE = BPF_LOCAL_STORAGE_GET_F_CREATE# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6228

enum_anon_74 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6237

BPF_F_GET_BRANCH_RECORDS_SIZE = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6237

enum_anon_75 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6244

BPF_RB_NO_WAKEUP = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6244

BPF_RB_FORCE_WAKEUP = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6244

enum_anon_76 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6250

BPF_RB_AVAIL_DATA = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6250

BPF_RB_RING_SIZE = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6250

BPF_RB_CONS_POS = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6250

BPF_RB_PROD_POS = 3# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6250

BPF_RB_OVERWRITE_POS = 4# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6250

enum_anon_77 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6259

BPF_RINGBUF_BUSY_BIT = (1 << 31)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6259

BPF_RINGBUF_DISCARD_BIT = (1 << 30)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6259

BPF_RINGBUF_HDR_SZ = 8# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6259

enum_anon_78 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6266

BPF_SK_LOOKUP_F_REPLACE = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6266

BPF_SK_LOOKUP_F_NO_REUSEPORT = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6266

enum_bpf_adj_room_mode = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6272

BPF_ADJ_ROOM_NET = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6272

BPF_ADJ_ROOM_MAC = (BPF_ADJ_ROOM_NET + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6272

enum_bpf_hdr_start_off = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6278

BPF_HDR_START_MAC = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6278

BPF_HDR_START_NET = (BPF_HDR_START_MAC + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6278

enum_bpf_lwt_encap_mode = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6284

BPF_LWT_ENCAP_SEG6 = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6284

BPF_LWT_ENCAP_SEG6_INLINE = (BPF_LWT_ENCAP_SEG6 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6284

BPF_LWT_ENCAP_IP = (BPF_LWT_ENCAP_SEG6_INLINE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6284

enum_anon_79 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6291

BPF_F_BPRM_SECUREEXEC = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6291

enum_anon_80 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6296

BPF_F_INGRESS = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6296

BPF_F_BROADCAST = (1 << 3)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6296

BPF_F_EXCLUDE_INGRESS = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6296

enum_anon_81 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6312

BPF_SKB_TSTAMP_UNSPEC = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6312

BPF_SKB_TSTAMP_DELIVERY_MONO = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6312

BPF_SKB_CLOCK_REALTIME = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6312

BPF_SKB_CLOCK_MONOTONIC = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6312

BPF_SKB_CLOCK_TAI = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6312

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7415
class struct_bpf_flow_keys(Structure):
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6357
class union_anon_82(Union):
    pass

union_anon_82.__slots__ = [
    'flow_keys',
    'unnamed_anon_82_1',
]
union_anon_82._fields_ = [
    ('flow_keys', POINTER(struct_bpf_flow_keys)),
    ('unnamed_anon_82_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6430
class struct_bpf_sock(Structure):
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6361
class union_anon_83(Union):
    pass

union_anon_83.__slots__ = [
    'sk',
    'unnamed_anon_83_1',
]
union_anon_83._fields_ = [
    ('sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_83_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6326
class struct___sk_buff(Structure):
    pass

struct___sk_buff.__slots__ = [
    'len',
    'pkt_type',
    'mark',
    'queue_mapping',
    'protocol',
    'vlan_present',
    'vlan_tci',
    'vlan_proto',
    'priority',
    'ingress_ifindex',
    'ifindex',
    'tc_index',
    'cb',
    'hash',
    'tc_classid',
    'data',
    'data_end',
    'napi_id',
    'family',
    'remote_ip4',
    'local_ip4',
    'remote_ip6',
    'local_ip6',
    'remote_port',
    'local_port',
    'data_meta',
    'unnamed___sk_buff_1',
    'tstamp',
    'wire_len',
    'gso_segs',
    'unnamed___sk_buff_2',
    'gso_size',
    'tstamp_type',
    'unnamed___sk_buff_3',
    'hwtstamp',
]
struct___sk_buff._anonymous_ = [
    'unnamed___sk_buff_1',
    'unnamed___sk_buff_2',
]
struct___sk_buff._fields_ = [
    ('len', __u32),
    ('pkt_type', __u32),
    ('mark', __u32),
    ('queue_mapping', __u32),
    ('protocol', __u32),
    ('vlan_present', __u32),
    ('vlan_tci', __u32),
    ('vlan_proto', __u32),
    ('priority', __u32),
    ('ingress_ifindex', __u32),
    ('ifindex', __u32),
    ('tc_index', __u32),
    ('cb', __u32 * int(5)),
    ('hash', __u32),
    ('tc_classid', __u32),
    ('data', __u32),
    ('data_end', __u32),
    ('napi_id', __u32),
    ('family', __u32),
    ('remote_ip4', __u32),
    ('local_ip4', __u32),
    ('remote_ip6', __u32 * int(4)),
    ('local_ip6', __u32 * int(4)),
    ('remote_port', __u32),
    ('local_port', __u32),
    ('data_meta', __u32),
    ('unnamed___sk_buff_1', union_anon_82),
    ('tstamp', __u64),
    ('wire_len', __u32),
    ('gso_segs', __u32),
    ('unnamed___sk_buff_2', union_anon_83),
    ('gso_size', __u32),
    ('tstamp_type', __u8),
    ('unnamed___sk_buff_3', __u32, 24),
    ('hwtstamp', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6370
class union_anon_84(Union):
    pass

union_anon_84.__slots__ = [
    'remote_ipv4',
    'remote_ipv6',
]
union_anon_84._fields_ = [
    ('remote_ipv4', __u32),
    ('remote_ipv6', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6376
class union_anon_85(Union):
    pass

union_anon_85.__slots__ = [
    'tunnel_ext',
    'tunnel_flags',
]
union_anon_85._fields_ = [
    ('tunnel_ext', __u16),
    ('tunnel_flags', __be16),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6381
class union_anon_86(Union):
    pass

union_anon_86.__slots__ = [
    'local_ipv4',
    'local_ipv6',
]
union_anon_86._fields_ = [
    ('local_ipv4', __u32),
    ('local_ipv6', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6368
class struct_bpf_tunnel_key(Structure):
    pass

struct_bpf_tunnel_key.__slots__ = [
    'tunnel_id',
    'unnamed_bpf_tunnel_key_1',
    'tunnel_tos',
    'tunnel_ttl',
    'unnamed_bpf_tunnel_key_2',
    'tunnel_label',
    'unnamed_bpf_tunnel_key_3',
]
struct_bpf_tunnel_key._anonymous_ = [
    'unnamed_bpf_tunnel_key_1',
    'unnamed_bpf_tunnel_key_2',
    'unnamed_bpf_tunnel_key_3',
]
struct_bpf_tunnel_key._fields_ = [
    ('tunnel_id', __u32),
    ('unnamed_bpf_tunnel_key_1', union_anon_84),
    ('tunnel_tos', __u8),
    ('tunnel_ttl', __u8),
    ('unnamed_bpf_tunnel_key_2', union_anon_85),
    ('tunnel_label', __u32),
    ('unnamed_bpf_tunnel_key_3', union_anon_86),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6395
class union_anon_87(Union):
    pass

union_anon_87.__slots__ = [
    'remote_ipv4',
    'remote_ipv6',
]
union_anon_87._fields_ = [
    ('remote_ipv4', __u32),
    ('remote_ipv6', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6390
class struct_bpf_xfrm_state(Structure):
    pass

struct_bpf_xfrm_state.__slots__ = [
    'reqid',
    'spi',
    'family',
    'ext',
    'unnamed_bpf_xfrm_state_1',
]
struct_bpf_xfrm_state._anonymous_ = [
    'unnamed_bpf_xfrm_state_1',
]
struct_bpf_xfrm_state._fields_ = [
    ('reqid', __u32),
    ('spi', __u32),
    ('family', __u16),
    ('ext', __u16),
    ('unnamed_bpf_xfrm_state_1', union_anon_87),
]

enum_bpf_ret_code = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6408

BPF_OK = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6408

BPF_DROP = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6408

BPF_REDIRECT = 7# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6408

BPF_LWT_REROUTE = 128# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6408

BPF_FLOW_DISSECTOR_CONTINUE = 129# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6408

struct_bpf_sock.__slots__ = [
    'bound_dev_if',
    'family',
    'type',
    'protocol',
    'mark',
    'priority',
    'src_ip4',
    'src_ip6',
    'src_port',
    'dst_port',
    'unnamed_bpf_sock_1',
    'dst_ip4',
    'dst_ip6',
    'state',
    'rx_queue_mapping',
]
struct_bpf_sock._fields_ = [
    ('bound_dev_if', __u32),
    ('family', __u32),
    ('type', __u32),
    ('protocol', __u32),
    ('mark', __u32),
    ('priority', __u32),
    ('src_ip4', __u32),
    ('src_ip6', __u32 * int(4)),
    ('src_port', __u32),
    ('dst_port', __be16),
    ('unnamed_bpf_sock_1', __u16, 16),
    ('dst_ip4', __u32),
    ('dst_ip6', __u32 * int(4)),
    ('state', __u32),
    ('rx_queue_mapping', __s32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6449
class struct_bpf_tcp_sock(Structure):
    pass

struct_bpf_tcp_sock.__slots__ = [
    'snd_cwnd',
    'srtt_us',
    'rtt_min',
    'snd_ssthresh',
    'rcv_nxt',
    'snd_nxt',
    'snd_una',
    'mss_cache',
    'ecn_flags',
    'rate_delivered',
    'rate_interval_us',
    'packets_out',
    'retrans_out',
    'total_retrans',
    'segs_in',
    'data_segs_in',
    'segs_out',
    'data_segs_out',
    'lost_out',
    'sacked_out',
    'bytes_received',
    'bytes_acked',
    'dsack_dups',
    'delivered',
    'delivered_ce',
    'icsk_retransmits',
]
struct_bpf_tcp_sock._fields_ = [
    ('snd_cwnd', __u32),
    ('srtt_us', __u32),
    ('rtt_min', __u32),
    ('snd_ssthresh', __u32),
    ('rcv_nxt', __u32),
    ('snd_nxt', __u32),
    ('snd_una', __u32),
    ('mss_cache', __u32),
    ('ecn_flags', __u32),
    ('rate_delivered', __u32),
    ('rate_interval_us', __u32),
    ('packets_out', __u32),
    ('retrans_out', __u32),
    ('total_retrans', __u32),
    ('segs_in', __u32),
    ('data_segs_in', __u32),
    ('segs_out', __u32),
    ('data_segs_out', __u32),
    ('lost_out', __u32),
    ('sacked_out', __u32),
    ('bytes_received', __u64),
    ('bytes_acked', __u64),
    ('dsack_dups', __u32),
    ('delivered', __u32),
    ('delivered_ce', __u32),
    ('icsk_retransmits', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6496
class struct_anon_88(Structure):
    pass

struct_anon_88.__slots__ = [
    'saddr',
    'daddr',
    'sport',
    'dport',
]
struct_anon_88._fields_ = [
    ('saddr', __be32),
    ('daddr', __be32),
    ('sport', __be16),
    ('dport', __be16),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6502
class struct_anon_89(Structure):
    pass

struct_anon_89.__slots__ = [
    'saddr',
    'daddr',
    'sport',
    'dport',
]
struct_anon_89._fields_ = [
    ('saddr', __be32 * int(4)),
    ('daddr', __be32 * int(4)),
    ('sport', __be16),
    ('dport', __be16),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6495
class union_anon_90(Union):
    pass

union_anon_90.__slots__ = [
    'ipv4',
    'ipv6',
]
union_anon_90._fields_ = [
    ('ipv4', struct_anon_88),
    ('ipv6', struct_anon_89),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6494
class struct_bpf_sock_tuple(Structure):
    pass

struct_bpf_sock_tuple.__slots__ = [
    'unnamed_bpf_sock_tuple_1',
]
struct_bpf_sock_tuple._anonymous_ = [
    'unnamed_bpf_sock_tuple_1',
]
struct_bpf_sock_tuple._fields_ = [
    ('unnamed_bpf_sock_tuple_1', union_anon_90),
]

enum_tcx_action_base = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6517

TCX_NEXT = (-1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6517

TCX_PASS = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6517

TCX_DROP = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6517

TCX_REDIRECT = 7# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6517

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6524
class struct_bpf_xdp_sock(Structure):
    pass

struct_bpf_xdp_sock.__slots__ = [
    'queue_id',
]
struct_bpf_xdp_sock._fields_ = [
    ('queue_id', __u32),
]

enum_xdp_action = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6535

XDP_ABORTED = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6535

XDP_DROP = (XDP_ABORTED + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6535

XDP_PASS = (XDP_DROP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6535

XDP_TX = (XDP_PASS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6535

XDP_REDIRECT = (XDP_TX + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6535

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6546
class struct_xdp_md(Structure):
    pass

struct_xdp_md.__slots__ = [
    'data',
    'data_end',
    'data_meta',
    'ingress_ifindex',
    'rx_queue_index',
    'egress_ifindex',
]
struct_xdp_md._fields_ = [
    ('data', __u32),
    ('data_end', __u32),
    ('data_meta', __u32),
    ('ingress_ifindex', __u32),
    ('rx_queue_index', __u32),
    ('egress_ifindex', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6564
class union_anon_91(Union):
    pass

union_anon_91.__slots__ = [
    'fd',
    'id',
]
union_anon_91._fields_ = [
    ('fd', c_int),
    ('id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6562
class struct_bpf_devmap_val(Structure):
    pass

struct_bpf_devmap_val.__slots__ = [
    'ifindex',
    'bpf_prog',
]
struct_bpf_devmap_val._fields_ = [
    ('ifindex', __u32),
    ('bpf_prog', union_anon_91),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6577
class union_anon_92(Union):
    pass

union_anon_92.__slots__ = [
    'fd',
    'id',
]
union_anon_92._fields_ = [
    ('fd', c_int),
    ('id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6575
class struct_bpf_cpumap_val(Structure):
    pass

struct_bpf_cpumap_val.__slots__ = [
    'qsize',
    'bpf_prog',
]
struct_bpf_cpumap_val._fields_ = [
    ('qsize', __u32),
    ('bpf_prog', union_anon_92),
]

enum_sk_action = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6583

SK_DROP = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6583

SK_PASS = (SK_DROP + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6583

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6592
class union_anon_93(Union):
    pass

union_anon_93.__slots__ = [
    'data',
    'unnamed_anon_93_1',
]
union_anon_93._fields_ = [
    ('data', POINTER(None)),
    ('unnamed_anon_93_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6593
class union_anon_94(Union):
    pass

union_anon_94.__slots__ = [
    'data_end',
    'unnamed_anon_94_1',
]
union_anon_94._fields_ = [
    ('data_end', POINTER(None)),
    ('unnamed_anon_94_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6604
class union_anon_95(Union):
    pass

union_anon_95.__slots__ = [
    'sk',
    'unnamed_anon_95_1',
]
union_anon_95._fields_ = [
    ('sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_95_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6591
class struct_sk_msg_md(Structure):
    pass

struct_sk_msg_md.__slots__ = [
    'unnamed_sk_msg_md_1',
    'unnamed_sk_msg_md_2',
    'family',
    'remote_ip4',
    'local_ip4',
    'remote_ip6',
    'local_ip6',
    'remote_port',
    'local_port',
    'size',
    'unnamed_sk_msg_md_3',
]
struct_sk_msg_md._anonymous_ = [
    'unnamed_sk_msg_md_1',
    'unnamed_sk_msg_md_2',
    'unnamed_sk_msg_md_3',
]
struct_sk_msg_md._fields_ = [
    ('unnamed_sk_msg_md_1', union_anon_93),
    ('unnamed_sk_msg_md_2', union_anon_94),
    ('family', __u32),
    ('remote_ip4', __u32),
    ('local_ip4', __u32),
    ('remote_ip6', __u32 * int(4)),
    ('local_ip6', __u32 * int(4)),
    ('remote_port', __u32),
    ('local_port', __u32),
    ('size', __u32),
    ('unnamed_sk_msg_md_3', union_anon_95),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6612
class union_anon_96(Union):
    pass

union_anon_96.__slots__ = [
    'data',
    'unnamed_anon_96_1',
]
union_anon_96._fields_ = [
    ('data', POINTER(None)),
    ('unnamed_anon_96_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6614
class union_anon_97(Union):
    pass

union_anon_97.__slots__ = [
    'data_end',
    'unnamed_anon_97_1',
]
union_anon_97._fields_ = [
    ('data_end', POINTER(None)),
    ('unnamed_anon_97_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6642
class union_anon_98(Union):
    pass

union_anon_98.__slots__ = [
    'sk',
    'unnamed_anon_98_1',
]
union_anon_98._fields_ = [
    ('sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_98_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6643
class union_anon_99(Union):
    pass

union_anon_99.__slots__ = [
    'migrating_sk',
    'unnamed_anon_99_1',
]
union_anon_99._fields_ = [
    ('migrating_sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_99_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6607
class struct_sk_reuseport_md(Structure):
    pass

struct_sk_reuseport_md.__slots__ = [
    'unnamed_sk_reuseport_md_1',
    'unnamed_sk_reuseport_md_2',
    'len',
    'eth_protocol',
    'ip_protocol',
    'bind_inany',
    'hash',
    'unnamed_sk_reuseport_md_3',
    'unnamed_sk_reuseport_md_4',
]
struct_sk_reuseport_md._anonymous_ = [
    'unnamed_sk_reuseport_md_1',
    'unnamed_sk_reuseport_md_2',
    'unnamed_sk_reuseport_md_3',
    'unnamed_sk_reuseport_md_4',
]
struct_sk_reuseport_md._fields_ = [
    ('unnamed_sk_reuseport_md_1', union_anon_96),
    ('unnamed_sk_reuseport_md_2', union_anon_97),
    ('len', __u32),
    ('eth_protocol', __u32),
    ('ip_protocol', __u32),
    ('bind_inany', __u32),
    ('hash', __u32),
    ('unnamed_sk_reuseport_md_3', union_anon_98),
    ('unnamed_sk_reuseport_md_4', union_anon_99),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6648
class struct_bpf_prog_info(Structure):
    pass

struct_bpf_prog_info.__slots__ = [
    'type',
    'id',
    'tag',
    'jited_prog_len',
    'xlated_prog_len',
    'jited_prog_insns',
    'xlated_prog_insns',
    'load_time',
    'created_by_uid',
    'nr_map_ids',
    'map_ids',
    'name',
    'ifindex',
    'gpl_compatible',
    'unnamed_bpf_prog_info_1',
    'netns_dev',
    'netns_ino',
    'nr_jited_ksyms',
    'nr_jited_func_lens',
    'jited_ksyms',
    'jited_func_lens',
    'btf_id',
    'func_info_rec_size',
    'func_info',
    'nr_func_info',
    'nr_line_info',
    'line_info',
    'jited_line_info',
    'nr_jited_line_info',
    'line_info_rec_size',
    'jited_line_info_rec_size',
    'nr_prog_tags',
    'prog_tags',
    'run_time_ns',
    'run_cnt',
    'recursion_misses',
    'verified_insns',
    'attach_btf_obj_id',
    'attach_btf_id',
]
struct_bpf_prog_info._fields_ = [
    ('type', __u32),
    ('id', __u32),
    ('tag', __u8 * int(8)),
    ('jited_prog_len', __u32),
    ('xlated_prog_len', __u32),
    ('jited_prog_insns', __u64),
    ('xlated_prog_insns', __u64),
    ('load_time', __u64),
    ('created_by_uid', __u32),
    ('nr_map_ids', __u32),
    ('map_ids', __u64),
    ('name', c_char * int(16)),
    ('ifindex', __u32),
    ('gpl_compatible', __u32, 1),
    ('unnamed_bpf_prog_info_1', __u32, 31),
    ('netns_dev', __u64),
    ('netns_ino', __u64),
    ('nr_jited_ksyms', __u32),
    ('nr_jited_func_lens', __u32),
    ('jited_ksyms', __u64),
    ('jited_func_lens', __u64),
    ('btf_id', __u32),
    ('func_info_rec_size', __u32),
    ('func_info', __u64),
    ('nr_func_info', __u32),
    ('nr_line_info', __u32),
    ('line_info', __u64),
    ('jited_line_info', __u64),
    ('nr_jited_line_info', __u32),
    ('line_info_rec_size', __u32),
    ('jited_line_info_rec_size', __u32),
    ('nr_prog_tags', __u32),
    ('prog_tags', __u64),
    ('run_time_ns', __u64),
    ('run_cnt', __u64),
    ('recursion_misses', __u64),
    ('verified_insns', __u32),
    ('attach_btf_obj_id', __u32),
    ('attach_btf_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6690
class struct_bpf_map_info(Structure):
    pass

struct_bpf_map_info.__slots__ = [
    'type',
    'id',
    'key_size',
    'value_size',
    'max_entries',
    'map_flags',
    'name',
    'ifindex',
    'btf_vmlinux_value_type_id',
    'netns_dev',
    'netns_ino',
    'btf_id',
    'btf_key_type_id',
    'btf_value_type_id',
    'btf_vmlinux_id',
    'map_extra',
    'hash',
    'hash_size',
]
struct_bpf_map_info._fields_ = [
    ('type', __u32),
    ('id', __u32),
    ('key_size', __u32),
    ('value_size', __u32),
    ('max_entries', __u32),
    ('map_flags', __u32),
    ('name', c_char * int(16)),
    ('ifindex', __u32),
    ('btf_vmlinux_value_type_id', __u32),
    ('netns_dev', __u64),
    ('netns_ino', __u64),
    ('btf_id', __u32),
    ('btf_key_type_id', __u32),
    ('btf_value_type_id', __u32),
    ('btf_vmlinux_id', __u32),
    ('map_extra', __u64),
    ('hash', __u64),
    ('hash_size', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6711
class struct_bpf_btf_info(Structure):
    pass

struct_bpf_btf_info.__slots__ = [
    'btf',
    'btf_size',
    'id',
    'name',
    'name_len',
    'kernel_btf',
]
struct_bpf_btf_info._fields_ = [
    ('btf', __u64),
    ('btf_size', __u32),
    ('id', __u32),
    ('name', __u64),
    ('name_len', __u32),
    ('kernel_btf', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6725
class struct_anon_100(Structure):
    pass

struct_anon_100.__slots__ = [
    'tp_name',
    'tp_name_len',
    'unnamed_anon_100_1',
    'cookie',
]
struct_anon_100._fields_ = [
    ('tp_name', __u64),
    ('tp_name_len', __u32),
    ('unnamed_anon_100_1', __u32, 32),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6731
class struct_anon_101(Structure):
    pass

struct_anon_101.__slots__ = [
    'attach_type',
    'target_obj_id',
    'target_btf_id',
    'unnamed_anon_101_1',
    'cookie',
]
struct_anon_101._fields_ = [
    ('attach_type', __u32),
    ('target_obj_id', __u32),
    ('target_btf_id', __u32),
    ('unnamed_anon_101_1', __u32, 32),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6738
class struct_anon_102(Structure):
    pass

struct_anon_102.__slots__ = [
    'cgroup_id',
    'attach_type',
]
struct_anon_102._fields_ = [
    ('cgroup_id', __u64),
    ('attach_type', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6751
class struct_anon_103(Structure):
    pass

struct_anon_103.__slots__ = [
    'map_id',
]
struct_anon_103._fields_ = [
    ('map_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6750
class union_anon_104(Union):
    pass

union_anon_104.__slots__ = [
    'map',
]
union_anon_104._fields_ = [
    ('map', struct_anon_103),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6756
class struct_anon_105(Structure):
    pass

struct_anon_105.__slots__ = [
    'cgroup_id',
    'order',
]
struct_anon_105._fields_ = [
    ('cgroup_id', __u64),
    ('order', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6760
class struct_anon_106(Structure):
    pass

struct_anon_106.__slots__ = [
    'tid',
    'pid',
]
struct_anon_106._fields_ = [
    ('tid', __u32),
    ('pid', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6755
class union_anon_107(Union):
    pass

union_anon_107.__slots__ = [
    'cgroup',
    'task',
]
union_anon_107._fields_ = [
    ('cgroup', struct_anon_105),
    ('task', struct_anon_106),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6742
class struct_anon_108(Structure):
    pass

struct_anon_108.__slots__ = [
    'target_name',
    'target_name_len',
    'unnamed_anon_108_1',
    'unnamed_anon_108_2',
]
struct_anon_108._anonymous_ = [
    'unnamed_anon_108_1',
    'unnamed_anon_108_2',
]
struct_anon_108._fields_ = [
    ('target_name', __u64),
    ('target_name_len', __u32),
    ('unnamed_anon_108_1', union_anon_104),
    ('unnamed_anon_108_2', union_anon_107),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6766
class struct_anon_109(Structure):
    pass

struct_anon_109.__slots__ = [
    'netns_ino',
    'attach_type',
]
struct_anon_109._fields_ = [
    ('netns_ino', __u32),
    ('attach_type', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6770
class struct_anon_110(Structure):
    pass

struct_anon_110.__slots__ = [
    'ifindex',
]
struct_anon_110._fields_ = [
    ('ifindex', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6773
class struct_anon_111(Structure):
    pass

struct_anon_111.__slots__ = [
    'map_id',
]
struct_anon_111._fields_ = [
    ('map_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6776
class struct_anon_112(Structure):
    pass

struct_anon_112.__slots__ = [
    'pf',
    'hooknum',
    'priority',
    'flags',
]
struct_anon_112._fields_ = [
    ('pf', __u32),
    ('hooknum', __u32),
    ('priority', __s32),
    ('flags', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6782
class struct_anon_113(Structure):
    pass

struct_anon_113.__slots__ = [
    'addrs',
    'count',
    'flags',
    'missed',
    'cookies',
]
struct_anon_113._fields_ = [
    ('addrs', __u64),
    ('count', __u32),
    ('flags', __u32),
    ('missed', __u64),
    ('cookies', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6789
class struct_anon_114(Structure):
    pass

struct_anon_114.__slots__ = [
    'path',
    'offsets',
    'ref_ctr_offsets',
    'cookies',
    'path_size',
    'count',
    'flags',
    'pid',
]
struct_anon_114._fields_ = [
    ('path', __u64),
    ('offsets', __u64),
    ('ref_ctr_offsets', __u64),
    ('cookies', __u64),
    ('path_size', __u32),
    ('count', __u32),
    ('flags', __u32),
    ('pid', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6803
class struct_anon_115(Structure):
    pass

struct_anon_115.__slots__ = [
    'file_name',
    'name_len',
    'offset',
    'cookie',
    'ref_ctr_offset',
]
struct_anon_115._fields_ = [
    ('file_name', __u64),
    ('name_len', __u32),
    ('offset', __u32),
    ('cookie', __u64),
    ('ref_ctr_offset', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6810
class struct_anon_116(Structure):
    pass

struct_anon_116.__slots__ = [
    'func_name',
    'name_len',
    'offset',
    'addr',
    'missed',
    'cookie',
]
struct_anon_116._fields_ = [
    ('func_name', __u64),
    ('name_len', __u32),
    ('offset', __u32),
    ('addr', __u64),
    ('missed', __u64),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6818
class struct_anon_117(Structure):
    pass

struct_anon_117.__slots__ = [
    'tp_name',
    'name_len',
    'unnamed_anon_117_1',
    'cookie',
]
struct_anon_117._fields_ = [
    ('tp_name', __u64),
    ('name_len', __u32),
    ('unnamed_anon_117_1', __u32, 32),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6824
class struct_anon_118(Structure):
    pass

struct_anon_118.__slots__ = [
    'config',
    'type',
    'unnamed_anon_118_1',
    'cookie',
]
struct_anon_118._fields_ = [
    ('config', __u64),
    ('type', __u32),
    ('unnamed_anon_118_1', __u32, 32),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6802
class union_anon_119(Union):
    pass

union_anon_119.__slots__ = [
    'uprobe',
    'kprobe',
    'tracepoint',
    'event',
]
union_anon_119._fields_ = [
    ('uprobe', struct_anon_115),
    ('kprobe', struct_anon_116),
    ('tracepoint', struct_anon_117),
    ('event', struct_anon_118),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6799
class struct_anon_120(Structure):
    pass

struct_anon_120.__slots__ = [
    'type',
    'unnamed_anon_120_1',
    'unnamed_anon_120_2',
]
struct_anon_120._anonymous_ = [
    'unnamed_anon_120_2',
]
struct_anon_120._fields_ = [
    ('type', __u32),
    ('unnamed_anon_120_1', __u32, 32),
    ('unnamed_anon_120_2', union_anon_119),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6832
class struct_anon_121(Structure):
    pass

struct_anon_121.__slots__ = [
    'ifindex',
    'attach_type',
]
struct_anon_121._fields_ = [
    ('ifindex', __u32),
    ('attach_type', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6836
class struct_anon_122(Structure):
    pass

struct_anon_122.__slots__ = [
    'ifindex',
    'attach_type',
]
struct_anon_122._fields_ = [
    ('ifindex', __u32),
    ('attach_type', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6840
class struct_anon_123(Structure):
    pass

struct_anon_123.__slots__ = [
    'map_id',
    'attach_type',
]
struct_anon_123._fields_ = [
    ('map_id', __u32),
    ('attach_type', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6724
class union_anon_124(Union):
    pass

union_anon_124.__slots__ = [
    'raw_tracepoint',
    'tracing',
    'cgroup',
    'iter',
    'netns',
    'xdp',
    'struct_ops',
    'netfilter',
    'kprobe_multi',
    'uprobe_multi',
    'perf_event',
    'tcx',
    'netkit',
    'sockmap',
]
union_anon_124._fields_ = [
    ('raw_tracepoint', struct_anon_100),
    ('tracing', struct_anon_101),
    ('cgroup', struct_anon_102),
    ('iter', struct_anon_108),
    ('netns', struct_anon_109),
    ('xdp', struct_anon_110),
    ('struct_ops', struct_anon_111),
    ('netfilter', struct_anon_112),
    ('kprobe_multi', struct_anon_113),
    ('uprobe_multi', struct_anon_114),
    ('perf_event', struct_anon_120),
    ('tcx', struct_anon_121),
    ('netkit', struct_anon_122),
    ('sockmap', struct_anon_123),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6720
class struct_bpf_link_info(Structure):
    pass

struct_bpf_link_info.__slots__ = [
    'type',
    'id',
    'prog_id',
    'unnamed_bpf_link_info_1',
]
struct_bpf_link_info._anonymous_ = [
    'unnamed_bpf_link_info_1',
]
struct_bpf_link_info._fields_ = [
    ('type', __u32),
    ('id', __u32),
    ('prog_id', __u32),
    ('unnamed_bpf_link_info_1', union_anon_124),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6847
class struct_bpf_token_info(Structure):
    pass

struct_bpf_token_info.__slots__ = [
    'allowed_cmds',
    'allowed_maps',
    'allowed_progs',
    'allowed_attachs',
]
struct_bpf_token_info._fields_ = [
    ('allowed_cmds', __u64),
    ('allowed_maps', __u64),
    ('allowed_progs', __u64),
    ('allowed_attachs', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6878
class union_anon_125(Union):
    pass

union_anon_125.__slots__ = [
    'sk',
    'unnamed_anon_125_1',
]
union_anon_125._fields_ = [
    ('sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_125_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6858
class struct_bpf_sock_addr(Structure):
    pass

struct_bpf_sock_addr.__slots__ = [
    'user_family',
    'user_ip4',
    'user_ip6',
    'user_port',
    'family',
    'type',
    'protocol',
    'msg_src_ip4',
    'msg_src_ip6',
    'unnamed_bpf_sock_addr_1',
]
struct_bpf_sock_addr._anonymous_ = [
    'unnamed_bpf_sock_addr_1',
]
struct_bpf_sock_addr._fields_ = [
    ('user_family', __u32),
    ('user_ip4', __u32),
    ('user_ip6', __u32 * int(4)),
    ('user_port', __u32),
    ('family', __u32),
    ('type', __u32),
    ('protocol', __u32),
    ('msg_src_ip4', __u32),
    ('msg_src_ip6', __u32 * int(4)),
    ('unnamed_bpf_sock_addr_1', union_anon_125),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6889
class union_anon_126(Union):
    pass

union_anon_126.__slots__ = [
    'args',
    'reply',
    'replylong',
]
union_anon_126._fields_ = [
    ('args', __u32 * int(4)),
    ('reply', __u32),
    ('replylong', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6930
class union_anon_127(Union):
    pass

union_anon_127.__slots__ = [
    'sk',
    'unnamed_anon_127_1',
]
union_anon_127._fields_ = [
    ('sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_127_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6945
class union_anon_128(Union):
    pass

union_anon_128.__slots__ = [
    'skb_data',
    'unnamed_anon_128_1',
]
union_anon_128._fields_ = [
    ('skb_data', POINTER(None)),
    ('unnamed_anon_128_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6946
class union_anon_129(Union):
    pass

union_anon_129.__slots__ = [
    'skb_data_end',
    'unnamed_anon_129_1',
]
union_anon_129._fields_ = [
    ('skb_data_end', POINTER(None)),
    ('unnamed_anon_129_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6887
class struct_bpf_sock_ops(Structure):
    pass

struct_bpf_sock_ops.__slots__ = [
    'op',
    'unnamed_bpf_sock_ops_1',
    'family',
    'remote_ip4',
    'local_ip4',
    'remote_ip6',
    'local_ip6',
    'remote_port',
    'local_port',
    'is_fullsock',
    'snd_cwnd',
    'srtt_us',
    'bpf_sock_ops_cb_flags',
    'state',
    'rtt_min',
    'snd_ssthresh',
    'rcv_nxt',
    'snd_nxt',
    'snd_una',
    'mss_cache',
    'ecn_flags',
    'rate_delivered',
    'rate_interval_us',
    'packets_out',
    'retrans_out',
    'total_retrans',
    'segs_in',
    'data_segs_in',
    'segs_out',
    'data_segs_out',
    'lost_out',
    'sacked_out',
    'sk_txhash',
    'bytes_received',
    'bytes_acked',
    'unnamed_bpf_sock_ops_2',
    'unnamed_bpf_sock_ops_3',
    'unnamed_bpf_sock_ops_4',
    'skb_len',
    'skb_tcp_flags',
    'skb_hwtstamp',
]
struct_bpf_sock_ops._anonymous_ = [
    'unnamed_bpf_sock_ops_1',
    'unnamed_bpf_sock_ops_2',
    'unnamed_bpf_sock_ops_3',
    'unnamed_bpf_sock_ops_4',
]
struct_bpf_sock_ops._fields_ = [
    ('op', __u32),
    ('unnamed_bpf_sock_ops_1', union_anon_126),
    ('family', __u32),
    ('remote_ip4', __u32),
    ('local_ip4', __u32),
    ('remote_ip6', __u32 * int(4)),
    ('local_ip6', __u32 * int(4)),
    ('remote_port', __u32),
    ('local_port', __u32),
    ('is_fullsock', __u32),
    ('snd_cwnd', __u32),
    ('srtt_us', __u32),
    ('bpf_sock_ops_cb_flags', __u32),
    ('state', __u32),
    ('rtt_min', __u32),
    ('snd_ssthresh', __u32),
    ('rcv_nxt', __u32),
    ('snd_nxt', __u32),
    ('snd_una', __u32),
    ('mss_cache', __u32),
    ('ecn_flags', __u32),
    ('rate_delivered', __u32),
    ('rate_interval_us', __u32),
    ('packets_out', __u32),
    ('retrans_out', __u32),
    ('total_retrans', __u32),
    ('segs_in', __u32),
    ('data_segs_in', __u32),
    ('segs_out', __u32),
    ('data_segs_out', __u32),
    ('lost_out', __u32),
    ('sacked_out', __u32),
    ('sk_txhash', __u32),
    ('bytes_received', __u64),
    ('bytes_acked', __u64),
    ('unnamed_bpf_sock_ops_2', union_anon_127),
    ('unnamed_bpf_sock_ops_3', union_anon_128),
    ('unnamed_bpf_sock_ops_4', union_anon_129),
    ('skb_len', __u32),
    ('skb_tcp_flags', __u32),
    ('skb_hwtstamp', __u64),
]

enum_anon_130 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_RTO_CB_FLAG = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_RETRANS_CB_FLAG = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_STATE_CB_FLAG = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_RTT_CB_FLAG = (1 << 3)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_PARSE_ALL_HDR_OPT_CB_FLAG = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_PARSE_UNKNOWN_HDR_OPT_CB_FLAG = (1 << 5)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_WRITE_HDR_OPT_CB_FLAG = (1 << 6)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

BPF_SOCK_OPS_ALL_CB_FLAGS = 0x7F# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6965

enum_anon_131 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7017

SK_BPF_CB_TX_TIMESTAMPING = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7017

SK_BPF_CB_MASK = ((SK_BPF_CB_TX_TIMESTAMPING - 1) | SK_BPF_CB_TX_TIMESTAMPING)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7017

enum_anon_132 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_VOID = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TIMEOUT_INIT = (BPF_SOCK_OPS_VOID + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_RWND_INIT = (BPF_SOCK_OPS_TIMEOUT_INIT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TCP_CONNECT_CB = (BPF_SOCK_OPS_RWND_INIT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_ACTIVE_ESTABLISHED_CB = (BPF_SOCK_OPS_TCP_CONNECT_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_PASSIVE_ESTABLISHED_CB = (BPF_SOCK_OPS_ACTIVE_ESTABLISHED_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_NEEDS_ECN = (BPF_SOCK_OPS_PASSIVE_ESTABLISHED_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_BASE_RTT = (BPF_SOCK_OPS_NEEDS_ECN + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_RTO_CB = (BPF_SOCK_OPS_BASE_RTT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_RETRANS_CB = (BPF_SOCK_OPS_RTO_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_STATE_CB = (BPF_SOCK_OPS_RETRANS_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TCP_LISTEN_CB = (BPF_SOCK_OPS_STATE_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_RTT_CB = (BPF_SOCK_OPS_TCP_LISTEN_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_PARSE_HDR_OPT_CB = (BPF_SOCK_OPS_RTT_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_HDR_OPT_LEN_CB = (BPF_SOCK_OPS_PARSE_HDR_OPT_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_WRITE_HDR_OPT_CB = (BPF_SOCK_OPS_HDR_OPT_LEN_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TSTAMP_SCHED_CB = (BPF_SOCK_OPS_WRITE_HDR_OPT_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TSTAMP_SND_SW_CB = (BPF_SOCK_OPS_TSTAMP_SCHED_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TSTAMP_SND_HW_CB = (BPF_SOCK_OPS_TSTAMP_SND_SW_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TSTAMP_ACK_CB = (BPF_SOCK_OPS_TSTAMP_SND_HW_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

BPF_SOCK_OPS_TSTAMP_SENDMSG_CB = (BPF_SOCK_OPS_TSTAMP_ACK_CB + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7026

enum_anon_133 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_ESTABLISHED = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_SYN_SENT = (BPF_TCP_ESTABLISHED + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_SYN_RECV = (BPF_TCP_SYN_SENT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_FIN_WAIT1 = (BPF_TCP_SYN_RECV + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_FIN_WAIT2 = (BPF_TCP_FIN_WAIT1 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_TIME_WAIT = (BPF_TCP_FIN_WAIT2 + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_CLOSE = (BPF_TCP_TIME_WAIT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_CLOSE_WAIT = (BPF_TCP_CLOSE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_LAST_ACK = (BPF_TCP_CLOSE_WAIT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_LISTEN = (BPF_TCP_LAST_ACK + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_CLOSING = (BPF_TCP_LISTEN + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_NEW_SYN_RECV = (BPF_TCP_CLOSING + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_BOUND_INACTIVE = (BPF_TCP_NEW_SYN_RECV + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

BPF_TCP_MAX_STATES = (BPF_TCP_BOUND_INACTIVE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7165

enum_anon_134 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_IW = 1001# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_SNDCWND_CLAMP = 1002# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_DELACK_MAX = 1003# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_RTO_MIN = 1004# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_SYN = 1005# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_SYN_IP = 1006# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_SYN_MAC = 1007# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

TCP_BPF_SOCK_OPS_CB_FLAGS = 1008# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

SK_BPF_CB_FLAGS = 1009# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

SK_BPF_BYPASS_PROT_MEM = 1010# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7183

enum_anon_135 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7229

BPF_LOAD_HDR_OPT_TCP_SYN = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7229

enum_anon_136 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7236

BPF_WRITE_HDR_TCP_CURRENT_MSS = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7236

BPF_WRITE_HDR_TCP_SYNACK_COOKIE = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7236

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7249
class struct_bpf_perf_event_value(Structure):
    pass

struct_bpf_perf_event_value.__slots__ = [
    'counter',
    'enabled',
    'running',
]
struct_bpf_perf_event_value._fields_ = [
    ('counter', __u64),
    ('enabled', __u64),
    ('running', __u64),
]

enum_anon_137 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7255

BPF_DEVCG_ACC_MKNOD = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7255

BPF_DEVCG_ACC_READ = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7255

BPF_DEVCG_ACC_WRITE = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7255

enum_anon_138 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7261

BPF_DEVCG_DEV_BLOCK = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7261

BPF_DEVCG_DEV_CHAR = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7261

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7266
class struct_bpf_cgroup_dev_ctx(Structure):
    pass

struct_bpf_cgroup_dev_ctx.__slots__ = [
    'access_type',
    'major',
    'minor',
]
struct_bpf_cgroup_dev_ctx._fields_ = [
    ('access_type', __u32),
    ('major', __u32),
    ('minor', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7273
class struct_bpf_raw_tracepoint_args(Structure):
    pass

struct_bpf_raw_tracepoint_args.__slots__ = [
    'args',
]
struct_bpf_raw_tracepoint_args._fields_ = [
    ('args', __u64 * int(0)),
]

enum_anon_139 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7280

BPF_FIB_LOOKUP_DIRECT = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7280

BPF_FIB_LOOKUP_OUTPUT = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7280

BPF_FIB_LOOKUP_SKIP_NEIGH = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7280

BPF_FIB_LOOKUP_TBID = (1 << 3)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7280

BPF_FIB_LOOKUP_SRC = (1 << 4)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7280

BPF_FIB_LOOKUP_MARK = (1 << 5)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7280

enum_anon_140 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_SUCCESS = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_BLACKHOLE = (BPF_FIB_LKUP_RET_SUCCESS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_UNREACHABLE = (BPF_FIB_LKUP_RET_BLACKHOLE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_PROHIBIT = (BPF_FIB_LKUP_RET_UNREACHABLE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_NOT_FWDED = (BPF_FIB_LKUP_RET_PROHIBIT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_FWD_DISABLED = (BPF_FIB_LKUP_RET_NOT_FWDED + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_UNSUPP_LWT = (BPF_FIB_LKUP_RET_FWD_DISABLED + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_NO_NEIGH = (BPF_FIB_LKUP_RET_UNSUPP_LWT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_FRAG_NEEDED = (BPF_FIB_LKUP_RET_NO_NEIGH + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

BPF_FIB_LKUP_RET_NO_SRC_ADDR = (BPF_FIB_LKUP_RET_FRAG_NEEDED + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7289

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7313
class union_anon_141(Union):
    pass

union_anon_141.__slots__ = [
    'tot_len',
    'mtu_result',
]
union_anon_141._fields_ = [
    ('tot_len', __u16),
    ('mtu_result', __u16),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7325
class union_anon_142(Union):
    pass

union_anon_142.__slots__ = [
    'tos',
    'flowinfo',
    'rt_metric',
]
union_anon_142._fields_ = [
    ('tos', __u8),
    ('flowinfo', __be32),
    ('rt_metric', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7337
class union_anon_143(Union):
    pass

union_anon_143.__slots__ = [
    'ipv4_src',
    'ipv6_src',
]
union_anon_143._fields_ = [
    ('ipv4_src', __be32),
    ('ipv6_src', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7346
class union_anon_144(Union):
    pass

union_anon_144.__slots__ = [
    'ipv4_dst',
    'ipv6_dst',
]
union_anon_144._fields_ = [
    ('ipv4_dst', __be32),
    ('ipv6_dst', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7352
class struct_anon_145(Structure):
    pass

struct_anon_145.__slots__ = [
    'h_vlan_proto',
    'h_vlan_TCI',
]
struct_anon_145._fields_ = [
    ('h_vlan_proto', __be16),
    ('h_vlan_TCI', __be16),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7351
class union_anon_146(Union):
    pass

union_anon_146.__slots__ = [
    'unnamed_anon_146_1',
    'tbid',
]
union_anon_146._anonymous_ = [
    'unnamed_anon_146_1',
]
union_anon_146._fields_ = [
    ('unnamed_anon_146_1', struct_anon_145),
    ('tbid', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7366
class struct_anon_147(Structure):
    pass

struct_anon_147.__slots__ = [
    'mark',
]
struct_anon_147._fields_ = [
    ('mark', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7372
class struct_anon_148(Structure):
    pass

struct_anon_148.__slots__ = [
    'smac',
    'dmac',
]
struct_anon_148._fields_ = [
    ('smac', __u8 * int(6)),
    ('dmac', __u8 * int(6)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7364
class union_anon_149(Union):
    pass

union_anon_149.__slots__ = [
    'unnamed_anon_149_1',
    'unnamed_anon_149_2',
]
union_anon_149._anonymous_ = [
    'unnamed_anon_149_1',
    'unnamed_anon_149_2',
]
union_anon_149._fields_ = [
    ('unnamed_anon_149_1', struct_anon_147),
    ('unnamed_anon_149_2', struct_anon_148),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7302
class struct_bpf_fib_lookup(Structure):
    pass

struct_bpf_fib_lookup.__slots__ = [
    'family',
    'l4_protocol',
    'sport',
    'dport',
    'unnamed_bpf_fib_lookup_1',
    'ifindex',
    'unnamed_bpf_fib_lookup_2',
    'unnamed_bpf_fib_lookup_3',
    'unnamed_bpf_fib_lookup_4',
    'unnamed_bpf_fib_lookup_5',
    'unnamed_bpf_fib_lookup_6',
]
struct_bpf_fib_lookup._anonymous_ = [
    'unnamed_bpf_fib_lookup_1',
    'unnamed_bpf_fib_lookup_2',
    'unnamed_bpf_fib_lookup_3',
    'unnamed_bpf_fib_lookup_4',
    'unnamed_bpf_fib_lookup_5',
    'unnamed_bpf_fib_lookup_6',
]
struct_bpf_fib_lookup._fields_ = [
    ('family', __u8),
    ('l4_protocol', __u8),
    ('sport', __be16),
    ('dport', __be16),
    ('unnamed_bpf_fib_lookup_1', union_anon_141),
    ('ifindex', __u32),
    ('unnamed_bpf_fib_lookup_2', union_anon_142),
    ('unnamed_bpf_fib_lookup_3', union_anon_143),
    ('unnamed_bpf_fib_lookup_4', union_anon_144),
    ('unnamed_bpf_fib_lookup_5', union_anon_146),
    ('unnamed_bpf_fib_lookup_6', union_anon_149),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7383
class union_anon_150(Union):
    pass

union_anon_150.__slots__ = [
    'ipv4_nh',
    'ipv6_nh',
]
union_anon_150._fields_ = [
    ('ipv4_nh', __be32),
    ('ipv6_nh', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7379
class struct_bpf_redir_neigh(Structure):
    pass

struct_bpf_redir_neigh.__slots__ = [
    'nh_family',
    'unnamed_bpf_redir_neigh_1',
]
struct_bpf_redir_neigh._anonymous_ = [
    'unnamed_bpf_redir_neigh_1',
]
struct_bpf_redir_neigh._fields_ = [
    ('nh_family', __u32),
    ('unnamed_bpf_redir_neigh_1', union_anon_150),
]

enum_bpf_check_mtu_flags = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7390

BPF_MTU_CHK_SEGS = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7390

enum_bpf_check_mtu_ret = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7394

BPF_MTU_CHK_RET_SUCCESS = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7394

BPF_MTU_CHK_RET_FRAG_NEEDED = (BPF_MTU_CHK_RET_SUCCESS + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7394

BPF_MTU_CHK_RET_SEGS_TOOBIG = (BPF_MTU_CHK_RET_FRAG_NEEDED + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7394

enum_bpf_task_fd_type = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7400

BPF_FD_TYPE_RAW_TRACEPOINT = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7400

BPF_FD_TYPE_TRACEPOINT = (BPF_FD_TYPE_RAW_TRACEPOINT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7400

BPF_FD_TYPE_KPROBE = (BPF_FD_TYPE_TRACEPOINT + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7400

BPF_FD_TYPE_KRETPROBE = (BPF_FD_TYPE_KPROBE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7400

BPF_FD_TYPE_UPROBE = (BPF_FD_TYPE_KRETPROBE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7400

BPF_FD_TYPE_URETPROBE = (BPF_FD_TYPE_UPROBE + 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7400

enum_anon_151 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7409

BPF_FLOW_DISSECTOR_F_PARSE_1ST_FRAG = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7409

BPF_FLOW_DISSECTOR_F_STOP_AT_FLOW_LABEL = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7409

BPF_FLOW_DISSECTOR_F_STOP_AT_ENCAP = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7409

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7427
class struct_anon_152(Structure):
    pass

struct_anon_152.__slots__ = [
    'ipv4_src',
    'ipv4_dst',
]
struct_anon_152._fields_ = [
    ('ipv4_src', __be32),
    ('ipv4_dst', __be32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7431
class struct_anon_153(Structure):
    pass

struct_anon_153.__slots__ = [
    'ipv6_src',
    'ipv6_dst',
]
struct_anon_153._fields_ = [
    ('ipv6_src', __u32 * int(4)),
    ('ipv6_dst', __u32 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7426
class union_anon_154(Union):
    pass

union_anon_154.__slots__ = [
    'unnamed_anon_154_1',
    'unnamed_anon_154_2',
]
union_anon_154._anonymous_ = [
    'unnamed_anon_154_1',
    'unnamed_anon_154_2',
]
union_anon_154._fields_ = [
    ('unnamed_anon_154_1', struct_anon_152),
    ('unnamed_anon_154_2', struct_anon_153),
]

struct_bpf_flow_keys.__slots__ = [
    'nhoff',
    'thoff',
    'addr_proto',
    'is_frag',
    'is_first_frag',
    'is_encap',
    'ip_proto',
    'n_proto',
    'sport',
    'dport',
    'unnamed_bpf_flow_keys_1',
    'flags',
    'flow_label',
]
struct_bpf_flow_keys._anonymous_ = [
    'unnamed_bpf_flow_keys_1',
]
struct_bpf_flow_keys._fields_ = [
    ('nhoff', __u16),
    ('thoff', __u16),
    ('addr_proto', __u16),
    ('is_frag', __u8),
    ('is_first_frag', __u8),
    ('is_encap', __u8),
    ('ip_proto', __u8),
    ('n_proto', __be16),
    ('sport', __be16),
    ('dport', __be16),
    ('unnamed_bpf_flow_keys_1', union_anon_154),
    ('flags', __u32),
    ('flow_label', __be32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7440
class struct_bpf_func_info(Structure):
    pass

struct_bpf_func_info.__slots__ = [
    'insn_off',
    'type_id',
]
struct_bpf_func_info._fields_ = [
    ('insn_off', __u32),
    ('type_id', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7448
class struct_bpf_line_info(Structure):
    pass

struct_bpf_line_info.__slots__ = [
    'insn_off',
    'file_name_off',
    'line_off',
    'line_col',
]
struct_bpf_line_info._fields_ = [
    ('insn_off', __u32),
    ('file_name_off', __u32),
    ('line_off', __u32),
    ('line_col', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7455
class struct_bpf_spin_lock(Structure):
    pass

struct_bpf_spin_lock.__slots__ = [
    'val',
]
struct_bpf_spin_lock._fields_ = [
    ('val', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7459
class struct_bpf_timer(Structure):
    pass

struct_bpf_timer.__slots__ = [
    '__opaque',
]
struct_bpf_timer._fields_ = [
    ('__opaque', __u64 * int(2)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7463
class struct_bpf_task_work(Structure):
    pass

struct_bpf_task_work.__slots__ = [
    '__opaque',
]
struct_bpf_task_work._fields_ = [
    ('__opaque', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7467
class struct_bpf_wq(Structure):
    pass

struct_bpf_wq.__slots__ = [
    '__opaque',
]
struct_bpf_wq._fields_ = [
    ('__opaque', __u64 * int(2)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7471
class struct_bpf_dynptr(Structure):
    pass

struct_bpf_dynptr.__slots__ = [
    '__opaque',
]
struct_bpf_dynptr._fields_ = [
    ('__opaque', __u64 * int(2)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7475
class struct_bpf_list_head(Structure):
    pass

struct_bpf_list_head.__slots__ = [
    '__opaque',
]
struct_bpf_list_head._fields_ = [
    ('__opaque', __u64 * int(2)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7479
class struct_bpf_list_node(Structure):
    pass

struct_bpf_list_node.__slots__ = [
    '__opaque',
]
struct_bpf_list_node._fields_ = [
    ('__opaque', __u64 * int(3)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7483
class struct_bpf_rb_root(Structure):
    pass

struct_bpf_rb_root.__slots__ = [
    '__opaque',
]
struct_bpf_rb_root._fields_ = [
    ('__opaque', __u64 * int(2)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7487
class struct_bpf_rb_node(Structure):
    pass

struct_bpf_rb_node.__slots__ = [
    '__opaque',
]
struct_bpf_rb_node._fields_ = [
    ('__opaque', __u64 * int(4)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7491
class struct_bpf_refcount(Structure):
    pass

struct_bpf_refcount.__slots__ = [
    '__opaque',
]
struct_bpf_refcount._fields_ = [
    ('__opaque', __u32 * int(1)),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7495
class struct_bpf_sysctl(Structure):
    pass

struct_bpf_sysctl.__slots__ = [
    'write',
    'file_pos',
]
struct_bpf_sysctl._fields_ = [
    ('write', __u32),
    ('file_pos', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7505
class union_anon_155(Union):
    pass

union_anon_155.__slots__ = [
    'sk',
    'unnamed_anon_155_1',
]
union_anon_155._fields_ = [
    ('sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_155_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7506
class union_anon_156(Union):
    pass

union_anon_156.__slots__ = [
    'optval',
    'unnamed_anon_156_1',
]
union_anon_156._fields_ = [
    ('optval', POINTER(None)),
    ('unnamed_anon_156_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7507
class union_anon_157(Union):
    pass

union_anon_157.__slots__ = [
    'optval_end',
    'unnamed_anon_157_1',
]
union_anon_157._fields_ = [
    ('optval_end', POINTER(None)),
    ('unnamed_anon_157_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7504
class struct_bpf_sockopt(Structure):
    pass

struct_bpf_sockopt.__slots__ = [
    'unnamed_bpf_sockopt_1',
    'unnamed_bpf_sockopt_2',
    'unnamed_bpf_sockopt_3',
    'level',
    'optname',
    'optlen',
    'retval',
]
struct_bpf_sockopt._anonymous_ = [
    'unnamed_bpf_sockopt_1',
    'unnamed_bpf_sockopt_2',
    'unnamed_bpf_sockopt_3',
]
struct_bpf_sockopt._fields_ = [
    ('unnamed_bpf_sockopt_1', union_anon_155),
    ('unnamed_bpf_sockopt_2', union_anon_156),
    ('unnamed_bpf_sockopt_3', union_anon_157),
    ('level', __s32),
    ('optname', __s32),
    ('optlen', __s32),
    ('retval', __s32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7515
class struct_bpf_pidns_info(Structure):
    pass

struct_bpf_pidns_info.__slots__ = [
    'pid',
    'tgid',
]
struct_bpf_pidns_info._fields_ = [
    ('pid', __u32),
    ('tgid', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7523
class union_anon_158(Union):
    pass

union_anon_158.__slots__ = [
    'sk',
    'unnamed_anon_158_1',
]
union_anon_158._fields_ = [
    ('sk', POINTER(struct_bpf_sock)),
    ('unnamed_anon_158_1', __u64, 64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7522
class union_anon_159(Union):
    pass

union_anon_159.__slots__ = [
    'unnamed_anon_159_1',
    'cookie',
]
union_anon_159._anonymous_ = [
    'unnamed_anon_159_1',
]
union_anon_159._fields_ = [
    ('unnamed_anon_159_1', union_anon_158),
    ('cookie', __u64),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7521
class struct_bpf_sk_lookup(Structure):
    pass

struct_bpf_sk_lookup.__slots__ = [
    'unnamed_bpf_sk_lookup_1',
    'family',
    'protocol',
    'remote_ip4',
    'remote_ip6',
    'remote_port',
    'unnamed_bpf_sk_lookup_2',
    'local_ip4',
    'local_ip6',
    'local_port',
    'ingress_ifindex',
]
struct_bpf_sk_lookup._anonymous_ = [
    'unnamed_bpf_sk_lookup_1',
]
struct_bpf_sk_lookup._fields_ = [
    ('unnamed_bpf_sk_lookup_1', union_anon_159),
    ('family', __u32),
    ('protocol', __u32),
    ('remote_ip4', __u32),
    ('remote_ip6', __u32 * int(4)),
    ('remote_port', __be16),
    ('unnamed_bpf_sk_lookup_2', __u16, 16),
    ('local_ip4', __u32),
    ('local_ip6', __u32 * int(4)),
    ('local_port', __u32),
    ('ingress_ifindex', __u32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7547
class struct_btf_ptr(Structure):
    pass

struct_btf_ptr.__slots__ = [
    'ptr',
    'type_id',
    'flags',
]
struct_btf_ptr._fields_ = [
    ('ptr', POINTER(None)),
    ('type_id', __u32),
    ('flags', __u32),
]

enum_anon_160 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7562

BTF_F_COMPACT = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7562

BTF_F_NONAME = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7562

BTF_F_PTR_RAW = (1 << 2)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7562

BTF_F_ZERO = (1 << 3)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7562

enum_bpf_core_relo_kind = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_FIELD_BYTE_OFFSET = 0# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_FIELD_BYTE_SIZE = 1# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_FIELD_EXISTS = 2# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_FIELD_SIGNED = 3# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_FIELD_LSHIFT_U64 = 4# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_FIELD_RSHIFT_U64 = 5# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_TYPE_ID_LOCAL = 6# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_TYPE_ID_TARGET = 7# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_TYPE_EXISTS = 8# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_TYPE_SIZE = 9# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_ENUMVAL_EXISTS = 10# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_ENUMVAL_VALUE = 11# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

BPF_CORE_TYPE_MATCHES = 12# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7573

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7637
class struct_bpf_core_relo(Structure):
    pass

struct_bpf_core_relo.__slots__ = [
    'insn_off',
    'type_id',
    'access_str_off',
    'kind',
]
struct_bpf_core_relo._fields_ = [
    ('insn_off', __u32),
    ('type_id', __u32),
    ('access_str_off', __u32),
    ('kind', enum_bpf_core_relo_kind),
]

enum_anon_161 = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7650

BPF_F_TIMER_ABS = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7650

BPF_F_TIMER_CPU_PIN = (1 << 1)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7650

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7656
class struct_bpf_iter_num(Structure):
    pass

struct_bpf_iter_num.__slots__ = [
    '__opaque',
]
struct_bpf_iter_num._fields_ = [
    ('__opaque', __u64 * int(1)),
]

enum_bpf_kfunc_flags = c_int# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7668

BPF_F_PAD_ZEROS = (1 << 0)# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7668

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7685
class struct_bpf_insn_array_value(Structure):
    pass

struct_bpf_insn_array_value.__slots__ = [
    'orig_off',
    'xlated_off',
    'jitted_off',
    'unnamed_bpf_insn_array_value_1',
]
struct_bpf_insn_array_value._fields_ = [
    ('orig_off', __u32),
    ('xlated_off', __u32),
    ('jitted_off', __u32),
    ('unnamed_bpf_insn_array_value_1', __u32, 32),
]

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 17
try:
    BPF_JMP32 = 0x06
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 18
try:
    BPF_ALU64 = 0x07
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 21
try:
    BPF_DW = 0x18
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 22
try:
    BPF_MEMSX = 0x80
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 23
try:
    BPF_ATOMIC = 0xc0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 24
try:
    BPF_XADD = 0xc0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 27
try:
    BPF_MOV = 0xb0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 28
try:
    BPF_ARSH = 0xc0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 31
try:
    BPF_END = 0xd0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 32
try:
    BPF_TO_LE = 0x00
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 33
try:
    BPF_TO_BE = 0x08
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 34
try:
    BPF_FROM_LE = BPF_TO_LE
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 35
try:
    BPF_FROM_BE = BPF_TO_BE
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 38
try:
    BPF_JNE = 0x50
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 39
try:
    BPF_JLT = 0xa0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 40
try:
    BPF_JLE = 0xb0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 41
try:
    BPF_JSGT = 0x60
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 42
try:
    BPF_JSGE = 0x70
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 43
try:
    BPF_JSLT = 0xc0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 44
try:
    BPF_JSLE = 0xd0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 45
try:
    BPF_JCOND = 0xe0
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 46
try:
    BPF_CALL = 0x80
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 47
try:
    BPF_EXIT = 0x90
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 50
try:
    BPF_FETCH = 0x01
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 51
try:
    BPF_XCHG = (0xe0 | BPF_FETCH)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 52
try:
    BPF_CMPXCHG = (0xf0 | BPF_FETCH)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 54
try:
    BPF_LOAD_ACQ = 0x100
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 55
try:
    BPF_STORE_REL = 0x110
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 78
try:
    MAX_BPF_REG = __MAX_BPF_REG
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1151
try:
    MAX_BPF_ATTACH_TYPE = __MAX_BPF_ATTACH_TYPE
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1175
try:
    MAX_BPF_LINK_TYPE = __MAX_BPF_LINK_TYPE
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1231
try:
    BPF_F_ALLOW_OVERRIDE = (1 << 0)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1232
try:
    BPF_F_ALLOW_MULTI = (1 << 1)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1234
try:
    BPF_F_REPLACE = (1 << 2)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1235
try:
    BPF_F_BEFORE = (1 << 3)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1236
try:
    BPF_F_AFTER = (1 << 4)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1237
try:
    BPF_F_ID = (1 << 5)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1238
try:
    BPF_F_PREORDER = (1 << 6)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1239
try:
    BPF_F_LINK = BPF_F_LINK
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1246
try:
    BPF_F_STRICT_ALIGNMENT = (1 << 0)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1260
try:
    BPF_F_ANY_ALIGNMENT = (1 << 1)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1278
try:
    BPF_F_TEST_RND_HI32 = (1 << 2)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1281
try:
    BPF_F_TEST_STATE_FREQ = (1 << 3)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1289
try:
    BPF_F_SLEEPABLE = (1 << 4)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1294
try:
    BPF_F_XDP_HAS_FRAGS = (1 << 5)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1299
try:
    BPF_F_XDP_DEV_BOUND_ONLY = (1 << 6)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1302
try:
    BPF_F_TEST_REG_INVARIANTS = (1 << 7)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1321
try:
    BPF_F_NETFILTER_IP_DEFRAG = (1 << 0)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1334
try:
    BPF_PSEUDO_MAP_FD = 1
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1335
try:
    BPF_PSEUDO_MAP_IDX = 5
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1345
try:
    BPF_PSEUDO_MAP_VALUE = 2
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1346
try:
    BPF_PSEUDO_MAP_IDX_VALUE = 6
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1357
try:
    BPF_PSEUDO_BTF_ID = 3
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1366
try:
    BPF_PSEUDO_FUNC = 4
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1371
try:
    BPF_PSEUDO_CALL = 1
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1375
try:
    BPF_PSEUDO_KFUNC_CALL = 2
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1456
try:
    BPF_F_QUERY_EFFECTIVE = (1 << 0)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1461
try:
    BPF_F_TEST_RUN_ON_CPU = (1 << 0)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1463
try:
    BPF_F_TEST_XDP_LIVE_FRAMES = (1 << 1)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1465
try:
    BPF_F_TEST_SKB_CHECKSUM_COMPLETE = (1 << 2)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1482
try:
    BPF_BUILD_ID_SIZE = 20
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1492
try:
    BPF_OBJ_NAME_LEN = 16
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6218
def BPF_F_ADJ_ROOM_ENCAP_L2(len):
    return (((__u64 (ord_if_char(len))).value & BPF_ADJ_ROOM_ENCAP_L2_MASK) << BPF_ADJ_ROOM_ENCAP_L2_SHIFT)

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6300
try:
    BPF_F_REDIRECT_FLAGS = ((BPF_F_INGRESS | BPF_F_BROADCAST) | BPF_F_EXCLUDE_INGRESS)
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6528
try:
    XDP_PACKET_HEADROOM = 256
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6646
try:
    BPF_TAG_SIZE = 8
except:
    pass

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7445
def BPF_LINE_INFO_LINE_NUM(line_col):
    return (line_col >> 10)

# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7446
def BPF_LINE_INFO_LINE_COL(line_col):
    return (line_col & 0x3ff)

bpf_insn = struct_bpf_insn# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 80

bpf_lpm_trie_key = struct_bpf_lpm_trie_key# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 92

bpf_lpm_trie_key_hdr = struct_bpf_lpm_trie_key_hdr# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 98

bpf_lpm_trie_key_u8 = struct_bpf_lpm_trie_key_u8# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 103

bpf_cgroup_storage_key = struct_bpf_cgroup_storage_key# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 111

bpf_iter_link_info = union_bpf_iter_link_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 124

bpf_stack_build_id = struct_bpf_stack_build_id# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1483

bpf_attr = union_bpf_attr# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 1499

bpf_flow_keys = struct_bpf_flow_keys# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7415

bpf_sock = struct_bpf_sock# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6430

__sk_buff = struct___sk_buff# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6326

bpf_tunnel_key = struct_bpf_tunnel_key# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6368

bpf_xfrm_state = struct_bpf_xfrm_state# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6390

bpf_tcp_sock = struct_bpf_tcp_sock# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6449

bpf_sock_tuple = struct_bpf_sock_tuple# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6494

bpf_xdp_sock = struct_bpf_xdp_sock# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6524

xdp_md = struct_xdp_md# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6546

bpf_devmap_val = struct_bpf_devmap_val# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6562

bpf_cpumap_val = struct_bpf_cpumap_val# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6575

sk_msg_md = struct_sk_msg_md# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6591

sk_reuseport_md = struct_sk_reuseport_md# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6607

bpf_prog_info = struct_bpf_prog_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6648

bpf_map_info = struct_bpf_map_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6690

bpf_btf_info = struct_bpf_btf_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6711

bpf_link_info = struct_bpf_link_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6720

bpf_token_info = struct_bpf_token_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6847

bpf_sock_addr = struct_bpf_sock_addr# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6858

bpf_sock_ops = struct_bpf_sock_ops# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 6887

bpf_perf_event_value = struct_bpf_perf_event_value# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7249

bpf_cgroup_dev_ctx = struct_bpf_cgroup_dev_ctx# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7266

bpf_raw_tracepoint_args = struct_bpf_raw_tracepoint_args# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7273

bpf_fib_lookup = struct_bpf_fib_lookup# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7302

bpf_redir_neigh = struct_bpf_redir_neigh# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7379

bpf_func_info = struct_bpf_func_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7440

bpf_line_info = struct_bpf_line_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7448

bpf_spin_lock = struct_bpf_spin_lock# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7455

bpf_timer = struct_bpf_timer# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7459

bpf_task_work = struct_bpf_task_work# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7463

bpf_wq = struct_bpf_wq# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7467

bpf_dynptr = struct_bpf_dynptr# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7471

bpf_list_head = struct_bpf_list_head# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7475

bpf_list_node = struct_bpf_list_node# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7479

bpf_rb_root = struct_bpf_rb_root# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7483

bpf_rb_node = struct_bpf_rb_node# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7487

bpf_refcount = struct_bpf_refcount# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7491

bpf_sysctl = struct_bpf_sysctl# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7495

bpf_sockopt = struct_bpf_sockopt# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7504

bpf_pidns_info = struct_bpf_pidns_info# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7515

bpf_sk_lookup = struct_bpf_sk_lookup# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7521

btf_ptr = struct_btf_ptr# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7547

bpf_core_relo = struct_bpf_core_relo# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7637

bpf_iter_num = struct_bpf_iter_num# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7656

bpf_insn_array_value = struct_bpf_insn_array_value# /home/m.bieganski/github/libbpf/include/uapi/linux/bpf.h: 7685

# No inserted files

# No prefix-stripping

