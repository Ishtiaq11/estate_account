from odoo import Command, api, fields, models


class Property(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        for record in self:
            self.env["account.move"].create({
                "partner_id": record.partner_id.id,
                "move_type": "out_invoice",
                "line_ids": [
                    Command.create({
                        "name": record.name,
                        "quantity": 1.0,
                        "price_unit": record.selling_price * 0.06
                    }),
                    Command.create({
                        "name": "Administrativ Cost",
                        "quantity": 1.0,
                        "price_unit": 100.0
                    })
                ]
            })
        return super().action_sold()