# Percentage coupons on bulk orders take too much off

The cart applies discounts in a fixed order: the bulk discount first, then the coupon
on what is left. But a 10-unit order at 10.00 with the coupon SAVE10 shows 80.00 in
the cart instead of 81.00:

- expected: 100.00, minus 10% bulk discount = 90.00, minus 10% coupon = 81.00
- actual: 80.00, as if the coupon took 10% of the full 100.00 price

Orders without a bulk discount, and the flat coupon FLAT5, look correct. Larger bulk
orders with SAVE25 are off by more.

Reproduction test: [`test_reproduce.py`](test_reproduce.py) (copy it into `tests/` to
reproduce the bug in CI).
