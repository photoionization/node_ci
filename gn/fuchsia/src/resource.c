#include <sys/resource.h>


int getrusage(int who, struct rusage *usage) {
    return 0;
}

int getrlimit(int resource, struct rlimit *rlim) {
    return 0;
}

int setrlimit(int resource, const struct rlimit *rlim) {
    return 0;
}

int getpriority(int which, id_t who) {
    return 0;
}

int setpriority(int which, id_t who, int prio) {
    return 0;
}
