# Bulk discount does not apply at exactly 10 units

Our pricing page says "10% off when you buy 10 or more". A customer ordered exactly
10 units at 10.00 and was charged 100.00 instead of 90.00. Ordering 11 units gives
the discount. The same happens at the 50-unit tier: 50 units get only 10% off
instead of 15%.

Failing test: `tests/test_pricing.py::test_bulk_discount_starts_at_ten_units`
