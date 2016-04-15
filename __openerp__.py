# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "eCommerce - Company shipping addresses for partner",
    'category': 'eCommerce',
    'version': '0.1',
    'author': ' Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['website_sale'],
    'description': """
eCommerce - Company shipping addresses for partner
==================================================
 * Pull shipping address suggestions from the parent company if the customer has one defined
 * Intended for situations where a customer company has multiple persons buying from Odoo Webshop, and they all want to use a common shipping address
""",
    'data': [],
}
