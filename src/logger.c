#include <stdio.h>
#include "telemetry.h"

void log_packet(TelemetryPacket *pkt) {

    // Console log
    printf("SEQ: %d | Temp: %.2f | Volt: %.2f\n",
           pkt->header.sequence,
           pkt->temperature,
           pkt->voltage);

    // CSV log
    FILE *fp = fopen("telemetry.csv", "a");

    if (fp == NULL) {
        printf("Error opening CSV file\n");
        return;
    }

   fprintf(fp, "%d,%u,%.2f,%.2f,%u\n",
        pkt->header.sequence,
        pkt->timestamp,
        pkt->temperature,
        pkt->voltage,
        pkt->crc);

    fclose(fp);
}
