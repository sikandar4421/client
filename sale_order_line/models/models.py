from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'product.product'

    percentage = fields.Float(string= 'Percantage', default= 0.0)

    @api.onchange('percentage')
    def get_sale_price(self):
        self.list_price = self.standard_price * (1 + self.percentage / 100)
    # percentage = fields.Float(string="Percentage (%)")
    # single_unit_price = fields.Float()
    # cost_unit = fields.Float(realted='product_template_id.standard_price', store=True, string='Cost Price')
    #
    # @api.onchange('percentage', 'product_template_id')
    # def _onchange_standard_price_percentage_increase(self):
    #     for line in self:
    #         if line.percentage:
    #             pp = line.product_template_id.standard_price
    #             line.price_unit = pp
    #             if line.percentage > 0.0:
    #                 line.single_unit_price = line.product_template_id.standard_price * (1 + line.percentage / 100)
    #                 line.price_unit = line.single_unit_price
    #         else:
    #             line.update({
    #                             'price_unit': pp,
    #                             'cost_unit' : line.product_template_id.standard_price
    #
    #                         })
                # print(line.price_unit)

    # @api.onchange('percentage', 'product_template_id')
    # def get_amount(self):
    #     for line in self:
    #         print(line.product_template_id.standard_price)
    #         line.price_unit = line.product_template_id.standard_price
    #         line.single_unit_price = 0
    #         # price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
    #         line.single_unit_price += (line.price_unit * (line.percentage or 0.0) / 100.0)
    #         print(line.single_unit_price)
    #
    #         line.price_unit = line.single_unit_price + line.product_template_id.standard_price
        # import pdb
        # pdb.set_trace()



    # @api.onchange('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    # def _compute_amount(self):
    #     """
    #     Compute the amounts of the SO line.
    #     """
    #     for line in self:
    #         line.ex_total = 0
    #         tax_results = self.env['account.tax']._compute_taxes([line._convert_to_tax_base_line_dict()])
    #         totals = list(tax_results['totals'].values())[0]
    #         amount_untaxed = totals['amount_untaxed'] + line.ex_total
    #         amount_tax = totals['amount_tax']
    #         line.ex_total += line.price_unit * (line.percentage or 0.0) / 100.0
    #
    #         line.update({
    #             'price_subtotal': amount_untaxed,
    #             'price_tax': amount_tax,
    #             'price_total': amount_untaxed + amount_tax,
    #         })
    #         if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
    #                 'account.group_account_manager'):
    #             line.tax_id.invalidate_recordset(['invoice_repartition_line_ids'])
