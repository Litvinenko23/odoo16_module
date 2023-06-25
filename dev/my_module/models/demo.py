from odoo.odoo import fields, models


class DemoDemo(models.Model):
    _name = "demo.demo"
    _description = "Demo module odoo"

    name = fields.Char(string="Name")
