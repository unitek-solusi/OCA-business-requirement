# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleLayoutCategory(models.Model):
    _inherit = 'sale.layout_category'

    br_deliverable_section_id = fields.Many2one(
        comodel_name='business.requirement.deliverable.section',
        string="Business Requirement Deliverable Section",
    )
