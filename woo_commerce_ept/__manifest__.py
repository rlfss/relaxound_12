{
    'name': 'Odoo WooCommerce Connector',
    'version': '12.0',
    
    'category': 'Sale',
    'summary' : 'Integrate & Manage all your WooCommerce operations from Odoo',
    'description': """
""",

    'depends': ['base','delivery','auto_invoice_workflow_ept'],    
    'data': [
             'security/group.xml',
             'data/import_order_status.xml',
             'views/woo_instance_main_menu_view.xml',
             'views/sale_workflow_config.xml',             
             'wizard/res_config_view.xml',
             'views/woo_template_view.xml',
             # 'views/woo_attribute_term_ept.xml',
             # 'views/woo_attribute_ept_view.xml',
             'views/woo_product_image_view.xml',
             # 'views/woo_variant_view.xml',
             'views/res_partner.xml',                          
             'views/sale_order.xml',
             'views/stock_picking_view.xml',
             'views/woo_tags_ept.xml',
             # 'views/woo_coupons_view.xml',
             'views/woo_product_categ_view.xml',
             'views/account_invoice_view.xml',
             'views/woo_process_job.xml',
             'views/woo_payment_gateway_view.xml',             
             'wizard/woo_process_import_export_view.xml',
             'wizard/woo_cancel_order_wizard_view.xml',
             # 'views/sale_report_view.xml',
             'security/ir.model.access.csv',             
             'views/web_templates.xml',
             'views/ir_cron.xml',
             'wizard/woo_installer.xml',
             'views/woo_instance_view.xml',  
             'views/woo_req_history_ept.xml',
             ],    
    'installable': True,
    'auto_install': False,
    'application' : True,
    'pre_init_hook':'version_check',
    'active': False,
    'images': ['static/description/main_screen.jpg'],
}
