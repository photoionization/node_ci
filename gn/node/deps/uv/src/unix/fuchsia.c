// These are temporarily shim used only to compile Node.
// TODO(v8:10292): Remove this once Node migrates off the POSIX APIs.

#include <stdint.h>
#include "unix/internal.h"

int uv_exepath(char* buffer, size_t* size) {
    return 0;
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
