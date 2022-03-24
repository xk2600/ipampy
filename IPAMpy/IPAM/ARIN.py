import IPAM.NET

# NOTE: Blocks with a masklen set are supernets of various subnets
#       within the originating parent supernet. Most class B and C
#       addresing has been rulled up int supernets as /8s. This
#       means in most cases, you use/allocate a NET-BLOCK allocation
#       first with the correct subnetlen applied. Then when you
#       assign segments out of this block, they'll be indexed as seen
#       in modern whois implementations. The CLASSFUL allocations 
#       are purely here for the edge use-case that requires them.

NET3   = IPAM.NET.NET3

NET100 = IPAM.NET.NET100
NET127 = IPAM.NET.NET127
NET169 = IPAM.NET.NET169
NET172 = IPAM.NET.NET172
NET192 = IPAM.NET.NET192
