import hashlib
import json


class EvidenceHasher:

    def create_fingerprint(self, evidence):
        canonical_data = json.dumps(
            evidence,
            sort_keys=True,
            separators=(",", ":")
        )

        fingerprint = hashlib.sha256(
            canonical_data.encode("utf-8")
        ).hexdigest()

        return fingerprint