# -*- coding: utf-8 -*-
{
    'name': "assistant",

    'summary': """
        c'est un module qui facilite les taches de l'utilisateur """,

    'description': """
        Ce module est un module d'assistant qui sert a orienter l'utilisateur de odoo et de lui faciliter l'execution de ses taches;Plus explicitement ,ce module recupere toute les taches que doit l'utilisateur faire prochainement .Il sert aussi a relancer les clients, avoir une vision globale sur les factures non reglées,les devis,les bons de commande et les articles.
    """,

    'author': "Groupe L3",
    'website': "localhost:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','sale','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/assistant_manager.xml','articles.xml','taches.xml','clients.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}