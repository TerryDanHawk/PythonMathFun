'''
Need install nmap
sudo apt-gte install nmap
sudo pip3 install python-map
'''

import  nmap
import optparse

def nmapScan(tgtHost,tgtPort):
    nmScan=nmap.PortScanner()
    state=nmScan.scan(tgtHost,tgtPort)
    #state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print("[*]"+tgtHost+" tcp/"+tgtPort+":")
    print(state)
def main():
    parser = optparse.OptionParser("Usage:\n\n -H <target host> -p <target port>"
                                   "\n\nDemo: python3 NMapScanner.py -H 192.168.0.100 -p 80,25,21,8081")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    for port in tgtPorts:
        nmapScan(tgtHost,port)

if __name__ == '__main__':
    main()