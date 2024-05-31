from scapy.all import ARP, Ether, srp
import socket
import struct
import fcntl

def get_local_ip(interface):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = fcntl.ioctl(
        sock.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(interface[:15], 'utf-8'))
    )[20:24]
    return socket.inet_ntoa(ip)

def scan_network(ip_range):
    # Create ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    # List to store discovered devices
    devices = []

    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    # Replace 'eth0' with your actual interface name if different
    interface = 'enp0s31f6'
    local_ip = get_local_ip(interface)
    ip_parts = local_ip.split('.')
    ip_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.1/24"

    print(f"Escaneando la red: {ip_range}")

    devices = scan_network(ip_range)

    if devices:
        print("Dispositivos encontrados:")
        for device in devices:
            print(f"IP: {device['ip']} - MAC: {device['mac']}")
    else:
        print("No se encontraron dispositivos.")

if __name__ == "__main__":
    main()
