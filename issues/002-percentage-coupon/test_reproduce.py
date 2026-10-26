"""Reproduction test for issue 002, attached to the bug report.

It is not part of the CI suite yet. To reproduce the bug, copy this file into tests/
(CI turns red), then let AutoFix repair it.
"""

from cartcalc import apply_coupon


def test_percent_coupon_takes_percent_off():
    """SAVE10 on 80.00 must give 72.00, not 0.00."""
    assert apply_coupon(80.0, "SAVE10") == 72.0
    assert apply_coupon(80.0, "SAVE25") == 60.0
