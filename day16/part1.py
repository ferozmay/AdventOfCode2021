
packet = open("input.txt").read().strip()
packet = bin(int(packet, 16))[2:].zfill(len(packet)*4)


ans = 0


def solve(packet):
    global ans
    version = int(packet[:3], 2)
    ans += version
    # print(version)

    packet = packet[3:]
    type_id = int(packet[:3], 2)
    # print(type_id)
    packet = packet[3:]

    if type_id == 4:  # literal value
        binary = ""
        while True:
            binary += packet[1:5]
            stop = packet[0]
            packet = packet[5:]
            if stop == '0':
                break

    else:  # operator value
        length_id = packet[0]
        packet = packet[1:]
        if length_id == '0':
            len_subpacket = int(packet[:15], 2)
            packet = packet[15:]
            remaining_subpackets = packet[:len_subpacket]
            while remaining_subpackets:
                remaining_subpackets = solve(remaining_subpackets)
                if remaining_subpackets == "":
                    break
            packet = packet[len_subpacket:]
        else:
            n_subpacket = int(packet[:11], 2)
            packet = packet[11:]
            for i in range(n_subpacket):
                packet = solve(packet)

    return packet


solve(packet)
print(ans)
