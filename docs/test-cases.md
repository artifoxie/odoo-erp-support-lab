# Stock Health Monitor — Test Cases

## Test Environment
- ERP: Odoo 18 Community
- Database: PostgreSQL 15
- Deployment: Docker Compose
- Module: stock_health

## TC-001: Healthy Stock

**Preconditions:**
- Storable product exists.
- Available quantity: 100.
- Minimum threshold: 50.

**Steps:**
1. Open Inventory > Products.
2. Select the product.
3. Set Minimum Stock Threshold to 50.
4. Save the product.
5. Check Stock Health.

**Expected Result:**
Status is "Healthy".

## TC-002: Low Stock

**Preconditions:**
- Available quantity: 20.
- Minimum threshold: 50.

**Expected Result:**
Status is "Low Stock".

## TC-003: Out of Stock

**Preconditions:**
- Available quantity: 0.
- Minimum threshold: 50.

**Expected Result:**
Status is "Out of Stock".

## TC-004: Boundary Value

**Preconditions:**
- Available quantity: 50.
- Minimum threshold: 50.

**Expected Result:**
Status is "Healthy".

## TC-005: Threshold Update

**Preconditions:**
- Available quantity: 30.
- Minimum threshold: 10.

**Steps:**
1. Open the product.
2. Change threshold from 10 to 40.
3. Save.
4. Reload the product.

**Expected Result:**
Status changes from "Healthy" to "Low Stock".


## E2E-001: Partial Purchase Receipt and Stock Health

**Environment:** Odoo 18 Community, PostgreSQL 15

**Product:** Brushless Motor 2207 - Tracked  
**Minimum Stock Threshold:** 20

### Steps

1. Create a tracked inventory product with zero stock.
2. Verify status: Out of Stock.
3. Create a purchase order for 50 units.
4. Validate a partial receipt of 10 units.
5. Create a backorder for the remaining 40 units.
6. Verify On Hand = 10 and status = Low Stock.
7. Validate the remaining 40 units.
8. Verify On Hand = 50 and status = Healthy.

### Actual Result

All three stock statuses displayed correctly.
The stock quantity was updated after completed receipts.

**Result:** PASS
