# Copyright 2021 OriolVForgeFlow
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Certification",
    "summary": "Defines certifications for different purrposes",
    "version": "14.0.1.0.0",
    "development_status": "Beta",
    "category": "Certification Management",
    "website": "https://github.com/OriolVForgeFlow",
    "author": "Odoo Community Association (OCA)",
    "maintainers": ["OriolVForgeFlow"],
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": ['security/ir.model.access.csv',
            'views/certification_view.xml',
            'views/res_partner_view.xml',
            'views/standard_view.xml'
    ]
}