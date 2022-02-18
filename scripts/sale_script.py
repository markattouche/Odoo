import xmlrpc.client

url = 'https://markattouche-odoo-develop-4264958.dev.odoo.com'
db = 'markattouche-odoo-develop-4264958'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)