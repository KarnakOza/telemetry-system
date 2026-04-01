#ifndef CRC_H
#define CRC_H

#include <stdint.h>
#include <stddef.h>

uint32_t compute_crc(uint8_t *data, size_t len);

#endif 
