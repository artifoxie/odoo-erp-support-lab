from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    stock_min_threshold = fields.Float(
        string="Minimum Stock Threshold",
        default=10.0,
        help="Minimum acceptable stock quantity.",
    )

    stock_health_status = fields.Selection(
        selection=[
            ("ok", "Healthy"),
            ("low", "Low Stock"),
            ("out", "Out of Stock"),
        ],
        string="Stock Health",
        compute="_compute_stock_health_status",
    )

    @api.depends(
        "qty_available",
        "stock_min_threshold",
        "is_storable",
    )
    def _compute_stock_health_status(self):
        for product in self:
            if not product.is_storable:
                product.stock_health_status = False
            elif product.qty_available <= 0:
                product.stock_health_status = "out"
            elif product.qty_available < product.stock_min_threshold:
                product.stock_health_status = "low"
            else:
                product.stock_health_status = "ok"