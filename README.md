# IPAMpy

ipam python module to make easy work of IP address management to include subnetting, 
supernetting, tracking usage, and things of the like.

This is an amalgomation of a various functions I've written, rewritten, chagned, and 
tweaked over the years. I finally ran into a usecase where I needed to do some fairly 
complex things and hence condensed the working bits into this library/module. It is not 
complete, and should be used with that understanding.

## WHY IPAMpy?

Lots of other libraries exist. But I have yet to find one that I can use arithmetic
to manipulate address space. IPAMpy does just that. The following is a synopsis of how 
it works:

IPAM.py exports the following:

 - Prefix
 - IPAM

### Prefix

`Prefix` is the base class which holds and hosts the primary functionality on which
IPAMpy operates. `Prefix` instances really just represnt two elements at their core:

 - **`netid`**-- an address-family representing a unique internetwork source or
   destination. (IPv4 or IPv6 address). 
 - **`masklen`**-- a number representing the bit boundary where the network ends and
   the subnetworks or hosts are allocated from.

Other attributes are tracked to enable in higher-level functions, for example:

 - **`net`**-- a representation

### IPAM

IPAM is a namespace containing the `CidrAllocation` class as well as various
constants documenting address allocations and delegations to registration authorities.

 - **`CidrAllocation`**-- a subclass of `Prefix` which implements the ability to
   includes a `descr` property allowing notation of the `CidrAlloication` as its 
   created or upon creation of subnets derived from a given `CidrAllocation`.
   
 - **`Whois`**-- a whois client which can lookup delegations and automatically create
   dependancy based `CidrAllocation` instances in the appropriate namespace for
   NET-BLOCKS assigned by the various delegated registration authorities.
   
 - Constants:
   - **`CLASS`**-- Prefix representation of classful addressing: `A`, `B`, `C`, `D`, and `E`.
   - **`IANA`**--  Reservations held and managed by the Internet-Assigned Numbering Authority.
   
     - **`SPECIAL_USE`**-- IANA Special Use Assignments containing IETF RFC allocations such
       as `LOCAL_IDENT`, `SHARED`, `LOOPBACK`, `LINK_LOCAL`, `TEST-NET`,  and `BENCHMARK`.

   - **`ARIN`**--  Delegated networks allocated and distributed by ARIN.
   - **`RIPE`**--  Delegated networks allocated and distributed by RIPE.
   - **`APNIC`**-- Delegated networks allocated and distributed by APNIC.

## NOTES ON NET BLOCKS

> NET blocks are representations of allocations within the whois 
> database. They are formed from the `name` field in the output of the whois 
> information by replacing hyphens (-) with underscores and capitalizing the
> text. 
    
> Blocks with a masklen set are supernets of various subnets within the 
> originating parent supernet. Most class B and C addresing has been rulled 
> up int supernets as /8s. This means in most cases, you use/allocate a 
> NET-BLOCK allocation first with the correct subnetlen applied. Then when 
> you assign segments out of this block, they'll be indexed as seen in modern 
> whois implementations. The CLASSFUL allocations are purely here for the 
> edge use-case that requires them.

## TODO

 - Change the <Prefix>.net proeprty from representing the ip component of 
   the prefix to return an instance of <class Net>--a subclass of Prefix.
   <class Net> extends the functionality of <class Prefix> for delegating
   iteration, subnet indexes, and arithmetic functions for interacting
   with prefixes (subnetting, supernetting, etc.)

 - Create a <Prefix>.host property to delegate host based allocation
   (effectively an alias which makes all subnet allocations /32s)
     
   > **`NOTE`** The above two items could possibly be written as descriptors.

 - Implement `Whois`, replacing shell script and exec.
