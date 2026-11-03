"""Reproduction test for issue 005, attached to the bug report.

It is not part of the CI suite yet. To reproduce the bug, copy this file into tests/
(CI turns red), then let AutoFix repair it.
"""

from cartcalc import cart_total


def test_coupon_applies_after_the_bulk_discount():
    """10 x 10.00 with SAVE10: 100.00 - 10% bulk = 90.00, then - 10% coupon = 81.00."""
    assert cart_total([(10.0, 10)], coupon="SAVE10") == 81.0
