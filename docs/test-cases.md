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