import IPAM.CLASS

def NetBlockGenerator(net, subnetlen, start, stop):
    NETS = { f"NET{_NET}":
                net.subnet( index=_NET, subnetlen=subnetlen) for _NET in range(start,stop) }
    globals().update(NETS)

# NOTE: Blocks with a masklen set are supernets of various subnets
#       within the originating parent supernet. Most class B and C
#       addresing has been rulled up int supernets as /8s. This
#       means in most cases, you use/allocate a NET-BLOCK allocation
#       first with the correct subnetlen applied. Then when you
#       assign segments out of this block, they'll be indexed as seen
#       in modern whois implementations. The CLASSFUL allocations 
#       are purely here for the edge use-case that requires them.

# create all the netblocks 0/8 throught 255/8
NetBlockGenerator(net=IPAM.CLASS.A, subnetlen=10, start=0,   end=128)
NetBlockGenerator(net=IPAM.CLASS.B, subnetlen=12, start=128, end=192)
NetBlockGenerator(net=IPAM.CLASS.C, subnetlen=16, start=192, end=224)
NetBlockGenerator(net=IPAM.CLASS.D, subnetlen=16, start=224, end=240)
NetBlockGenerator(net=IPAM.CLASS.E, subnetlen=16, start=240, end=256)

del NetBlockGenerator

# Supernets which combine sections of a subnet.
NET100 = IPAM.CLASS.A.subnet(            index=100,       subnetlen=10 )
NET127 = IPAM.CLASS.A.subnet(            index=127,       subnetlen=8  )
NET169 = IPAM.CLASS.B.subnet( masklen=8, index=(169-128), subnetlen=12 )
NET172 = IPAM.CLASS.B.subnet( masklen=8, index=(172-128), subnetlen=12 )
NET192 = IPAM.CLASS.C.subnet( masklen=8, index=0,         subnetlen=16 )

