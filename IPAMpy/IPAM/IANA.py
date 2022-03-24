import IPAM.CLASS
import IPAM.ARIN

# NOTE: Blocks with a masklen set are supernets of various subnets
#       within the originating parent supernet. Most class B and C
#       addresing has been rulled up int supernets as /8s. This
#       means in most cases, you use/allocate a NET-BLOCK allocation
#       first with the correct subnetlen applied. Then when you
#       assign segments out of this block, they'll be indexed as seen
#       in modern whois implementations. The CLASSFUL allocations 
#       are purely here for the edge use-case that requires them.

# IANA SPECIAL USE ALLOCATIONS
#
IANA.SPECIAL_USE.LOCAL_IDENT         = CLASS.A.subnet(
											masklen=0,  index=0,   subnetlen=32)  # 0.0.0.0/8

IANA.SPECIAL_USE.RFC1918.NET_10      = CLASS.A.subnet(index=10)          # 10.0.0.0/8

IANA.SPECIAL_USE.SHARED              = ARIN.NET100.subnet(
											masklen=10, index=1,   subnetlen=16)  # 100.64.0.0/10

IANA.SPECIAL_USE.LOOPBACK            = ARIN.NET127.subnet(subnetlen=32)  # 127.0.0.0/8

IANA.SPECIAL_USE.LINK_LOCAL          = ARIN.NET169.subnet(
											masklen=16, index=127, subnetlen=16)  # 169.254.0.0/16

IANA.SPECIAL_USE.RFC1918.NET_172_16  = ARIN.NET172.subnet(
											masklen=12, index=1, subnetlen=16)  # 172.16.0.0/12

IANA.SPECIAL_USE.RFC1918.NET_192_168 = ARIN.NET192.subnet(
											masklen=16, index=168, subnetlen=24)  # 192.168.0.0/16


