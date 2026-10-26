# autofix-demo: cartcalc

A small shopping-cart pricing package (subtotals, bulk discounts, coupons, tax,
shipping) used as a **demo target for AutoFix**, an LLM-based automatic program repair
tool.

It has two real-looking bugs, each with a bug report in `issues/`:

| Issue | Bug | Status |
| --- | --- | --- |
| [001](issues/001-bulk-discount-boundary/README.md) | bulk discount starts at 11 units instead of 10 | failing test `tests/test_pricing.py::test_bulk_discount_starts_at_ten_units` is in the suite, so CI on `main` is red; fixed by AutoFix in PR #1 |
| [002](issues/002-percentage-coupon/README.md) | percentage coupons make the order free | reported with a reproduction test in the issue folder, for the live demo |

All other tests pass and act as the regression suite.

## Run the tests

```bash
pip install -r requirements.txt
pytest -q
```

## Live demo: repair issue 002 with AutoFix

```bash
# 1. Reproduce: add the issue's test to the suite. CI turns red.
cp issues/002-percentage-coupon/test_reproduce.py tests/test_issue_002.py
git add tests/test_issue_002.py && git commit -m "Reproduce issue 002" && git push

# 2. Repair (from the autofix folder)
autofix run --repo ../autofix-demo --test tests/test_issue_002.py \
    --issue ../autofix-demo/issues/002-percentage-coupon/README.md --regression tests \
    -c configs/groq20b.yaml

# 3. Open a pull request with the evidence pack. Its CI turns green.
autofix pr <run_id> --repo-path ../autofix-demo --base main -c configs/groq20b.yaml
```

AutoFix reproduces the failure, localizes the faulty function, proposes candidate
patches, validates them (including mutation-guided tests that probe what the existing
tests miss) and opens a pull request whose description is the evidence: the bug
report, suspects, tests run, candidates, mutation verdict, model and tokens.
