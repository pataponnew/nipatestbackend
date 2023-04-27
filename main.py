from pydoc import describe
from typing import Union,Optional
from fastapi import FastAPI
from pydantic import BaseModel
from service.TicketService import TicketService
from helper.ErrException import ErrException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://10.10.10.59:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CreateTicket(BaseModel):
    title: str
    description: str
    contactInformation: str

class UpdateTicket(BaseModel):
    Id: int
    status: str

@app.post("/addticket")
def add(ticket:CreateTicket):
    ticket_dict = ticket.dict()
    try:
        result = TicketService().createTicket(ticket_dict)
    except ErrException as error:
        result = {'responsecode':int(error.code), 'status':'failed', 'messages':error.msg}
    return result

@app.get("/status")
def select(status:str):
    try:
        result = TicketService().selectTicket(status)
    except ErrException as error:
        result = {'responsecode':int(error.code), 'status':'failed', 'messages':error.msg}
    return result

@app.post("/updateStatus")
def update(data:UpdateTicket):
    data = data.dict()
    try:
        result = TicketService().updateTicket(data)
    except ErrException as error:
        result = {'responsecode':int(error.code), 'status':'failed', 'messages':error.msg}
    return result