"""cartcalc: shopping-cart pricing (a demo target for AutoFix)."""

from cartcalc.pricing import (
    apply_coupon,
    bulk_discount,
    checkout_total,
    round_cents,
    shipping_cost,
    subtotal,
    tax,
)

__all__ = [
    "apply_coupon",
    "bulk_discount",
    "checkout_total",
    "round_cents",
    "shipping_cost",
    "subtotal",
    "tax",
]
