import unittest

def debug(message):
	pass                           # disables debugging output
	print(f"DEBUG: {message}")

class netwidth(int):
    """ similar to timespan, but for addressing mechanics. `netwidth` allows only
        a masklen to be defined which can then be summed with a Prefix to derive
        a new prefix.
    """
	pass
	
class Prefix:
	""" Enables ipPrefixes to be treated like generic numeric types while
	    preserving thier presentation and allowing subnetting and suppernetting
	    to be applied to networks. Prefix maintains linkage to parent and child
	    prefixes as well, allowing a tree of allocations to be observed should
	    one use this to build IP based topologies or as tooling for IPAM functions.
	    
	    TODO:
	"""
	
	__author__    = "Christopher M. Stephan"
	__copywrite__ = "Copywrite (C) 2016 Christopher Stephan"  
	__license__   = "2-cluase BSD License"
	__version__   = "0.1.2"
	    
	IPV4: Prefix = None
	_supernet: Prefix = None
	
	@staticmethod
	def toBytes(netid: int = 0):
		result = []
		remainder = netid
		for bitval in range(24, -1, -8):
			octet = remainder >> bitval
			remainder = remainder % (2 ** bitval)
			result.append(octet)
		return result
		
	@staticmethod
	def toStr(netid: int = 0):
		lnet = [ str(octet) for octet in Prefix.toBytes(netid) ]
		return '.'.join(lnet)
		
	@property
	def masklen(self):
		return self._masklen
		
	@masklen.setter
	def masklen(self, masklen):
		debug(f"<prefix>.masklen.__set__: {masklen}")
		try:
			self._masklen = int(masklen)
			self._netid = self.netid & ( 4294967295 << (32 - self._masklen) )
		except:
			raise ValueError("mask must be an integer between 0 and 32")
		debug(f"<prefix>.masklen.__set__: (self.netid, self._masklen): {self.netid}, {self.masklen}")
	
	@property
	def netid(self):
		return self._netid
		
	@property
	def net(self):
		return self.toStr(self._netid)
		
	@net.setter
	def net(self, net: str):
		debug(f"<prefix>.net.__set__: net: {net}")
		if isinstance(net, str):
			# convert to integer
			net = net.split(".")
			assert len(net) == 4, "malformed dotted decimal address, should be 'x.x.x.x'"
			try:
				for octet in net.copy():
					net = ((net << 8) + int(octet)) if isinstance(net, int) else int(octet)
			except:
				raise ValueError("net must be a dotted-decimal string")
		debug(f"<prefix>.net.__set__: {net}")
		self._netid = net
	
	@property
	def supernet(self):
		return self._supernet
		
	@supernet.setter
	def supernet(self, supernet):
		self._supernet = supernet
		
	@property
	def boundary(self):
		return self._boundary
		
	@boundary.setter
	def boundary(self, boundary):
		self._boundary = boundary
		
	@property
	def subnetlen(self):
		return self._subnetlen
		
	@subnetlen.setter
	def subnetlen(self, subnetlen):
		self._subnetlen = subnetlen
		
	@property
	def netpath(self):
		result = []
		cursor = self
		while cursor.supernet is not Prefix.IPV4:
			debug(f"<prefix>.netpath: cursor.supernet: {cursor.supernet}")
			result.insert(0, cursor.supernet)
			cursor = cursor.supernet
		result.insert(0, cursor.supernet)
		return resulttattr(self, arg, val)
	
	def subnet(self, masklen: int = None, index=0, subnetlen=None):
		if masklen is None:
			masklen = self.subnetlen
		netid = self.netid + ((1 << (32 - masklen)) * index)
		boundary = self.netid + (1 << (32 - self.masklen)) - 1
		debug(f"<prefix>.subnet: (masklen, netid, boundary): {masklen}, {netid}, {boundary}")
		if netid >= self.boundary or boundary > self.boundary:
			raise IndexError("The index of the subnet requested is beyond " + 
			                 "the bounds of this subnet's supernet")
		prefix = self.__class__(netid, masklen, supernet=self, boundary=boundary)
		if subnetlen is not None:
			prefix.subnetlen = subnetlen
		self._subnets[str(prefix)] = prefix
		return prefix
		
	def next(self):
		netid = self._netid + (1 << (32 - self._masklen))
		if netid >= self._boundary:
			raise IndexError("The next subnet is beyond the " + 
			                 "bounds of this subnet's supernet")
		prefix = self.__class__(netid, self._masklen, supernet = self._supernet)
		return Prefix
		
	def __str__(self):
		result = self.net + "/" + str(self.masklen)
		return result
		
	def __repr__(self):
		# TODO: FIXME
		return str(self)
		
	def __getitem__(self, indexOrPrefix: int or str or Prefix):
		""" look up an assigned subnet from this Prefix using prefix notation (str)
		    or subnet index (int) based on the subnetlen associated with this Prefix.
		    
		    indexOrPrefix: (str)   prefix notation key: 
		"""
		try:
			if isinstance(indexOrPRefix, slice):      # TODO: handle slices
				pass
			if isinstance(indexOrPrefix, int):        # int index based on subnetlen
				index = indexOrPrefix
				netid = self.netid + ((1 << (32 - self.subnetlen)) * index)
				prefix = "{netid}/{self.subnetlen}"
			elif isinstance(indexOrPrefix, str):      # string repr of Prefix
				prefix = indexOrPrefix
			else:
				raise IndexError()
			if prefix in self._subnets:
				return self._subnets[prefix]
		except IndexError as e:
			raise IndexError("key must be int or str and reference an instance of <class Prefix>")
		
	def __setitem__(self, indexOrPrefix, prefixObject):
		# TODO: WRITE ME
		return NotImplemented
		
	def __delitem__(self, indexOrPrefix):
	    # TODO: WRITE ME
		return NotImplemented
		
	def __contains__(self, needle):
		selfbegins = self.netid
		selfends = self.next().netid - 1
		needlebegins = needle.netid
		needleends = needle.next().netid - 1
		return selfbegins <= needlebegins and selfends >= needleends
		
	def __len__(self):
		return 1 << self.masklen
		
	def __ceil__(self):
		return self.__class__(self._boundary - 1, 32, supernet=self)
		
	def __index__(self):
		pass
		
	def __iter__(self):
		pass
		
	def __lt__(self, prefix):
		pass
		
	def __gt__(self, prefix):
		pass
		
	def __le__(self, prefix):
		pass
		
	def __ge__(self, prefix):
		pass
		
	def __eq__(self, prefix):
		pass
		
	def __ne__(self, prefix):
		pass
	
	def __init__(self, prefix, masklen=None, supernet=None, subnetlen=None, boundary=None):
		self._netid = None
		self._masklen = None
		self._boundary = (((2 ** 31) - 1) << 1) + 1
		self._subnetlen = 0
		self._subnets = {}
		if supernet is not None:
			self.supernet = supernet
			self.boundary = self.supernet.boundary
			self.subnetlen = self.supernet.subnetlen
			debug(f"<prefix>.__init__: <prefix>.(subnetlen, boundary) ->" +
					   f" {self.subnetlen}, {self.boundary}")
		if subnetlen is not None:
			self.subnetlen = subnetlen
			debug(f"<prefix>.__init__: <prefix>.subnetlen -> {self.subnetlen}")
		if boundary is not None:
			self.boundary = boundary
			debug(f"<prefix>.__init__: <prefix>.boundary -> {self.boundary}")
		if isinstance(prefix, str):
			try:
				prefix = prefix.split("/")
				debug(f"<prefix>.__init__: prefix: {prefix}, masklen: {masklen}")
				self.net = prefix[0]
				if len(prefix) == 1:
					self.masklen = masklen
				elif len(prefix) == 2:
					self.masklen = prefix[1]
			except:
				raise ValueError("mask must be an integer value between 0 and 32")	
		elif isinstance(prefix, int):
			self._netid = prefix
			self._masklen = masklen
		debug(f"<prefix>.__init__: returning instance <prefix {self} of <supernet>{self.supernet} >:")
		debug(f"                   " + 
				f"<netid>{self.netid}, " + 
				f"<net>{self.net}, <masklen>{self.masklen}, " + 
				f"<boundary>{self.toStr(self.boundary)}")
				
	# Root Prefix (All IPV4 Addressing)
	IPV4 = __class__.(0, masklen=0, supernet=Prefix.IPV4)
	__class__._supernet = __class__.IPV4
ext().netid - 1
		needlebegins = needle.netid
		needleends = needle.next().netid - 1
		return selfbegins <= needlebegins and selfends >= needleends
		
	def __len__(self):
		return 1 << self.masklen
		
	def __ceil__(self):
		return self.__class__(self._boundary - 1, 32, supernet=self)
		
	def __index__(self):
		pass
		
	def __iter__(self):
		pass
		
	def __lt__(self, prefix):
		pass
		
	def __gt__(self, prefix):
		pass
		
	def __le__(self, prefix):
		pass
		
	def __ge__(self, prefix):
		pass
		
	def __eq__(self, prefix):
		pass
		
	def __ne__(self, prefix):
		pass
	
	def __init__(self, prefix, masklen=None, supernet=None, subnetlen=None, boundary=None):
		self._netid = None
		self._masklen = None
		self._boundary = (((2 ** 31) - 1) << 1) + 1
		self._subnetlen = 0
		self._subnets = {}
		if supernet is not None:
			self.supernet = supernet
			self.boundary = self.supernet.boundary
			self.subnetlen = self.supernet.subnetlen
			debug(f"<prefix>.__init__: <prefix>.(subnetlen, boundary) ->" +
					   f" {self.subnetlen}, {self.boundary}")
		if subnetlen is not None:
			self.subnetlen = subnetlen
			debug(f"<prefix>.__init__: <prefix>.subnetlen -> {self.subnetlen}")
		if boundary is not None:
			self.boundary = boundary
			debug(f"<prefix>.__init__: <prefix>.boundary -> {self.boundary}")
		if isinstance(prefix, str):
			try:
				prefix = prefix.split("/")
				debug(f"<prefix>.__init__: prefix: {prefix}, masklen: {masklen}")
				self.net = prefix[0]
				if len(prefix) == 1:
					self.masklen = masklen
				elif len(prefix) == 2:
					self.masklen = prefix[1]
			except:
				raise ValueError("mask must be an integer value between 0 and 32")	
		elif isinstance(prefix, int):
			self._netid = prefix
			self._masklen = masklen
		debug(f"<prefix>.__init__: returning instance <prefix {self} of <supernet>{self.supernet} >:")
		debug(f"                   " + 
				f"<netid>{self.netid}, " + 
				f"<net>{self.net}, <masklen>{self.masklen}, " + 
				f"<boundary>{self.toStr(self.boundary)}")
				
	# Root Prefix (All IPV4 Addressing)
	IPV4 = __class__.(0, masklen=0, supernet=Prefix.IPV4)
	__class__._supernet = __class__.IPV4
