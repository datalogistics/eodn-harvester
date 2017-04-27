from itertools import cycle
from libdlt.schedule import AbstractSchedule

class AlternateDepotSchedule(AbstractSchedule):
    def __init__(self, ceph):
        self._use_ceph = bool(ceph)
        self._ceph = cycle(ceph)
        
    def setSource(self, source):
        self._ls = cycle(source)

    def get(self, context):
        return next(self._ceph)
