// TODO(v8:10292): Remove this once Node migrates off the POSIX APIs.
// Execinfo is a GNU extension.

#ifndef _EXECINFO_H_
#define _EXECINFO_H_

inline int backtrace(void **frames, int count) {
    *frames = nullptr;
    return 0;
}

#endif