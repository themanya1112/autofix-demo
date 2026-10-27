"""Shopping-cart pricing: subtotals, bulk discounts, coupons, tax and shipping.

All money values are floats in the shop's currency and every public function returns
an amount rounded to whole cents (half-up).
"""

from __future__ import annotations

import math
from decimal import ROUND_HALF_UP, Decimal

# Bulk tiers as (minimum quantity, percent off), checked from the largest tier down.
BULK_TIERS = [(50, 15), (10, 10)]

# Coupon codes: ("percent", n) takes n% off, ("flat", x) takes x off.
COUPONS = {
    "SAVE10": ("percent", 10),
    "SAVE25": ("percent", 25),
    "FLAT5": ("flat", 5.0),
}

SHIPPING_BASE = 4.99  # first kilogram (or part of it)
SHIPPING_PER_KG = 1.50  # each further started kilogram
FREE_SHIPPING_FROM = 75.0  # standard shipping is free from this order value


def round_cents(amount: float) -> float:
    """Round to whole cents, halves away from zero (2.675 -> 2.68)."""
    return float(Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def subtotal(items: list[tuple[float, int]]) -> float:
    """Sum of unit_price * quantity over (unit_price, quantity) items."""
    return round_cents(sum(price * qty for price, qty in items))


def bulk_discount(qty: int, unit_price: float) -> float:
    """Line total for `qty` units after the bulk discount.

    10 or more units get 10% off, 50 or more get 15% off; fewer than 10 pay full price.
    """
    for min_qty, pct in BULK_TIERS:
        if qty >= min_qty:
            return round_cents(qty * unit_price * (100 - pct) / 100)
    return round_cents(qty * unit_price)


def apply_coupon(total: float, code: str | None) -> float:
    """Total after applying a coupon code. Unknown codes change nothing, and a coupon
    never makes the total negative."""
    if not code or code not in COUPONS:
        return round_cents(total)
    kind, value = COUPONS[code]
    if kind == "percent":
        discounted = total - total * value / 100
    else:
        discounted = total - value
    return round_cents(max(discounted, 0.0))


def tax(amount: float, rate: float) -> float:
    """Tax due on `amount` at `rate` (0.08 means 8%), rounded to cents."""
    return round_cents(amount * rate)


def shipping_cost(weight_kg: float, express: bool = False, order_value: float = 0.0) -> float:
    """Shipping for a parcel: 4.99 for the first kilogram plus 1.50 for each further
    started kilogram. Express doubles the price. Standard (not express) shipping is free
    for orders of 75.00 or more."""
    if weight_kg <= 0:
        return 0.0
    if not express and order_value >= FREE_SHIPPING_FROM:
        return 0.0
    extra_kg = max(0, math.ceil(weight_kg) - 1)
    cost = SHIPPING_BASE + SHIPPING_PER_KG * extra_kg
    return round_cents(cost * 2 if express else cost)


def checkout_total(
    items: list[tuple[float, int]],
    coupon: str | None = None,
    tax_rate: float = 0.08,
    weight_kg: float = 0.0,
    express: bool = False,
) -> float:
    """What the customer pays: bulk-discounted lines, then the coupon, then tax on the
    discounted amount, then shipping."""
    lines = sum(bulk_discount(qty, price) for price, qty in items)
    after_coupon = apply_coupon(lines, coupon)
    taxed = after_coupon + tax(after_coupon, tax_rate)
    return round_cents(taxed + shipping_cost(weight_kg, express, after_coupon))
