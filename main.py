import uvicorn
from fastapi import FastAPI

import models
from database import engine
from routers import blog, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
