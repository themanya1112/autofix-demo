# autofix-demo: cartcalc

A small shopping-cart pricing package (subtotals, bulk discounts, coupons, tax,
shipping) used as a **demo target for AutoFix**, an LLM-based automatic program repair
tool.

It has real-looking bugs, each with a bug report in `issues/`:

| Issue | Bug | Status |
| --- | --- | --- |
| [001](issues/001-bulk-discount-boundary/README.md) | bulk discount starts at 11 units instead of 10 | fixed by AutoFix in PR #1 |
| [002](issues/002-percentage-coupon/README.md) | percentage coupons make the order free | reported with a reproduction test, for the live demo |
| [003](issues/003-tax-before-coupon/README.md) | tax is charged on the price before the coupon | reported with a reproduction test, for the live demo |
| [004](issues/004-express-free-shipping/README.md) | express shipping is free on big orders | reported with a reproduction test, for the live demo |

All other tests pass and act as the regression suite.

## Run the tests

```bash
pip install -r requirements.txt
pytest -q
```

## Live demo: repair an issue with AutoFix

Replace `003-tax-before-coupon` and `test_issue_003.py` with the issue you want to show.

```bash
# 1. Reproduce: add the issue's test to the suite. CI turns red.
cp issues/003-tax-before-coupon/test_reproduce.py tests/test_issue_003.py
git add tests/test_issue_003.py
git commit -m "Reproduce issue 003"
git push

# 2. Repair (from the autofix folder)
autofix run --repo ../autofix-demo --test tests/test_issue_003.py \
    --issue ../autofix-demo/issues/003-tax-before-coupon/README.md --regression tests \
    -c configs/groq20b.yaml

# 3. Open a pull request with the evidence pack.
autofix pr <run_id> --repo-path ../autofix-demo --base main -c configs/groq20b.yaml
```

AutoFix reproduces the failure, localizes the faulty function, proposes candidate
patches, validates them (including mutation-guided tests that probe what the existing
tests miss) and opens a pull request whose description is the evidence: the bug
report, suspects, tests run, candidates, mutation verdict, model and tokens.
