from user import User
from admin import Admin, Privileges

privileges = ['can add post','can delete post','can ben user']
mpy = Admin('Peiyu', 'Ma','22',privileges)
mpy.privileges.show_privileges()