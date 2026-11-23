
# Odoo ERP Support Lab

A practical Odoo 18 Community project demonstrating ERP customization, inventory monitoring, automated testing, and application support workflows.

## Overview

This project extends Odoo Inventory with a custom **Stock Health Monitor** module.

It evaluates product stock levels against configurable minimum thresholds and displays a visual stock status.

Built as a technical portfolio project focused on ERP development, QA, and troubleshooting.

## Tech Stack

- Odoo 18 Community
- Python / Odoo ORM
- PostgreSQL 15
- Docker Compose
- XML Views
- Odoo TransactionCase

## Features

- Configurable minimum stock threshold
- Automatic stock health calculation
- Healthy / Low Stock / Out of Stock statuses
- Visual status badges in product forms
- Integration with Odoo Inventory
- Automated business logic tests

## Business Rules

| Condition | Status |
|---|---|
| Quantity <= 0 | Out of Stock |
| 0 < Quantity < Threshold | Low Stock |
| Quantity >= Threshold | Healthy |
| Non-storable product | Not applicable |

## Quick Start

### Requirements

- Docker
- Docker Compose

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/odoo-erp-support-lab.git
cd odoo-erp-support-lab
docker compose up -d
```

Open http://localhost:8069.

Create a database named `forgeerp`, install the Inventory application, then install **Stock Health Monitor** from Apps.

Use a local-only database master password and replace all example credentials before deploying outside a development environment.

## Run Tests

Stop the application container:

```bash
docker compose stop odoo
```

Run the module tests:

```bash
docker compose run --rm odoo \
  odoo -d forgeerp \
  -u stock_health \
  --test-enable \
  --test-tags /stock_health \
  --stop-after-init \
  --no-http \
  --log-level=test
```

Restart Odoo:

```bash
docker compose up -d odoo
```

### Latest Local Test Result

- 4 automated tests
- 0 failures
- 0 errors

## QA & Support Documentation

- [Test Cases](docs/test-cases.md)
- [Troubleshooting Guide](docs/troubleshooting.md)

## Screenshots

Screenshots of the product form and stock status scenarios will be added here.

## Limitations

- Stock status uses `qty_available`, not forecasted stock.
- The minimum threshold is configured per product template.
- Multi-warehouse and multi-company behavior is not explicitly handled.
- Automated tests cover the core stock status rules.

## Author

Artur Aivazian

Backend Developer | ERP Development & Application Support
