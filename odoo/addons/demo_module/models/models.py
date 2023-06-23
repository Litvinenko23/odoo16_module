from odoo.odoo import models, fields


class Demo(models.Model):
    _name = "demo.demo"
    _description = "Demo object"

    name = fields.Char(string="Name", required=True)