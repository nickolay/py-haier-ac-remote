from haierac import HaierAC

print("-- HaierAC recv demo --")

# Change the IP address to your AC's IP address
h = HaierAC(ip='192.168.1.67',mac='04FA838F845A')
h.test_recv_loop()
