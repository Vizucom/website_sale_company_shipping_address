# -*- coding: utf-8 -*-
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale
from openerp import SUPERUSER_ID


class WebsiteSale(website_sale):

    def checkout_values(self, data=None):

        values = super(WebsiteSale, self).checkout_values(data=data)

        cr, context, registry = request.cr, request.context, request.registry
        orm_partner = registry.get('res.partner')
        orm_user = registry.get('res.users')

        partner = orm_user.browse(cr, SUPERUSER_ID, request.uid, context).partner_id

        if partner.company_type == 'person' and partner.parent_id:
            search_args = [('parent_id', '=', partner.parent_id.id), ('type', '=', 'delivery')]
            parent_shipping_ids = orm_partner.search(cr, SUPERUSER_ID, search_args, context=context)
            ctx = dict(context, show_address=1)
            parent_shippings = orm_partner.browse(cr, SUPERUSER_ID, list(parent_shipping_ids), ctx)

            # Concatenate the two recordsets
            if parent_shippings:
                values['shippings'] += parent_shippings

        return values
