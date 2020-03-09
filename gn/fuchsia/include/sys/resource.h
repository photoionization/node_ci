// X/Open System Interface Extension
// https://pubs.opengroup.org/onlinepubs/9699919799/

#ifndef _SYS_RESOURCE_H_
#define _SYS_RESOURCE_H_

#ifdef __cplusplus
#define EXTERN extern "C"
#else
#define EXTERN
#endif

#include <sys/types.h>
#include <sys/time.h>

// priority
#define PRIO_PROCESS 0
#define PRIO_PGRP 1
#define PRIO_USER 2

// rlimit resources
#define RLIMIT_CPU      0
#define RLIMIT_FSIZE    1
#define RLIMIT_DATA     2
#define RLIMIT_STACK    3
#define RLIMIT_CORE     4
#define RLIMIT_RSS      5
#define RLIMIT_NPROC    6
#define RLIMIT_NOFILE   7
#define RLIMIT_MEMLOCK  8
#define RLIMIT_AS       9
#define RLIMIT_LOCKS    10
#define RLIM_INFINITY   11
#define RLIM_SAVED_MAX  12
#define RLIM_SAVED_CUR  13

// rlimit
#define RUSAGE_SELF 0 

typedef unsigned rlim_t;

struct rlimit {
    rlim_t rlim_cur;  /* Soft limit */
    rlim_t rlim_max;  /* Hard limit (ceiling for rlim_cur) */
};

struct rusage {
    struct timeval ru_utime; /* user CPU time used */
    struct timeval ru_stime; /* system CPU time used */
    long   ru_maxrss;        /* maximum resident set size */
    long   ru_ixrss;         /* integral shared memory size */
    long   ru_idrss;         /* integral unshared data size */
    long   ru_isrss;         /* integral unshared stack size */
    long   ru_minflt;        /* page reclaims (soft page faults) */
    long   ru_majflt;        /* page faults (hard page faults) */
    long   ru_nswap;         /* swaps */
    long   ru_inblock;       /* block input operations */
    long   ru_oublock;       /* block output operations */
    long   ru_msgsnd;        /* IPC messages sent */
    long   ru_msgrcv;        /* IPC messages received */
    long   ru_nsignals;      /* signals received */
    long   ru_nvcsw;         /* voluntary context switches */
    long   ru_nivcsw;        /* involuntary context switches */
};


EXTERN int getrusage(int who, struct rusage *usage);
EXTERN int getrlimit(int resource, struct rlimit *rlim);
EXTERN int setrlimit(int resource, const struct rlimit *rlim);
EXTERN int getpriority(int which, id_t who);
EXTERN int setpriority(int which, id_t who, int prio);

#endif // _SYS_RESOURCE_H_