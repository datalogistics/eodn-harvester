from itertools import cycle
from libdlt.schedule import AbstractSchedule

class DuplicateUploadSchedule(AbstractSchedule):
    def __init__(self, ceph):
        self._use_ceph = bool(ceph)
        self._ceph = cycle(ceph)
        self._seen = []
        
    def setSource(self, source):
        self._ls = cycle(source)

    def get(self, context):
        if context["offset"] in self._seen and self._use_ceph:
            return next(self._ceph)
        else:
            self._seen.append(context["offset"])
            return next(self._ls)
