"""Reproduction test for issue 004, attached to the bug report.

It is not part of the CI suite yet. To reproduce the bug, copy this file into tests/
(CI turns red), then let AutoFix repair it.
"""

from cartcalc import shipping_cost


def test_express_shipping_is_never_free():
    """80.00 order, 2.2 kg: standard is free, express costs 2 x 7.99 = 15.98."""
    assert shipping_cost(2.2, express=True, order_value=80.0) == 15.98
    assert shipping_cost(2.2, express=False, order_value=80.0) == 0.0
