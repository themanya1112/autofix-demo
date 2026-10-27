# Express shipping is free on big orders

Free shipping from 75.00 is meant for standard shipping only; express always costs
double the standard price. But an 80.00 order with a 2.2 kg parcel and express
shipping is charged 0.00 for shipping instead of 15.98 (2 x 7.99). Standard shipping
for the same order is correctly free.

Reproduction test: [`test_reproduce.py`](test_reproduce.py) (copy it into `tests/` to
reproduce the bug in CI).
