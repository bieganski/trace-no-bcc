"""Wrapper for libbpf.c

Generated with:
/home/m.bieganski/.local/bin/ctypesgen -l libbpf.so.1 -D__signed__=signed -D__builtin_constant_p(x)='1' -I ../../libbpf//include/ -I ../../libbpf//include/uapi/ ../../libbpf//src/libbpf.c ../../libbpf//src/libbpf.h

Do not modify this file.
"""
__docformat__ = 'restructuredtext'
import ctypes
import sys
from ctypes import *
_int_types = ctypes.c_int16, ctypes.c_int32
if hasattr(ctypes, 'c_int64'):
    _int_types += ctypes.c_int64,
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

    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):
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

    def __init__(self, string=''):
        self.data = string

    def __hash__(self):
        raise TypeError('unhashable type (it is mutable)')

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1:]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1:]

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
    _fields_ = [('raw', ctypes.POINTER(ctypes.c_char)), ('data', ctypes.
        c_char_p)]

    def __init__(self, obj=b''):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())
        elif isinstance(obj, String):
            return obj
        elif isinstance(obj, bytes):
            return cls(obj)
        elif isinstance(obj, str):
            return cls(obj.encode())
        elif isinstance(obj, ctypes.c_char_p):
            return obj
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


def UNCHECKED(type):
    if hasattr(type, '_type_') and isinstance(type._type_, str
        ) and type._type_ != 'P':
        return type
    else:
        return ctypes.c_void_p


class _variadic_function(object):

    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*(fixed_args + list(args[i:])))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if isinstance(value, bytes) or isinstance(value, str
        ) else value


_libs = {}
_libdirs = []
"""
Load libraries - appropriately for all our supported platforms
"""
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
        return os.environ[name].split(':')
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """
    name_formats = ['%s']


    class Lookup:
        """Looking up calling conventions for a platform"""
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention='cdecl'):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".
                    format(calling_convention, name))
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention='cdecl'):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access['cdecl'], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)
        for path in paths:
            try:
                return self.Lookup(path)
            except Exception:
                pass
        raise ImportError('Could not load %s.' % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    yield os.path.join(dir_i, fmt % libname)
            try:
                this_file = __file__
            except NameError:
                this_file = None
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(
                        __file__), fmt % libname))
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path
            for path in self.getplatformpaths(libname):
                yield path
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt %
                    libname))

    def getplatformpaths(self, _libname):
        """Return all the library paths available in this platform"""
        return []


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""
    name_formats = ['lib%s.dylib', 'lib%s.so', 'lib%s.bundle', '%s.dylib',
        '%s.so', '%s.bundle', '%s']


    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [(fmt % libname) for fmt in self.name_formats]
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
        dyld_fallback_library_path = _environ_path('DYLD_FALLBACK_LIBRARY_PATH'
            )
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                '/usr/local/lib', '/usr/lib']
        dirs = []
        if '/' in libname:
            dirs.extend(_environ_path('DYLD_LIBRARY_PATH'))
        else:
            dirs.extend(_environ_path('LD_LIBRARY_PATH'))
            dirs.extend(_environ_path('DYLD_LIBRARY_PATH'))
            dirs.extend(_environ_path('LD_RUN_PATH'))
        if hasattr(sys, 'frozen') and getattr(sys, 'frozen') == 'macosx_app':
            dirs.append(os.path.join(os.environ['RESOURCEPATH'], '..',
                'Frameworks'))
        dirs.extend(dyld_fallback_library_path)
        return dirs


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""
    _ld_so_cache = None
    _include = re.compile('^\\s*include\\s+(?P<pattern>.*)')
    name_formats = ['lib%s.so', '%s.so', '%s']


    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
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
                        for dir2 in glob.glob(match.group('pattern')):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        directories = self._Directories()
        for name in ('LD_LIBRARY_PATH', 'SHLIB_PATH', 'LIBPATH', 'LIBRARY_PATH'
            ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        self._get_ld_so_conf_dirs('/etc/ld.so.conf', directories)
        bitage = platform.architecture()[0]
        unix_lib_dirs_list = []
        if bitage.startswith('64'):
            unix_lib_dirs_list += ['/lib64', '/usr/lib64']
        unix_lib_dirs_list += ['/lib', '/usr/lib']
        if sys.platform.startswith('linux'):
            if bitage.startswith('32'):
                unix_lib_dirs_list += ['/lib/i386-linux-gnu',
                    '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu',
                    '/usr/lib/x86_64-linux-gnu']
            else:
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)
        cache = {}
        lib_re = re.compile('lib(.*)\\.s[ol]')
        for our_dir in directories.ordered():
            try:
                for path in glob.glob('%s/*.s[ol]*' % our_dir):
                    file = os.path.basename(path)
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)
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
            yield i


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""
    name_formats = ['%s.dll', 'lib%s.dll', '%slib.dll', '%s']


    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access['stdcall'] = ctypes.windll.LoadLibrary(path)


loaderclass = {'darwin': DarwinLibraryLoader, 'cygwin':
    WindowsLibraryLoader, 'win32': WindowsLibraryLoader, 'msys':
    WindowsLibraryLoader}
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
add_library_search_dirs([])
_libs['libbpf.so.1'] = load_library('libbpf.so.1')
__uint16_t = c_ushort
__uint32_t = c_uint
__uint64_t = c_ulong
__off_t = c_long
__off64_t = c_long
__pid_t = c_int


class struct_anon_4(Structure):
    pass


struct_anon_4.__slots__ = ['__val']
struct_anon_4._fields_ = [('__val', c_int * int(2))]
__fsid_t = struct_anon_4
__rlim_t = c_ulong
__fsblkcnt_t = c_ulong
__fsfilcnt_t = c_ulong
__fsword_t = c_long
pid_t = __pid_t


class struct__IO_FILE(Structure):
    pass


FILE = struct__IO_FILE


class struct__IO_marker(Structure):
    pass


class struct__IO_codecvt(Structure):
    pass


class struct__IO_wide_data(Structure):
    pass


_IO_lock_t = None
struct__IO_FILE.__slots__ = ['_flags', '_IO_read_ptr', '_IO_read_end',
    '_IO_read_base', '_IO_write_base', '_IO_write_ptr', '_IO_write_end',
    '_IO_buf_base', '_IO_buf_end', '_IO_save_base', '_IO_backup_base',
    '_IO_save_end', '_markers', '_chain', '_fileno', '_flags2',
    '_old_offset', '_cur_column', '_vtable_offset', '_shortbuf', '_lock',
    '_offset', '_codecvt', '_wide_data', '_freeres_list', '_freeres_buf',
    '__pad5', '_mode', '_unused2']
struct__IO_FILE._fields_ = [('_flags', c_int), ('_IO_read_ptr', String), (
    '_IO_read_end', String), ('_IO_read_base', String), ('_IO_write_base',
    String), ('_IO_write_ptr', String), ('_IO_write_end', String), (
    '_IO_buf_base', String), ('_IO_buf_end', String), ('_IO_save_base',
    String), ('_IO_backup_base', String), ('_IO_save_end', String), (
    '_markers', POINTER(struct__IO_marker)), ('_chain', POINTER(
    struct__IO_FILE)), ('_fileno', c_int), ('_flags2', c_int), (
    '_old_offset', __off_t), ('_cur_column', c_ushort), ('_vtable_offset',
    c_char), ('_shortbuf', c_char * int(1)), ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t), ('_codecvt', POINTER(struct__IO_codecvt)), (
    '_wide_data', POINTER(struct__IO_wide_data)), ('_freeres_list', POINTER
    (struct__IO_FILE)), ('_freeres_buf', POINTER(None)), ('__pad5',
    c_size_t), ('_mode', c_int), ('_unused2', c_char * int(15 * sizeof(
    c_int) - 4 * sizeof(POINTER(None)) - sizeof(c_size_t)))]
uint16_t = __uint16_t
uint32_t = __uint32_t
uint64_t = __uint64_t
__u8 = c_ubyte
__s16 = c_short
__u16 = c_ushort
__s32 = c_int
__u32 = c_uint
__s64 = c_longlong
__u64 = c_ulonglong


class struct_bpf_insn(Structure):
    pass


struct_bpf_insn.__slots__ = ['code', 'dst_reg', 'src_reg', 'off', 'imm']
struct_bpf_insn._fields_ = [('code', __u8), ('dst_reg', __u8, 4), (
    'src_reg', __u8, 4), ('off', __s16), ('imm', __s32)]
enum_bpf_cgroup_iter_order = c_int


class struct_anon_28(Structure):
    pass


struct_anon_28.__slots__ = ['map_fd']
struct_anon_28._fields_ = [('map_fd', __u32)]


class struct_anon_29(Structure):
    pass


struct_anon_29.__slots__ = ['order', 'cgroup_fd', 'cgroup_id']
struct_anon_29._fields_ = [('order', enum_bpf_cgroup_iter_order), (
    'cgroup_fd', __u32), ('cgroup_id', __u64)]


class struct_anon_30(Structure):
    pass


struct_anon_30.__slots__ = ['tid', 'pid', 'pid_fd']
struct_anon_30._fields_ = [('tid', __u32), ('pid', __u32), ('pid_fd', __u32)]


class union_bpf_iter_link_info(Union):
    pass


union_bpf_iter_link_info.__slots__ = ['map', 'cgroup', 'task']
union_bpf_iter_link_info._fields_ = [('map', struct_anon_28), ('cgroup',
    struct_anon_29), ('task', struct_anon_30)]
enum_bpf_map_type = c_int
enum_bpf_prog_type = c_int
enum_bpf_attach_type = c_int
enum_bpf_link_type = c_int
enum_bpf_func_id = c_int


class struct_bpf_prog_info(Structure):
    pass


struct_bpf_prog_info.__slots__ = ['type', 'id', 'tag', 'jited_prog_len',
    'xlated_prog_len', 'jited_prog_insns', 'xlated_prog_insns', 'load_time',
    'created_by_uid', 'nr_map_ids', 'map_ids', 'name', 'ifindex',
    'gpl_compatible', 'unnamed_bpf_prog_info_1', 'netns_dev', 'netns_ino',
    'nr_jited_ksyms', 'nr_jited_func_lens', 'jited_ksyms',
    'jited_func_lens', 'btf_id', 'func_info_rec_size', 'func_info',
    'nr_func_info', 'nr_line_info', 'line_info', 'jited_line_info',
    'nr_jited_line_info', 'line_info_rec_size', 'jited_line_info_rec_size',
    'nr_prog_tags', 'prog_tags', 'run_time_ns', 'run_cnt',
    'recursion_misses', 'verified_insns', 'attach_btf_obj_id', 'attach_btf_id']
struct_bpf_prog_info._fields_ = [('type', __u32), ('id', __u32), ('tag', 
    __u8 * int(8)), ('jited_prog_len', __u32), ('xlated_prog_len', __u32),
    ('jited_prog_insns', __u64), ('xlated_prog_insns', __u64), ('load_time',
    __u64), ('created_by_uid', __u32), ('nr_map_ids', __u32), ('map_ids',
    __u64), ('name', c_char * int(16)), ('ifindex', __u32), (
    'gpl_compatible', __u32, 1), ('unnamed_bpf_prog_info_1', __u32, 31), (
    'netns_dev', __u64), ('netns_ino', __u64), ('nr_jited_ksyms', __u32), (
    'nr_jited_func_lens', __u32), ('jited_ksyms', __u64), (
    'jited_func_lens', __u64), ('btf_id', __u32), ('func_info_rec_size',
    __u32), ('func_info', __u64), ('nr_func_info', __u32), ('nr_line_info',
    __u32), ('line_info', __u64), ('jited_line_info', __u64), (
    'nr_jited_line_info', __u32), ('line_info_rec_size', __u32), (
    'jited_line_info_rec_size', __u32), ('nr_prog_tags', __u32), (
    'prog_tags', __u64), ('run_time_ns', __u64), ('run_cnt', __u64), (
    'recursion_misses', __u64), ('verified_insns', __u32), (
    'attach_btf_obj_id', __u32), ('attach_btf_id', __u32)]


class struct_bpf_map_info(Structure):
    pass


struct_bpf_map_info.__slots__ = ['type', 'id', 'key_size', 'value_size',
    'max_entries', 'map_flags', 'name', 'ifindex',
    'btf_vmlinux_value_type_id', 'netns_dev', 'netns_ino', 'btf_id',
    'btf_key_type_id', 'btf_value_type_id', 'btf_vmlinux_id', 'map_extra']
struct_bpf_map_info._fields_ = [('type', __u32), ('id', __u32), ('key_size',
    __u32), ('value_size', __u32), ('max_entries', __u32), ('map_flags',
    __u32), ('name', c_char * int(16)), ('ifindex', __u32), (
    'btf_vmlinux_value_type_id', __u32), ('netns_dev', __u64), ('netns_ino',
    __u64), ('btf_id', __u32), ('btf_key_type_id', __u32), (
    'btf_value_type_id', __u32), ('btf_vmlinux_id', __u32), ('map_extra',
    __u64)]


class struct_bpf_btf_info(Structure):
    pass


struct_bpf_btf_info.__slots__ = ['btf', 'btf_size', 'id', 'name',
    'name_len', 'kernel_btf']
struct_bpf_btf_info._fields_ = [('btf', __u64), ('btf_size', __u32), ('id',
    __u32), ('name', __u64), ('name_len', __u32), ('kernel_btf', __u32)]


class struct_bpf_line_info(Structure):
    pass


struct_bpf_line_info.__slots__ = ['insn_off', 'file_name_off', 'line_off',
    'line_col']
struct_bpf_line_info._fields_ = [('insn_off', __u32), ('file_name_off',
    __u32), ('line_off', __u32), ('line_col', __u32)]
enum_bpf_core_relo_kind = c_int


class struct_bpf_core_relo(Structure):
    pass


struct_bpf_core_relo.__slots__ = ['insn_off', 'type_id', 'access_str_off',
    'kind']
struct_bpf_core_relo._fields_ = [('insn_off', __u32), ('type_id', __u32), (
    'access_str_off', __u32), ('kind', enum_bpf_core_relo_kind)]


class union_anon_176(Union):
    pass


union_anon_176.__slots__ = ['size', 'type']
union_anon_176._fields_ = [('size', __u32), ('type', __u32)]


class struct_btf_type(Structure):
    pass


struct_btf_type.__slots__ = ['name_off', 'info', 'unnamed_btf_type_1']
struct_btf_type._anonymous_ = ['unnamed_btf_type_1']
struct_btf_type._fields_ = [('name_off', __u32), ('info', __u32), (
    'unnamed_btf_type_1', union_anon_176)]


class struct_btf_array(Structure):
    pass


struct_btf_array.__slots__ = ['type', 'index_type', 'nelems']
struct_btf_array._fields_ = [('type', __u32), ('index_type', __u32), (
    'nelems', __u32)]


class struct_btf_member(Structure):
    pass


struct_btf_member.__slots__ = ['name_off', 'type', 'offset']
struct_btf_member._fields_ = [('name_off', __u32), ('type', __u32), (
    'offset', __u32)]


class struct_btf_param(Structure):
    pass


struct_btf_param.__slots__ = ['name_off', 'type']
struct_btf_param._fields_ = [('name_off', __u32), ('type', __u32)]


class struct_btf_var(Structure):
    pass


struct_btf_var.__slots__ = ['linkage']
struct_btf_var._fields_ = [('linkage', __u32)]


class struct_btf_var_secinfo(Structure):
    pass


struct_btf_var_secinfo.__slots__ = ['type', 'offset', 'size']
struct_btf_var_secinfo._fields_ = [('type', __u32), ('offset', __u32), (
    'size', __u32)]


class union_anon_184(Union):
    pass


union_anon_184.__slots__ = ['sample_period', 'sample_freq']
union_anon_184._fields_ = [('sample_period', __u64), ('sample_freq', __u64)]


class union_anon_185(Union):
    pass


union_anon_185.__slots__ = ['wakeup_events', 'wakeup_watermark']
union_anon_185._fields_ = [('wakeup_events', __u32), ('wakeup_watermark',
    __u32)]


class union_anon_186(Union):
    pass


union_anon_186.__slots__ = ['bp_addr', 'kprobe_func', 'uprobe_path', 'config1']
union_anon_186._fields_ = [('bp_addr', __u64), ('kprobe_func', __u64), (
    'uprobe_path', __u64), ('config1', __u64)]


class union_anon_187(Union):
    pass


union_anon_187.__slots__ = ['bp_len', 'kprobe_addr', 'probe_offset', 'config2']
union_anon_187._fields_ = [('bp_len', __u64), ('kprobe_addr', __u64), (
    'probe_offset', __u64), ('config2', __u64)]


class struct_perf_event_attr(Structure):
    pass


struct_perf_event_attr.__slots__ = ['type', 'size', 'config',
    'unnamed_perf_event_attr_1', 'sample_type', 'read_format', 'disabled',
    'inherit', 'pinned', 'exclusive', 'exclude_user', 'exclude_kernel',
    'exclude_hv', 'exclude_idle', 'mmap', 'comm', 'freq', 'inherit_stat',
    'enable_on_exec', 'task', 'watermark', 'precise_ip', 'mmap_data',
    'sample_id_all', 'exclude_host', 'exclude_guest',
    'exclude_callchain_kernel', 'exclude_callchain_user', 'mmap2',
    'comm_exec', 'use_clockid', 'context_switch', 'write_backward',
    'namespaces', 'ksymbol', 'bpf_event', 'aux_output', 'cgroup',
    'text_poke', 'build_id', 'inherit_thread', 'remove_on_exec', 'sigtrap',
    '__reserved_1', 'unnamed_perf_event_attr_2', 'bp_type',
    'unnamed_perf_event_attr_3', 'unnamed_perf_event_attr_4',
    'branch_sample_type', 'sample_regs_user', 'sample_stack_user',
    'clockid', 'sample_regs_intr', 'aux_watermark', 'sample_max_stack',
    '__reserved_2', 'aux_sample_size', '__reserved_3', 'sig_data', 'config3']
struct_perf_event_attr._anonymous_ = ['unnamed_perf_event_attr_1',
    'unnamed_perf_event_attr_2', 'unnamed_perf_event_attr_3',
    'unnamed_perf_event_attr_4']
struct_perf_event_attr._fields_ = [('type', __u32), ('size', __u32), (
    'config', __u64), ('unnamed_perf_event_attr_1', union_anon_184), (
    'sample_type', __u64), ('read_format', __u64), ('disabled', __u64, 1),
    ('inherit', __u64, 1), ('pinned', __u64, 1), ('exclusive', __u64, 1), (
    'exclude_user', __u64, 1), ('exclude_kernel', __u64, 1), ('exclude_hv',
    __u64, 1), ('exclude_idle', __u64, 1), ('mmap', __u64, 1), ('comm',
    __u64, 1), ('freq', __u64, 1), ('inherit_stat', __u64, 1), (
    'enable_on_exec', __u64, 1), ('task', __u64, 1), ('watermark', __u64, 1
    ), ('precise_ip', __u64, 2), ('mmap_data', __u64, 1), ('sample_id_all',
    __u64, 1), ('exclude_host', __u64, 1), ('exclude_guest', __u64, 1), (
    'exclude_callchain_kernel', __u64, 1), ('exclude_callchain_user', __u64,
    1), ('mmap2', __u64, 1), ('comm_exec', __u64, 1), ('use_clockid', __u64,
    1), ('context_switch', __u64, 1), ('write_backward', __u64, 1), (
    'namespaces', __u64, 1), ('ksymbol', __u64, 1), ('bpf_event', __u64, 1),
    ('aux_output', __u64, 1), ('cgroup', __u64, 1), ('text_poke', __u64, 1),
    ('build_id', __u64, 1), ('inherit_thread', __u64, 1), ('remove_on_exec',
    __u64, 1), ('sigtrap', __u64, 1), ('__reserved_1', __u64, 26), (
    'unnamed_perf_event_attr_2', union_anon_185), ('bp_type', __u32), (
    'unnamed_perf_event_attr_3', union_anon_186), (
    'unnamed_perf_event_attr_4', union_anon_187), ('branch_sample_type',
    __u64), ('sample_regs_user', __u64), ('sample_stack_user', __u32), (
    'clockid', __s32), ('sample_regs_intr', __u64), ('aux_watermark', __u32
    ), ('sample_max_stack', __u16), ('__reserved_2', __u16), (
    'aux_sample_size', __u32), ('__reserved_3', __u32), ('sig_data', __u64),
    ('config3', __u64)]


class struct_anon_188(Structure):
    pass


struct_anon_188.__slots__ = ['cap_bit0', 'cap_bit0_is_deprecated',
    'cap_user_rdpmc', 'cap_user_time', 'cap_user_time_zero',
    'cap_user_time_short', 'cap_____res']
struct_anon_188._fields_ = [('cap_bit0', __u64, 1), (
    'cap_bit0_is_deprecated', __u64, 1), ('cap_user_rdpmc', __u64, 1), (
    'cap_user_time', __u64, 1), ('cap_user_time_zero', __u64, 1), (
    'cap_user_time_short', __u64, 1), ('cap_____res', __u64, 58)]


class union_anon_189(Union):
    pass


union_anon_189.__slots__ = ['capabilities', 'unnamed_anon_189_1']
union_anon_189._anonymous_ = ['unnamed_anon_189_1']
union_anon_189._fields_ = [('capabilities', __u64), ('unnamed_anon_189_1',
    struct_anon_188)]


class struct_perf_event_mmap_page(Structure):
    pass


struct_perf_event_mmap_page.__slots__ = ['version', 'compat_version',
    'lock', 'index', 'offset', 'time_enabled', 'time_running',
    'unnamed_perf_event_mmap_page_1', 'pmc_width', 'time_shift',
    'time_mult', 'time_offset', 'time_zero', 'size', '__reserved_1',
    'time_cycles', 'time_mask', '__reserved', 'data_head', 'data_tail',
    'data_offset', 'data_size', 'aux_head', 'aux_tail', 'aux_offset',
    'aux_size']
struct_perf_event_mmap_page._anonymous_ = ['unnamed_perf_event_mmap_page_1']
struct_perf_event_mmap_page._fields_ = [('version', __u32), (
    'compat_version', __u32), ('lock', __u32), ('index', __u32), ('offset',
    __s64), ('time_enabled', __u64), ('time_running', __u64), (
    'unnamed_perf_event_mmap_page_1', union_anon_189), ('pmc_width', __u16),
    ('time_shift', __u16), ('time_mult', __u32), ('time_offset', __u64), (
    'time_zero', __u64), ('size', __u32), ('__reserved_1', __u32), (
    'time_cycles', __u64), ('time_mask', __u64), ('__reserved', __u8 * int(
    116 * 8)), ('data_head', __u64), ('data_tail', __u64), ('data_offset',
    __u64), ('data_size', __u64), ('aux_head', __u64), ('aux_tail', __u64),
    ('aux_offset', __u64), ('aux_size', __u64)]


class struct_perf_event_header(Structure):
    pass


struct_perf_event_header.__slots__ = ['type', 'misc', 'size']
struct_perf_event_header._fields_ = [('type', __u32), ('misc', __u16), (
    'size', __u16)]


class union_epoll_data(Union):
    pass


union_epoll_data.__slots__ = ['ptr', 'fd', 'u32', 'u64']
union_epoll_data._fields_ = [('ptr', POINTER(None)), ('fd', c_int), ('u32',
    uint32_t), ('u64', uint64_t)]
epoll_data_t = union_epoll_data


class struct_epoll_event(Structure):
    pass


struct_epoll_event.__slots__ = ['events', 'data']
struct_epoll_event._fields_ = [('events', uint32_t), ('data', epoll_data_t)]


class struct_statfs(Structure):
    pass


struct_statfs.__slots__ = ['f_type', 'f_bsize', 'f_blocks', 'f_bfree',
    'f_bavail', 'f_files', 'f_ffree', 'f_fsid', 'f_namelen', 'f_frsize',
    'f_flags', 'f_spare']
struct_statfs._fields_ = [('f_type', __fsword_t), ('f_bsize', __fsword_t),
    ('f_blocks', __fsblkcnt_t), ('f_bfree', __fsblkcnt_t), ('f_bavail',
    __fsblkcnt_t), ('f_files', __fsfilcnt_t), ('f_ffree', __fsfilcnt_t), (
    'f_fsid', __fsid_t), ('f_namelen', __fsword_t), ('f_frsize', __fsword_t
    ), ('f_flags', __fsword_t), ('f_spare', __fsword_t * int(4))]


class struct_utsname(Structure):
    pass


struct_utsname.__slots__ = ['sysname', 'nodename', 'release', 'version',
    'machine', 'domainname']
struct_utsname._fields_ = [('sysname', c_char * int(65)), ('nodename', 
    c_char * int(65)), ('release', c_char * int(65)), ('version', c_char *
    int(65)), ('machine', c_char * int(65)), ('domainname', c_char * int(65))]
rlim_t = __rlim_t


class struct_rlimit(Structure):
    pass


struct_rlimit.__slots__ = ['rlim_cur', 'rlim_max']
struct_rlimit._fields_ = [('rlim_cur', rlim_t), ('rlim_max', rlim_t)]
Elf64_Half = uint16_t
Elf64_Word = uint32_t
Elf64_Xword = uint64_t
Elf64_Addr = uint64_t
Elf64_Off = uint64_t
Elf64_Section = uint16_t


class struct_anon_209(Structure):
    pass


struct_anon_209.__slots__ = ['e_ident', 'e_type', 'e_machine', 'e_version',
    'e_entry', 'e_phoff', 'e_shoff', 'e_flags', 'e_ehsize', 'e_phentsize',
    'e_phnum', 'e_shentsize', 'e_shnum', 'e_shstrndx']
struct_anon_209._fields_ = [('e_ident', c_ubyte * int(16)), ('e_type',
    Elf64_Half), ('e_machine', Elf64_Half), ('e_version', Elf64_Word), (
    'e_entry', Elf64_Addr), ('e_phoff', Elf64_Off), ('e_shoff', Elf64_Off),
    ('e_flags', Elf64_Word), ('e_ehsize', Elf64_Half), ('e_phentsize',
    Elf64_Half), ('e_phnum', Elf64_Half), ('e_shentsize', Elf64_Half), (
    'e_shnum', Elf64_Half), ('e_shstrndx', Elf64_Half)]
Elf64_Ehdr = struct_anon_209


class struct_anon_211(Structure):
    pass


struct_anon_211.__slots__ = ['sh_name', 'sh_type', 'sh_flags', 'sh_addr',
    'sh_offset', 'sh_size', 'sh_link', 'sh_info', 'sh_addralign', 'sh_entsize']
struct_anon_211._fields_ = [('sh_name', Elf64_Word), ('sh_type', Elf64_Word
    ), ('sh_flags', Elf64_Xword), ('sh_addr', Elf64_Addr), ('sh_offset',
    Elf64_Off), ('sh_size', Elf64_Xword), ('sh_link', Elf64_Word), (
    'sh_info', Elf64_Word), ('sh_addralign', Elf64_Xword), ('sh_entsize',
    Elf64_Xword)]
Elf64_Shdr = struct_anon_211


class struct_anon_215(Structure):
    pass


struct_anon_215.__slots__ = ['st_name', 'st_info', 'st_other', 'st_shndx',
    'st_value', 'st_size']
struct_anon_215._fields_ = [('st_name', Elf64_Word), ('st_info', c_ubyte),
    ('st_other', c_ubyte), ('st_shndx', Elf64_Section), ('st_value',
    Elf64_Addr), ('st_size', Elf64_Xword)]
Elf64_Sym = struct_anon_215


class struct_anon_219(Structure):
    pass


struct_anon_219.__slots__ = ['r_offset', 'r_info']
struct_anon_219._fields_ = [('r_offset', Elf64_Addr), ('r_info', Elf64_Xword)]
Elf64_Rel = struct_anon_219
enum_anon_254 = c_int
Elf_Type = enum_anon_254


class struct_anon_255(Structure):
    pass


struct_anon_255.__slots__ = ['d_buf', 'd_type', 'd_version', 'd_size',
    'd_off', 'd_align']
struct_anon_255._fields_ = [('d_buf', POINTER(None)), ('d_type', Elf_Type),
    ('d_version', c_uint), ('d_size', c_size_t), ('d_off', c_int64), (
    'd_align', c_size_t)]
Elf_Data = struct_anon_255


class struct_Elf(Structure):
    pass


Elf = struct_Elf


class struct_Elf_Scn(Structure):
    pass


Elf_Scn = struct_Elf_Scn


class struct_gzFile_s(Structure):
    pass


gzFile = POINTER(struct_gzFile_s)
struct_gzFile_s.__slots__ = ['have', 'next', 'pos']
struct_gzFile_s._fields_ = [('have', c_uint), ('next', POINTER(c_ubyte)), (
    'pos', c_int64)]


class struct_bpf_program(Structure):
    pass


class struct_bpf_map(Structure):
    pass


class struct_btf(Structure):
    pass


class struct_btf_ext(Structure):
    pass


if _libs['libbpf.so.1'].has('libbpf_major_version', 'cdecl'):
    libbpf_major_version = _libs['libbpf.so.1'].get('libbpf_major_version',
        'cdecl')
    libbpf_major_version.argtypes = []
    libbpf_major_version.restype = __u32
if _libs['libbpf.so.1'].has('libbpf_minor_version', 'cdecl'):
    libbpf_minor_version = _libs['libbpf.so.1'].get('libbpf_minor_version',
        'cdecl')
    libbpf_minor_version.argtypes = []
    libbpf_minor_version.restype = __u32
if _libs['libbpf.so.1'].has('libbpf_version_string', 'cdecl'):
    libbpf_version_string = _libs['libbpf.so.1'].get('libbpf_version_string',
        'cdecl')
    libbpf_version_string.argtypes = []
    libbpf_version_string.restype = c_char_p
enum_libbpf_errno = c_int
__LIBBPF_ERRNO__START = 4000
LIBBPF_ERRNO__LIBELF = __LIBBPF_ERRNO__START
LIBBPF_ERRNO__FORMAT = LIBBPF_ERRNO__LIBELF + 1
LIBBPF_ERRNO__KVERSION = LIBBPF_ERRNO__FORMAT + 1
LIBBPF_ERRNO__ENDIAN = LIBBPF_ERRNO__KVERSION + 1
LIBBPF_ERRNO__INTERNAL = LIBBPF_ERRNO__ENDIAN + 1
LIBBPF_ERRNO__RELOC = LIBBPF_ERRNO__INTERNAL + 1
LIBBPF_ERRNO__LOAD = LIBBPF_ERRNO__RELOC + 1
LIBBPF_ERRNO__VERIFY = LIBBPF_ERRNO__LOAD + 1
LIBBPF_ERRNO__PROG2BIG = LIBBPF_ERRNO__VERIFY + 1
LIBBPF_ERRNO__KVER = LIBBPF_ERRNO__PROG2BIG + 1
LIBBPF_ERRNO__PROGTYPE = LIBBPF_ERRNO__KVER + 1
LIBBPF_ERRNO__WRNGPID = LIBBPF_ERRNO__PROGTYPE + 1
LIBBPF_ERRNO__INVSEQ = LIBBPF_ERRNO__WRNGPID + 1
LIBBPF_ERRNO__NLPARSE = LIBBPF_ERRNO__INVSEQ + 1
__LIBBPF_ERRNO__END = LIBBPF_ERRNO__NLPARSE + 1
if _libs['libbpf.so.1'].has('libbpf_strerror', 'cdecl'):
    libbpf_strerror = _libs['libbpf.so.1'].get('libbpf_strerror', 'cdecl')
    libbpf_strerror.argtypes = [c_int, String, c_size_t]
    libbpf_strerror.restype = c_int
if _libs['libbpf.so.1'].has('libbpf_bpf_attach_type_str', 'cdecl'):
    libbpf_bpf_attach_type_str = _libs['libbpf.so.1'].get(
        'libbpf_bpf_attach_type_str', 'cdecl')
    libbpf_bpf_attach_type_str.argtypes = [enum_bpf_attach_type]
    libbpf_bpf_attach_type_str.restype = c_char_p
if _libs['libbpf.so.1'].has('libbpf_bpf_link_type_str', 'cdecl'):
    libbpf_bpf_link_type_str = _libs['libbpf.so.1'].get(
        'libbpf_bpf_link_type_str', 'cdecl')
    libbpf_bpf_link_type_str.argtypes = [enum_bpf_link_type]
    libbpf_bpf_link_type_str.restype = c_char_p
if _libs['libbpf.so.1'].has('libbpf_bpf_map_type_str', 'cdecl'):
    libbpf_bpf_map_type_str = _libs['libbpf.so.1'].get(
        'libbpf_bpf_map_type_str', 'cdecl')
    libbpf_bpf_map_type_str.argtypes = [enum_bpf_map_type]
    libbpf_bpf_map_type_str.restype = c_char_p
if _libs['libbpf.so.1'].has('libbpf_bpf_prog_type_str', 'cdecl'):
    libbpf_bpf_prog_type_str = _libs['libbpf.so.1'].get(
        'libbpf_bpf_prog_type_str', 'cdecl')
    libbpf_bpf_prog_type_str.argtypes = [enum_bpf_prog_type]
    libbpf_bpf_prog_type_str.restype = c_char_p
enum_libbpf_print_level = c_int
LIBBPF_WARN = 0
LIBBPF_INFO = LIBBPF_WARN + 1
LIBBPF_DEBUG = LIBBPF_INFO + 1
libbpf_print_fn_t = CFUNCTYPE(UNCHECKED(c_int), enum_libbpf_print_level,
    String, c_void_p)
if _libs['libbpf.so.1'].has('libbpf_set_print', 'cdecl'):
    libbpf_set_print = _libs['libbpf.so.1'].get('libbpf_set_print', 'cdecl')
    libbpf_set_print.argtypes = [libbpf_print_fn_t]
    libbpf_set_print.restype = libbpf_print_fn_t


class struct_bpf_object(Structure):
    pass


class struct_bpf_object_open_opts(Structure):
    pass


struct_bpf_object_open_opts.__slots__ = ['sz', 'object_name',
    'relaxed_maps', 'pin_root_path', 'unnamed_bpf_object_open_opts_1',
    'kconfig', 'btf_custom_path', 'kernel_log_buf', 'kernel_log_size',
    'kernel_log_level', 'bpf_token_path', 'unnamed_bpf_object_open_opts_2']
struct_bpf_object_open_opts._fields_ = [('sz', c_size_t), ('object_name',
    String), ('relaxed_maps', c_bool), ('pin_root_path', String), (
    'unnamed_bpf_object_open_opts_1', __u32, 32), ('kconfig', String), (
    'btf_custom_path', String), ('kernel_log_buf', String), (
    'kernel_log_size', c_size_t), ('kernel_log_level', __u32), (
    'bpf_token_path', String)]
if _libs['libbpf.so.1'].has('bpf_object__open', 'cdecl'):
    bpf_object__open = _libs['libbpf.so.1'].get('bpf_object__open', 'cdecl')
    bpf_object__open.argtypes = [String]
    bpf_object__open.restype = POINTER(struct_bpf_object)
if _libs['libbpf.so.1'].has('bpf_object__open_file', 'cdecl'):
    bpf_object__open_file = _libs['libbpf.so.1'].get('bpf_object__open_file',
        'cdecl')
    bpf_object__open_file.argtypes = [String, POINTER(
        struct_bpf_object_open_opts)]
    bpf_object__open_file.restype = POINTER(struct_bpf_object)
if _libs['libbpf.so.1'].has('bpf_object__open_mem', 'cdecl'):
    bpf_object__open_mem = _libs['libbpf.so.1'].get('bpf_object__open_mem',
        'cdecl')
    bpf_object__open_mem.argtypes = [POINTER(None), c_size_t, POINTER(
        struct_bpf_object_open_opts)]
    bpf_object__open_mem.restype = POINTER(struct_bpf_object)
if _libs['libbpf.so.1'].has('bpf_object__load', 'cdecl'):
    bpf_object__load = _libs['libbpf.so.1'].get('bpf_object__load', 'cdecl')
    bpf_object__load.argtypes = [POINTER(struct_bpf_object)]
    bpf_object__load.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__close', 'cdecl'):
    bpf_object__close = _libs['libbpf.so.1'].get('bpf_object__close', 'cdecl')
    bpf_object__close.argtypes = [POINTER(struct_bpf_object)]
    bpf_object__close.restype = None
if _libs['libbpf.so.1'].has('bpf_object__pin_maps', 'cdecl'):
    bpf_object__pin_maps = _libs['libbpf.so.1'].get('bpf_object__pin_maps',
        'cdecl')
    bpf_object__pin_maps.argtypes = [POINTER(struct_bpf_object), String]
    bpf_object__pin_maps.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__unpin_maps', 'cdecl'):
    bpf_object__unpin_maps = _libs['libbpf.so.1'].get('bpf_object__unpin_maps',
        'cdecl')
    bpf_object__unpin_maps.argtypes = [POINTER(struct_bpf_object), String]
    bpf_object__unpin_maps.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__pin_programs', 'cdecl'):
    bpf_object__pin_programs = _libs['libbpf.so.1'].get(
        'bpf_object__pin_programs', 'cdecl')
    bpf_object__pin_programs.argtypes = [POINTER(struct_bpf_object), String]
    bpf_object__pin_programs.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__unpin_programs', 'cdecl'):
    bpf_object__unpin_programs = _libs['libbpf.so.1'].get(
        'bpf_object__unpin_programs', 'cdecl')
    bpf_object__unpin_programs.argtypes = [POINTER(struct_bpf_object), String]
    bpf_object__unpin_programs.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__pin', 'cdecl'):
    bpf_object__pin = _libs['libbpf.so.1'].get('bpf_object__pin', 'cdecl')
    bpf_object__pin.argtypes = [POINTER(struct_bpf_object), String]
    bpf_object__pin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__unpin', 'cdecl'):
    bpf_object__unpin = _libs['libbpf.so.1'].get('bpf_object__unpin', 'cdecl')
    bpf_object__unpin.argtypes = [POINTER(struct_bpf_object), String]
    bpf_object__unpin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__name', 'cdecl'):
    bpf_object__name = _libs['libbpf.so.1'].get('bpf_object__name', 'cdecl')
    bpf_object__name.argtypes = [POINTER(struct_bpf_object)]
    bpf_object__name.restype = c_char_p
if _libs['libbpf.so.1'].has('bpf_object__kversion', 'cdecl'):
    bpf_object__kversion = _libs['libbpf.so.1'].get('bpf_object__kversion',
        'cdecl')
    bpf_object__kversion.argtypes = [POINTER(struct_bpf_object)]
    bpf_object__kversion.restype = c_uint
if _libs['libbpf.so.1'].has('bpf_object__set_kversion', 'cdecl'):
    bpf_object__set_kversion = _libs['libbpf.so.1'].get(
        'bpf_object__set_kversion', 'cdecl')
    bpf_object__set_kversion.argtypes = [POINTER(struct_bpf_object), __u32]
    bpf_object__set_kversion.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__btf', 'cdecl'):
    bpf_object__btf = _libs['libbpf.so.1'].get('bpf_object__btf', 'cdecl')
    bpf_object__btf.argtypes = [POINTER(struct_bpf_object)]
    bpf_object__btf.restype = POINTER(struct_btf)
if _libs['libbpf.so.1'].has('bpf_object__btf_fd', 'cdecl'):
    bpf_object__btf_fd = _libs['libbpf.so.1'].get('bpf_object__btf_fd', 'cdecl'
        )
    bpf_object__btf_fd.argtypes = [POINTER(struct_bpf_object)]
    bpf_object__btf_fd.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__find_program_by_name', 'cdecl'):
    bpf_object__find_program_by_name = _libs['libbpf.so.1'].get(
        'bpf_object__find_program_by_name', 'cdecl')
    bpf_object__find_program_by_name.argtypes = [POINTER(struct_bpf_object),
        String]
    bpf_object__find_program_by_name.restype = POINTER(struct_bpf_program)
if _libs['libbpf.so.1'].has('libbpf_prog_type_by_name', 'cdecl'):
    libbpf_prog_type_by_name = _libs['libbpf.so.1'].get(
        'libbpf_prog_type_by_name', 'cdecl')
    libbpf_prog_type_by_name.argtypes = [String, POINTER(enum_bpf_prog_type
        ), POINTER(enum_bpf_attach_type)]
    libbpf_prog_type_by_name.restype = c_int
if _libs['libbpf.so.1'].has('libbpf_attach_type_by_name', 'cdecl'):
    libbpf_attach_type_by_name = _libs['libbpf.so.1'].get(
        'libbpf_attach_type_by_name', 'cdecl')
    libbpf_attach_type_by_name.argtypes = [String, POINTER(
        enum_bpf_attach_type)]
    libbpf_attach_type_by_name.restype = c_int
if _libs['libbpf.so.1'].has('libbpf_find_vmlinux_btf_id', 'cdecl'):
    libbpf_find_vmlinux_btf_id = _libs['libbpf.so.1'].get(
        'libbpf_find_vmlinux_btf_id', 'cdecl')
    libbpf_find_vmlinux_btf_id.argtypes = [String, enum_bpf_attach_type]
    libbpf_find_vmlinux_btf_id.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__next_program', 'cdecl'):
    bpf_object__next_program = _libs['libbpf.so.1'].get(
        'bpf_object__next_program', 'cdecl')
    bpf_object__next_program.argtypes = [POINTER(struct_bpf_object),
        POINTER(struct_bpf_program)]
    bpf_object__next_program.restype = POINTER(struct_bpf_program)
if _libs['libbpf.so.1'].has('bpf_object__prev_program', 'cdecl'):
    bpf_object__prev_program = _libs['libbpf.so.1'].get(
        'bpf_object__prev_program', 'cdecl')
    bpf_object__prev_program.argtypes = [POINTER(struct_bpf_object),
        POINTER(struct_bpf_program)]
    bpf_object__prev_program.restype = POINTER(struct_bpf_program)
if _libs['libbpf.so.1'].has('bpf_program__set_ifindex', 'cdecl'):
    bpf_program__set_ifindex = _libs['libbpf.so.1'].get(
        'bpf_program__set_ifindex', 'cdecl')
    bpf_program__set_ifindex.argtypes = [POINTER(struct_bpf_program), __u32]
    bpf_program__set_ifindex.restype = None
if _libs['libbpf.so.1'].has('bpf_program__name', 'cdecl'):
    bpf_program__name = _libs['libbpf.so.1'].get('bpf_program__name', 'cdecl')
    bpf_program__name.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__name.restype = c_char_p
if _libs['libbpf.so.1'].has('bpf_program__section_name', 'cdecl'):
    bpf_program__section_name = _libs['libbpf.so.1'].get(
        'bpf_program__section_name', 'cdecl')
    bpf_program__section_name.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__section_name.restype = c_char_p
if _libs['libbpf.so.1'].has('bpf_program__autoload', 'cdecl'):
    bpf_program__autoload = _libs['libbpf.so.1'].get('bpf_program__autoload',
        'cdecl')
    bpf_program__autoload.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__autoload.restype = c_bool
if _libs['libbpf.so.1'].has('bpf_program__set_autoload', 'cdecl'):
    bpf_program__set_autoload = _libs['libbpf.so.1'].get(
        'bpf_program__set_autoload', 'cdecl')
    bpf_program__set_autoload.argtypes = [POINTER(struct_bpf_program), c_bool]
    bpf_program__set_autoload.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__autoattach', 'cdecl'):
    bpf_program__autoattach = _libs['libbpf.so.1'].get(
        'bpf_program__autoattach', 'cdecl')
    bpf_program__autoattach.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__autoattach.restype = c_bool
if _libs['libbpf.so.1'].has('bpf_program__set_autoattach', 'cdecl'):
    bpf_program__set_autoattach = _libs['libbpf.so.1'].get(
        'bpf_program__set_autoattach', 'cdecl')
    bpf_program__set_autoattach.argtypes = [POINTER(struct_bpf_program), c_bool
        ]
    bpf_program__set_autoattach.restype = None
if _libs['libbpf.so.1'].has('bpf_program__insns', 'cdecl'):
    bpf_program__insns = _libs['libbpf.so.1'].get('bpf_program__insns', 'cdecl'
        )
    bpf_program__insns.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__insns.restype = POINTER(struct_bpf_insn)
if _libs['libbpf.so.1'].has('bpf_program__set_insns', 'cdecl'):
    bpf_program__set_insns = _libs['libbpf.so.1'].get('bpf_program__set_insns',
        'cdecl')
    bpf_program__set_insns.argtypes = [POINTER(struct_bpf_program), POINTER
        (struct_bpf_insn), c_size_t]
    bpf_program__set_insns.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__insn_cnt', 'cdecl'):
    bpf_program__insn_cnt = _libs['libbpf.so.1'].get('bpf_program__insn_cnt',
        'cdecl')
    bpf_program__insn_cnt.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__insn_cnt.restype = c_size_t
if _libs['libbpf.so.1'].has('bpf_program__fd', 'cdecl'):
    bpf_program__fd = _libs['libbpf.so.1'].get('bpf_program__fd', 'cdecl')
    bpf_program__fd.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__fd.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__pin', 'cdecl'):
    bpf_program__pin = _libs['libbpf.so.1'].get('bpf_program__pin', 'cdecl')
    bpf_program__pin.argtypes = [POINTER(struct_bpf_program), String]
    bpf_program__pin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__unpin', 'cdecl'):
    bpf_program__unpin = _libs['libbpf.so.1'].get('bpf_program__unpin', 'cdecl'
        )
    bpf_program__unpin.argtypes = [POINTER(struct_bpf_program), String]
    bpf_program__unpin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__unload', 'cdecl'):
    bpf_program__unload = _libs['libbpf.so.1'].get('bpf_program__unload',
        'cdecl')
    bpf_program__unload.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__unload.restype = None


class struct_bpf_link(Structure):
    pass


if _libs['libbpf.so.1'].has('bpf_link__open', 'cdecl'):
    bpf_link__open = _libs['libbpf.so.1'].get('bpf_link__open', 'cdecl')
    bpf_link__open.argtypes = [String]
    bpf_link__open.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_link__fd', 'cdecl'):
    bpf_link__fd = _libs['libbpf.so.1'].get('bpf_link__fd', 'cdecl')
    bpf_link__fd.argtypes = [POINTER(struct_bpf_link)]
    bpf_link__fd.restype = c_int
if _libs['libbpf.so.1'].has('bpf_link__pin_path', 'cdecl'):
    bpf_link__pin_path = _libs['libbpf.so.1'].get('bpf_link__pin_path', 'cdecl'
        )
    bpf_link__pin_path.argtypes = [POINTER(struct_bpf_link)]
    bpf_link__pin_path.restype = c_char_p
if _libs['libbpf.so.1'].has('bpf_link__pin', 'cdecl'):
    bpf_link__pin = _libs['libbpf.so.1'].get('bpf_link__pin', 'cdecl')
    bpf_link__pin.argtypes = [POINTER(struct_bpf_link), String]
    bpf_link__pin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_link__unpin', 'cdecl'):
    bpf_link__unpin = _libs['libbpf.so.1'].get('bpf_link__unpin', 'cdecl')
    bpf_link__unpin.argtypes = [POINTER(struct_bpf_link)]
    bpf_link__unpin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_link__update_program', 'cdecl'):
    bpf_link__update_program = _libs['libbpf.so.1'].get(
        'bpf_link__update_program', 'cdecl')
    bpf_link__update_program.argtypes = [POINTER(struct_bpf_link), POINTER(
        struct_bpf_program)]
    bpf_link__update_program.restype = c_int
if _libs['libbpf.so.1'].has('bpf_link__disconnect', 'cdecl'):
    bpf_link__disconnect = _libs['libbpf.so.1'].get('bpf_link__disconnect',
        'cdecl')
    bpf_link__disconnect.argtypes = [POINTER(struct_bpf_link)]
    bpf_link__disconnect.restype = None
if _libs['libbpf.so.1'].has('bpf_link__detach', 'cdecl'):
    bpf_link__detach = _libs['libbpf.so.1'].get('bpf_link__detach', 'cdecl')
    bpf_link__detach.argtypes = [POINTER(struct_bpf_link)]
    bpf_link__detach.restype = c_int
if _libs['libbpf.so.1'].has('bpf_link__destroy', 'cdecl'):
    bpf_link__destroy = _libs['libbpf.so.1'].get('bpf_link__destroy', 'cdecl')
    bpf_link__destroy.argtypes = [POINTER(struct_bpf_link)]
    bpf_link__destroy.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__attach', 'cdecl'):
    bpf_program__attach = _libs['libbpf.so.1'].get('bpf_program__attach',
        'cdecl')
    bpf_program__attach.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__attach.restype = POINTER(struct_bpf_link)


class struct_bpf_perf_event_opts(Structure):
    pass


struct_bpf_perf_event_opts.__slots__ = ['sz', 'bpf_cookie',
    'force_ioctl_attach', 'unnamed_bpf_perf_event_opts_1']
struct_bpf_perf_event_opts._fields_ = [('sz', c_size_t), ('bpf_cookie',
    __u64), ('force_ioctl_attach', c_bool)]
if _libs['libbpf.so.1'].has('bpf_program__attach_perf_event', 'cdecl'):
    bpf_program__attach_perf_event = _libs['libbpf.so.1'].get(
        'bpf_program__attach_perf_event', 'cdecl')
    bpf_program__attach_perf_event.argtypes = [POINTER(struct_bpf_program),
        c_int]
    bpf_program__attach_perf_event.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_perf_event_opts', 'cdecl'):
    bpf_program__attach_perf_event_opts = _libs['libbpf.so.1'].get(
        'bpf_program__attach_perf_event_opts', 'cdecl')
    bpf_program__attach_perf_event_opts.argtypes = [POINTER(
        struct_bpf_program), c_int, POINTER(struct_bpf_perf_event_opts)]
    bpf_program__attach_perf_event_opts.restype = POINTER(struct_bpf_link)
enum_probe_attach_mode = c_int
PROBE_ATTACH_MODE_DEFAULT = 0
PROBE_ATTACH_MODE_LEGACY = PROBE_ATTACH_MODE_DEFAULT + 1
PROBE_ATTACH_MODE_PERF = PROBE_ATTACH_MODE_LEGACY + 1
PROBE_ATTACH_MODE_LINK = PROBE_ATTACH_MODE_PERF + 1


class struct_bpf_kprobe_opts(Structure):
    pass


struct_bpf_kprobe_opts.__slots__ = ['sz', 'bpf_cookie', 'offset',
    'retprobe', 'attach_mode', 'unnamed_bpf_kprobe_opts_1']
struct_bpf_kprobe_opts._fields_ = [('sz', c_size_t), ('bpf_cookie', __u64),
    ('offset', c_size_t), ('retprobe', c_bool), ('attach_mode',
    enum_probe_attach_mode)]
if _libs['libbpf.so.1'].has('bpf_program__attach_kprobe', 'cdecl'):
    bpf_program__attach_kprobe = _libs['libbpf.so.1'].get(
        'bpf_program__attach_kprobe', 'cdecl')
    bpf_program__attach_kprobe.argtypes = [POINTER(struct_bpf_program),
        c_bool, String]
    bpf_program__attach_kprobe.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_kprobe_opts', 'cdecl'):
    bpf_program__attach_kprobe_opts = _libs['libbpf.so.1'].get(
        'bpf_program__attach_kprobe_opts', 'cdecl')
    bpf_program__attach_kprobe_opts.argtypes = [POINTER(struct_bpf_program),
        String, POINTER(struct_bpf_kprobe_opts)]
    bpf_program__attach_kprobe_opts.restype = POINTER(struct_bpf_link)


class struct_bpf_kprobe_multi_opts(Structure):
    pass


struct_bpf_kprobe_multi_opts.__slots__ = ['sz', 'syms', 'addrs', 'cookies',
    'cnt', 'retprobe', 'unnamed_bpf_kprobe_multi_opts_1']
struct_bpf_kprobe_multi_opts._fields_ = [('sz', c_size_t), ('syms', POINTER
    (POINTER(c_char))), ('addrs', POINTER(c_ulong)), ('cookies', POINTER(
    __u64)), ('cnt', c_size_t), ('retprobe', c_bool)]
if _libs['libbpf.so.1'].has('bpf_program__attach_kprobe_multi_opts', 'cdecl'):
    bpf_program__attach_kprobe_multi_opts = _libs['libbpf.so.1'].get(
        'bpf_program__attach_kprobe_multi_opts', 'cdecl')
    bpf_program__attach_kprobe_multi_opts.argtypes = [POINTER(
        struct_bpf_program), String, POINTER(struct_bpf_kprobe_multi_opts)]
    bpf_program__attach_kprobe_multi_opts.restype = POINTER(struct_bpf_link)


class struct_bpf_uprobe_multi_opts(Structure):
    pass


struct_bpf_uprobe_multi_opts.__slots__ = ['sz', 'syms', 'offsets',
    'ref_ctr_offsets', 'cookies', 'cnt', 'retprobe',
    'unnamed_bpf_uprobe_multi_opts_1']
struct_bpf_uprobe_multi_opts._fields_ = [('sz', c_size_t), ('syms', POINTER
    (POINTER(c_char))), ('offsets', POINTER(c_ulong)), ('ref_ctr_offsets',
    POINTER(c_ulong)), ('cookies', POINTER(__u64)), ('cnt', c_size_t), (
    'retprobe', c_bool)]
if _libs['libbpf.so.1'].has('bpf_program__attach_uprobe_multi', 'cdecl'):
    bpf_program__attach_uprobe_multi = _libs['libbpf.so.1'].get(
        'bpf_program__attach_uprobe_multi', 'cdecl')
    bpf_program__attach_uprobe_multi.argtypes = [POINTER(struct_bpf_program
        ), pid_t, String, String, POINTER(struct_bpf_uprobe_multi_opts)]
    bpf_program__attach_uprobe_multi.restype = POINTER(struct_bpf_link)


class struct_bpf_ksyscall_opts(Structure):
    pass


struct_bpf_ksyscall_opts.__slots__ = ['sz', 'bpf_cookie', 'retprobe',
    'unnamed_bpf_ksyscall_opts_1']
struct_bpf_ksyscall_opts._fields_ = [('sz', c_size_t), ('bpf_cookie', __u64
    ), ('retprobe', c_bool)]
if _libs['libbpf.so.1'].has('bpf_program__attach_ksyscall', 'cdecl'):
    bpf_program__attach_ksyscall = _libs['libbpf.so.1'].get(
        'bpf_program__attach_ksyscall', 'cdecl')
    bpf_program__attach_ksyscall.argtypes = [POINTER(struct_bpf_program),
        String, POINTER(struct_bpf_ksyscall_opts)]
    bpf_program__attach_ksyscall.restype = POINTER(struct_bpf_link)


class struct_bpf_uprobe_opts(Structure):
    pass


struct_bpf_uprobe_opts.__slots__ = ['sz', 'ref_ctr_offset', 'bpf_cookie',
    'retprobe', 'func_name', 'attach_mode', 'unnamed_bpf_uprobe_opts_1']
struct_bpf_uprobe_opts._fields_ = [('sz', c_size_t), ('ref_ctr_offset',
    c_size_t), ('bpf_cookie', __u64), ('retprobe', c_bool), ('func_name',
    String), ('attach_mode', enum_probe_attach_mode)]
if _libs['libbpf.so.1'].has('bpf_program__attach_uprobe', 'cdecl'):
    bpf_program__attach_uprobe = _libs['libbpf.so.1'].get(
        'bpf_program__attach_uprobe', 'cdecl')
    bpf_program__attach_uprobe.argtypes = [POINTER(struct_bpf_program),
        c_bool, pid_t, String, c_size_t]
    bpf_program__attach_uprobe.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_uprobe_opts', 'cdecl'):
    bpf_program__attach_uprobe_opts = _libs['libbpf.so.1'].get(
        'bpf_program__attach_uprobe_opts', 'cdecl')
    bpf_program__attach_uprobe_opts.argtypes = [POINTER(struct_bpf_program),
        pid_t, String, c_size_t, POINTER(struct_bpf_uprobe_opts)]
    bpf_program__attach_uprobe_opts.restype = POINTER(struct_bpf_link)


class struct_bpf_usdt_opts(Structure):
    pass


struct_bpf_usdt_opts.__slots__ = ['sz', 'usdt_cookie',
    'unnamed_bpf_usdt_opts_1']
struct_bpf_usdt_opts._fields_ = [('sz', c_size_t), ('usdt_cookie', __u64)]
if _libs['libbpf.so.1'].has('bpf_program__attach_usdt', 'cdecl'):
    bpf_program__attach_usdt = _libs['libbpf.so.1'].get(
        'bpf_program__attach_usdt', 'cdecl')
    bpf_program__attach_usdt.argtypes = [POINTER(struct_bpf_program), pid_t,
        String, String, String, POINTER(struct_bpf_usdt_opts)]
    bpf_program__attach_usdt.restype = POINTER(struct_bpf_link)


class struct_bpf_tracepoint_opts(Structure):
    pass


struct_bpf_tracepoint_opts.__slots__ = ['sz', 'bpf_cookie']
struct_bpf_tracepoint_opts._fields_ = [('sz', c_size_t), ('bpf_cookie', __u64)]
if _libs['libbpf.so.1'].has('bpf_program__attach_tracepoint', 'cdecl'):
    bpf_program__attach_tracepoint = _libs['libbpf.so.1'].get(
        'bpf_program__attach_tracepoint', 'cdecl')
    bpf_program__attach_tracepoint.argtypes = [POINTER(struct_bpf_program),
        String, String]
    bpf_program__attach_tracepoint.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_tracepoint_opts', 'cdecl'):
    bpf_program__attach_tracepoint_opts = _libs['libbpf.so.1'].get(
        'bpf_program__attach_tracepoint_opts', 'cdecl')
    bpf_program__attach_tracepoint_opts.argtypes = [POINTER(
        struct_bpf_program), String, String, POINTER(
        struct_bpf_tracepoint_opts)]
    bpf_program__attach_tracepoint_opts.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_raw_tracepoint', 'cdecl'):
    bpf_program__attach_raw_tracepoint = _libs['libbpf.so.1'].get(
        'bpf_program__attach_raw_tracepoint', 'cdecl')
    bpf_program__attach_raw_tracepoint.argtypes = [POINTER(
        struct_bpf_program), String]
    bpf_program__attach_raw_tracepoint.restype = POINTER(struct_bpf_link)


class struct_bpf_trace_opts(Structure):
    pass


struct_bpf_trace_opts.__slots__ = ['sz', 'cookie']
struct_bpf_trace_opts._fields_ = [('sz', c_size_t), ('cookie', __u64)]
if _libs['libbpf.so.1'].has('bpf_program__attach_trace', 'cdecl'):
    bpf_program__attach_trace = _libs['libbpf.so.1'].get(
        'bpf_program__attach_trace', 'cdecl')
    bpf_program__attach_trace.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__attach_trace.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_trace_opts', 'cdecl'):
    bpf_program__attach_trace_opts = _libs['libbpf.so.1'].get(
        'bpf_program__attach_trace_opts', 'cdecl')
    bpf_program__attach_trace_opts.argtypes = [POINTER(struct_bpf_program),
        POINTER(struct_bpf_trace_opts)]
    bpf_program__attach_trace_opts.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_lsm', 'cdecl'):
    bpf_program__attach_lsm = _libs['libbpf.so.1'].get(
        'bpf_program__attach_lsm', 'cdecl')
    bpf_program__attach_lsm.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__attach_lsm.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_cgroup', 'cdecl'):
    bpf_program__attach_cgroup = _libs['libbpf.so.1'].get(
        'bpf_program__attach_cgroup', 'cdecl')
    bpf_program__attach_cgroup.argtypes = [POINTER(struct_bpf_program), c_int]
    bpf_program__attach_cgroup.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_netns', 'cdecl'):
    bpf_program__attach_netns = _libs['libbpf.so.1'].get(
        'bpf_program__attach_netns', 'cdecl')
    bpf_program__attach_netns.argtypes = [POINTER(struct_bpf_program), c_int]
    bpf_program__attach_netns.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_xdp', 'cdecl'):
    bpf_program__attach_xdp = _libs['libbpf.so.1'].get(
        'bpf_program__attach_xdp', 'cdecl')
    bpf_program__attach_xdp.argtypes = [POINTER(struct_bpf_program), c_int]
    bpf_program__attach_xdp.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__attach_freplace', 'cdecl'):
    bpf_program__attach_freplace = _libs['libbpf.so.1'].get(
        'bpf_program__attach_freplace', 'cdecl')
    bpf_program__attach_freplace.argtypes = [POINTER(struct_bpf_program),
        c_int, String]
    bpf_program__attach_freplace.restype = POINTER(struct_bpf_link)


class struct_bpf_netfilter_opts(Structure):
    pass


struct_bpf_netfilter_opts.__slots__ = ['sz', 'pf', 'hooknum', 'priority',
    'flags']
struct_bpf_netfilter_opts._fields_ = [('sz', c_size_t), ('pf', __u32), (
    'hooknum', __u32), ('priority', __s32), ('flags', __u32)]
if _libs['libbpf.so.1'].has('bpf_program__attach_netfilter', 'cdecl'):
    bpf_program__attach_netfilter = _libs['libbpf.so.1'].get(
        'bpf_program__attach_netfilter', 'cdecl')
    bpf_program__attach_netfilter.argtypes = [POINTER(struct_bpf_program),
        POINTER(struct_bpf_netfilter_opts)]
    bpf_program__attach_netfilter.restype = POINTER(struct_bpf_link)


class struct_bpf_tcx_opts(Structure):
    pass


struct_bpf_tcx_opts.__slots__ = ['sz', 'flags', 'relative_fd',
    'relative_id', 'expected_revision', 'unnamed_bpf_tcx_opts_1']
struct_bpf_tcx_opts._fields_ = [('sz', c_size_t), ('flags', __u32), (
    'relative_fd', __u32), ('relative_id', __u32), ('expected_revision', __u64)
    ]
if _libs['libbpf.so.1'].has('bpf_program__attach_tcx', 'cdecl'):
    bpf_program__attach_tcx = _libs['libbpf.so.1'].get(
        'bpf_program__attach_tcx', 'cdecl')
    bpf_program__attach_tcx.argtypes = [POINTER(struct_bpf_program), c_int,
        POINTER(struct_bpf_tcx_opts)]
    bpf_program__attach_tcx.restype = POINTER(struct_bpf_link)


class struct_bpf_netkit_opts(Structure):
    pass


struct_bpf_netkit_opts.__slots__ = ['sz', 'flags', 'relative_fd',
    'relative_id', 'expected_revision', 'unnamed_bpf_netkit_opts_1']
struct_bpf_netkit_opts._fields_ = [('sz', c_size_t), ('flags', __u32), (
    'relative_fd', __u32), ('relative_id', __u32), ('expected_revision', __u64)
    ]
if _libs['libbpf.so.1'].has('bpf_program__attach_netkit', 'cdecl'):
    bpf_program__attach_netkit = _libs['libbpf.so.1'].get(
        'bpf_program__attach_netkit', 'cdecl')
    bpf_program__attach_netkit.argtypes = [POINTER(struct_bpf_program),
        c_int, POINTER(struct_bpf_netkit_opts)]
    bpf_program__attach_netkit.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_map__attach_struct_ops', 'cdecl'):
    bpf_map__attach_struct_ops = _libs['libbpf.so.1'].get(
        'bpf_map__attach_struct_ops', 'cdecl')
    bpf_map__attach_struct_ops.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__attach_struct_ops.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_link__update_map', 'cdecl'):
    bpf_link__update_map = _libs['libbpf.so.1'].get('bpf_link__update_map',
        'cdecl')
    bpf_link__update_map.argtypes = [POINTER(struct_bpf_link), POINTER(
        struct_bpf_map)]
    bpf_link__update_map.restype = c_int


class struct_bpf_iter_attach_opts(Structure):
    pass


struct_bpf_iter_attach_opts.__slots__ = ['sz', 'link_info', 'link_info_len']
struct_bpf_iter_attach_opts._fields_ = [('sz', c_size_t), ('link_info',
    POINTER(union_bpf_iter_link_info)), ('link_info_len', __u32)]
if _libs['libbpf.so.1'].has('bpf_program__attach_iter', 'cdecl'):
    bpf_program__attach_iter = _libs['libbpf.so.1'].get(
        'bpf_program__attach_iter', 'cdecl')
    bpf_program__attach_iter.argtypes = [POINTER(struct_bpf_program),
        POINTER(struct_bpf_iter_attach_opts)]
    bpf_program__attach_iter.restype = POINTER(struct_bpf_link)
if _libs['libbpf.so.1'].has('bpf_program__type', 'cdecl'):
    bpf_program__type = _libs['libbpf.so.1'].get('bpf_program__type', 'cdecl')
    bpf_program__type.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__type.restype = enum_bpf_prog_type
if _libs['libbpf.so.1'].has('bpf_program__set_type', 'cdecl'):
    bpf_program__set_type = _libs['libbpf.so.1'].get('bpf_program__set_type',
        'cdecl')
    bpf_program__set_type.argtypes = [POINTER(struct_bpf_program),
        enum_bpf_prog_type]
    bpf_program__set_type.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__expected_attach_type', 'cdecl'):
    bpf_program__expected_attach_type = _libs['libbpf.so.1'].get(
        'bpf_program__expected_attach_type', 'cdecl')
    bpf_program__expected_attach_type.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__expected_attach_type.restype = enum_bpf_attach_type
if _libs['libbpf.so.1'].has('bpf_program__set_expected_attach_type', 'cdecl'):
    bpf_program__set_expected_attach_type = _libs['libbpf.so.1'].get(
        'bpf_program__set_expected_attach_type', 'cdecl')
    bpf_program__set_expected_attach_type.argtypes = [POINTER(
        struct_bpf_program), enum_bpf_attach_type]
    bpf_program__set_expected_attach_type.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__flags', 'cdecl'):
    bpf_program__flags = _libs['libbpf.so.1'].get('bpf_program__flags', 'cdecl'
        )
    bpf_program__flags.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__flags.restype = __u32
if _libs['libbpf.so.1'].has('bpf_program__set_flags', 'cdecl'):
    bpf_program__set_flags = _libs['libbpf.so.1'].get('bpf_program__set_flags',
        'cdecl')
    bpf_program__set_flags.argtypes = [POINTER(struct_bpf_program), __u32]
    bpf_program__set_flags.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__log_level', 'cdecl'):
    bpf_program__log_level = _libs['libbpf.so.1'].get('bpf_program__log_level',
        'cdecl')
    bpf_program__log_level.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__log_level.restype = __u32
if _libs['libbpf.so.1'].has('bpf_program__set_log_level', 'cdecl'):
    bpf_program__set_log_level = _libs['libbpf.so.1'].get(
        'bpf_program__set_log_level', 'cdecl')
    bpf_program__set_log_level.argtypes = [POINTER(struct_bpf_program), __u32]
    bpf_program__set_log_level.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__log_buf', 'cdecl'):
    bpf_program__log_buf = _libs['libbpf.so.1'].get('bpf_program__log_buf',
        'cdecl')
    bpf_program__log_buf.argtypes = [POINTER(struct_bpf_program), POINTER(
        c_size_t)]
    bpf_program__log_buf.restype = c_char_p
if _libs['libbpf.so.1'].has('bpf_program__set_log_buf', 'cdecl'):
    bpf_program__set_log_buf = _libs['libbpf.so.1'].get(
        'bpf_program__set_log_buf', 'cdecl')
    bpf_program__set_log_buf.argtypes = [POINTER(struct_bpf_program),
        String, c_size_t]
    bpf_program__set_log_buf.restype = c_int
if _libs['libbpf.so.1'].has('bpf_program__set_attach_target', 'cdecl'):
    bpf_program__set_attach_target = _libs['libbpf.so.1'].get(
        'bpf_program__set_attach_target', 'cdecl')
    bpf_program__set_attach_target.argtypes = [POINTER(struct_bpf_program),
        c_int, String]
    bpf_program__set_attach_target.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__find_map_by_name', 'cdecl'):
    bpf_object__find_map_by_name = _libs['libbpf.so.1'].get(
        'bpf_object__find_map_by_name', 'cdecl')
    bpf_object__find_map_by_name.argtypes = [POINTER(struct_bpf_object), String
        ]
    bpf_object__find_map_by_name.restype = POINTER(struct_bpf_map)
if _libs['libbpf.so.1'].has('bpf_object__find_map_fd_by_name', 'cdecl'):
    bpf_object__find_map_fd_by_name = _libs['libbpf.so.1'].get(
        'bpf_object__find_map_fd_by_name', 'cdecl')
    bpf_object__find_map_fd_by_name.argtypes = [POINTER(struct_bpf_object),
        String]
    bpf_object__find_map_fd_by_name.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__next_map', 'cdecl'):
    bpf_object__next_map = _libs['libbpf.so.1'].get('bpf_object__next_map',
        'cdecl')
    bpf_object__next_map.argtypes = [POINTER(struct_bpf_object), POINTER(
        struct_bpf_map)]
    bpf_object__next_map.restype = POINTER(struct_bpf_map)
if _libs['libbpf.so.1'].has('bpf_object__prev_map', 'cdecl'):
    bpf_object__prev_map = _libs['libbpf.so.1'].get('bpf_object__prev_map',
        'cdecl')
    bpf_object__prev_map.argtypes = [POINTER(struct_bpf_object), POINTER(
        struct_bpf_map)]
    bpf_object__prev_map.restype = POINTER(struct_bpf_map)
if _libs['libbpf.so.1'].has('bpf_map__set_autocreate', 'cdecl'):
    bpf_map__set_autocreate = _libs['libbpf.so.1'].get(
        'bpf_map__set_autocreate', 'cdecl')
    bpf_map__set_autocreate.argtypes = [POINTER(struct_bpf_map), c_bool]
    bpf_map__set_autocreate.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__autocreate', 'cdecl'):
    bpf_map__autocreate = _libs['libbpf.so.1'].get('bpf_map__autocreate',
        'cdecl')
    bpf_map__autocreate.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__autocreate.restype = c_bool
if _libs['libbpf.so.1'].has('bpf_map__fd', 'cdecl'):
    bpf_map__fd = _libs['libbpf.so.1'].get('bpf_map__fd', 'cdecl')
    bpf_map__fd.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__fd.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__reuse_fd', 'cdecl'):
    bpf_map__reuse_fd = _libs['libbpf.so.1'].get('bpf_map__reuse_fd', 'cdecl')
    bpf_map__reuse_fd.argtypes = [POINTER(struct_bpf_map), c_int]
    bpf_map__reuse_fd.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__name', 'cdecl'):
    bpf_map__name = _libs['libbpf.so.1'].get('bpf_map__name', 'cdecl')
    bpf_map__name.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__name.restype = c_char_p
if _libs['libbpf.so.1'].has('bpf_map__type', 'cdecl'):
    bpf_map__type = _libs['libbpf.so.1'].get('bpf_map__type', 'cdecl')
    bpf_map__type.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__type.restype = enum_bpf_map_type
if _libs['libbpf.so.1'].has('bpf_map__set_type', 'cdecl'):
    bpf_map__set_type = _libs['libbpf.so.1'].get('bpf_map__set_type', 'cdecl')
    bpf_map__set_type.argtypes = [POINTER(struct_bpf_map), enum_bpf_map_type]
    bpf_map__set_type.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__max_entries', 'cdecl'):
    bpf_map__max_entries = _libs['libbpf.so.1'].get('bpf_map__max_entries',
        'cdecl')
    bpf_map__max_entries.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__max_entries.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__set_max_entries', 'cdecl'):
    bpf_map__set_max_entries = _libs['libbpf.so.1'].get(
        'bpf_map__set_max_entries', 'cdecl')
    bpf_map__set_max_entries.argtypes = [POINTER(struct_bpf_map), __u32]
    bpf_map__set_max_entries.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__map_flags', 'cdecl'):
    bpf_map__map_flags = _libs['libbpf.so.1'].get('bpf_map__map_flags', 'cdecl'
        )
    bpf_map__map_flags.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__map_flags.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__set_map_flags', 'cdecl'):
    bpf_map__set_map_flags = _libs['libbpf.so.1'].get('bpf_map__set_map_flags',
        'cdecl')
    bpf_map__set_map_flags.argtypes = [POINTER(struct_bpf_map), __u32]
    bpf_map__set_map_flags.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__numa_node', 'cdecl'):
    bpf_map__numa_node = _libs['libbpf.so.1'].get('bpf_map__numa_node', 'cdecl'
        )
    bpf_map__numa_node.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__numa_node.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__set_numa_node', 'cdecl'):
    bpf_map__set_numa_node = _libs['libbpf.so.1'].get('bpf_map__set_numa_node',
        'cdecl')
    bpf_map__set_numa_node.argtypes = [POINTER(struct_bpf_map), __u32]
    bpf_map__set_numa_node.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__key_size', 'cdecl'):
    bpf_map__key_size = _libs['libbpf.so.1'].get('bpf_map__key_size', 'cdecl')
    bpf_map__key_size.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__key_size.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__set_key_size', 'cdecl'):
    bpf_map__set_key_size = _libs['libbpf.so.1'].get('bpf_map__set_key_size',
        'cdecl')
    bpf_map__set_key_size.argtypes = [POINTER(struct_bpf_map), __u32]
    bpf_map__set_key_size.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__value_size', 'cdecl'):
    bpf_map__value_size = _libs['libbpf.so.1'].get('bpf_map__value_size',
        'cdecl')
    bpf_map__value_size.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__value_size.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__set_value_size', 'cdecl'):
    bpf_map__set_value_size = _libs['libbpf.so.1'].get(
        'bpf_map__set_value_size', 'cdecl')
    bpf_map__set_value_size.argtypes = [POINTER(struct_bpf_map), __u32]
    bpf_map__set_value_size.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__btf_key_type_id', 'cdecl'):
    bpf_map__btf_key_type_id = _libs['libbpf.so.1'].get(
        'bpf_map__btf_key_type_id', 'cdecl')
    bpf_map__btf_key_type_id.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__btf_key_type_id.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__btf_value_type_id', 'cdecl'):
    bpf_map__btf_value_type_id = _libs['libbpf.so.1'].get(
        'bpf_map__btf_value_type_id', 'cdecl')
    bpf_map__btf_value_type_id.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__btf_value_type_id.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__ifindex', 'cdecl'):
    bpf_map__ifindex = _libs['libbpf.so.1'].get('bpf_map__ifindex', 'cdecl')
    bpf_map__ifindex.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__ifindex.restype = __u32
if _libs['libbpf.so.1'].has('bpf_map__set_ifindex', 'cdecl'):
    bpf_map__set_ifindex = _libs['libbpf.so.1'].get('bpf_map__set_ifindex',
        'cdecl')
    bpf_map__set_ifindex.argtypes = [POINTER(struct_bpf_map), __u32]
    bpf_map__set_ifindex.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__map_extra', 'cdecl'):
    bpf_map__map_extra = _libs['libbpf.so.1'].get('bpf_map__map_extra', 'cdecl'
        )
    bpf_map__map_extra.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__map_extra.restype = __u64
if _libs['libbpf.so.1'].has('bpf_map__set_map_extra', 'cdecl'):
    bpf_map__set_map_extra = _libs['libbpf.so.1'].get('bpf_map__set_map_extra',
        'cdecl')
    bpf_map__set_map_extra.argtypes = [POINTER(struct_bpf_map), __u64]
    bpf_map__set_map_extra.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__set_initial_value', 'cdecl'):
    bpf_map__set_initial_value = _libs['libbpf.so.1'].get(
        'bpf_map__set_initial_value', 'cdecl')
    bpf_map__set_initial_value.argtypes = [POINTER(struct_bpf_map), POINTER
        (None), c_size_t]
    bpf_map__set_initial_value.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__initial_value', 'cdecl'):
    bpf_map__initial_value = _libs['libbpf.so.1'].get('bpf_map__initial_value',
        'cdecl')
    bpf_map__initial_value.argtypes = [POINTER(struct_bpf_map), POINTER(
        c_size_t)]
    bpf_map__initial_value.restype = POINTER(c_ubyte)
    bpf_map__initial_value.errcheck = lambda v, *a: cast(v, c_void_p)
if _libs['libbpf.so.1'].has('bpf_map__is_internal', 'cdecl'):
    bpf_map__is_internal = _libs['libbpf.so.1'].get('bpf_map__is_internal',
        'cdecl')
    bpf_map__is_internal.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__is_internal.restype = c_bool
if _libs['libbpf.so.1'].has('bpf_map__set_pin_path', 'cdecl'):
    bpf_map__set_pin_path = _libs['libbpf.so.1'].get('bpf_map__set_pin_path',
        'cdecl')
    bpf_map__set_pin_path.argtypes = [POINTER(struct_bpf_map), String]
    bpf_map__set_pin_path.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__pin_path', 'cdecl'):
    bpf_map__pin_path = _libs['libbpf.so.1'].get('bpf_map__pin_path', 'cdecl')
    bpf_map__pin_path.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__pin_path.restype = c_char_p
if _libs['libbpf.so.1'].has('bpf_map__is_pinned', 'cdecl'):
    bpf_map__is_pinned = _libs['libbpf.so.1'].get('bpf_map__is_pinned', 'cdecl'
        )
    bpf_map__is_pinned.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__is_pinned.restype = c_bool
if _libs['libbpf.so.1'].has('bpf_map__pin', 'cdecl'):
    bpf_map__pin = _libs['libbpf.so.1'].get('bpf_map__pin', 'cdecl')
    bpf_map__pin.argtypes = [POINTER(struct_bpf_map), String]
    bpf_map__pin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__unpin', 'cdecl'):
    bpf_map__unpin = _libs['libbpf.so.1'].get('bpf_map__unpin', 'cdecl')
    bpf_map__unpin.argtypes = [POINTER(struct_bpf_map), String]
    bpf_map__unpin.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__set_inner_map_fd', 'cdecl'):
    bpf_map__set_inner_map_fd = _libs['libbpf.so.1'].get(
        'bpf_map__set_inner_map_fd', 'cdecl')
    bpf_map__set_inner_map_fd.argtypes = [POINTER(struct_bpf_map), c_int]
    bpf_map__set_inner_map_fd.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__inner_map', 'cdecl'):
    bpf_map__inner_map = _libs['libbpf.so.1'].get('bpf_map__inner_map', 'cdecl'
        )
    bpf_map__inner_map.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__inner_map.restype = POINTER(struct_bpf_map)
if _libs['libbpf.so.1'].has('bpf_map__lookup_elem', 'cdecl'):
    bpf_map__lookup_elem = _libs['libbpf.so.1'].get('bpf_map__lookup_elem',
        'cdecl')
    bpf_map__lookup_elem.argtypes = [POINTER(struct_bpf_map), POINTER(None),
        c_size_t, POINTER(None), c_size_t, __u64]
    bpf_map__lookup_elem.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__update_elem', 'cdecl'):
    bpf_map__update_elem = _libs['libbpf.so.1'].get('bpf_map__update_elem',
        'cdecl')
    bpf_map__update_elem.argtypes = [POINTER(struct_bpf_map), POINTER(None),
        c_size_t, POINTER(None), c_size_t, __u64]
    bpf_map__update_elem.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__delete_elem', 'cdecl'):
    bpf_map__delete_elem = _libs['libbpf.so.1'].get('bpf_map__delete_elem',
        'cdecl')
    bpf_map__delete_elem.argtypes = [POINTER(struct_bpf_map), POINTER(None),
        c_size_t, __u64]
    bpf_map__delete_elem.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__lookup_and_delete_elem', 'cdecl'):
    bpf_map__lookup_and_delete_elem = _libs['libbpf.so.1'].get(
        'bpf_map__lookup_and_delete_elem', 'cdecl')
    bpf_map__lookup_and_delete_elem.argtypes = [POINTER(struct_bpf_map),
        POINTER(None), c_size_t, POINTER(None), c_size_t, __u64]
    bpf_map__lookup_and_delete_elem.restype = c_int
if _libs['libbpf.so.1'].has('bpf_map__get_next_key', 'cdecl'):
    bpf_map__get_next_key = _libs['libbpf.so.1'].get('bpf_map__get_next_key',
        'cdecl')
    bpf_map__get_next_key.argtypes = [POINTER(struct_bpf_map), POINTER(None
        ), POINTER(None), c_size_t]
    bpf_map__get_next_key.restype = c_int


class struct_bpf_xdp_set_link_opts(Structure):
    pass


struct_bpf_xdp_set_link_opts.__slots__ = ['sz', 'old_fd',
    'unnamed_bpf_xdp_set_link_opts_1']
struct_bpf_xdp_set_link_opts._fields_ = [('sz', c_size_t), ('old_fd', c_int)]


class struct_bpf_xdp_attach_opts(Structure):
    pass


struct_bpf_xdp_attach_opts.__slots__ = ['sz', 'old_prog_fd',
    'unnamed_bpf_xdp_attach_opts_1']
struct_bpf_xdp_attach_opts._fields_ = [('sz', c_size_t), ('old_prog_fd', c_int)
    ]


class struct_bpf_xdp_query_opts(Structure):
    pass


struct_bpf_xdp_query_opts.__slots__ = ['sz', 'prog_id', 'drv_prog_id',
    'hw_prog_id', 'skb_prog_id', 'attach_mode', 'feature_flags',
    'xdp_zc_max_segs', 'unnamed_bpf_xdp_query_opts_1']
struct_bpf_xdp_query_opts._fields_ = [('sz', c_size_t), ('prog_id', __u32),
    ('drv_prog_id', __u32), ('hw_prog_id', __u32), ('skb_prog_id', __u32),
    ('attach_mode', __u8), ('feature_flags', __u64), ('xdp_zc_max_segs', __u32)
    ]
if _libs['libbpf.so.1'].has('bpf_xdp_attach', 'cdecl'):
    bpf_xdp_attach = _libs['libbpf.so.1'].get('bpf_xdp_attach', 'cdecl')
    bpf_xdp_attach.argtypes = [c_int, c_int, __u32, POINTER(
        struct_bpf_xdp_attach_opts)]
    bpf_xdp_attach.restype = c_int
if _libs['libbpf.so.1'].has('bpf_xdp_detach', 'cdecl'):
    bpf_xdp_detach = _libs['libbpf.so.1'].get('bpf_xdp_detach', 'cdecl')
    bpf_xdp_detach.argtypes = [c_int, __u32, POINTER(
        struct_bpf_xdp_attach_opts)]
    bpf_xdp_detach.restype = c_int
if _libs['libbpf.so.1'].has('bpf_xdp_query', 'cdecl'):
    bpf_xdp_query = _libs['libbpf.so.1'].get('bpf_xdp_query', 'cdecl')
    bpf_xdp_query.argtypes = [c_int, c_int, POINTER(struct_bpf_xdp_query_opts)]
    bpf_xdp_query.restype = c_int
if _libs['libbpf.so.1'].has('bpf_xdp_query_id', 'cdecl'):
    bpf_xdp_query_id = _libs['libbpf.so.1'].get('bpf_xdp_query_id', 'cdecl')
    bpf_xdp_query_id.argtypes = [c_int, c_int, POINTER(__u32)]
    bpf_xdp_query_id.restype = c_int
enum_bpf_tc_attach_point = c_int
BPF_TC_INGRESS = 1 << 0
BPF_TC_EGRESS = 1 << 1
BPF_TC_CUSTOM = 1 << 2
enum_bpf_tc_flags = c_int
BPF_TC_F_REPLACE = 1 << 0


class struct_bpf_tc_hook(Structure):
    pass


struct_bpf_tc_hook.__slots__ = ['sz', 'ifindex', 'attach_point', 'parent',
    'unnamed_bpf_tc_hook_1']
struct_bpf_tc_hook._fields_ = [('sz', c_size_t), ('ifindex', c_int), (
    'attach_point', enum_bpf_tc_attach_point), ('parent', __u32)]


class struct_bpf_tc_opts(Structure):
    pass


struct_bpf_tc_opts.__slots__ = ['sz', 'prog_fd', 'flags', 'prog_id',
    'handle', 'priority', 'unnamed_bpf_tc_opts_1']
struct_bpf_tc_opts._fields_ = [('sz', c_size_t), ('prog_fd', c_int), (
    'flags', __u32), ('prog_id', __u32), ('handle', __u32), ('priority', __u32)
    ]
if _libs['libbpf.so.1'].has('bpf_tc_hook_create', 'cdecl'):
    bpf_tc_hook_create = _libs['libbpf.so.1'].get('bpf_tc_hook_create', 'cdecl'
        )
    bpf_tc_hook_create.argtypes = [POINTER(struct_bpf_tc_hook)]
    bpf_tc_hook_create.restype = c_int
if _libs['libbpf.so.1'].has('bpf_tc_hook_destroy', 'cdecl'):
    bpf_tc_hook_destroy = _libs['libbpf.so.1'].get('bpf_tc_hook_destroy',
        'cdecl')
    bpf_tc_hook_destroy.argtypes = [POINTER(struct_bpf_tc_hook)]
    bpf_tc_hook_destroy.restype = c_int
if _libs['libbpf.so.1'].has('bpf_tc_attach', 'cdecl'):
    bpf_tc_attach = _libs['libbpf.so.1'].get('bpf_tc_attach', 'cdecl')
    bpf_tc_attach.argtypes = [POINTER(struct_bpf_tc_hook), POINTER(
        struct_bpf_tc_opts)]
    bpf_tc_attach.restype = c_int
if _libs['libbpf.so.1'].has('bpf_tc_detach', 'cdecl'):
    bpf_tc_detach = _libs['libbpf.so.1'].get('bpf_tc_detach', 'cdecl')
    bpf_tc_detach.argtypes = [POINTER(struct_bpf_tc_hook), POINTER(
        struct_bpf_tc_opts)]
    bpf_tc_detach.restype = c_int
if _libs['libbpf.so.1'].has('bpf_tc_query', 'cdecl'):
    bpf_tc_query = _libs['libbpf.so.1'].get('bpf_tc_query', 'cdecl')
    bpf_tc_query.argtypes = [POINTER(struct_bpf_tc_hook), POINTER(
        struct_bpf_tc_opts)]
    bpf_tc_query.restype = c_int


class struct_ring_buffer(Structure):
    pass


class struct_ring(Structure):
    pass


class struct_user_ring_buffer(Structure):
    pass


ring_buffer_sample_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(
    None), c_size_t)


class struct_ring_buffer_opts(Structure):
    pass


struct_ring_buffer_opts.__slots__ = ['sz']
struct_ring_buffer_opts._fields_ = [('sz', c_size_t)]
if _libs['libbpf.so.1'].has('ring_buffer__new', 'cdecl'):
    ring_buffer__new = _libs['libbpf.so.1'].get('ring_buffer__new', 'cdecl')
    ring_buffer__new.argtypes = [c_int, ring_buffer_sample_fn, POINTER(None
        ), POINTER(struct_ring_buffer_opts)]
    ring_buffer__new.restype = POINTER(struct_ring_buffer)
if _libs['libbpf.so.1'].has('ring_buffer__free', 'cdecl'):
    ring_buffer__free = _libs['libbpf.so.1'].get('ring_buffer__free', 'cdecl')
    ring_buffer__free.argtypes = [POINTER(struct_ring_buffer)]
    ring_buffer__free.restype = None
if _libs['libbpf.so.1'].has('ring_buffer__add', 'cdecl'):
    ring_buffer__add = _libs['libbpf.so.1'].get('ring_buffer__add', 'cdecl')
    ring_buffer__add.argtypes = [POINTER(struct_ring_buffer), c_int,
        ring_buffer_sample_fn, POINTER(None)]
    ring_buffer__add.restype = c_int
if _libs['libbpf.so.1'].has('ring_buffer__poll', 'cdecl'):
    ring_buffer__poll = _libs['libbpf.so.1'].get('ring_buffer__poll', 'cdecl')
    ring_buffer__poll.argtypes = [POINTER(struct_ring_buffer), c_int]
    ring_buffer__poll.restype = c_int
if _libs['libbpf.so.1'].has('ring_buffer__consume', 'cdecl'):
    ring_buffer__consume = _libs['libbpf.so.1'].get('ring_buffer__consume',
        'cdecl')
    ring_buffer__consume.argtypes = [POINTER(struct_ring_buffer)]
    ring_buffer__consume.restype = c_int
if _libs['libbpf.so.1'].has('ring_buffer__epoll_fd', 'cdecl'):
    ring_buffer__epoll_fd = _libs['libbpf.so.1'].get('ring_buffer__epoll_fd',
        'cdecl')
    ring_buffer__epoll_fd.argtypes = [POINTER(struct_ring_buffer)]
    ring_buffer__epoll_fd.restype = c_int
if _libs['libbpf.so.1'].has('ring_buffer__ring', 'cdecl'):
    ring_buffer__ring = _libs['libbpf.so.1'].get('ring_buffer__ring', 'cdecl')
    ring_buffer__ring.argtypes = [POINTER(struct_ring_buffer), c_uint]
    ring_buffer__ring.restype = POINTER(struct_ring)
if _libs['libbpf.so.1'].has('ring__consumer_pos', 'cdecl'):
    ring__consumer_pos = _libs['libbpf.so.1'].get('ring__consumer_pos', 'cdecl'
        )
    ring__consumer_pos.argtypes = [POINTER(struct_ring)]
    ring__consumer_pos.restype = c_ulong
if _libs['libbpf.so.1'].has('ring__producer_pos', 'cdecl'):
    ring__producer_pos = _libs['libbpf.so.1'].get('ring__producer_pos', 'cdecl'
        )
    ring__producer_pos.argtypes = [POINTER(struct_ring)]
    ring__producer_pos.restype = c_ulong
if _libs['libbpf.so.1'].has('ring__avail_data_size', 'cdecl'):
    ring__avail_data_size = _libs['libbpf.so.1'].get('ring__avail_data_size',
        'cdecl')
    ring__avail_data_size.argtypes = [POINTER(struct_ring)]
    ring__avail_data_size.restype = c_size_t
if _libs['libbpf.so.1'].has('ring__size', 'cdecl'):
    ring__size = _libs['libbpf.so.1'].get('ring__size', 'cdecl')
    ring__size.argtypes = [POINTER(struct_ring)]
    ring__size.restype = c_size_t
if _libs['libbpf.so.1'].has('ring__map_fd', 'cdecl'):
    ring__map_fd = _libs['libbpf.so.1'].get('ring__map_fd', 'cdecl')
    ring__map_fd.argtypes = [POINTER(struct_ring)]
    ring__map_fd.restype = c_int
if _libs['libbpf.so.1'].has('ring__consume', 'cdecl'):
    ring__consume = _libs['libbpf.so.1'].get('ring__consume', 'cdecl')
    ring__consume.argtypes = [POINTER(struct_ring)]
    ring__consume.restype = c_int


class struct_user_ring_buffer_opts(Structure):
    pass


struct_user_ring_buffer_opts.__slots__ = ['sz']
struct_user_ring_buffer_opts._fields_ = [('sz', c_size_t)]
if _libs['libbpf.so.1'].has('user_ring_buffer__new', 'cdecl'):
    user_ring_buffer__new = _libs['libbpf.so.1'].get('user_ring_buffer__new',
        'cdecl')
    user_ring_buffer__new.argtypes = [c_int, POINTER(
        struct_user_ring_buffer_opts)]
    user_ring_buffer__new.restype = POINTER(struct_user_ring_buffer)
if _libs['libbpf.so.1'].has('user_ring_buffer__reserve', 'cdecl'):
    user_ring_buffer__reserve = _libs['libbpf.so.1'].get(
        'user_ring_buffer__reserve', 'cdecl')
    user_ring_buffer__reserve.argtypes = [POINTER(struct_user_ring_buffer),
        __u32]
    user_ring_buffer__reserve.restype = POINTER(c_ubyte)
    user_ring_buffer__reserve.errcheck = lambda v, *a: cast(v, c_void_p)
if _libs['libbpf.so.1'].has('user_ring_buffer__reserve_blocking', 'cdecl'):
    user_ring_buffer__reserve_blocking = _libs['libbpf.so.1'].get(
        'user_ring_buffer__reserve_blocking', 'cdecl')
    user_ring_buffer__reserve_blocking.argtypes = [POINTER(
        struct_user_ring_buffer), __u32, c_int]
    user_ring_buffer__reserve_blocking.restype = POINTER(c_ubyte)
    user_ring_buffer__reserve_blocking.errcheck = lambda v, *a: cast(v,
        c_void_p)
if _libs['libbpf.so.1'].has('user_ring_buffer__submit', 'cdecl'):
    user_ring_buffer__submit = _libs['libbpf.so.1'].get(
        'user_ring_buffer__submit', 'cdecl')
    user_ring_buffer__submit.argtypes = [POINTER(struct_user_ring_buffer),
        POINTER(None)]
    user_ring_buffer__submit.restype = None
if _libs['libbpf.so.1'].has('user_ring_buffer__discard', 'cdecl'):
    user_ring_buffer__discard = _libs['libbpf.so.1'].get(
        'user_ring_buffer__discard', 'cdecl')
    user_ring_buffer__discard.argtypes = [POINTER(struct_user_ring_buffer),
        POINTER(None)]
    user_ring_buffer__discard.restype = None
if _libs['libbpf.so.1'].has('user_ring_buffer__free', 'cdecl'):
    user_ring_buffer__free = _libs['libbpf.so.1'].get('user_ring_buffer__free',
        'cdecl')
    user_ring_buffer__free.argtypes = [POINTER(struct_user_ring_buffer)]
    user_ring_buffer__free.restype = None


class struct_perf_buffer(Structure):
    pass


perf_buffer_sample_fn = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int,
    POINTER(None), __u32)
perf_buffer_lost_fn = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, __u64)


class struct_perf_buffer_opts(Structure):
    pass


struct_perf_buffer_opts.__slots__ = ['sz', 'sample_period',
    'unnamed_perf_buffer_opts_1']
struct_perf_buffer_opts._fields_ = [('sz', c_size_t), ('sample_period', __u32)]
if _libs['libbpf.so.1'].has('perf_buffer__new', 'cdecl'):
    perf_buffer__new = _libs['libbpf.so.1'].get('perf_buffer__new', 'cdecl')
    perf_buffer__new.argtypes = [c_int, c_size_t, perf_buffer_sample_fn,
        perf_buffer_lost_fn, POINTER(None), POINTER(struct_perf_buffer_opts)]
    perf_buffer__new.restype = POINTER(struct_perf_buffer)
enum_bpf_perf_event_ret = c_int
LIBBPF_PERF_EVENT_DONE = 0
LIBBPF_PERF_EVENT_ERROR = -1
LIBBPF_PERF_EVENT_CONT = -2
perf_buffer_event_fn = CFUNCTYPE(UNCHECKED(enum_bpf_perf_event_ret),
    POINTER(None), c_int, POINTER(struct_perf_event_header))


class struct_perf_buffer_raw_opts(Structure):
    pass


struct_perf_buffer_raw_opts.__slots__ = ['sz',
    'unnamed_perf_buffer_raw_opts_1', 'unnamed_perf_buffer_raw_opts_2',
    'cpu_cnt', 'cpus', 'map_keys']
struct_perf_buffer_raw_opts._fields_ = [('sz', c_size_t), (
    'padding_mock1_7', ctypes.c_char), ('padding_mock2_7', ctypes.c_char),
    ('padding_mock2_6', ctypes.c_char), ('padding_mock2_5', ctypes.c_char),
    ('padding_mock2_4', ctypes.c_char), ('padding_mock2_3', ctypes.c_char),
    ('padding_mock2_2', ctypes.c_char), ('padding_mock2_1', ctypes.c_char),
    ('padding_mock2_0', ctypes.c_char), ('padding_mock1_6', ctypes.c_char),
    ('padding_mock1_5', ctypes.c_char), ('padding_mock1_4', ctypes.c_char),
    ('padding_mock1_3', ctypes.c_char), ('padding_mock1_2', ctypes.c_char),
    ('padding_mock1_1', ctypes.c_char), ('padding_mock1_0', ctypes.c_char),
    ('cpu_cnt', c_int), ('cpus', POINTER(c_int)), ('map_keys', POINTER(c_int))]
if _libs['libbpf.so.1'].has('perf_buffer__new_raw', 'cdecl'):
    perf_buffer__new_raw = _libs['libbpf.so.1'].get('perf_buffer__new_raw',
        'cdecl')
    perf_buffer__new_raw.argtypes = [c_int, c_size_t, POINTER(
        struct_perf_event_attr), perf_buffer_event_fn, POINTER(None),
        POINTER(struct_perf_buffer_raw_opts)]
    perf_buffer__new_raw.restype = POINTER(struct_perf_buffer)
if _libs['libbpf.so.1'].has('perf_buffer__free', 'cdecl'):
    perf_buffer__free = _libs['libbpf.so.1'].get('perf_buffer__free', 'cdecl')
    perf_buffer__free.argtypes = [POINTER(struct_perf_buffer)]
    perf_buffer__free.restype = None
if _libs['libbpf.so.1'].has('perf_buffer__epoll_fd', 'cdecl'):
    perf_buffer__epoll_fd = _libs['libbpf.so.1'].get('perf_buffer__epoll_fd',
        'cdecl')
    perf_buffer__epoll_fd.argtypes = [POINTER(struct_perf_buffer)]
    perf_buffer__epoll_fd.restype = c_int
if _libs['libbpf.so.1'].has('perf_buffer__poll', 'cdecl'):
    perf_buffer__poll = _libs['libbpf.so.1'].get('perf_buffer__poll', 'cdecl')
    perf_buffer__poll.argtypes = [POINTER(struct_perf_buffer), c_int]
    perf_buffer__poll.restype = c_int
if _libs['libbpf.so.1'].has('perf_buffer__consume', 'cdecl'):
    perf_buffer__consume = _libs['libbpf.so.1'].get('perf_buffer__consume',
        'cdecl')
    perf_buffer__consume.argtypes = [POINTER(struct_perf_buffer)]
    perf_buffer__consume.restype = c_int
if _libs['libbpf.so.1'].has('perf_buffer__consume_buffer', 'cdecl'):
    perf_buffer__consume_buffer = _libs['libbpf.so.1'].get(
        'perf_buffer__consume_buffer', 'cdecl')
    perf_buffer__consume_buffer.argtypes = [POINTER(struct_perf_buffer),
        c_size_t]
    perf_buffer__consume_buffer.restype = c_int
if _libs['libbpf.so.1'].has('perf_buffer__buffer_cnt', 'cdecl'):
    perf_buffer__buffer_cnt = _libs['libbpf.so.1'].get(
        'perf_buffer__buffer_cnt', 'cdecl')
    perf_buffer__buffer_cnt.argtypes = [POINTER(struct_perf_buffer)]
    perf_buffer__buffer_cnt.restype = c_size_t
if _libs['libbpf.so.1'].has('perf_buffer__buffer_fd', 'cdecl'):
    perf_buffer__buffer_fd = _libs['libbpf.so.1'].get('perf_buffer__buffer_fd',
        'cdecl')
    perf_buffer__buffer_fd.argtypes = [POINTER(struct_perf_buffer), c_size_t]
    perf_buffer__buffer_fd.restype = c_int
if _libs['libbpf.so.1'].has('perf_buffer__buffer', 'cdecl'):
    perf_buffer__buffer = _libs['libbpf.so.1'].get('perf_buffer__buffer',
        'cdecl')
    perf_buffer__buffer.argtypes = [POINTER(struct_perf_buffer), c_int,
        POINTER(POINTER(None)), POINTER(c_size_t)]
    perf_buffer__buffer.restype = c_int


class struct_bpf_prog_linfo(Structure):
    pass


if _libs['libbpf.so.1'].has('bpf_prog_linfo__free', 'cdecl'):
    bpf_prog_linfo__free = _libs['libbpf.so.1'].get('bpf_prog_linfo__free',
        'cdecl')
    bpf_prog_linfo__free.argtypes = [POINTER(struct_bpf_prog_linfo)]
    bpf_prog_linfo__free.restype = None
if _libs['libbpf.so.1'].has('bpf_prog_linfo__new', 'cdecl'):
    bpf_prog_linfo__new = _libs['libbpf.so.1'].get('bpf_prog_linfo__new',
        'cdecl')
    bpf_prog_linfo__new.argtypes = [POINTER(struct_bpf_prog_info)]
    bpf_prog_linfo__new.restype = POINTER(struct_bpf_prog_linfo)
if _libs['libbpf.so.1'].has('bpf_prog_linfo__lfind_addr_func', 'cdecl'):
    bpf_prog_linfo__lfind_addr_func = _libs['libbpf.so.1'].get(
        'bpf_prog_linfo__lfind_addr_func', 'cdecl')
    bpf_prog_linfo__lfind_addr_func.argtypes = [POINTER(
        struct_bpf_prog_linfo), __u64, __u32, __u32]
    bpf_prog_linfo__lfind_addr_func.restype = POINTER(struct_bpf_line_info)
if _libs['libbpf.so.1'].has('bpf_prog_linfo__lfind', 'cdecl'):
    bpf_prog_linfo__lfind = _libs['libbpf.so.1'].get('bpf_prog_linfo__lfind',
        'cdecl')
    bpf_prog_linfo__lfind.argtypes = [POINTER(struct_bpf_prog_linfo), __u32,
        __u32]
    bpf_prog_linfo__lfind.restype = POINTER(struct_bpf_line_info)
if _libs['libbpf.so.1'].has('libbpf_probe_bpf_prog_type', 'cdecl'):
    libbpf_probe_bpf_prog_type = _libs['libbpf.so.1'].get(
        'libbpf_probe_bpf_prog_type', 'cdecl')
    libbpf_probe_bpf_prog_type.argtypes = [enum_bpf_prog_type, POINTER(None)]
    libbpf_probe_bpf_prog_type.restype = c_int
if _libs['libbpf.so.1'].has('libbpf_probe_bpf_map_type', 'cdecl'):
    libbpf_probe_bpf_map_type = _libs['libbpf.so.1'].get(
        'libbpf_probe_bpf_map_type', 'cdecl')
    libbpf_probe_bpf_map_type.argtypes = [enum_bpf_map_type, POINTER(None)]
    libbpf_probe_bpf_map_type.restype = c_int
if _libs['libbpf.so.1'].has('libbpf_probe_bpf_helper', 'cdecl'):
    libbpf_probe_bpf_helper = _libs['libbpf.so.1'].get(
        'libbpf_probe_bpf_helper', 'cdecl')
    libbpf_probe_bpf_helper.argtypes = [enum_bpf_prog_type,
        enum_bpf_func_id, POINTER(None)]
    libbpf_probe_bpf_helper.restype = c_int
if _libs['libbpf.so.1'].has('libbpf_num_possible_cpus', 'cdecl'):
    libbpf_num_possible_cpus = _libs['libbpf.so.1'].get(
        'libbpf_num_possible_cpus', 'cdecl')
    libbpf_num_possible_cpus.argtypes = []
    libbpf_num_possible_cpus.restype = c_int


class struct_bpf_map_skeleton(Structure):
    pass


struct_bpf_map_skeleton.__slots__ = ['name', 'map', 'mmaped']
struct_bpf_map_skeleton._fields_ = [('name', String), ('map', POINTER(
    POINTER(struct_bpf_map))), ('mmaped', POINTER(POINTER(None)))]


class struct_bpf_prog_skeleton(Structure):
    pass


struct_bpf_prog_skeleton.__slots__ = ['name', 'prog', 'link']
struct_bpf_prog_skeleton._fields_ = [('name', String), ('prog', POINTER(
    POINTER(struct_bpf_program))), ('link', POINTER(POINTER(struct_bpf_link)))]


class struct_bpf_object_skeleton(Structure):
    pass


struct_bpf_object_skeleton.__slots__ = ['sz', 'name', 'data', 'data_sz',
    'obj', 'map_cnt', 'map_skel_sz', 'maps', 'prog_cnt', 'prog_skel_sz',
    'progs']
struct_bpf_object_skeleton._fields_ = [('sz', c_size_t), ('name', String),
    ('data', POINTER(None)), ('data_sz', c_size_t), ('obj', POINTER(POINTER
    (struct_bpf_object))), ('map_cnt', c_int), ('map_skel_sz', c_int), (
    'maps', POINTER(struct_bpf_map_skeleton)), ('prog_cnt', c_int), (
    'prog_skel_sz', c_int), ('progs', POINTER(struct_bpf_prog_skeleton))]
if _libs['libbpf.so.1'].has('bpf_object__open_skeleton', 'cdecl'):
    bpf_object__open_skeleton = _libs['libbpf.so.1'].get(
        'bpf_object__open_skeleton', 'cdecl')
    bpf_object__open_skeleton.argtypes = [POINTER(
        struct_bpf_object_skeleton), POINTER(struct_bpf_object_open_opts)]
    bpf_object__open_skeleton.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__load_skeleton', 'cdecl'):
    bpf_object__load_skeleton = _libs['libbpf.so.1'].get(
        'bpf_object__load_skeleton', 'cdecl')
    bpf_object__load_skeleton.argtypes = [POINTER(struct_bpf_object_skeleton)]
    bpf_object__load_skeleton.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__attach_skeleton', 'cdecl'):
    bpf_object__attach_skeleton = _libs['libbpf.so.1'].get(
        'bpf_object__attach_skeleton', 'cdecl')
    bpf_object__attach_skeleton.argtypes = [POINTER(struct_bpf_object_skeleton)
        ]
    bpf_object__attach_skeleton.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__detach_skeleton', 'cdecl'):
    bpf_object__detach_skeleton = _libs['libbpf.so.1'].get(
        'bpf_object__detach_skeleton', 'cdecl')
    bpf_object__detach_skeleton.argtypes = [POINTER(struct_bpf_object_skeleton)
        ]
    bpf_object__detach_skeleton.restype = None
if _libs['libbpf.so.1'].has('bpf_object__destroy_skeleton', 'cdecl'):
    bpf_object__destroy_skeleton = _libs['libbpf.so.1'].get(
        'bpf_object__destroy_skeleton', 'cdecl')
    bpf_object__destroy_skeleton.argtypes = [POINTER(
        struct_bpf_object_skeleton)]
    bpf_object__destroy_skeleton.restype = None


class struct_bpf_var_skeleton(Structure):
    pass


struct_bpf_var_skeleton.__slots__ = ['name', 'map', 'addr']
struct_bpf_var_skeleton._fields_ = [('name', String), ('map', POINTER(
    POINTER(struct_bpf_map))), ('addr', POINTER(POINTER(None)))]


class struct_bpf_object_subskeleton(Structure):
    pass


struct_bpf_object_subskeleton.__slots__ = ['sz', 'obj', 'map_cnt',
    'map_skel_sz', 'maps', 'prog_cnt', 'prog_skel_sz', 'progs', 'var_cnt',
    'var_skel_sz', 'vars']
struct_bpf_object_subskeleton._fields_ = [('sz', c_size_t), ('obj', POINTER
    (struct_bpf_object)), ('map_cnt', c_int), ('map_skel_sz', c_int), (
    'maps', POINTER(struct_bpf_map_skeleton)), ('prog_cnt', c_int), (
    'prog_skel_sz', c_int), ('progs', POINTER(struct_bpf_prog_skeleton)), (
    'var_cnt', c_int), ('var_skel_sz', c_int), ('vars', POINTER(
    struct_bpf_var_skeleton))]
if _libs['libbpf.so.1'].has('bpf_object__open_subskeleton', 'cdecl'):
    bpf_object__open_subskeleton = _libs['libbpf.so.1'].get(
        'bpf_object__open_subskeleton', 'cdecl')
    bpf_object__open_subskeleton.argtypes = [POINTER(
        struct_bpf_object_subskeleton)]
    bpf_object__open_subskeleton.restype = c_int
if _libs['libbpf.so.1'].has('bpf_object__destroy_subskeleton', 'cdecl'):
    bpf_object__destroy_subskeleton = _libs['libbpf.so.1'].get(
        'bpf_object__destroy_subskeleton', 'cdecl')
    bpf_object__destroy_subskeleton.argtypes = [POINTER(
        struct_bpf_object_subskeleton)]
    bpf_object__destroy_subskeleton.restype = None


class struct_gen_loader_opts(Structure):
    pass


struct_gen_loader_opts.__slots__ = ['sz', 'data', 'insns', 'data_sz',
    'insns_sz']
struct_gen_loader_opts._fields_ = [('sz', c_size_t), ('data', String), (
    'insns', String), ('data_sz', __u32), ('insns_sz', __u32)]
if _libs['libbpf.so.1'].has('bpf_object__gen_loader', 'cdecl'):
    bpf_object__gen_loader = _libs['libbpf.so.1'].get('bpf_object__gen_loader',
        'cdecl')
    bpf_object__gen_loader.argtypes = [POINTER(struct_bpf_object), POINTER(
        struct_gen_loader_opts)]
    bpf_object__gen_loader.restype = c_int
enum_libbpf_tristate = c_int
TRI_NO = 0
TRI_YES = 1
TRI_MODULE = 2


class struct_bpf_linker_opts(Structure):
    pass


struct_bpf_linker_opts.__slots__ = ['sz']
struct_bpf_linker_opts._fields_ = [('sz', c_size_t)]


class struct_bpf_linker_file_opts(Structure):
    pass


struct_bpf_linker_file_opts.__slots__ = ['sz']
struct_bpf_linker_file_opts._fields_ = [('sz', c_size_t)]


class struct_bpf_linker(Structure):
    pass


if _libs['libbpf.so.1'].has('bpf_linker__new', 'cdecl'):
    bpf_linker__new = _libs['libbpf.so.1'].get('bpf_linker__new', 'cdecl')
    bpf_linker__new.argtypes = [String, POINTER(struct_bpf_linker_opts)]
    bpf_linker__new.restype = POINTER(struct_bpf_linker)
if _libs['libbpf.so.1'].has('bpf_linker__add_file', 'cdecl'):
    bpf_linker__add_file = _libs['libbpf.so.1'].get('bpf_linker__add_file',
        'cdecl')
    bpf_linker__add_file.argtypes = [POINTER(struct_bpf_linker), String,
        POINTER(struct_bpf_linker_file_opts)]
    bpf_linker__add_file.restype = c_int
if _libs['libbpf.so.1'].has('bpf_linker__finalize', 'cdecl'):
    bpf_linker__finalize = _libs['libbpf.so.1'].get('bpf_linker__finalize',
        'cdecl')
    bpf_linker__finalize.argtypes = [POINTER(struct_bpf_linker)]
    bpf_linker__finalize.restype = c_int
if _libs['libbpf.so.1'].has('bpf_linker__free', 'cdecl'):
    bpf_linker__free = _libs['libbpf.so.1'].get('bpf_linker__free', 'cdecl')
    bpf_linker__free.argtypes = [POINTER(struct_bpf_linker)]
    bpf_linker__free.restype = None


class struct_bpf_prog_load_opts(Structure):
    pass


libbpf_prog_setup_fn_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(
    struct_bpf_program), c_long)
libbpf_prog_prepare_load_fn_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(
    struct_bpf_program), POINTER(struct_bpf_prog_load_opts), c_long)
libbpf_prog_attach_fn_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(
    struct_bpf_program), c_long, POINTER(POINTER(struct_bpf_link)))


class struct_libbpf_prog_handler_opts(Structure):
    pass


struct_libbpf_prog_handler_opts.__slots__ = ['sz', 'cookie',
    'prog_setup_fn', 'prog_prepare_load_fn', 'prog_attach_fn']
struct_libbpf_prog_handler_opts._fields_ = [('sz', c_size_t), ('cookie',
    c_long), ('prog_setup_fn', libbpf_prog_setup_fn_t), (
    'prog_prepare_load_fn', libbpf_prog_prepare_load_fn_t), (
    'prog_attach_fn', libbpf_prog_attach_fn_t)]
if _libs['libbpf.so.1'].has('libbpf_register_prog_handler', 'cdecl'):
    libbpf_register_prog_handler = _libs['libbpf.so.1'].get(
        'libbpf_register_prog_handler', 'cdecl')
    libbpf_register_prog_handler.argtypes = [String, enum_bpf_prog_type,
        enum_bpf_attach_type, POINTER(struct_libbpf_prog_handler_opts)]
    libbpf_register_prog_handler.restype = c_int
if _libs['libbpf.so.1'].has('libbpf_unregister_prog_handler', 'cdecl'):
    libbpf_unregister_prog_handler = _libs['libbpf.so.1'].get(
        'libbpf_unregister_prog_handler', 'cdecl')
    libbpf_unregister_prog_handler.argtypes = [c_int]
    libbpf_unregister_prog_handler.restype = c_int
struct_bpf_prog_load_opts.__slots__ = ['sz', 'attempts',
    'expected_attach_type', 'prog_btf_fd', 'prog_flags', 'prog_ifindex',
    'kern_version', 'attach_btf_id', 'attach_prog_fd', 'attach_btf_obj_fd',
    'fd_array', 'func_info', 'func_info_cnt', 'func_info_rec_size',
    'line_info', 'line_info_cnt', 'line_info_rec_size', 'log_level',
    'log_size', 'log_buf', 'log_true_size', 'token_fd',
    'unnamed_bpf_prog_load_opts_1']
struct_bpf_prog_load_opts._fields_ = [('sz', c_size_t), ('attempts', c_int),
    ('expected_attach_type', enum_bpf_attach_type), ('prog_btf_fd', __u32),
    ('prog_flags', __u32), ('prog_ifindex', __u32), ('kern_version', __u32),
    ('attach_btf_id', __u32), ('attach_prog_fd', __u32), (
    'attach_btf_obj_fd', __u32), ('fd_array', POINTER(c_int)), ('func_info',
    POINTER(None)), ('func_info_cnt', __u32), ('func_info_rec_size', __u32),
    ('line_info', POINTER(None)), ('line_info_cnt', __u32), (
    'line_info_rec_size', __u32), ('log_level', __u32), ('log_size', __u32),
    ('log_buf', String), ('log_true_size', __u32), ('token_fd', __u32)]


class struct_bpf_core_cand(Structure):
    pass


struct_bpf_core_cand.__slots__ = ['btf', 'id']
struct_bpf_core_cand._fields_ = [('btf', POINTER(struct_btf)), ('id', __u32)]


class struct_bpf_core_cand_list(Structure):
    pass


struct_bpf_core_cand_list.__slots__ = ['cands', 'len']
struct_bpf_core_cand_list._fields_ = [('cands', POINTER(
    struct_bpf_core_cand)), ('len', c_int)]


class struct_bpf_core_accessor(Structure):
    pass


struct_bpf_core_accessor.__slots__ = ['type_id', 'idx', 'name']
struct_bpf_core_accessor._fields_ = [('type_id', __u32), ('idx', __u32), (
    'name', String)]


class struct_bpf_core_spec(Structure):
    pass


struct_bpf_core_spec.__slots__ = ['btf', 'spec', 'root_type_id',
    'relo_kind', 'len', 'raw_spec', 'raw_len', 'bit_offset']
struct_bpf_core_spec._fields_ = [('btf', POINTER(struct_btf)), ('spec', 
    struct_bpf_core_accessor * int(64)), ('root_type_id', __u32), (
    'relo_kind', enum_bpf_core_relo_kind), ('len', c_int), ('raw_spec', 
    c_int * int(64)), ('raw_len', c_int), ('bit_offset', __u32)]


class struct_bpf_core_relo_res(Structure):
    pass


struct_bpf_core_relo_res.__slots__ = ['orig_val', 'new_val', 'poison',
    'validate', 'fail_memsz_adjust', 'orig_sz', 'orig_type_id', 'new_sz',
    'new_type_id']
struct_bpf_core_relo_res._fields_ = [('orig_val', __u64), ('new_val', __u64
    ), ('poison', c_bool), ('validate', c_bool), ('fail_memsz_adjust',
    c_bool), ('orig_sz', __u32), ('orig_type_id', __u32), ('new_sz', __u32),
    ('new_type_id', __u32)]
struct_bpf_link.__slots__ = ['detach', 'dealloc', 'pin_path', 'fd',
    'disconnected']
struct_bpf_link._fields_ = [('detach', CFUNCTYPE(UNCHECKED(c_int), POINTER(
    struct_bpf_link))), ('dealloc', CFUNCTYPE(UNCHECKED(None), POINTER(
    struct_bpf_link))), ('pin_path', String), ('fd', c_int), (
    'disconnected', c_bool)]
FEAT_PROG_NAME = 0
FEAT_GLOBAL_DATA = FEAT_PROG_NAME + 1
FEAT_BTF = FEAT_GLOBAL_DATA + 1
FEAT_BTF_FUNC = FEAT_BTF + 1
FEAT_BTF_DATASEC = FEAT_BTF_FUNC + 1
FEAT_BTF_GLOBAL_FUNC = FEAT_BTF_DATASEC + 1
FEAT_ARRAY_MMAP = FEAT_BTF_GLOBAL_FUNC + 1
FEAT_EXP_ATTACH_TYPE = FEAT_ARRAY_MMAP + 1
FEAT_PROBE_READ_KERN = FEAT_EXP_ATTACH_TYPE + 1
FEAT_PROG_BIND_MAP = FEAT_PROBE_READ_KERN + 1
FEAT_MODULE_BTF = FEAT_PROG_BIND_MAP + 1
FEAT_BTF_FLOAT = FEAT_MODULE_BTF + 1
FEAT_PERF_LINK = FEAT_BTF_FLOAT + 1
FEAT_BTF_DECL_TAG = FEAT_PERF_LINK + 1
FEAT_BTF_TYPE_TAG = FEAT_BTF_DECL_TAG + 1
FEAT_MEMCG_ACCOUNT = FEAT_BTF_TYPE_TAG + 1
FEAT_BPF_COOKIE = FEAT_MEMCG_ACCOUNT + 1
FEAT_BTF_ENUM64 = FEAT_BPF_COOKIE + 1
FEAT_SYSCALL_WRAPPER = FEAT_BTF_ENUM64 + 1
FEAT_UPROBE_MULTI_LINK = FEAT_SYSCALL_WRAPPER + 1
__FEAT_CNT = FEAT_UPROBE_MULTI_LINK + 1
enum_kern_feature_result = c_int


class struct_kern_feature_cache(Structure):
    pass


struct_kern_feature_cache.__slots__ = ['res', 'token_fd']
struct_kern_feature_cache._fields_ = [('res', enum_kern_feature_result *
    int(__FEAT_CNT)), ('token_fd', c_int)]


class struct_btf_ext_info(Structure):
    pass


struct_btf_ext_info.__slots__ = ['info', 'rec_size', 'len', 'sec_idxs',
    'sec_cnt']
struct_btf_ext_info._fields_ = [('info', POINTER(None)), ('rec_size', __u32
    ), ('len', __u32), ('sec_idxs', POINTER(__u32)), ('sec_cnt', c_int)]


class struct_btf_ext_header(Structure):
    pass


struct_btf_ext_header.__slots__ = ['magic', 'version', 'flags', 'hdr_len',
    'func_info_off', 'func_info_len', 'line_info_off', 'line_info_len',
    'core_relo_off', 'core_relo_len']
struct_btf_ext_header._fields_ = [('magic', __u16), ('version', __u8), (
    'flags', __u8), ('hdr_len', __u32), ('func_info_off', __u32), (
    'func_info_len', __u32), ('line_info_off', __u32), ('line_info_len',
    __u32), ('core_relo_off', __u32), ('core_relo_len', __u32)]


class union_anon_272(Union):
    pass


union_anon_272.__slots__ = ['hdr', 'data']
union_anon_272._fields_ = [('hdr', POINTER(struct_btf_ext_header)), ('data',
    POINTER(None))]
struct_btf_ext.__slots__ = ['unnamed_btf_ext_1', 'func_info', 'line_info',
    'core_relo_info', 'data_size']
struct_btf_ext._anonymous_ = ['unnamed_btf_ext_1']
struct_btf_ext._fields_ = [('unnamed_btf_ext_1', union_anon_272), (
    'func_info', struct_btf_ext_info), ('line_info', struct_btf_ext_info),
    ('core_relo_info', struct_btf_ext_info), ('data_size', __u32)]


class struct_btf_ext_info_sec(Structure):
    pass


struct_btf_ext_info_sec.__slots__ = ['sec_name_off', 'num_info', 'data']
struct_btf_ext_info_sec._fields_ = [('sec_name_off', __u32), ('num_info',
    __u32), ('data', POINTER(__u8))]


class struct_bpf_func_info_min(Structure):
    pass


struct_bpf_func_info_min.__slots__ = ['insn_off', 'type_id']
struct_bpf_func_info_min._fields_ = [('insn_off', __u32), ('type_id', __u32)]
for _lib in _libs.values():
    try:
        old_fd = c_int.in_dll(_lib, 'old_fd')
        break
    except:
        pass


class struct_usdt_manager(Structure):
    pass


hashmap_hash_fn = CFUNCTYPE(UNCHECKED(c_size_t), c_long, POINTER(None))
hashmap_equal_fn = CFUNCTYPE(UNCHECKED(c_bool), c_long, c_long, POINTER(None))


class union_anon_273(Union):
    pass


union_anon_273.__slots__ = ['key', 'pkey']
union_anon_273._fields_ = [('key', c_long), ('pkey', POINTER(None))]


class union_anon_274(Union):
    pass


union_anon_274.__slots__ = ['value', 'pvalue']
union_anon_274._fields_ = [('value', c_long), ('pvalue', POINTER(None))]


class struct_hashmap_entry(Structure):
    pass


struct_hashmap_entry.__slots__ = ['unnamed_hashmap_entry_1',
    'unnamed_hashmap_entry_2', 'next']
struct_hashmap_entry._anonymous_ = ['unnamed_hashmap_entry_1',
    'unnamed_hashmap_entry_2']
struct_hashmap_entry._fields_ = [('unnamed_hashmap_entry_1', union_anon_273
    ), ('unnamed_hashmap_entry_2', union_anon_274), ('next', POINTER(
    struct_hashmap_entry))]


class struct_hashmap(Structure):
    pass


struct_hashmap.__slots__ = ['hash_fn', 'equal_fn', 'ctx', 'buckets', 'cap',
    'cap_bits', 'sz']
struct_hashmap._fields_ = [('hash_fn', hashmap_hash_fn), ('equal_fn',
    hashmap_equal_fn), ('ctx', POINTER(None)), ('buckets', POINTER(POINTER(
    struct_hashmap_entry))), ('cap', c_size_t), ('cap_bits', c_size_t), (
    'sz', c_size_t)]


class struct_ksym_relo_desc(Structure):
    pass


struct_ksym_relo_desc.__slots__ = ['name', 'kind', 'insn_idx', 'is_weak',
    'is_typeless', 'is_ld64']
struct_ksym_relo_desc._fields_ = [('name', String), ('kind', c_int), (
    'insn_idx', c_int), ('is_weak', c_bool), ('is_typeless', c_bool), (
    'is_ld64', c_bool)]


class union_anon_275(Union):
    pass


union_anon_275.__slots__ = ['off', 'typeless']
union_anon_275._fields_ = [('off', c_int), ('typeless', c_bool)]


class struct_ksym_desc(Structure):
    pass


struct_ksym_desc.__slots__ = ['name', 'ref', 'kind', 'unnamed_ksym_desc_1',
    'insn', 'is_ld64']
struct_ksym_desc._anonymous_ = ['unnamed_ksym_desc_1']
struct_ksym_desc._fields_ = [('name', String), ('ref', c_int), ('kind',
    c_int), ('unnamed_ksym_desc_1', union_anon_275), ('insn', c_int), (
    'is_ld64', c_bool)]


class struct_bpf_gen(Structure):
    pass


struct_bpf_gen.__slots__ = ['opts', 'data_start', 'data_cur', 'insn_start',
    'insn_cur', 'cleanup_label', 'nr_progs', 'nr_maps', 'log_level',
    'error', 'relos', 'relo_cnt', 'core_relos', 'core_relo_cnt',
    'attach_target', 'attach_kind', 'ksyms', 'nr_ksyms', 'fd_array',
    'nr_fd_array']
struct_bpf_gen._fields_ = [('opts', POINTER(struct_gen_loader_opts)), (
    'data_start', POINTER(None)), ('data_cur', POINTER(None)), (
    'insn_start', POINTER(None)), ('insn_cur', POINTER(None)), (
    'cleanup_label', c_ptrdiff_t), ('nr_progs', __u32), ('nr_maps', __u32),
    ('log_level', c_int), ('error', c_int), ('relos', POINTER(
    struct_ksym_relo_desc)), ('relo_cnt', c_int), ('core_relos', POINTER(
    struct_bpf_core_relo)), ('core_relo_cnt', c_int), ('attach_target', 
    c_char * int(128)), ('attach_kind', c_int), ('ksyms', POINTER(
    struct_ksym_desc)), ('nr_ksyms', __u32), ('fd_array', c_int), (
    'nr_fd_array', c_int)]


class struct_zip_archive(Structure):
    pass


class struct_zip_entry(Structure):
    pass


struct_zip_entry.__slots__ = ['compression', 'name', 'name_length', 'data',
    'data_length', 'data_offset']
struct_zip_entry._fields_ = [('compression', __u16), ('name', String), (
    'name_length', __u16), ('data', POINTER(None)), ('data_length', __u32),
    ('data_offset', __u32)]
if _libs['libbpf.so.1'].has('bpf_object__add_map', 'cdecl'):
    bpf_object__add_map = _libs['libbpf.so.1'].get('bpf_object__add_map',
        'cdecl')
    bpf_object__add_map.argtypes = [POINTER(struct_bpf_object)]
    bpf_object__add_map.restype = POINTER(struct_bpf_map)
if _libs['libbpf.so.1'].has('prog_is_subprog', 'cdecl'):
    prog_is_subprog = _libs['libbpf.so.1'].get('prog_is_subprog', 'cdecl')
    prog_is_subprog.argtypes = [POINTER(struct_bpf_object), POINTER(
        struct_bpf_program)]
    prog_is_subprog.restype = c_bool
if _libs['libbpf.so.1'].has('map_set_def_max_entries', 'cdecl'):
    map_set_def_max_entries = _libs['libbpf.so.1'].get(
        'map_set_def_max_entries', 'cdecl')
    map_set_def_max_entries.argtypes = [POINTER(struct_bpf_map)]
    map_set_def_max_entries.restype = c_int
for _lib in _libs.values():
    try:
        old_print_fn = libbpf_print_fn_t.in_dll(_lib, 'old_print_fn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        args = c_void_p.in_dll(_lib, 'args')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        old_errno = c_int.in_dll(_lib, 'old_errno')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        print_fn = libbpf_print_fn_t.in_dll(_lib, 'print_fn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        limit = struct_rlimit.in_dll(_lib, 'limit')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(100)).in_dll(_lib, 'buf')
        break
    except:
        pass
enum_reloc_type = c_int
RELO_LD64 = 0
RELO_CALL = RELO_LD64 + 1
RELO_DATA = RELO_CALL + 1
RELO_EXTERN_LD64 = RELO_DATA + 1
RELO_EXTERN_CALL = RELO_EXTERN_LD64 + 1
RELO_SUBPROG_ADDR = RELO_EXTERN_CALL + 1
RELO_CORE = RELO_SUBPROG_ADDR + 1


class struct_anon_276(Structure):
    pass


struct_anon_276.__slots__ = ['map_idx', 'sym_off', 'ext_idx']
struct_anon_276._fields_ = [('map_idx', c_int), ('sym_off', c_int), (
    'ext_idx', c_int)]


class union_anon_277(Union):
    pass


union_anon_277.__slots__ = ['core_relo', 'unnamed_anon_277_1']
union_anon_277._anonymous_ = ['unnamed_anon_277_1']
union_anon_277._fields_ = [('core_relo', POINTER(struct_bpf_core_relo)), (
    'unnamed_anon_277_1', struct_anon_276)]


class struct_reloc_desc(Structure):
    pass


struct_reloc_desc.__slots__ = ['type', 'insn_idx', 'unnamed_reloc_desc_1']
struct_reloc_desc._anonymous_ = ['unnamed_reloc_desc_1']
struct_reloc_desc._fields_ = [('type', enum_reloc_type), ('insn_idx', c_int
    ), ('unnamed_reloc_desc_1', union_anon_277)]
enum_sec_def_flags = c_int
SEC_NONE = 0
SEC_EXP_ATTACH_OPT = 1
SEC_ATTACHABLE = 2
SEC_ATTACHABLE_OPT = SEC_ATTACHABLE | SEC_EXP_ATTACH_OPT
SEC_ATTACH_BTF = 4
SEC_SLEEPABLE = 8
SEC_XDP_FRAGS = 16
SEC_USDT = 32


class struct_bpf_sec_def(Structure):
    pass


struct_bpf_sec_def.__slots__ = ['sec', 'prog_type', 'expected_attach_type',
    'cookie', 'handler_id', 'prog_setup_fn', 'prog_prepare_load_fn',
    'prog_attach_fn']
struct_bpf_sec_def._fields_ = [('sec', String), ('prog_type',
    enum_bpf_prog_type), ('expected_attach_type', enum_bpf_attach_type), (
    'cookie', c_long), ('handler_id', c_int), ('prog_setup_fn',
    libbpf_prog_setup_fn_t), ('prog_prepare_load_fn',
    libbpf_prog_prepare_load_fn_t), ('prog_attach_fn', libbpf_prog_attach_fn_t)
    ]
struct_bpf_program.__slots__ = ['name', 'sec_name', 'sec_idx', 'sec_def',
    'sec_insn_off', 'sec_insn_cnt', 'sub_insn_off', 'insns', 'insns_cnt',
    'reloc_desc', 'nr_reloc', 'log_buf', 'log_size', 'log_level', 'obj',
    'fd', 'autoload', 'autoattach', 'sym_global', 'mark_btf_static', 'type',
    'expected_attach_type', 'exception_cb_idx', 'prog_ifindex',
    'attach_btf_obj_fd', 'attach_btf_id', 'attach_prog_fd', 'func_info',
    'func_info_rec_size', 'func_info_cnt', 'line_info',
    'line_info_rec_size', 'line_info_cnt', 'prog_flags']
struct_bpf_program._fields_ = [('name', String), ('sec_name', String), (
    'sec_idx', c_size_t), ('sec_def', POINTER(struct_bpf_sec_def)), (
    'sec_insn_off', c_size_t), ('sec_insn_cnt', c_size_t), ('sub_insn_off',
    c_size_t), ('insns', POINTER(struct_bpf_insn)), ('insns_cnt', c_size_t),
    ('reloc_desc', POINTER(struct_reloc_desc)), ('nr_reloc', c_int), (
    'log_buf', String), ('log_size', c_size_t), ('log_level', __u32), (
    'obj', POINTER(struct_bpf_object)), ('fd', c_int), ('autoload', c_bool),
    ('autoattach', c_bool), ('sym_global', c_bool), ('mark_btf_static',
    c_bool), ('type', enum_bpf_prog_type), ('expected_attach_type',
    enum_bpf_attach_type), ('exception_cb_idx', c_int), ('prog_ifindex',
    c_int), ('attach_btf_obj_fd', __u32), ('attach_btf_id', __u32), (
    'attach_prog_fd', __u32), ('func_info', POINTER(None)), (
    'func_info_rec_size', __u32), ('func_info_cnt', __u32), ('line_info',
    POINTER(None)), ('line_info_rec_size', __u32), ('line_info_cnt', __u32),
    ('prog_flags', __u32)]


class struct_bpf_struct_ops(Structure):
    pass


struct_bpf_struct_ops.__slots__ = ['tname', 'type', 'progs',
    'kern_func_off', 'data', 'kern_vdata', 'type_id']
struct_bpf_struct_ops._fields_ = [('tname', String), ('type', POINTER(
    struct_btf_type)), ('progs', POINTER(POINTER(struct_bpf_program))), (
    'kern_func_off', POINTER(__u32)), ('data', POINTER(None)), (
    'kern_vdata', POINTER(None)), ('type_id', __u32)]
enum_libbpf_map_type = c_int
LIBBPF_MAP_UNSPEC = 0
LIBBPF_MAP_DATA = LIBBPF_MAP_UNSPEC + 1
LIBBPF_MAP_BSS = LIBBPF_MAP_DATA + 1
LIBBPF_MAP_RODATA = LIBBPF_MAP_BSS + 1
LIBBPF_MAP_KCONFIG = LIBBPF_MAP_RODATA + 1


class struct_bpf_map_def(Structure):
    pass


struct_bpf_map_def.__slots__ = ['type', 'key_size', 'value_size',
    'max_entries', 'map_flags']
struct_bpf_map_def._fields_ = [('type', c_uint), ('key_size', c_uint), (
    'value_size', c_uint), ('max_entries', c_uint), ('map_flags', c_uint)]
struct_bpf_map.__slots__ = ['obj', 'name', 'real_name', 'fd', 'sec_idx',
    'sec_offset', 'map_ifindex', 'inner_map_fd', '_def', 'numa_node',
    'btf_var_idx', 'mod_btf_fd', 'btf_key_type_id', 'btf_value_type_id',
    'btf_vmlinux_value_type_id', 'libbpf_type', 'mmaped', 'st_ops',
    'inner_map', 'init_slots', 'init_slots_sz', 'pin_path', 'pinned',
    'reused', 'autocreate', 'map_extra']
struct_bpf_map._fields_ = [('obj', POINTER(struct_bpf_object)), ('name',
    String), ('real_name', String), ('fd', c_int), ('sec_idx', c_int), (
    'sec_offset', c_size_t), ('map_ifindex', c_int), ('inner_map_fd', c_int
    ), ('_def', struct_bpf_map_def), ('numa_node', __u32), ('btf_var_idx',
    __u32), ('mod_btf_fd', c_int), ('btf_key_type_id', __u32), (
    'btf_value_type_id', __u32), ('btf_vmlinux_value_type_id', __u32), (
    'libbpf_type', enum_libbpf_map_type), ('mmaped', POINTER(None)), (
    'st_ops', POINTER(struct_bpf_struct_ops)), ('inner_map', POINTER(
    struct_bpf_map)), ('init_slots', POINTER(POINTER(None))), (
    'init_slots_sz', c_int), ('pin_path', String), ('pinned', c_bool), (
    'reused', c_bool), ('autocreate', c_bool), ('map_extra', __u64)]
enum_extern_type = c_int
EXT_UNKNOWN = 0
EXT_KCFG = EXT_UNKNOWN + 1
EXT_KSYM = EXT_KCFG + 1
enum_kcfg_type = c_int
KCFG_UNKNOWN = 0
KCFG_CHAR = KCFG_UNKNOWN + 1
KCFG_BOOL = KCFG_CHAR + 1
KCFG_INT = KCFG_BOOL + 1
KCFG_TRISTATE = KCFG_INT + 1
KCFG_CHAR_ARR = KCFG_TRISTATE + 1


class struct_anon_278(Structure):
    pass


struct_anon_278.__slots__ = ['type', 'sz', 'align', 'data_off', 'is_signed']
struct_anon_278._fields_ = [('type', enum_kcfg_type), ('sz', c_int), (
    'align', c_int), ('data_off', c_int), ('is_signed', c_bool)]


class struct_anon_279(Structure):
    pass


struct_anon_279.__slots__ = ['addr', 'kernel_btf_obj_fd', 'kernel_btf_id',
    'type_id', 'btf_fd_idx']
struct_anon_279._fields_ = [('addr', c_ulonglong), ('kernel_btf_obj_fd',
    c_int), ('kernel_btf_id', c_int), ('type_id', __u32), ('btf_fd_idx', __s16)
    ]


class union_anon_280(Union):
    pass


union_anon_280.__slots__ = ['kcfg', 'ksym']
union_anon_280._fields_ = [('kcfg', struct_anon_278), ('ksym', struct_anon_279)
    ]


class struct_extern_desc(Structure):
    pass


struct_extern_desc.__slots__ = ['type', 'sym_idx', 'btf_id', 'sec_btf_id',
    'name', 'essent_name', 'is_set', 'is_weak', 'unnamed_extern_desc_1']
struct_extern_desc._anonymous_ = ['unnamed_extern_desc_1']
struct_extern_desc._fields_ = [('type', enum_extern_type), ('sym_idx',
    c_int), ('btf_id', c_int), ('sec_btf_id', c_int), ('name', String), (
    'essent_name', String), ('is_set', c_bool), ('is_weak', c_bool), (
    'unnamed_extern_desc_1', union_anon_280)]


class struct_module_btf(Structure):
    pass


struct_module_btf.__slots__ = ['btf', 'name', 'id', 'fd', 'fd_array_idx']
struct_module_btf._fields_ = [('btf', POINTER(struct_btf)), ('name', String
    ), ('id', __u32), ('fd', c_int), ('fd_array_idx', c_int)]
enum_sec_type = c_int
SEC_UNUSED = 0
SEC_RELO = SEC_UNUSED + 1
SEC_BSS = SEC_RELO + 1
SEC_DATA = SEC_BSS + 1
SEC_RODATA = SEC_DATA + 1


class struct_elf_sec_desc(Structure):
    pass


struct_elf_sec_desc.__slots__ = ['sec_type', 'shdr', 'data']
struct_elf_sec_desc._fields_ = [('sec_type', enum_sec_type), ('shdr',
    POINTER(Elf64_Shdr)), ('data', POINTER(Elf_Data))]


class struct_elf_state(Structure):
    pass


struct_elf_state.__slots__ = ['fd', 'obj_buf', 'obj_buf_sz', 'elf', 'ehdr',
    'symbols', 'st_ops_data', 'st_ops_link_data', 'shstrndx', 'strtabidx',
    'secs', 'sec_cnt', 'btf_maps_shndx', 'btf_maps_sec_btf_id',
    'text_shndx', 'symbols_shndx', 'st_ops_shndx', 'st_ops_link_shndx']
struct_elf_state._fields_ = [('fd', c_int), ('obj_buf', POINTER(None)), (
    'obj_buf_sz', c_size_t), ('elf', POINTER(Elf)), ('ehdr', POINTER(
    Elf64_Ehdr)), ('symbols', POINTER(Elf_Data)), ('st_ops_data', POINTER(
    Elf_Data)), ('st_ops_link_data', POINTER(Elf_Data)), ('shstrndx',
    c_size_t), ('strtabidx', c_size_t), ('secs', POINTER(
    struct_elf_sec_desc)), ('sec_cnt', c_size_t), ('btf_maps_shndx', c_int),
    ('btf_maps_sec_btf_id', __u32), ('text_shndx', c_int), ('symbols_shndx',
    c_int), ('st_ops_shndx', c_int), ('st_ops_link_shndx', c_int)]
struct_bpf_object.__slots__ = ['name', 'license', 'kern_version',
    'programs', 'nr_programs', 'maps', 'nr_maps', 'maps_cap', 'kconfig',
    'externs', 'nr_extern', 'kconfig_map_idx', 'loaded', 'has_subcalls',
    'has_rodata', 'gen_loader', 'efile', 'btf', 'btf_ext', 'btf_vmlinux',
    'btf_custom_path', 'btf_vmlinux_override', 'btf_modules',
    'btf_modules_loaded', 'btf_module_cnt', 'btf_module_cap', 'log_buf',
    'log_size', 'log_level', 'fd_array', 'fd_array_cap', 'fd_array_cnt',
    'usdt_man', 'feat_cache', 'token_path', 'token_fd', 'path']
struct_bpf_object._fields_ = [('name', c_char * int(16)), ('license', 
    c_char * int(64)), ('kern_version', __u32), ('programs', POINTER(
    struct_bpf_program)), ('nr_programs', c_size_t), ('maps', POINTER(
    struct_bpf_map)), ('nr_maps', c_size_t), ('maps_cap', c_size_t), (
    'kconfig', String), ('externs', POINTER(struct_extern_desc)), (
    'nr_extern', c_int), ('kconfig_map_idx', c_int), ('loaded', c_bool), (
    'has_subcalls', c_bool), ('has_rodata', c_bool), ('gen_loader', POINTER
    (struct_bpf_gen)), ('efile', struct_elf_state), ('btf', POINTER(
    struct_btf)), ('btf_ext', POINTER(struct_btf_ext)), ('btf_vmlinux',
    POINTER(struct_btf)), ('btf_custom_path', String), (
    'btf_vmlinux_override', POINTER(struct_btf)), ('btf_modules', POINTER(
    struct_module_btf)), ('btf_modules_loaded', c_bool), ('btf_module_cnt',
    c_size_t), ('btf_module_cap', c_size_t), ('log_buf', String), (
    'log_size', c_size_t), ('log_level', __u32), ('fd_array', POINTER(c_int
    )), ('fd_array_cap', c_size_t), ('fd_array_cnt', c_size_t), ('usdt_man',
    POINTER(struct_usdt_manager)), ('feat_cache', POINTER(
    struct_kern_feature_cache)), ('token_path', String), ('token_fd', c_int
    ), ('path', POINTER(c_char))]
if _libs['libbpf.so.1'].has('elf_sym_str', 'cdecl'):
    elf_sym_str = _libs['libbpf.so.1'].get('elf_sym_str', 'cdecl')
    elf_sym_str.argtypes = [POINTER(struct_bpf_object), c_size_t]
    elf_sym_str.restype = c_char_p
if _libs['libbpf.so.1'].has('elf_sec_str', 'cdecl'):
    elf_sec_str = _libs['libbpf.so.1'].get('elf_sec_str', 'cdecl')
    elf_sec_str.argtypes = [POINTER(struct_bpf_object), c_size_t]
    elf_sec_str.restype = c_char_p
if _libs['libbpf.so.1'].has('elf_sec_by_idx', 'cdecl'):
    elf_sec_by_idx = _libs['libbpf.so.1'].get('elf_sec_by_idx', 'cdecl')
    elf_sec_by_idx.argtypes = [POINTER(struct_bpf_object), c_size_t]
    elf_sec_by_idx.restype = POINTER(Elf_Scn)
if _libs['libbpf.so.1'].has('elf_sec_by_name', 'cdecl'):
    elf_sec_by_name = _libs['libbpf.so.1'].get('elf_sec_by_name', 'cdecl')
    elf_sec_by_name.argtypes = [POINTER(struct_bpf_object), String]
    elf_sec_by_name.restype = POINTER(Elf_Scn)
if _libs['libbpf.so.1'].has('elf_sec_hdr', 'cdecl'):
    elf_sec_hdr = _libs['libbpf.so.1'].get('elf_sec_hdr', 'cdecl')
    elf_sec_hdr.argtypes = [POINTER(struct_bpf_object), POINTER(Elf_Scn)]
    elf_sec_hdr.restype = POINTER(Elf64_Shdr)
if _libs['libbpf.so.1'].has('elf_sec_name', 'cdecl'):
    elf_sec_name = _libs['libbpf.so.1'].get('elf_sec_name', 'cdecl')
    elf_sec_name.argtypes = [POINTER(struct_bpf_object), POINTER(Elf_Scn)]
    elf_sec_name.restype = c_char_p
if _libs['libbpf.so.1'].has('elf_sec_data', 'cdecl'):
    elf_sec_data = _libs['libbpf.so.1'].get('elf_sec_data', 'cdecl')
    elf_sec_data.argtypes = [POINTER(struct_bpf_object), POINTER(Elf_Scn)]
    elf_sec_data.restype = POINTER(Elf_Data)
if _libs['libbpf.so.1'].has('elf_sym_by_idx', 'cdecl'):
    elf_sym_by_idx = _libs['libbpf.so.1'].get('elf_sym_by_idx', 'cdecl')
    elf_sym_by_idx.argtypes = [POINTER(struct_bpf_object), c_size_t]
    elf_sym_by_idx.restype = POINTER(Elf64_Sym)
if _libs['libbpf.so.1'].has('elf_rel_by_idx', 'cdecl'):
    elf_rel_by_idx = _libs['libbpf.so.1'].get('elf_rel_by_idx', 'cdecl')
    elf_rel_by_idx.argtypes = [POINTER(Elf_Data), c_size_t]
    elf_rel_by_idx.restype = POINTER(Elf64_Rel)
for _lib in _libs.values():
    try:
        symbols = POINTER(Elf_Data).in_dll(_lib, 'symbols')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        progs = POINTER(struct_bpf_program).in_dll(_lib, 'progs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(None).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_sz = c_size_t.in_dll(_lib, 'sec_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_off = c_size_t.in_dll(_lib, 'sec_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_sz = c_size_t.in_dll(_lib, 'prog_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nr_syms = c_size_t.in_dll(_lib, 'nr_syms')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nr_progs = c_int.in_dll(_lib, 'nr_progs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym = POINTER(Elf64_Sym).in_dll(_lib, 'sym')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        m = POINTER(struct_btf_member).in_dll(_lib, 'm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        m = POINTER(struct_btf_member).in_dll(_lib, 'm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('find_ksym_btf_id', 'cdecl'):
    find_ksym_btf_id = _libs['libbpf.so.1'].get('find_ksym_btf_id', 'cdecl')
    find_ksym_btf_id.argtypes = [POINTER(struct_bpf_object), String, __u16,
        POINTER(POINTER(struct_btf)), POINTER(POINTER(struct_module_btf))]
    find_ksym_btf_id.restype = c_int
if _libs['libbpf.so.1'].has('find_btf_by_prefix_kind', 'cdecl'):
    find_btf_by_prefix_kind = _libs['libbpf.so.1'].get(
        'find_btf_by_prefix_kind', 'cdecl')
    find_btf_by_prefix_kind.argtypes = [POINTER(struct_btf), String, String,
        __u32]
    find_btf_by_prefix_kind.restype = c_int
for _lib in _libs.values():
    try:
        kern_type = POINTER(struct_btf_type).in_dll(_lib, 'kern_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_vtype = POINTER(struct_btf_type).in_dll(_lib, 'kern_vtype')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_data_member = POINTER(struct_btf_member).in_dll(_lib,
            'kern_data_member')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_vtype_id = __s32.in_dll(_lib, 'kern_vtype_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_type_id = __s32.in_dll(_lib, 'kern_type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = __u32.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        member = POINTER(struct_btf_member).in_dll(_lib, 'member')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_member = POINTER(struct_btf_member).in_dll(_lib, 'kern_member')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_data_member = POINTER(struct_btf_member).in_dll(_lib,
            'kern_data_member')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = POINTER(struct_btf_type).in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_type = POINTER(struct_btf_type).in_dll(_lib, 'kern_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_vtype = POINTER(struct_btf_type).in_dll(_lib, 'kern_vtype')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = __u32.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_type_id = __u32.in_dll(_lib, 'kern_type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_vtype_id = __u32.in_dll(_lib, 'kern_vtype_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_data_off = __u32.in_dll(_lib, 'kern_data_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        st_ops = POINTER(struct_bpf_struct_ops).in_dll(_lib, 'st_ops')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_btf = POINTER(struct_btf).in_dll(_lib, 'kern_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mod_btf = POINTER(struct_module_btf).in_dll(_lib, 'mod_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(None).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_data = POINTER(None).in_dll(_lib, 'kern_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tname = String.in_dll(_lib, 'tname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mtype = POINTER(struct_btf_type).in_dll(_lib, 'mtype')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_mtype = POINTER(struct_btf_type).in_dll(_lib, 'kern_mtype')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mtype_id = __u32.in_dll(_lib, 'mtype_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_mtype_id = __u32.in_dll(_lib, 'kern_mtype_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mdata = POINTER(None).in_dll(_lib, 'mdata')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_mdata = POINTER(None).in_dll(_lib, 'kern_mdata')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        msize = __s64.in_dll(_lib, 'msize')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_msize = __s64.in_dll(_lib, 'kern_msize')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        moff = __u32.in_dll(_lib, 'moff')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_moff = __u32.in_dll(_lib, 'kern_moff')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_member_idx = __u32.in_dll(_lib, 'kern_member_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mname = String.in_dll(_lib, 'mname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_size_t.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = POINTER(struct_btf_type).in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        datasec = POINTER(struct_btf_type).in_dll(_lib, 'datasec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vsi = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vsi')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        st_ops = POINTER(struct_bpf_struct_ops).in_dll(_lib, 'st_ops')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tname = String.in_dll(_lib, 'tname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_name = String.in_dll(_lib, 'var_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type_id = __s32.in_dll(_lib, 'type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        datasec_id = __s32.in_dll(_lib, 'datasec_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = __u32.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        end = String.in_dll(_lib, 'end')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ___err = c_int.in_dll(_lib, '___err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ehdr = POINTER(Elf64_Ehdr).in_dll(_lib, 'ehdr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        elf = POINTER(Elf).in_dll(_lib, 'elf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kver = __u32.in_dll(_lib, 'kver')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(Elf_Data).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        symbols = POINTER(Elf_Data).in_dll(_lib, 'symbols')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sname = String.in_dll(_lib, 'sname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        si = c_size_t.in_dll(_lib, 'si')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym = POINTER(Elf64_Sym).in_dll(_lib, 'sym')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        page_sz = c_long.in_dll(_lib, 'page_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_sz = c_size_t.in_dll(_lib, 'map_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmaped = POINTER(None).in_dll(_lib, 'mmaped')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_name = (c_char * int(16)).in_dll(_lib, 'map_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        p = String.in_dll(_lib, 'p')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('map_fill_btf_type_info', 'cdecl'):
    map_fill_btf_type_info = _libs['libbpf.so.1'].get('map_fill_btf_type_info',
        'cdecl')
    map_fill_btf_type_info.argtypes = [POINTER(struct_bpf_object), POINTER(
        struct_bpf_map)]
    map_fill_btf_type_info.restype = c_int
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vt = POINTER(struct_btf_type).in_dll(_lib, 'vt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vsi = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vsi')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        _def = POINTER(struct_bpf_map_def).in_dll(_lib, 'def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmap_sz = c_size_t.in_dll(_lib, 'mmap_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_desc = POINTER(struct_elf_sec_desc).in_dll(_lib, 'sec_desc')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_idx = c_int.in_dll(_lib, 'sec_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_size_t.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        value_end = String.in_dll(_lib, 'value_end')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        bit_sz = c_int.in_dll(_lib, 'bit_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sep = String.in_dll(_lib, 'sep')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        value = String.in_dll(_lib, 'value')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_int.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext_val = POINTER(None).in_dll(_lib, 'ext_val')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        num = __u64.in_dll(_lib, 'num')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(4096)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        uts = struct_utsname.in_dll(_lib, 'uts')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_int.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = gzFile.in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(4096)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = POINTER(FILE).in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        last_ext = POINTER(struct_extern_desc).in_dll(_lib, 'last_ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_sz = c_size_t.in_dll(_lib, 'map_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        arr_info = POINTER(struct_btf_array).in_dll(_lib, 'arr_info')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        arr_t = POINTER(struct_btf_type).in_dll(_lib, 'arr_t')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_int.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(4096)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
enum_libbpf_pin_type = c_int
LIBBPF_PIN_NONE = 0
LIBBPF_PIN_BY_NAME = LIBBPF_PIN_NONE + 1
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        m = POINTER(struct_btf_member).in_dll(_lib, 'm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        is_inner = c_bool.in_dll(_lib, 'is_inner')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vlen = c_int.in_dll(_lib, 'vlen')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sz = __u32.in_dll(_lib, 'sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sz = __s64.in_dll(_lib, 'sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sz = __u32.in_dll(_lib, 'sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sz = __s64.in_dll(_lib, 'sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        is_map_in_map = c_bool.in_dll(_lib, 'is_map_in_map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        is_prog_array = c_bool.in_dll(_lib, 'is_prog_array')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        desc = String.in_dll(_lib, 'desc')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        inner_map_name = (c_char * int(128)).in_dll(_lib, 'inner_map_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        val = __u32.in_dll(_lib, 'val')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_extra = __u32.in_dll(_lib, 'map_extra')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        page_sz = __u32.in_dll(_lib, 'page_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mul = __u32.in_dll(_lib, 'mul')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var = POINTER(struct_btf_type).in_dll(_lib, 'var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        __def = POINTER(struct_btf_type).in_dll(_lib, 'def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vi = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vi')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_extra = POINTER(struct_btf_var).in_dll(_lib, 'var_extra')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_name = String.in_dll(_lib, 'map_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec = POINTER(struct_btf_type).in_dll(_lib, 'sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nr_types = c_int.in_dll(_lib, 'nr_types')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vlen = c_int.in_dll(_lib, 'vlen')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(Elf_Data).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pin_root_path = String.in_dll(_lib, 'pin_root_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        strict = c_bool.in_dll(_lib, 'strict')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sh = POINTER(Elf64_Shdr).in_dll(_lib, 'sh')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_func_global = c_bool.in_dll(_lib, 'has_func_global')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_datasec = c_bool.in_dll(_lib, 'has_datasec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_float = c_bool.in_dll(_lib, 'has_float')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_func = c_bool.in_dll(_lib, 'has_func')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_decl_tag = c_bool.in_dll(_lib, 'has_decl_tag')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_type_tag = c_bool.in_dll(_lib, 'has_type_tag')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_enum64 = c_bool.in_dll(_lib, 'has_enum64')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_func_global = c_bool.in_dll(_lib, 'has_func_global')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_datasec = c_bool.in_dll(_lib, 'has_datasec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_float = c_bool.in_dll(_lib, 'has_float')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_func = c_bool.in_dll(_lib, 'has_func')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_decl_tag = c_bool.in_dll(_lib, 'has_decl_tag')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_type_tag = c_bool.in_dll(_lib, 'has_type_tag')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        has_enum64 = c_bool.in_dll(_lib, 'has_enum64')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        enum64_placeholder_id = c_int.in_dll(_lib, 'enum64_placeholder_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_int.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vlen = c_int.in_dll(_lib, 'vlen')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        v = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'v')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        m = POINTER(struct_btf_member).in_dll(_lib, 'm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vt = POINTER(struct_btf_type).in_dll(_lib, 'vt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        m = POINTER(struct_btf_member).in_dll(_lib, 'm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext_segs = (POINTER(struct_btf_ext_info) * int(3)).in_dll(_lib,
            'ext_segs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        seg_num = c_int.in_dll(_lib, 'seg_num')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_num = c_int.in_dll(_lib, 'sec_num')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        seg = POINTER(struct_btf_ext_info).in_dll(_lib, 'seg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec = POINTER(struct_btf_ext_info_sec).in_dll(_lib, 'sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        a = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'a')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        b = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'b')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        size = __u32.in_dll(_lib, 'size')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = __u32.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vars = __u32.in_dll(_lib, 'vars')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vsi = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vsi')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fixup_offsets = c_bool.in_dll(_lib, 'fixup_offsets')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t_var = POINTER(struct_btf_type).in_dll(_lib, 't_var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var = POINTER(struct_btf_var).in_dll(_lib, 'var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_name = String.in_dll(_lib, 'var_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym = POINTER(Elf64_Sym).in_dll(_lib, 'sym')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_btf = POINTER(struct_btf).in_dll(_lib, 'kern_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_mandatory = c_bool.in_dll(_lib, 'btf_mandatory')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sanitize = c_bool.in_dll(_lib, 'sanitize')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_int.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        raw_data = POINTER(None).in_dll(_lib, 'raw_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sz = __u32.in_dll(_lib, 'sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        raw_size = __u32.in_dll(_lib, 'raw_size')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        raw_data = POINTER(None).in_dll(_lib, 'raw_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        elf = POINTER(Elf).in_dll(_lib, 'elf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        shdr = POINTER(Elf64_Shdr).in_dll(_lib, 'shdr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sh = POINTER(Elf64_Shdr).in_dll(_lib, 'sh')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(Elf_Data).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        a = POINTER(struct_bpf_program).in_dll(_lib, 'a')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        b = POINTER(struct_bpf_program).in_dll(_lib, 'b')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_desc = POINTER(struct_elf_sec_desc).in_dll(_lib, 'sec_desc')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        elf = POINTER(Elf).in_dll(_lib, 'elf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_ext_data = POINTER(Elf_Data).in_dll(_lib, 'btf_ext_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_data = POINTER(Elf_Data).in_dll(_lib, 'btf_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        idx = c_int.in_dll(_lib, 'idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(Elf_Data).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sh = POINTER(Elf64_Shdr).in_dll(_lib, 'sh')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_sec_idx = c_int.in_dll(_lib, 'targ_sec_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        bind = c_int.in_dll(_lib, 'bind')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        bind = c_int.in_dll(_lib, 'bind')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = c_int.in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tname = String.in_dll(_lib, 'tname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vs = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_int.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        enc = c_int.in_dll(_lib, 'enc')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        a = POINTER(struct_extern_desc).in_dll(_lib, 'a')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        b = POINTER(struct_extern_desc).in_dll(_lib, 'b')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        int_btf_id = c_int.in_dll(_lib, 'int_btf_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_btf_id = c_int.in_dll(_lib, 'sec_btf_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        dummy_var_btf_id = c_int.in_dll(_lib, 'dummy_var_btf_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vs = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec = POINTER(struct_btf_type).in_dll(_lib, 'sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vt = POINTER(struct_btf_type).in_dll(_lib, 'vt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec = POINTER(struct_btf_type).in_dll(_lib, 'sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kcfg_sec = POINTER(struct_btf_type).in_dll(_lib, 'kcfg_sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ksym_sec = POINTER(struct_btf_type).in_dll(_lib, 'ksym_sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        off = c_int.in_dll(_lib, 'off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        dummy_var_btf_id = c_int.in_dll(_lib, 'dummy_var_btf_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext_name = String.in_dll(_lib, 'ext_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext_essent_len = c_size_t.in_dll(_lib, 'ext_essent_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sh = POINTER(Elf64_Shdr).in_dll(_lib, 'sh')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym = POINTER(Elf64_Sym).in_dll(_lib, 'sym')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        int_btf_id = c_int.in_dll(_lib, 'int_btf_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        dummy_var = POINTER(struct_btf_type).in_dll(_lib, 'dummy_var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vs = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vt = POINTER(struct_btf_type).in_dll(_lib, 'vt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_proto = POINTER(struct_btf_type).in_dll(_lib, 'func_proto')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        param = POINTER(struct_btf_param).in_dll(_lib, 'param')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_int.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vs = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn = POINTER(struct_bpf_insn).in_dll(_lib, 'insn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_idx = c_size_t.in_dll(_lib, 'map_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nr_maps = c_size_t.in_dll(_lib, 'nr_maps')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        shdr_idx = __u32.in_dll(_lib, 'shdr_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = enum_libbpf_map_type.in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_sec_name = String.in_dll(_lib, 'sym_sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_idx = c_int.in_dll(_lib, 'sym_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        l = c_int.in_dll(_lib, 'l')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        r = c_int.in_dll(_lib, 'r')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        m = c_int.in_dll(_lib, 'm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo_sec_name = String.in_dll(_lib, 'relo_sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_idx = c_size_t.in_dll(_lib, 'sec_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_idx = c_size_t.in_dll(_lib, 'sym_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relos = POINTER(struct_reloc_desc).in_dll(_lib, 'relos')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nrels = c_int.in_dll(_lib, 'nrels')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_name = String.in_dll(_lib, 'sym_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = __u32.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn = POINTER(Elf_Scn).in_dll(_lib, 'scn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        scn_data = POINTER(Elf_Data).in_dll(_lib, 'scn_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym = POINTER(Elf64_Sym).in_dll(_lib, 'sym')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rel = POINTER(Elf64_Rel).in_dll(_lib, 'rel')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        id = c_int.in_dll(_lib, 'id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = (c_char * int(4096)).in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buff = (c_char * int(4096)).in_dll(_lib, 'buff')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fp = POINTER(FILE).in_dll(_lib, 'fp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        val = __u32.in_dll(_lib, 'val')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        info = struct_bpf_map_info.in_dll(_lib, 'info')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = __u32.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name_len = __u32.in_dll(_lib, 'name_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_fd = c_int.in_dll(_lib, 'new_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_name = String.in_dll(_lib, 'new_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        bpffs_path = String.in_dll(_lib, 'bpffs_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        bpffs_fd = c_int.in_dll(_lib, 'bpffs_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        token_fd = c_int.in_dll(_lib, 'token_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mandatory = c_bool.in_dll(_lib, 'mandatory')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        level = enum_libbpf_print_level.in_dll(_lib, 'level')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_info = struct_bpf_map_info.in_dll(_lib, 'map_info')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        msg = (c_char * int(128)).in_dll(_lib, 'msg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_info_len = __u32.in_dll(_lib, 'map_info_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pin_fd = c_int.in_dll(_lib, 'pin_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_type = enum_libbpf_map_type.in_dll(_lib, 'map_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        zero = c_int.in_dll(_lib, 'zero')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('bpf_map__destroy', 'cdecl'):
    bpf_map__destroy = _libs['libbpf.so.1'].get('bpf_map__destroy', 'cdecl')
    bpf_map__destroy.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__destroy.restype = None
for _lib in _libs.values():
    try:
        ___def = POINTER(struct_bpf_map_def).in_dll(_lib, 'def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_name = String.in_dll(_lib, 'map_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_fd = c_int.in_dll(_lib, 'map_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_map = POINTER(struct_bpf_map).in_dll(_lib, 'targ_map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_uint.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_prog = POINTER(struct_bpf_program).in_dll(_lib, 'targ_prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_uint.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nr_cpus = c_int.in_dll(_lib, 'nr_cpus')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_uint.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_uint.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        retried = c_bool.in_dll(_lib, 'retried')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_size_t.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_cands = POINTER(struct_bpf_core_cand).in_dll(_lib, 'new_cands')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cand = POINTER(struct_bpf_core_cand).in_dll(_lib, 'cand')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_t = POINTER(struct_btf_type).in_dll(_lib, 'local_t')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_name = String.in_dll(_lib, 'targ_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_name = String.in_dll(_lib, 'local_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_essent_len = c_size_t.in_dll(_lib, 'targ_essent_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        info = struct_bpf_btf_info.in_dll(_lib, 'info')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mod_btf = POINTER(struct_module_btf).in_dll(_lib, 'mod_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = (c_char * int(64)).in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        id = __u32.in_dll(_lib, 'id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = __u32.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cands = POINTER(struct_bpf_core_cand_list).in_dll(_lib, 'cands')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        main_btf = POINTER(struct_btf).in_dll(_lib, 'main_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_t = POINTER(struct_btf_type).in_dll(_lib, 'local_t')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_name = String.in_dll(_lib, 'local_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_essent_len = c_size_t.in_dll(_lib, 'local_essent_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relos = POINTER(struct_reloc_desc).in_dll(_lib, 'relos')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_reloc_desc).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_reloc_desc).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cands = POINTER(struct_bpf_core_cand_list).in_dll(_lib, 'cands')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_name = String.in_dll(_lib, 'prog_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_type = POINTER(struct_btf_type).in_dll(_lib, 'local_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_name = String.in_dll(_lib, 'local_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_id = __u32.in_dll(_lib, 'local_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec = POINTER(struct_btf_ext_info_sec).in_dll(_lib, 'sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_res = struct_bpf_core_relo_res.in_dll(_lib, 'targ_res')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rec = POINTER(struct_bpf_core_relo).in_dll(_lib, 'rec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        seg = POINTER(struct_btf_ext_info).in_dll(_lib, 'seg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        entry = POINTER(struct_hashmap_entry).in_dll(_lib, 'entry')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cand_cache = POINTER(struct_hashmap).in_dll(_lib, 'cand_cache')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn = POINTER(struct_bpf_insn).in_dll(_lib, 'insn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = c_int.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_idx = c_int.in_dll(_lib, 'sec_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_num = c_int.in_dll(_lib, 'sec_num')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_reloc_desc).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn = POINTER(struct_bpf_insn).in_dll(_lib, 'insn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        copy_start = POINTER(None).in_dll(_lib, 'copy_start')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        copy_end = POINTER(None).in_dll(_lib, 'copy_end')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rec = POINTER(None).in_dll(_lib, 'rec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rec_end = POINTER(None).in_dll(_lib, 'rec_end')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_prog_info = POINTER(None).in_dll(_lib, 'new_prog_info')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec = POINTER(struct_btf_ext_info_sec).in_dll(_lib, 'sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        old_sz = c_size_t.in_dll(_lib, 'old_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_sz = c_size_t.in_dll(_lib, 'new_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_num = c_int.in_dll(_lib, 'sec_num')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_idx = c_int.in_dll(_lib, 'sec_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        off_adj = c_int.in_dll(_lib, 'off_adj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_off = __u32.in_dll(_lib, 'insn_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_off = POINTER(__u32).in_dll(_lib, 'insn_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = c_size_t.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_reloc_desc).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_cnt = c_int.in_dll(_lib, 'new_cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relos = POINTER(struct_reloc_desc).in_dll(_lib, 'relos')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insns = POINTER(struct_bpf_insn).in_dll(_lib, 'insns')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_cnt = c_size_t.in_dll(_lib, 'new_cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sub_insn_idx = c_size_t.in_dll(_lib, 'sub_insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = c_size_t.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        subprog = POINTER(struct_bpf_program).in_dll(_lib, 'subprog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_reloc_desc).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn = POINTER(struct_bpf_insn).in_dll(_lib, 'insn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        subprog = POINTER(struct_bpf_program).in_dll(_lib, 'subprog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        a = POINTER(struct_reloc_desc).in_dll(_lib, 'a')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        b = POINTER(struct_reloc_desc).in_dll(_lib, 'b')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        p = POINTER(struct_bpf_program).in_dll(_lib, 'p')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        str = String.in_dll(_lib, 'str')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfx_len = c_size_t.in_dll(_lib, 'pfx_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_int.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        subprog = POINTER(struct_bpf_program).in_dll(_lib, 'subprog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tname = String.in_dll(_lib, 'tname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_id = c_int.in_dll(_lib, 'fn_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_proto_id = c_int.in_dll(_lib, 'fn_proto_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret_type_id = c_int.in_dll(_lib, 'ret_type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        orig_proto_id = c_int.in_dll(_lib, 'orig_proto_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        arg_cnt = c_int.in_dll(_lib, 'arg_cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_name_off = c_int.in_dll(_lib, 'fn_name_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        linkage = c_int.in_dll(_lib, 'linkage')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_t = POINTER(struct_btf_type).in_dll(_lib, 'fn_t')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_proto_t = POINTER(struct_btf_type).in_dll(_lib, 'fn_proto_t')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        p = POINTER(struct_btf_param).in_dll(_lib, 'p')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name_off = c_int.in_dll(_lib, 'name_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        types = POINTER(__u32).in_dll(_lib, 'types')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_fd = c_int.in_dll(_lib, 'btf_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_cnt = c_int.in_dll(_lib, 'insn_cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ctx_name = String.in_dll(_lib, 'ctx_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ctx_tag = String.in_dll(_lib, 'ctx_tag')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_name = String.in_dll(_lib, 'fn_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_rec = POINTER(struct_bpf_func_info_min).in_dll(_lib, 'func_rec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_t = POINTER(struct_btf_type).in_dll(_lib, 'fn_t')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_proto_t = POINTER(struct_btf_type).in_dll(_lib, 'fn_proto_t')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        p = POINTER(struct_btf_param).in_dll(_lib, 'p')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ptr_id = c_int.in_dll(_lib, 'ptr_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        struct_id = c_int.in_dll(_lib, 'struct_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tag_id = c_int.in_dll(_lib, 'tag_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        orig_fn_id = c_int.in_dll(_lib, 'orig_fn_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        arg_idx = c_int.in_dll(_lib, 'arg_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        arg_cnt = c_int.in_dll(_lib, 'arg_cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rec_idx = c_int.in_dll(_lib, 'rec_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        orig_ids = POINTER(c_int).in_dll(_lib, 'orig_ids')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fn_id = c_int.in_dll(_lib, 'fn_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_size_t.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_size_t.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_reloc_desc).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn = POINTER(struct_bpf_insn).in_dll(_lib, 'insn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        subprog = POINTER(struct_bpf_program).in_dll(_lib, 'subprog')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('bpf_object__collect_st_ops_relos', 'cdecl'):
    bpf_object__collect_st_ops_relos = _libs['libbpf.so.1'].get(
        'bpf_object__collect_st_ops_relos', 'cdecl')
    bpf_object__collect_st_ops_relos.argtypes = [POINTER(struct_bpf_object),
        POINTER(Elf64_Shdr), POINTER(Elf_Data)]
    bpf_object__collect_st_ops_relos.restype = c_int
for _lib in _libs.values():
    try:
        bpf_ptr_sz = c_int.in_dll(_lib, 'bpf_ptr_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        host_ptr_sz = c_int.in_dll(_lib, 'host_ptr_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_int.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nrels = c_int.in_dll(_lib, 'nrels')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_sz = c_int.in_dll(_lib, 'new_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vi = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'vi')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec = POINTER(struct_btf_type).in_dll(_lib, 'sec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var = POINTER(struct_btf_type).in_dll(_lib, 'var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ____def = POINTER(struct_btf_type).in_dll(_lib, 'def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_map = POINTER(struct_bpf_map).in_dll(_lib, 'targ_map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_prog = POINTER(struct_bpf_program).in_dll(_lib, 'targ_prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        is_prog_array = c_bool.in_dll(_lib, 'is_prog_array')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        is_map_in_map = c_bool.in_dll(_lib, 'is_map_in_map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        member = POINTER(struct_btf_member).in_dll(_lib, 'member')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mname = String.in_dll(_lib, 'mname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = String.in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        moff = c_uint.in_dll(_lib, 'moff')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym = POINTER(Elf64_Sym).in_dll(_lib, 'sym')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rel = POINTER(Elf64_Rel).in_dll(_lib, 'rel')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tmp = POINTER(None).in_dll(_lib, 'tmp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_desc = POINTER(struct_elf_sec_desc).in_dll(_lib, 'sec_desc')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        shdr = POINTER(Elf64_Shdr).in_dll(_lib, 'shdr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(Elf_Data).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        idx = c_int.in_dll(_lib, 'idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn = POINTER(struct_bpf_insn).in_dll(_lib, 'insn')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_id = enum_bpf_func_id.in_dll(_lib, 'func_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('libbpf_find_attach_btf_id', 'cdecl'):
    libbpf_find_attach_btf_id = _libs['libbpf.so.1'].get(
        'libbpf_find_attach_btf_id', 'cdecl')
    libbpf_find_attach_btf_id.argtypes = [POINTER(struct_bpf_program),
        String, POINTER(c_int), POINTER(c_int)]
    libbpf_find_attach_btf_id.restype = c_int
for _lib in _libs.values():
    try:
        _____def = enum_sec_def_flags.in_dll(_lib, 'def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_obj_fd = c_int.in_dll(_lib, 'btf_obj_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_type_id = c_int.in_dll(_lib, 'btf_type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attach_name = String.in_dll(_lib, 'attach_name')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('fixup_verifier_log', 'cdecl'):
    fixup_verifier_log = _libs['libbpf.so.1'].get('fixup_verifier_log', 'cdecl'
        )
    fixup_verifier_log.argtypes = [POINTER(struct_bpf_program), String,
        c_size_t]
    fixup_verifier_log.restype = None
for _lib in _libs.values():
    try:
        prog_name = String.in_dll(_lib, 'prog_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        log_buf_size = c_size_t.in_dll(_lib, 'log_buf_size')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        log_buf = String.in_dll(_lib, 'log_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tmp = String.in_dll(_lib, 'tmp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_fd = c_int.in_dll(_lib, 'btf_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        own_log_buf = c_bool.in_dll(_lib, 'own_log_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        log_level = __u32.in_dll(_lib, 'log_level')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        p = String.in_dll(_lib, 'p')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rem_sz = c_size_t.in_dll(_lib, 'rem_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        patch_sz = c_size_t.in_dll(_lib, 'patch_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_bpf_core_relo).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        spec = struct_bpf_core_spec.in_dll(_lib, 'spec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        patch = (c_char * int(512)).in_dll(_lib, 'patch')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        spec_buf = (c_char * int(256)).in_dll(_lib, 'spec_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = c_int.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        spec_len = c_int.in_dll(_lib, 'spec_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = c_int.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_idx = c_int.in_dll(_lib, 'map_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        patch = (c_char * int(128)).in_dll(_lib, 'patch')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = c_int.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext_idx = c_int.in_dll(_lib, 'ext_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        patch = (c_char * int(128)).in_dll(_lib, 'patch')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        max_last_line_cnt = c_size_t.in_dll(_lib, 'max_last_line_cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prev_line = String.in_dll(_lib, 'prev_line')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cur_line = String.in_dll(_lib, 'cur_line')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        next_line = String.in_dll(_lib, 'next_line')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        log_sz = c_size_t.in_dll(_lib, 'log_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relo = POINTER(struct_reloc_desc).in_dll(_lib, 'relo')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kind = c_int.in_dll(_lib, 'kind')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_size_t.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('find_sec_def', 'cdecl'):
    find_sec_def = _libs['libbpf.so.1'].get('find_sec_def', 'cdecl')
    find_sec_def.argtypes = [String]
    find_sec_def.restype = POINTER(struct_bpf_sec_def)
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj_name = String.in_dll(_lib, 'obj_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kconfig = String.in_dll(_lib, 'kconfig')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_tmp_path = String.in_dll(_lib, 'btf_tmp_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        token_path = String.in_dll(_lib, 'token_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tmp_name = (c_char * int(64)).in_dll(_lib, 'tmp_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        log_buf = String.in_dll(_lib, 'log_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        log_size = c_size_t.in_dll(_lib, 'log_size')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        log_level = __u32.in_dll(_lib, 'log_level')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_size_t.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        m = POINTER(struct_bpf_map).in_dll(_lib, 'm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_type = c_char.in_dll(_lib, 'sym_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_name = (c_char * int(500)).in_dll(_lib, 'sym_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_addr = c_ulonglong.in_dll(_lib, 'sym_addr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        f = POINTER(FILE).in_dll(_lib, 'f')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mod_btf = POINTER(struct_module_btf).in_dll(_lib, 'mod_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        id = c_int.in_dll(_lib, 'id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_var = POINTER(struct_btf_type).in_dll(_lib, 'targ_var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_type = POINTER(struct_btf_type).in_dll(_lib, 'targ_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_type_id = __u32.in_dll(_lib, 'targ_type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_type_id = __u32.in_dll(_lib, 'local_type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mod_btf = POINTER(struct_module_btf).in_dll(_lib, 'mod_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_var_name = String.in_dll(_lib, 'targ_var_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        id = c_int.in_dll(_lib, 'id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_type = POINTER(struct_btf_type).in_dll(_lib, 'local_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        targ_name = String.in_dll(_lib, 'targ_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_name = String.in_dll(_lib, 'local_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        local_func_proto_id = c_int.in_dll(_lib, 'local_func_proto_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kfunc_proto_id = c_int.in_dll(_lib, 'kfunc_proto_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kfunc_id = c_int.in_dll(_lib, 'kfunc_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mod_btf = POINTER(struct_module_btf).in_dll(_lib, 'mod_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_func = POINTER(struct_btf_type).in_dll(_lib, 'kern_func')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_btf = POINTER(struct_btf).in_dll(_lib, 'kern_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        t = POINTER(struct_btf_type).in_dll(_lib, 't')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        need_config = c_bool.in_dll(_lib, 'need_config')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        need_kallsyms = c_bool.in_dll(_lib, 'need_kallsyms')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        need_vmlinux_btf = c_bool.in_dll(_lib, 'need_vmlinux_btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext = POINTER(struct_extern_desc).in_dll(_lib, 'ext')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kcfg_data = POINTER(None).in_dll(_lib, 'kcfg_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ext_ptr = POINTER(None).in_dll(_lib, 'ext_ptr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        value = __u64.in_dll(_lib, 'value')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        st_ops = POINTER(struct_bpf_struct_ops).in_dll(_lib, 'st_ops')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = __u32.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kern_data = POINTER(None).in_dll(_lib, 'kern_data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        dname = String.in_dll(_lib, 'dname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        dir = String.in_dll(_lib, 'dir')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        st_fs = struct_statfs.in_dll(_lib, 'st_fs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        dname = String.in_dll(_lib, 'dname')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        dir = String.in_dll(_lib, 'dir')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cp = String.in_dll(_lib, 'cp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new = String.in_dll(_lib, 'new')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('bpf_map__get_pin_path', 'cdecl'):
    bpf_map__get_pin_path = _libs['libbpf.so.1'].get('bpf_map__get_pin_path',
        'cdecl')
    bpf_map__get_pin_path.argtypes = [POINTER(struct_bpf_map)]
    bpf_map__get_pin_path.restype = c_char_p
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pin_path = String.in_dll(_lib, 'pin_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(4096)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pin_path = String.in_dll(_lib, 'pin_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(4096)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(4096)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(4096)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmap_sz = c_size_t.in_dll(_lib, 'mmap_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ___err = c_int.in_dll(_lib, '___err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_size_t.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        gen = POINTER(struct_bpf_gen).in_dll(_lib, 'gen')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nr_programs = c_size_t.in_dll(_lib, 'nr_programs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        idx = c_ptrdiff_t.in_dll(_lib, 'idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insns = POINTER(struct_bpf_insn).in_dll(_lib, 'insns')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('bpf_program__get_type', 'cdecl'):
    bpf_program__get_type = _libs['libbpf.so.1'].get('bpf_program__get_type',
        'cdecl')
    bpf_program__get_type.argtypes = [POINTER(struct_bpf_program)]
    bpf_program__get_type.restype = enum_bpf_prog_type
if _libs['libbpf.so.1'].has('bpf_program__get_expected_attach_type', 'cdecl'):
    bpf_program__get_expected_attach_type = _libs['libbpf.so.1'].get(
        'bpf_program__get_expected_attach_type', 'cdecl')
    bpf_program__get_expected_attach_type.argtypes = [POINTER(
        struct_bpf_program)]
    bpf_program__get_expected_attach_type.restype = enum_bpf_attach_type
if _libs['libbpf.so.1'].has('attach_kprobe', 'cdecl'):
    attach_kprobe = _libs['libbpf.so.1'].get('attach_kprobe', 'cdecl')
    attach_kprobe.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_kprobe.restype = c_int
if _libs['libbpf.so.1'].has('attach_uprobe', 'cdecl'):
    attach_uprobe = _libs['libbpf.so.1'].get('attach_uprobe', 'cdecl')
    attach_uprobe.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_uprobe.restype = c_int
if _libs['libbpf.so.1'].has('attach_ksyscall', 'cdecl'):
    attach_ksyscall = _libs['libbpf.so.1'].get('attach_ksyscall', 'cdecl')
    attach_ksyscall.argtypes = [POINTER(struct_bpf_program), c_long,
        POINTER(POINTER(struct_bpf_link))]
    attach_ksyscall.restype = c_int
if _libs['libbpf.so.1'].has('attach_usdt', 'cdecl'):
    attach_usdt = _libs['libbpf.so.1'].get('attach_usdt', 'cdecl')
    attach_usdt.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_usdt.restype = c_int
if _libs['libbpf.so.1'].has('attach_tp', 'cdecl'):
    attach_tp = _libs['libbpf.so.1'].get('attach_tp', 'cdecl')
    attach_tp.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_tp.restype = c_int
if _libs['libbpf.so.1'].has('attach_raw_tp', 'cdecl'):
    attach_raw_tp = _libs['libbpf.so.1'].get('attach_raw_tp', 'cdecl')
    attach_raw_tp.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_raw_tp.restype = c_int
if _libs['libbpf.so.1'].has('attach_trace', 'cdecl'):
    attach_trace = _libs['libbpf.so.1'].get('attach_trace', 'cdecl')
    attach_trace.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_trace.restype = c_int
if _libs['libbpf.so.1'].has('attach_kprobe_multi', 'cdecl'):
    attach_kprobe_multi = _libs['libbpf.so.1'].get('attach_kprobe_multi',
        'cdecl')
    attach_kprobe_multi.argtypes = [POINTER(struct_bpf_program), c_long,
        POINTER(POINTER(struct_bpf_link))]
    attach_kprobe_multi.restype = c_int
if _libs['libbpf.so.1'].has('attach_uprobe_multi', 'cdecl'):
    attach_uprobe_multi = _libs['libbpf.so.1'].get('attach_uprobe_multi',
        'cdecl')
    attach_uprobe_multi.argtypes = [POINTER(struct_bpf_program), c_long,
        POINTER(POINTER(struct_bpf_link))]
    attach_uprobe_multi.restype = c_int
if _libs['libbpf.so.1'].has('attach_lsm', 'cdecl'):
    attach_lsm = _libs['libbpf.so.1'].get('attach_lsm', 'cdecl')
    attach_lsm.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_lsm.restype = c_int
if _libs['libbpf.so.1'].has('attach_iter', 'cdecl'):
    attach_iter = _libs['libbpf.so.1'].get('attach_iter', 'cdecl')
    attach_iter.argtypes = [POINTER(struct_bpf_program), c_long, POINTER(
        POINTER(struct_bpf_link))]
    attach_iter.restype = c_int
for _lib in _libs.values():
    try:
        sec_def = POINTER(struct_bpf_sec_def).in_dll(_lib, 'sec_def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_defs = POINTER(struct_bpf_sec_def).in_dll(_lib, 'sec_defs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_size_t.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_def = POINTER(struct_bpf_sec_def).in_dll(_lib, 'sec_def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_int.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = String.in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_def = POINTER(struct_bpf_sec_def).in_dll(_lib, 'sec_def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_def = POINTER(struct_bpf_sec_def).in_dll(_lib, 'sec_def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type_names = String.in_dll(_lib, 'type_names')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_size_t.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        member = POINTER(struct_btf_member).in_dll(_lib, 'member')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        st_ops = POINTER(struct_bpf_struct_ops).in_dll(_lib, 'st_ops')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        shdr_idx = c_uint.in_dll(_lib, 'shdr_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        moff = c_uint.in_dll(_lib, 'moff')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        insn_idx = c_uint.in_dll(_lib, 'insn_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        member_idx = __u32.in_dll(_lib, 'member_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym = POINTER(Elf64_Sym).in_dll(_lib, 'sym')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        rel = POINTER(Elf64_Rel).in_dll(_lib, 'rel')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nrels = c_int.in_dll(_lib, 'nrels')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_type_name = (c_char * int(128)).in_dll(_lib, 'btf_type_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prefix = String.in_dll(_lib, 'prefix')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        kind = c_int.in_dll(_lib, 'kind')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        info = struct_bpf_prog_info.in_dll(_lib, 'info')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        info_len = __u32.in_dll(_lib, 'info_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mod = POINTER(struct_module_btf).in_dll(_lib, 'mod')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attach_type = enum_bpf_attach_type.in_dll(_lib, 'attach_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attach_prog_fd = __u32.in_dll(_lib, 'attach_prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type_names = String.in_dll(_lib, 'type_names')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_def = POINTER(struct_bpf_sec_def).in_dll(_lib, 'sec_def')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        datasec_type = POINTER(struct_btf_type).in_dll(_lib, 'datasec_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_type = POINTER(struct_btf_type).in_dll(_lib, 'var_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        array_type = POINTER(struct_btf_type).in_dll(_lib, 'array_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        array = POINTER(struct_btf_array).in_dll(_lib, 'array')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        vlen = c_int.in_dll(_lib, 'vlen')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        element_sz = c_int.in_dll(_lib, 'element_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        new_array_id = c_int.in_dll(_lib, 'new_array_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        nr_elements = __u32.in_dll(_lib, 'nr_elements')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmap_old_sz = c_size_t.in_dll(_lib, 'mmap_old_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmap_new_sz = c_size_t.in_dll(_lib, 'mmap_new_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        idx = c_ptrdiff_t.in_dll(_lib, 'idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        s = POINTER(struct_bpf_map).in_dll(_lib, 's')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        e = POINTER(struct_bpf_map).in_dll(_lib, 'e')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pos = POINTER(struct_bpf_map).in_dll(_lib, 'pos')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        num_cpu = c_int.in_dll(_lib, 'num_cpu')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass


class struct_bpf_link_perf(Structure):
    pass


struct_bpf_link_perf.__slots__ = ['link', 'perf_event_fd',
    'legacy_probe_name', 'legacy_is_kprobe', 'legacy_is_retprobe']
struct_bpf_link_perf._fields_ = [('link', struct_bpf_link), (
    'perf_event_fd', c_int), ('legacy_probe_name', String), (
    'legacy_is_kprobe', c_bool), ('legacy_is_retprobe', c_bool)]
if _libs['libbpf.so.1'].has('remove_kprobe_event_legacy', 'cdecl'):
    remove_kprobe_event_legacy = _libs['libbpf.so.1'].get(
        'remove_kprobe_event_legacy', 'cdecl')
    remove_kprobe_event_legacy.argtypes = [String, c_bool]
    remove_kprobe_event_legacy.restype = c_int
if _libs['libbpf.so.1'].has('remove_uprobe_event_legacy', 'cdecl'):
    remove_uprobe_event_legacy = _libs['libbpf.so.1'].get(
        'remove_uprobe_event_legacy', 'cdecl')
    remove_uprobe_event_legacy.argtypes = [String, c_bool]
    remove_uprobe_event_legacy.restype = c_int
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link_perf).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link_fd = c_int.in_dll(_lib, 'link_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        force_ioctl_attach = c_bool.in_dll(_lib, 'force_ioctl_attach')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(128)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        f = POINTER(FILE).in_dll(_lib, 'f')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = String.in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = String.in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = String.in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = String.in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr_sz = c_size_t.in_dll(_lib, 'attr_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr = struct_perf_event_attr.in_dll(_lib, 'attr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = c_int.in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        bit = c_int.in_dll(_lib, 'bit')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ap = c_void_p.in_dll(_lib, 'ap')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(1024)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = (c_char * int(256)).in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr_sz = c_size_t.in_dll(_lib, 'attr_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr = struct_perf_event_attr.in_dll(_lib, 'attr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = c_int.in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        syscall_name = (c_char * int(64)).in_dll(_lib, 'syscall_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ksys_pfx = String.in_dll(_lib, 'ksys_pfx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        probe_name = (c_char * int(128)).in_dll(_lib, 'probe_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attach_mode = enum_probe_attach_mode.in_dll(_lib, 'attach_mode')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        legacy_probe = String.in_dll(_lib, 'legacy_probe')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        offset = c_size_t.in_dll(_lib, 'offset')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        retprobe = c_bool.in_dll(_lib, 'retprobe')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        legacy = c_bool.in_dll(_lib, 'legacy')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        probe_name = (c_char * int(256)).in_dll(_lib, 'probe_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_name = (c_char * int(128)).in_dll(_lib, 'func_name')
        break
    except:
        pass


class struct_kprobe_multi_resolve(Structure):
    pass


struct_kprobe_multi_resolve.__slots__ = ['pattern', 'addrs', 'cap', 'cnt']
struct_kprobe_multi_resolve._fields_ = [('pattern', String), ('addrs',
    POINTER(c_ulong)), ('cap', c_size_t), ('cnt', c_size_t)]


class struct_avail_kallsyms_data(Structure):
    pass


struct_avail_kallsyms_data.__slots__ = ['syms', 'cnt', 'res']
struct_avail_kallsyms_data._fields_ = [('syms', POINTER(POINTER(c_char))),
    ('cnt', c_size_t), ('res', POINTER(struct_kprobe_multi_resolve))]
for _lib in _libs.values():
    try:
        data = POINTER(struct_avail_kallsyms_data).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        res = POINTER(struct_kprobe_multi_resolve).in_dll(_lib, 'res')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        available_functions_file = String.in_dll(_lib,
            'available_functions_file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = struct_avail_kallsyms_data.in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_name = (c_char * int(500)).in_dll(_lib, 'sym_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        f = POINTER(FILE).in_dll(_lib, 'f')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        syms = POINTER(POINTER(c_char)).in_dll(_lib, 'syms')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cap = c_size_t.in_dll(_lib, 'cap')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cnt = c_size_t.in_dll(_lib, 'cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        available_path = String.in_dll(_lib, 'available_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_name = (c_char * int(500)).in_dll(_lib, 'sym_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        f = POINTER(FILE).in_dll(_lib, 'f')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_addr = c_ulonglong.in_dll(_lib, 'sym_addr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        addrs = POINTER(c_ulong).in_dll(_lib, 'addrs')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link_fd = c_int.in_dll(_lib, 'link_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cookies = POINTER(__u64).in_dll(_lib, 'cookies')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        syms = POINTER(POINTER(c_char)).in_dll(_lib, 'syms')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        retprobe = c_bool.in_dll(_lib, 'retprobe')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cnt = c_size_t.in_dll(_lib, 'cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        offset = c_ulong.in_dll(_lib, 'offset')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_name = String.in_dll(_lib, 'func_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func = String.in_dll(_lib, 'func')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        syscall_name = String.in_dll(_lib, 'syscall_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        spec = String.in_dll(_lib, 'spec')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pattern = String.in_dll(_lib, 'pattern')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        probe_type = String.in_dll(_lib, 'probe_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        binary_path = String.in_dll(_lib, 'binary_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_name = String.in_dll(_lib, 'func_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = (c_char * int(512)).in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr_sz = c_size_t.in_dll(_lib, 'attr_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr = struct_perf_event_attr.in_dll(_lib, 'attr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        type = c_int.in_dll(_lib, 'type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        archive = POINTER(struct_zip_archive).in_dll(_lib, 'archive')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        entry = struct_zip_entry.in_dll(_lib, 'entry')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_long.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        elf = POINTER(Elf).in_dll(_lib, 'elf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        perm = c_int.in_dll(_lib, 'perm')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        s = String.in_dll(_lib, 's')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        next_path = String.in_dll(_lib, 'next_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        seg_len = c_int.in_dll(_lib, 'seg_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ref_ctr_offsets = POINTER(c_ulong).in_dll(_lib, 'ref_ctr_offsets')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        offsets = POINTER(c_ulong).in_dll(_lib, 'offsets')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        resolved_offsets = POINTER(c_ulong).in_dll(_lib, 'resolved_offsets')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link_fd = c_int.in_dll(_lib, 'link_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        full_path = (c_char * int(4096)).in_dll(_lib, 'full_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cookies = POINTER(__u64).in_dll(_lib, 'cookies')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        syms = POINTER(POINTER(c_char)).in_dll(_lib, 'syms')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cnt = c_size_t.in_dll(_lib, 'cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        archive_path = String.in_dll(_lib, 'archive_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        archive_sep = String.in_dll(_lib, 'archive_sep')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        legacy_probe = String.in_dll(_lib, 'legacy_probe')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attach_mode = enum_probe_attach_mode.in_dll(_lib, 'attach_mode')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        full_path = (c_char * int(4096)).in_dll(_lib, 'full_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ref_ctr_off = c_size_t.in_dll(_lib, 'ref_ctr_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        retprobe = c_bool.in_dll(_lib, 'retprobe')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        legacy = c_bool.in_dll(_lib, 'legacy')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_name = String.in_dll(_lib, 'func_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sym_off = c_long.in_dll(_lib, 'sym_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        probe_name = (c_char * int(4096 + 64)).in_dll(_lib, 'probe_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        probe_type = String.in_dll(_lib, 'probe_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        binary_path = String.in_dll(_lib, 'binary_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_name = String.in_dll(_lib, 'func_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        func_off = String.in_dll(_lib, 'func_off')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        c = c_int.in_dll(_lib, 'c')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        offset = c_long.in_dll(_lib, 'offset')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        resolved_path = (c_char * int(512)).in_dll(_lib, 'resolved_path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        usdt_cookie = __u64.in_dll(_lib, 'usdt_cookie')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        path = String.in_dll(_lib, 'path')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        provider = String.in_dll(_lib, 'provider')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        file = (c_char * int(4096)).in_dll(_lib, 'file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr_sz = c_size_t.in_dll(_lib, 'attr_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attr = struct_perf_event_attr.in_dll(_lib, 'attr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tp_id = c_int.in_dll(_lib, 'tp_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        sec_name = String.in_dll(_lib, 'sec_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tp_cat = String.in_dll(_lib, 'tp_cat')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tp_name = String.in_dll(_lib, 'tp_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_size_t.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tp_name = String.in_dll(_lib, 'tp_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfx_len = c_size_t.in_dll(_lib, 'pfx_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pfd = c_int.in_dll(_lib, 'pfd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        attach_type = enum_bpf_attach_type.in_dll(_lib, 'attach_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link_fd = c_int.in_dll(_lib, 'link_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relative_id = __u32.in_dll(_lib, 'relative_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relative_fd = c_int.in_dll(_lib, 'relative_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relative_id = __u32.in_dll(_lib, 'relative_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        relative_fd = c_int.in_dll(_lib, 'relative_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_id = c_int.in_dll(_lib, 'btf_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link_fd = c_int.in_dll(_lib, 'link_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        target_fd = __u32.in_dll(_lib, 'target_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog_fd = c_int.in_dll(_lib, 'prog_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link_fd = c_int.in_dll(_lib, 'link_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        errmsg = (c_char * int(128)).in_dll(_lib, 'errmsg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass


class struct_bpf_link_struct_ops(Structure):
    pass


struct_bpf_link_struct_ops.__slots__ = ['link', 'map_fd']
struct_bpf_link_struct_ops._fields_ = [('link', struct_bpf_link), ('map_fd',
    c_int)]
for _lib in _libs.values():
    try:
        st_link = POINTER(struct_bpf_link_struct_ops).in_dll(_lib, 'st_link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        zero = __u32.in_dll(_lib, 'zero')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(struct_bpf_link_struct_ops).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        zero = __u32.in_dll(_lib, 'zero')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        st_ops_link = POINTER(struct_bpf_link_struct_ops).in_dll(_lib,
            'st_ops_link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        zero = __u32.in_dll(_lib, 'zero')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
bpf_perf_event_print_t = CFUNCTYPE(UNCHECKED(enum_bpf_perf_event_ret),
    POINTER(struct_perf_event_header), POINTER(None))
for _lib in _libs.values():
    try:
        header = POINTER(struct_perf_event_mmap_page).in_dll(_lib, 'header')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data_head = __u64.in_dll(_lib, 'data_head')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data_tail = __u64.in_dll(_lib, 'data_tail')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        base = POINTER(None).in_dll(_lib, 'base')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = c_int.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ehdr = POINTER(struct_perf_event_header).in_dll(_lib, 'ehdr')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ehdr_size = c_size_t.in_dll(_lib, 'ehdr_size')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        copy_start = POINTER(None).in_dll(_lib, 'copy_start')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len_first = c_size_t.in_dll(_lib, 'len_first')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len_secnd = c_size_t.in_dll(_lib, 'len_secnd')
        break
    except:
        pass


class struct_perf_buffer_params(Structure):
    pass


struct_perf_buffer_params.__slots__ = ['attr', 'event_cb', 'sample_cb',
    'lost_cb', 'ctx', 'cpu_cnt', 'cpus', 'map_keys']
struct_perf_buffer_params._fields_ = [('attr', POINTER(
    struct_perf_event_attr)), ('event_cb', perf_buffer_event_fn), (
    'sample_cb', perf_buffer_sample_fn), ('lost_cb', perf_buffer_lost_fn),
    ('ctx', POINTER(None)), ('cpu_cnt', c_int), ('cpus', POINTER(c_int)), (
    'map_keys', POINTER(c_int))]


class struct_perf_cpu_buf(Structure):
    pass


struct_perf_cpu_buf.__slots__ = ['pb', 'base', 'buf', 'buf_size', 'fd',
    'cpu', 'map_key']
struct_perf_cpu_buf._fields_ = [('pb', POINTER(struct_perf_buffer)), (
    'base', POINTER(None)), ('buf', POINTER(None)), ('buf_size', c_size_t),
    ('fd', c_int), ('cpu', c_int), ('map_key', c_int)]
struct_perf_buffer.__slots__ = ['event_cb', 'sample_cb', 'lost_cb', 'ctx',
    'page_size', 'mmap_size', 'cpu_bufs', 'events', 'cpu_cnt', 'epoll_fd',
    'map_fd']
struct_perf_buffer._fields_ = [('event_cb', perf_buffer_event_fn), (
    'sample_cb', perf_buffer_sample_fn), ('lost_cb', perf_buffer_lost_fn),
    ('ctx', POINTER(None)), ('page_size', c_size_t), ('mmap_size', c_size_t
    ), ('cpu_bufs', POINTER(POINTER(struct_perf_cpu_buf))), ('events',
    POINTER(struct_epoll_event)), ('cpu_cnt', c_int), ('epoll_fd', c_int),
    ('map_fd', c_int)]
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        msg = (c_char * int(128)).in_dll(_lib, 'msg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
if _libs['libbpf.so.1'].has('__perf_buffer__new', 'cdecl'):
    __perf_buffer__new = _libs['libbpf.so.1'].get('__perf_buffer__new', 'cdecl'
        )
    __perf_buffer__new.argtypes = [c_int, c_size_t, POINTER(
        struct_perf_buffer_params)]
    __perf_buffer__new.restype = POINTER(struct_perf_buffer)
for _lib in _libs.values():
    try:
        attr_sz = c_size_t.in_dll(_lib, 'attr_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        online_cpus_file = String.in_dll(_lib, 'online_cpus_file')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = struct_bpf_map_info.in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        msg = (c_char * int(128)).in_dll(_lib, 'msg')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pb = POINTER(struct_perf_buffer).in_dll(_lib, 'pb')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        online = POINTER(c_bool).in_dll(_lib, 'online')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_info_len = __u32.in_dll(_lib, 'map_info_len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        j = c_int.in_dll(_lib, 'j')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu = c_int.in_dll(_lib, 'cpu')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_key = c_int.in_dll(_lib, 'map_key')
        break
    except:
        pass


class struct_perf_sample_raw(Structure):
    pass


struct_perf_sample_raw.__slots__ = ['header', 'size', 'data']
struct_perf_sample_raw._fields_ = [('header', struct_perf_event_header), (
    'size', uint32_t), ('data', POINTER(c_char))]


class struct_perf_sample_lost(Structure):
    pass


struct_perf_sample_lost.__slots__ = ['header', 'id', 'lost', 'sample_id']
struct_perf_sample_lost._fields_ = [('header', struct_perf_event_header), (
    'id', uint64_t), ('lost', uint64_t), ('sample_id', uint64_t)]
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        pb = POINTER(struct_perf_buffer).in_dll(_lib, 'pb')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        data = POINTER(None).in_dll(_lib, 'data')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        s = POINTER(struct_perf_sample_raw).in_dll(_lib, 's')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        s = POINTER(struct_perf_sample_lost).in_dll(_lib, 's')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        ret = enum_bpf_perf_event_ret.in_dll(_lib, 'ret')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cnt = c_int.in_dll(_lib, 'cnt')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        cpu_buf = POINTER(struct_perf_cpu_buf).in_dll(_lib, 'cpu_buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_obj_fd = c_int.in_dll(_lib, 'btf_obj_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf_id = c_int.in_dll(_lib, 'btf_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_int.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        start = c_int.in_dll(_lib, 'start')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        end = c_int.in_dll(_lib, 'end')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tmp = POINTER(c_bool).in_dll(_lib, 'tmp')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        fd = c_int.in_dll(_lib, 'fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_int.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        buf = (c_char * int(128)).in_dll(_lib, 'buf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        n = c_int.in_dll(_lib, 'n')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        tmp_cpus = c_int.in_dll(_lib, 'tmp_cpus')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mask = POINTER(c_bool).in_dll(_lib, 'mask')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(POINTER(struct_bpf_map)).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmaped = POINTER(POINTER(None)).in_dll(_lib, 'mmaped')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(POINTER(struct_bpf_program)).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        name = String.in_dll(_lib, 'name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        obj = POINTER(struct_bpf_object).in_dll(_lib, 'obj')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        len = c_int.in_dll(_lib, 'len')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_idx = c_int.in_dll(_lib, 'var_idx')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_name = String.in_dll(_lib, 'var_name')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        btf = POINTER(struct_btf).in_dll(_lib, 'btf')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_type_id = __u32.in_dll(_lib, 'map_type_id')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_type = POINTER(struct_btf_type).in_dll(_lib, 'map_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_type = POINTER(struct_btf_type).in_dll(_lib, 'var_type')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var_skel = POINTER(struct_bpf_var_skeleton).in_dll(_lib, 'var_skel')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        var = POINTER(struct_btf_var_secinfo).in_dll(_lib, 'var')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map = POINTER(struct_bpf_map).in_dll(_lib, 'map')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmap_sz = c_size_t.in_dll(_lib, 'mmap_sz')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prot = c_int.in_dll(_lib, 'prot')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        map_fd = c_int.in_dll(_lib, 'map_fd')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        mmaped = POINTER(POINTER(None)).in_dll(_lib, 'mmaped')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        err = c_int.in_dll(_lib, 'err')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        prog = POINTER(struct_bpf_program).in_dll(_lib, 'prog')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(POINTER(struct_bpf_link)).in_dll(_lib, 'link')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        i = c_int.in_dll(_lib, 'i')
        break
    except:
        pass
for _lib in _libs.values():
    try:
        link = POINTER(POINTER(struct_bpf_link)).in_dll(_lib, 'link')
        break
    except:
        pass
try:
    bpf_perf_event_opts__last_field = force_ioctl_attach
except:
    pass
try:
    bpf_kprobe_opts__last_field = attach_mode
except:
    pass
try:
    bpf_kprobe_multi_opts__last_field = retprobe
except:
    pass
try:
    bpf_uprobe_multi_opts__last_field = retprobe
except:
    pass
try:
    bpf_ksyscall_opts__last_field = retprobe
except:
    pass
try:
    bpf_uprobe_opts__last_field = attach_mode
except:
    pass
try:
    bpf_usdt_opts__last_field = usdt_cookie
except:
    pass
try:
    bpf_xdp_set_link_opts__last_field = old_fd
except:
    pass


def BPF_TC_PARENT(a, b):
    return a << 16 & 4294901760 | b & 65535


try:
    ring_buffer_opts__last_field = sz
except:
    pass
try:
    user_ring_buffer_opts__last_field = sz
except:
    pass
try:
    bpf_linker_opts__last_field = sz
except:
    pass
try:
    bpf_linker_file_opts__last_field = sz
except:
    pass
try:
    BPF_FS_MAGIC = 3405662737
except:
    pass
try:
    BPF_FS_DEFAULT_PATH = '/sys/fs/bpf'
except:
    pass
try:
    BPF_INSN_SZ = sizeof(struct_bpf_insn)
except:
    pass
try:
    STRERR_BUFSIZE = 128
except:
    pass


def __S(X):
    return X


def _S(X):
    return __S(X)


try:
    del _S
except NameError:
    pass
try:
    del __S
except NameError:
    pass
try:
    DATA_SEC = '.data'
except:
    pass
try:
    BSS_SEC = '.bss'
except:
    pass
try:
    RODATA_SEC = '.rodata'
except:
    pass
try:
    KCONFIG_SEC = '.kconfig'
except:
    pass
try:
    KSYMS_SEC = '.ksyms'
except:
    pass
try:
    STRUCT_OPS_SEC = '.struct_ops'
except:
    pass
try:
    STRUCT_OPS_LINK_SEC = '.struct_ops.link'
except:
    pass
try:
    STRUCT_OPS_VALUE_PREFIX = 'bpf_struct_ops_'
except:
    pass
try:
    POISON_LDIMM64_MAP_BASE = 2001000000
except:
    pass
try:
    POISON_LDIMM64_MAP_PFX = '200100'
except:
    pass
try:
    POISON_CALL_KFUNC_BASE = 2002000000
except:
    pass
try:
    POISON_CALL_KFUNC_PFX = '2002'
except:
    pass
try:
    MAX_TYPE_NAME_SIZE = 32
except:
    pass
try:
    BTF_TRACE_PREFIX = 'btf_trace_'
except:
    pass
try:
    BTF_LSM_PREFIX = 'bpf_lsm_'
except:
    pass
try:
    BTF_ITER_PREFIX = 'bpf_iter_'
except:
    pass
try:
    BTF_MAX_NAME_SIZE = 128
except:
    pass
try:
    PERF_UPROBE_REF_CTR_OFFSET_BITS = 32
except:
    pass
try:
    PERF_UPROBE_REF_CTR_OFFSET_SHIFT = 32
except:
    pass
try:
    DEBUGFS = '/sys/kernel/debug/tracing'
except:
    pass
try:
    TRACEFS = '/sys/kernel/tracing'
except:
    pass
bpf_program = struct_bpf_program
bpf_map = struct_bpf_map
bpf_object = struct_bpf_object
bpf_object_open_opts = struct_bpf_object_open_opts
bpf_perf_event_opts = struct_bpf_perf_event_opts
bpf_kprobe_opts = struct_bpf_kprobe_opts
bpf_kprobe_multi_opts = struct_bpf_kprobe_multi_opts
bpf_uprobe_multi_opts = struct_bpf_uprobe_multi_opts
bpf_ksyscall_opts = struct_bpf_ksyscall_opts
bpf_uprobe_opts = struct_bpf_uprobe_opts
bpf_usdt_opts = struct_bpf_usdt_opts
bpf_tracepoint_opts = struct_bpf_tracepoint_opts
bpf_trace_opts = struct_bpf_trace_opts
bpf_netfilter_opts = struct_bpf_netfilter_opts
bpf_tcx_opts = struct_bpf_tcx_opts
bpf_netkit_opts = struct_bpf_netkit_opts
bpf_iter_attach_opts = struct_bpf_iter_attach_opts
bpf_xdp_set_link_opts = struct_bpf_xdp_set_link_opts
bpf_xdp_attach_opts = struct_bpf_xdp_attach_opts
bpf_xdp_query_opts = struct_bpf_xdp_query_opts
bpf_tc_hook = struct_bpf_tc_hook
bpf_tc_opts = struct_bpf_tc_opts
ring_buffer = struct_ring_buffer
ring = struct_ring
user_ring_buffer = struct_user_ring_buffer
ring_buffer_opts = struct_ring_buffer_opts
user_ring_buffer_opts = struct_user_ring_buffer_opts
perf_buffer = struct_perf_buffer
perf_buffer_opts = struct_perf_buffer_opts
perf_buffer_raw_opts = struct_perf_buffer_raw_opts
bpf_prog_linfo = struct_bpf_prog_linfo
bpf_map_skeleton = struct_bpf_map_skeleton
bpf_prog_skeleton = struct_bpf_prog_skeleton
bpf_object_skeleton = struct_bpf_object_skeleton
bpf_var_skeleton = struct_bpf_var_skeleton
bpf_object_subskeleton = struct_bpf_object_subskeleton
gen_loader_opts = struct_gen_loader_opts
bpf_linker_opts = struct_bpf_linker_opts
bpf_linker_file_opts = struct_bpf_linker_file_opts
bpf_linker = struct_bpf_linker
libbpf_prog_handler_opts = struct_libbpf_prog_handler_opts
reloc_desc = struct_reloc_desc
bpf_sec_def = struct_bpf_sec_def
bpf_struct_ops = struct_bpf_struct_ops
bpf_map_def = struct_bpf_map_def
extern_desc = struct_extern_desc
module_btf = struct_module_btf
elf_sec_desc = struct_elf_sec_desc
elf_state = struct_elf_state
bpf_link_perf = struct_bpf_link_perf
kprobe_multi_resolve = struct_kprobe_multi_resolve
avail_kallsyms_data = struct_avail_kallsyms_data
bpf_link_struct_ops = struct_bpf_link_struct_ops
perf_buffer_params = struct_perf_buffer_params
perf_cpu_buf = struct_perf_cpu_buf
perf_sample_raw = struct_perf_sample_raw
perf_sample_lost = struct_perf_sample_lost
