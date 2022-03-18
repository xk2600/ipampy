from CidrAllocation import CidrAllocation

# NOTE: Blocks with a masklen set are supernets of various subnets
#       within the originating parent supernet. Most class B and C
#       addresing has been rulled up int supernets as /8s. This
#       means in most cases, you use/allocate a NET-BLOCK allocation
#       first with the correct subnetlen applied. Then when you
#       assign segments out of this block, they'll be indexed as seen
#       in modern whois implementations. The CLASSFUL allocations 
#       are purely here for the edge use-case that requires them.

# CLASSFUL ALLOCATIONS
#
IPAM.CLASS.A = IPAM.CidrAllocation( "0.0.0.0/1",   subnetlen=8  )
IPAM.CLASS.B = IPAM.CidrAllocation( "128.0.0.0/2", subnetlen=16 )
IPAM.CLASS.C = IPAM.CidrAllocation( "192.0.0.0/3", subnetlen=24 )
IPAM.CLASS.D = IPAM.CidrAllocation( "224.0.0.0/4", subnetlen=8  )
IPAM.CLASS.E = IPAM.CidrAllocation( "240.0.0.0/4", subnetlen=8  )

# NET-BLOCK REGISTRY DELEGATIONS
# 
#    TODO: FLESH THIS OUT... these are examples in the interim..
#
IPAM.APNIC.NET1  = IPAM.CLASS.A.subnet( index=1, subnetlen=12 )
IPAM.RIPE.NET2   = IPAM.CLASS.A.subnet( index=2, subnetlen=12 )
IPAM.ARIN.NET3   = IPAM.CLASS.A.subnet( index=3, subnetlen=12 )

IPAM.ARIN.NET100 = IPAM.CLASS.A.subnet(            index=100,       subnetlen=10 )
IPAM.ARIN.NET127 = IPAM.CLASS.A.subnet(            index=127,       subnetlen=8  )
IPAM.ARIN.NET169 = IPAM.CLASS.B.subnet( masklen=8, index=(169-128), subnetlen=12 )
IPAM.ARIN.NET172 = IPAM.CLASS.B.subnet( masklen=8, index=(172-128), subnetlen=12 )
IPAM.ARIN.NET192 = IPAM.CLASS.C.subnet( masklen=8, index=0, subnetlen=16 )

# IANA SPECIAL USE ALLOCATIONS
#
IPAM.IANA.SPECIAL_USE.LOCAL_IDENT         = IPAM.CLASS.A.subnet(
											masklen=0,  index=0,   subnetlen=32)  # 0.0.0.0/8

IPAM.IANA.SPECIAL_USE.RFC1918.NET_10      = IPAM.CLASS.A.subnet(index=10)          # 10.0.0.0/8

IPAM.IANA.SPECIAL_USE.SHARED              = IPAM.ARIN.NET100.subnet(
											masklen=10, index=1,   subnetlen=16)  # 100.64.0.0/10

IPAM.IANA.SPECIAL_USE.LOOPBACK            = IPAM.ARIN.NET127.subnet(subnetlen=32)  # 127.0.0.0/8

IPAM.IANA.SPECIAL_USE.LINK_LOCAL          = IPAM.ARIN.NET169.subnet(
											masklen=16, index=127, subnetlen=16)  # 169.254.0.0/16

IPAM.IANA.SPECIAL_USE.RFC1918.NET_172_16  = IPAM.ARIN.NET172.subnet(
											masklen=12, index=1, subnetlen=16)  # 172.16.0.0/12

IPAM.IANA.SPECIAL_USE.RFC1918.NET_192_168 = IPAM.ARIN.NET192.subnet(
											masklen=16, index=168, subnetlen=24)  # 192.168.0.0/16


