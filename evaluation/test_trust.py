import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
from trust.trust_manager import TrustManager

tm = TrustManager()

print(tm.get_all_trust())

tm.update("semantic", True)

print(tm.get_all_trust())

tm.update("semantic", False)

print(tm.get_all_trust())