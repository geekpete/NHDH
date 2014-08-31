from NHDH import principals

from flask.ext.principal import Permission, RoleNeed, UserNeed

user_permission = Permission(RoleNeed('None'))

admin_permission = Permission(RoleNeed('None'))

