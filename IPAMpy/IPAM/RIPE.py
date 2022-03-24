import IPAM.CLASS

# NOTE: Blocks with a masklen set are supernets of various subnets
#       within the originating parent supernet. Most class B and C
#       addresing has been rulled up int supernets as /8s. This
#       means in most cases, you use/allocate a NET-BLOCK allocation
#       first with the correct subnetlen applied. Then when you
#       assign segments out of this block, they'll be indexed as seen
#       in modern whois implementations. The CLASSFUL allocations 
#       are purely here for the edge use-case that requires them.

RIPE.NET2   = IPAM.CLASS.A.subnet( index=2, subnetlen=12 )
