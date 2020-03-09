// These are temporarily shim used only to compile Node.
// TODO(v8:10292): Remove this once Node migrates off the POSIX APIs.

#include <stdint.h>
#include "unix/internal.h"

int uv_exepath(char* buffer, size_t* size) {
    return 0;
}

int uv_set_process_title(const char* title) {
    return 0;
}

int uv_get_process_title(char* buffer, size_t size) {
    *buffer = 0;
    return 0;
}

char** uv_setup_args(int argc, char** argv) {
    return argv;
}

void uv_loadavg(double avg[3]) {
}

int uv_uptime(double* uptime) {
    return 0;
}

int uv_cpu_info(uv_cpu_info_t** cpu_infos, int* count) {
    return 0;
}

uint64_t uv_get_free_memory(void) {
    return 0;
}

uint64_t uv_get_constrained_memory(void) {
  return 0;
}

uint64_t uv_get_total_memory(void) {
    return 0;
}

int uv_interface_addresses(uv_interface_address_t** addresses, int* count) {
    return 0;
}

void uv_free_interface_addresses(uv_interface_address_t* addresses,
  int count) {
}

int uv_resident_set_memory(size_t* rss) {
    return 0;
}

int uv_fs_event_init(uv_loop_t* loop, uv_fs_event_t* handle) {
    return 0;
}

int uv_fs_event_start(uv_fs_event_t* handle,
                      uv_fs_event_cb cb,
                      const char* filename,
                      unsigned int flags) {
    return 0;
}

void uv__fs_event_close(uv_fs_event_t* handle) {
}

int uv__platform_loop_init(uv_loop_t* loop) {
    return 0;
}

int uv__io_check_fd(uv_loop_t* loop, int fd) {
    return 0;
}

int uv__io_fork(uv_loop_t* loop) {
    assert(0 && "Fuchsia does not support fork()");
    return 0;
}

void uv__io_poll(uv_loop_t* loop, int timeout) {
}

void uv__platform_invalidate_fd(uv_loop_t* loop, int fd) {
}

void uv__platform_loop_delete(uv_loop_t* loop) {
}

uint64_t uv__hrtime(uv_clocktype_t type) {
    return 0;
}