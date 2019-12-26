How to run the program (on windows):
1)Open cmd and type ipconfig to find your IPv4
2)Next enter 'py SteganoSender.py' into cmd
2)Open another cmd and enter 'py SteganoReceiver.py'
3)Enter your IPv4 address into SteganoSender program
4)Enter your IPv4 address into SteganoReceiver program
5)Enter secret message into StegoSender before timeout (set to 15 seconds, until SteganoReceiver stops sniffing)
6)After time out, the secret message will appear in SteganoReceiver program

Note: 
I made it so that the program stops sniffing after 15 seconds, but there are better ways to do it.
This still fulfills the requirements of the question however.
Furthermore, I attached an ICMP packet to my IP packets sent on SteganoSender because I had too many other
packets showing up while sniffing and needed a better way to differentiate my desired packets.
However, there is also many other ways to do this part as well and make it more concealable. 