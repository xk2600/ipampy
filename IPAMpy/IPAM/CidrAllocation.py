import IPAMpy.Model.PrefixModel.PrefixModel

class CidrAllocation(PrefixModel):
    def __init__(self, prefix, masklen=None, 
                        supernet=None, subnetlen=None, boundary=None, descr=None):
        self.descr = descr
        super().__init__(prefix=prefix, masklen=masklen, 
                        supernet=supernet, subnetlen=subnetlen, boundary=boundary)
                        
    def subnet(self, masklen: int = None, index=0, subnetlen=None, descr=None):
        prefix = super().subnet(masklen=masklen, index=index, subnetlen=subnetlen)
        prefix.descr = descr
        return prefix


