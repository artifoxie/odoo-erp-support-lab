# Odoo ERP — Troubleshooting Guide

## 1. Odoo is not accessible

Check containers:

```bash
docker compose ps
```

Inspect logs:

```bash
docker compose logs --tail=100 odoo
```

Check HTTP:

```bash
curl -I http://localhost:8069
```

## 2. Custom module is not visible

Possible causes:
- Incorrect addons_path.
- Missing __manifest__.py.
- Apps list not updated.
- Python import errors.

Check the addon directory:

```bash
docker compose exec odoo \
  ls -la /mnt/extra-addons/stock_health
```

## 3. Stock Health status is incorrect

Verify:
1. Product is storable.
2. Available quantity is correct.
3. Minimum threshold is correct.
4. Product form was refreshed.
5. No unexpected warehouse/company context is active.

Note: qty_available represents available on-hand
quantity in the current Odoo context.