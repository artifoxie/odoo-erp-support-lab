from odoo.tests.common import TransactionCase


class TestStockHealth(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.product = cls.env["product.product"].create({
            "name": "Test Electronic Component",
            "is_storable": True,
            "stock_min_threshold": 10.0,
        })

    def test_out_of_stock(self):
        """Product without stock should be OUT."""
        self.assertEqual(
            self.product.stock_health_status,
            "out",
        )

    def test_low_stock(self):
        """Stock below threshold should be LOW."""
        self.product.stock_min_threshold = 40.0

        self.env["stock.quant"]._update_available_quantity(
            self.product,
            self.env.ref("stock.stock_location_stock"),
            20.0,
        )

        self.assertEqual(
            self.product.stock_health_status,
            "low",
        )

    def test_healthy_stock(self):
        """Stock above threshold should be OK."""
        self.env["stock.quant"]._update_available_quantity(
            self.product,
            self.env.ref("stock.stock_location_stock"),
            50.0,
        )

        self.assertEqual(
            self.product.stock_health_status,
            "ok",
        )

    def test_stock_equal_threshold(self):
        """Stock equal to threshold should be OK."""
        self.env["stock.quant"]._update_available_quantity(
            self.product,
            self.env.ref("stock.stock_location_stock"),
            10.0,
        )

        self.assertEqual(
            self.product.stock_health_status,
            "ok",
        )