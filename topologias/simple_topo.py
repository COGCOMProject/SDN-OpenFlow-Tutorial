from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI


"Create a network"
net = Mininet(link=TCLink, switch=OVSKernelSwitch)

print "Creating Nodes"
h1 = net.addHost('h1', ip='10.0.0.1/8')
h2 = net.addHost('h2', ip='10.0.0.2/8')


print "Creating Switch"
s1 = net.addSwitch('s1')

c1 = net.addController('c1', controller=Controller)

print "Associating and creating links"
net.addLink(h1, s1)
net.addLink(h2, s1)

print "Starting network"
net.build()
net.start()

print "Running CLI"
CLI(net)

print "Stopping network"
net.stop()
