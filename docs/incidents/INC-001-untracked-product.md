# INC-001: Inventory Quantity Not Updated for an Untracked Product

**System:** Odoo 18 Community  
**Module:** Inventory / Purchase / Stock Health Monitor  
**Environment:** Docker Compose, PostgreSQL 15  
**Incident date:** 2026-11-23  
**Status:** Resolved — Configuration Issue

## 1. Incident Summary

A product named `Brushless Motor 2207` displayed an on-hand quantity of `0.00` despite multiple completed inventory movements.

The custom `stock_health` module did not display a stock health status for this product.

The investigation identified that the product was not configured for inventory tracking.

## 2. Expected vs. Actual Behavior

Three inventory movements were completed:

| Reference | Movement | Quantity |
|---|---|---:|
| WH/IN/00007 | Vendor → WH/Stock | +50 |
| WH/OUT/00008 | WH/Stock → Vendor | -50 |
| WH/IN/00008 | Vendor → WH/Stock | +10 |

**Expected:** On-hand quantity of 10 units for an inventory-tracked product.

**Actual:** On-hand quantity remained 0 units.

## 3. Investigation

The investigation started with the product's **Moves History** screen.

All three movements were marked as `Done`, and their source and destination locations matched the expected warehouse flow.

The product was then inspected using Odoo Shell:

```python
product = env["product.product"].search([
    ("name", "=", "Brushless Motor 2207")
], limit=1)

print(product.id)
print(product.type)
print(product.is_storable)
print(product.qty_available)
print(product.virtual_available)
print(product.stock_health_status)
```

Observed output:

```text
Product ID: 46
Type: consu
Is Storable: False
Qty Available: 0.0
Forecasted: 40.0
Stock Health: False
```

The current stock quantities were inspected through `stock.quant`:

```python
quants = env["stock.quant"].search([
    ("product_id", "=", product.id)
])

for quant in quants:
    print(
        quant.location_id.complete_name,
        quant.quantity,
        quant.reserved_quantity
    )
```

**Result:** No stock quant records were returned.

## 4. Root Cause

The product had `is_storable=False`.

In Odoo 18, a product can be categorized as `Goods` while inventory tracking remains disabled.

As a result, the completed inventory movements did not produce the expected on-hand quantity for this product.

The custom Stock Health Monitor was designed to calculate inventory health only for storable products.

Therefore, its empty stock health status was consistent with the product configuration.

**Classification:** Product configuration issue, not a confirmed software defect.

## 5. Resolution

A new product was created with inventory tracking enabled:

- Product: `Brushless Motor 2207 - Tracked`
- Product Type: Goods
- Track Inventory: Enabled
- Minimum Stock Threshold: 20 units

A new purchase order was created for 50 units.

The order was fulfilled in two receipts:

1. Initial receipt: 10 units.
2. Backorder receipt: 40 units.

## 6. Verification

| Stage | On Hand | Stock Health | Result |
|---|---:|---|---|
| Before receiving stock | 0 | Out of Stock | PASS |
| After partial receipt | 10 | Low Stock | PASS |
| After backorder completion | 50 | Healthy | PASS |

The final on-hand quantity and forecasted quantity were both 50 units.

The custom Stock Health Monitor displayed the expected status throughout the workflow.

## 7. Preventive Actions

- Verify inventory tracking before processing stock movements.
- Confirm product configuration when stock quantities appear inconsistent.
- Compare completed stock movements with `stock.quant` records.
- Use Odoo Shell for read-only diagnostics when UI information is insufficient.
- Include tracked and untracked product scenarios in regression testing.

## 8. Conclusion

The incident was resolved by identifying an inventory tracking configuration issue and validating the expected behavior using a correctly configured product.

The investigation demonstrated the use of Odoo's Inventory and Purchase workflows, ORM diagnostics, and structured incident reporting.