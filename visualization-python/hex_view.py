with open("telemetry.bin", "rb") as f:
    data = f.read(128)  # only first 128 bytes

for i in range(0, len(data), 16):
    chunk = data[i:i+16]

    hex_bytes = " ".join(f"{b:02X}" for b in chunk)
    ascii_bytes = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)

    print(f"{i:08X}  {hex_bytes:<48}  {ascii_bytes}")
