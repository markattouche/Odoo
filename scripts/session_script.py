from xmlrpc import client

url = 'https://markattouche-odoo-develop-4264958.dev.odoo.com'
db = 'markattouche-odoo-develop-4264958'
username = 'admin'
password = 'admin'
# 3054e4c38f04c40fa0cf5a5c308eb2690f90bbb2

common = client.ServerProxy('%s/xmlrpc/2/common' % url)
print(common.version())
print("----------------------------------------------------------------------------------")
uid = common.authenticate(db, username, password, {})
print(uid)
print("----------------------------------------------------------------------------------")
models = client.ServerProxy('%s/xmlrpc/2/object' % url)

model_access = models.execute_kw(db,uid,password, 'academy.session', 'check_access_rights',
                                ['write'],{'raise_exception': False})

print(model_access)
("----------------------------------------------------------------------------------")
courses = models.execute_kw(db,uid,password, 'academy.course', 'search_read',
                                [[['level','in', ['intermediate','beginner']]]])

print(courses)

print("----------------------------------------------------------------------------------")
course = models.execute_kw(db,uid,password, 'academy.course', 'search',
                                [[['level','in', ['intermediate','beginner']]]])
print(course)

print("----------------------------------------------------------------------------------")
session_fields = models.execute_kw(db,uid,password, 'academy.session', 'fields_get',
                                [], {'attributes': ['string','type','required']})
print(session_fields)

new_session = models.execute(
    db,uid,password, 'academy.session', 'create',
    [
        {
            'course_id':course[0],
            'state': 'open',
            'duration': 5,
        }
    ]
)

print(new_session)