from odoo import fields, models, api
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_cost = fields.Float(string='Minimum Cost')
    brand_name = fields.Char(string='Brand Name')
    brand_id = fields.Many2one('product.brand', string='Brand')

    @api.onchange('minimum_cost')
    def _onchange_minimum_cost(self):
        if self.minimum_cost > self.list_price:
            self.list_price = self.minimum_cost

    @api.constrains('minimum_cost', 'list_price')
    def _check_minimum_cost(self):
        for record in self:
            if record.minimum_cost > record.list_price:
                raise UserError("Minimum cost should not be greater than the unit price.")


class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char(string='Brand Name', required=True)



