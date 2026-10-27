# Tax is charged on the price before the coupon

Checking out 2 items at 10.00 each with the coupon FLAT5 and 1 kg standard shipping
should cost 21.19: 20.00 minus the 5.00 coupon is 15.00, plus 8% tax on 15.00 (1.20),
plus 4.99 shipping. The shop charges 21.59 instead, because the 8% tax (1.60) is
computed on the 20.00 before the coupon. Customers with a coupon pay too much tax.

Reproduction test: [`test_reproduce.py`](test_reproduce.py) (copy it into `tests/` to
reproduce the bug in CI).
