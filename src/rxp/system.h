#ifndef _RXP_SYSTEM_H
#define _RXP_SYSTEM_H
#define SOCKETS_IMPLEMENTED
#define HAVE_LONG_LONG_INT

#define _stringize(n) #n
#define stringize(n) _stringize(n)
#ifdef DEBUG_PYRXP
/*system.h debugging on*/
#	define RLDEBUG(...) fprintf(stderr,__VA_ARGS__)
#else
#	define RLDEBUG(...)
#endif

#define STD_API
#define XML_API
#define WIN_IMP
#ifdef _WIN32
#	ifndef WIN32
#		define WIN32
#	endif
#	ifndef PY_LONG_LONG
#		define PY_LONG_LONG __int64
#	endif
#endif
#ifndef PY_LONG_LONG
#	if defined(__GNUC__)
#		define PY_LONG_LONG long long
#	endif
#endif

void *Malloc(int bytes);
void *Realloc(void *mem, int bytes);
void Free(void *mem);
void CFree(void *mem);
#endif
