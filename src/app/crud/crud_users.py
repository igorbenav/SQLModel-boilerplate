from fastcrud import FastCRUD

from ..models.user import User, UserCreateInternal, UserDelete, UserUpdate, UserUpdateInternal

CRUDUser = FastCRUD[User, UserCreateInternal, UserUpdate, UserUpdateInternal, UserDelete]
crud_users = CRUDUser(User)
