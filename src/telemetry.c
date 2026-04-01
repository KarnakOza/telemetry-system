#include "telemetry.h"
#include <stdlib.h>
#include <time.h>

void fill_fake_data(TelemetryPacket *pkt, int seq) {

    pkt->header.version = 1;
    pkt->header.apid = 100;
    pkt->header.sequence = seq;
    pkt->header.length = sizeof(TelemetryPacket);

    pkt->timestamp = time(NULL);

    pkt->temperature = 20.0 + (rand() % 100) / 10.0;
    pkt->voltage = 3.3 + (rand() % 10) / 100.0;

    pkt->position[0] = rand() % 1000;
    pkt->position[1] = rand() % 1000;
    pkt->position[2] = rand() % 1000;

    pkt->status = 1;
}
