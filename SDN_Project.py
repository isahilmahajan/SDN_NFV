from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch, RemoteController 
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

class CustomTopology(Topo):
    # Creating a custom topology
    def __init__(self):

        # Initializing the topology 
        Topo.__init__(self)

        # Creating switches
        s1= self.addSwitch('s1', protocols = "OpenFlow13")
        s2= self.addSwitch('s2', protocols = "OpenFlow13")
        s3= self.addSwitch('s3', protocols = "OpenFlow13")
        s4= self.addSwitch('s4', protocols = "OpenFlow13")

        #creating hosts
        h1= self.addHost('h1', ip = "10.0.0.1/24")
        h2= self.addHost('h2', ip = "10.0.0.2/24")
        h3= self.addHost('h3', ip = "10.0.0.3/24")
        h4= self.addHost('h4', ip = "10.0.0.4/24")

        # linking hosts h1, h2 to s1 
        self.addLink(h1, s1, 1, 3, bw = 20)
        self.addLink(h2, s1, 1, 4, bw = 20)

        #linking hosts h3, h4 to s4
        self.addLink(h3, s4, 1, 3, bw = 20)
        self.addLink (h4, s4, 1, 4, bw = 20)


        #linking switch s2 to s1 and s4 
        self.addLink(s2, s1, 1, 1, bw = 1)
        self.addLink(s2, s4, 2, 1, bw = 1)

        # linking switch s3 to s1 and s4
        self.addLink(s3, s1, 1, 2, bw = 10)
        self.addLink(s3, s4, 2, 2, bw = 10)

if __name__ == '__main__':
    setLogLevel('info')
    topo = CustomTopology()
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController(
            name,
            ip="127.0.0.1"
        ),
        switch=OVSSwitch,
        link=TCLink,
    )

    net.start()