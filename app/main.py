from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers

from app.models.User import User
from app.models.Category import Category
from app.models.FileAttachment import FileAttachment
from app.models.Note import Note
from app.auth.sign_up import router
app.include_router(router)
from app.auth.login import router
app.include_router(router)
from app.notes.manage_notes import router
app.include_router(router)
from app.notes.search_notes import router
app.include_router(router)
from app.categories.manage_categories import router
app.include_router(router)
from app.reminders.handle_scheduled_reminders import router
app.include_router(router)

# Database

from app.modassembly.database.sql.get_sql_session import Base, engine
Base.metadata.create_all(engine)
