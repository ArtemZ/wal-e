import json

from wal_e.blobstore import swift
from wal_e.storage.base import BackupInfo


class SwiftBackupInfo(BackupInfo):
    def load_detail(self, conn):
        if self._details_loaded:
            return

        uri = "{scheme}://{bucket}/{path}".format(
            scheme=self.layout.scheme,
            bucket=self.layout.store_name(),
            path=self.layout.basebackup_sentinel(self))

        data = json.loads(swift.uri_get_file(None, uri, conn=conn))
        for k, v in data.items():
            setattr(self, k, v)

        self._details_loaded = True
