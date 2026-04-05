import struct

packet_size = 40

with open("telemetry.bin", "rb") as f:

    i = 0
    while True:
        data = f.read(packet_size)
        if len(data) < packet_size:
            break

 
