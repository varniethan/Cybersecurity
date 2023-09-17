IP_fake = "10.9.0.99"
ether = Ether(src="aa:bb:cc:dd:ee:ff", dst="ff:ff:ff:ff:ff:ff")
arp = ARP(psrc=IP_fake, hwsrc="aa:bb:cc:dd:ee:ff",
          pdst=IP_fake, hwdst="ff:ff:ff:ff:ff:ff")
arp.op = 2