import scapy.all as scapy
import argparse
from scapy.layers import http

def get_interface():
    """
    Get the network interface from the user via command-line arguments.
    This function prompts the user to specify the network interface for packet sniffing.
    """
    parser = argparse.ArgumentParser(description="Specify the interface to sniff packets.")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Network interface to sniff packets on")
    arguments = parser.parse_args()
    return arguments.interface

def sniff_packets(interface):
    """
    Sniff packets on the specified network interface.
    This function continuously listens for incoming packets and processes them.
    """
    print(f"[*] Starting packet sniffing on interface: {interface}")
    # Start sniffing packets on the specified interface, calling `process_packet` for each captured packet
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    """
    Process each captured packet and extract relevant information.
    This function checks if the packet contains useful data like IP or HTTP request information.
    """
    if packet.haslayer(scapy.IP):  # Check if packet has an IP layer
        try:
            src_ip = packet[scapy.IP].src
            dst_ip = packet[scapy.IP].dst
            protocol = "TCP" if packet.haslayer(scapy.TCP) else "UDP" if packet.haslayer(scapy.UDP) else "Other"
            print(f"[+] Source: {src_ip} -> Destination: {dst_ip} | Protocol: {protocol}")
        except Exception as e:
            print(f"[-] Error processing IP layer: {e}")

    # Check for HTTP requests and display details
    if packet.haslayer(http.HTTPRequest):
        try:
            host = packet[http.HTTPRequest].Host.decode(errors="ignore")
            path = packet[http.HTTPRequest].Path.decode(errors="ignore")
            print(f"[HTTP] {host}{path}")
            
            # Extract possible sensitive data (e.g., usernames or passwords) from payload
            if packet.haslayer(scapy.Raw):
                load = packet[scapy.Raw].load.decode("utf-8", errors="ignore")
                print(f"[HTTP Payload] {load}")
                keys = ["username", "password", "pass", "email", "token", "credit card"]
                for key in keys:
                    if key in load.lower():  # Case-insensitive search for sensitive data
                        print(f"[!] Possible sensitive data found: {load}")
                        break
        except Exception as e:
            print(f"[-] Error processing HTTP request: {e}")

# Main execution
if __name__ == "__main__":
    try:
        iface = get_interface()  # Get the interface to sniff on
        sniff_packets(iface)  # Start sniffing packets
    except Exception as e:
        print(f"[-] Error: {e}")
        print("[*] Ensure that the correct interface is specified and you have the necessary permissions.")
