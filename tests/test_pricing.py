import pytest

from cartcalc import (
    apply_coupon,
    bulk_discount,
    checkout_total,
    round_cents,
    shipping_cost,
    subtotal,
    tax,
)


def test_round_cents_half_up():
    assert round_cents(2.675) == 2.68
    assert round_cents(1.004) == 1.0


def test_subtotal():
    assert subtotal([(2.50, 4), (1.99, 1)]) == 11.99
    assert subtotal([]) == 0.0


def test_no_bulk_discount_below_ten():
    assert bulk_discount(9, 10.0) == 90.0


def test_bulk_discount_well_inside_tiers():
    assert bulk_discount(20, 10.0) == 180.0
    assert bulk_discount(60, 10.0) == 510.0


def test_unknown_or_missing_coupon_changes_nothing():
    assert apply_coupon(80.0, "NOPE") == 80.0
    assert apply_coupon(80.0, None) == 80.0


def test_flat_coupon_never_negative():
    assert apply_coupon(20.0, "FLAT5") == 15.0
    assert apply_coupon(3.0, "FLAT5") == 0.0


def test_tax_rounds_to_cents():
    assert tax(19.99, 0.08) == 1.6
    assert tax(0, 0.2) == 0.0


@pytest.mark.parametrize(
    "weight, express, value, expected",
    [(0.5, False, 10, 4.99), (2.2, False, 10, 7.99), (2.2, True, 10, 15.98), (3, False, 80, 0.0)],
)
def test_shipping(weight, express, value, expected):
    assert shipping_cost(weight, express, value) == expected


def test_checkout_without_discounts():
    # 2 x 10.00, 8% tax, 1 kg standard shipping.
    assert checkout_total([(10.0, 2)], weight_kg=1) == 26.59


# --- Bug reports (see issues/) --------------------------------------------------------


def test_bulk_discount_starts_at_ten_units():
    """issues/001-bulk-discount-boundary: exactly 10 units must already get 10% off."""
    assert bulk_discount(10, 10.0) == 90.0
    assert bulk_discount(50, 10.0) == 425.0

def test_percent_coupon_takes_percent_off():
    """SAVE10 on 80.00 must give 72.00, not 0.00."""
    assert apply_coupon(80.0, "SAVE10") == 72.0
    assert apply_coupon(80.0, "SAVE25") == 60.0
