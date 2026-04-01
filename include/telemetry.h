#ifndef TELEMETRY_H
#define TELEMETRY_H

#include <stdint.h>

typedef struct {
    uint16_t version;
    uint16_t apid;
    uint16_t sequence;
    uint16_t length;

} CCSDS_HEADER ; 

typedef struct  
{
    CCSDS_HEADER header;
    uint32_t timestamp;
    float temperature;
    float voltage;
    float position[3];
    uint8_t status;
    uint32_t crc;
} TelemetryPacket;

void fill_fake_data(TelemetryPacket *pkt, int seq);

#endif

