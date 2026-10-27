"""Reproduction test for issue 003, attached to the bug report.

It is not part of the CI suite yet. To reproduce the bug, copy this file into tests/
(CI turns red), then let AutoFix repair it.
"""

from cartcalc import checkout_total


def test_tax_is_charged_after_the_coupon():
    """2 x 10.00, FLAT5, 8% tax, 1 kg standard shipping: 15.00 + 1.20 + 4.99 = 21.19."""
    assert checkout_total([(10.0, 2)], coupon="FLAT5", weight_kg=1) == 21.19
