# Percentage coupons make the order free

Applying the coupon SAVE10 to an 80.00 order brings the total to 0.00 instead of
72.00 (10% off). SAVE25 does the same. The flat coupon FLAT5 works correctly.

Reproduction test: [`test_reproduce.py`](test_reproduce.py) (copy it into `tests/` to
reproduce the bug in CI).
