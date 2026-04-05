import struct

packet_size = 40

with open("telemetry.bin", "rb") as f:

    i = 0
    while True:
        data = f.read(packet_size)
        if len(data) < packet_size:
            break

        unpacked = struct.unpack("<HHHHIff3fBxxxI", data)

        print("\n" + "="*60)
        print(f"📦 PACKET #{i}")
        print("="*60)
    
        print(f"Header:")
        print(f"  Version   : {unpacked[0]}")
        print(f"  APID      : {unpacked[1]}")
        print(f"  Sequence  : {unpacked[2]}")
        print(f"  Length    : {unpacked[3]}")

        print(f"\nTelemetry:")
        print(f"  Timestamp : {unpacked[4]}")
        print(f"  Temp (°C) : {unpacked[5]:.2f}")
        print(f"  Voltage   : {unpacked[6]:.2f}")

        print(f"\nPosition:")
        print(f"  X: {unpacked[7]:.1f}")
        print(f"  Y: {unpacked[8]:.1f}")
        print(f"  Z: {unpacked[9]:.1f}")

        print(f"\nStatus:")
        print(f"  Health    : {unpacked[10]}")
        print(f"  CRC       : {unpacked[11]}")

        i += 1

 
