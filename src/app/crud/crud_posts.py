from fastcrud import FastCRUD

from ..models.post import Post, PostCreateInternal, PostDelete, PostUpdate, PostUpdateInternal

CRUDPost = FastCRUD[Post, PostCreateInternal, PostUpdate, PostUpdateInternal, PostDelete]
crud_posts = CRUDPost(Post)
