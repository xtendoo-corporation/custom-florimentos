# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, tools


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_woocommerce_exported = fields.Boolean(
        string='Is Exported to WooCommerce',
        default=False,
    )
    woo_product_template_ept_ids = fields.One2many(
        comodel_name='woo.product.template.ept',
        string='WooCommerce Product Template',
    )

    @api.onchange('woo_product_template_ept_ids')
    def _onchange_woo_product_template_ept_ids(self):
        for record in self:
            record.is_woocommerce_exported = bool(record.woo_product_template_ept_ids)
