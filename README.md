# autofix-demo: cartcalc

A small shopping-cart pricing package (subtotals, bulk discounts, coupons, tax,
shipping) used as a **demo target for AutoFix**, an LLM-based automatic program repair tool.

It contains two real-looking bugs on purpose, each with a bug report in `issues/` and a
failing test, so CI on `main` is red:

| Issue | Bug | Failing test |
| --- | --- | --- |
| [001](issues/001-bulk-discount-boundary.md) | bulk discount starts at 11 units instead of 10 | `test_bulk_discount_starts_at_ten_units` |
| [002](issues/002-percentage-coupon.md) | percentage coupons make the order free | `test_percent_coupon_takes_percent_off` |

All other tests pass and act as the regression suite.

## Run the tests

```bash
pip install -r requirements.txt
pytest -q
```

## Repair a bug with AutoFix

```bash
autofix run --repo . --test tests/test_pricing.py::test_bulk_discount_starts_at_ten_units \
    --issue issues/001-bulk-discount-boundary.md --regression tests -c <autofix>/configs/groq.yaml
autofix pr <run_id> --repo-path . --base main -c <autofix>/configs/groq.yaml
```

AutoFix reproduces the failure, localizes the faulty function, proposes candidate
patches, validates them (including mutation-guided tests that probe what the existing
tests miss) and opens a pull request with the evidence.
