from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    # describe column headers and the data type
    at.Table1.custom.cols = [
        { "field": "id", "headerName": "ID" },
        { "field": "firstName", "headerName": "First name" },
        { "field": "lastName", "headerName": "Last name" },
        { "field": "age", "headerName": "Age", "type": "number" }
        ]

    # add rows
    at.Table1.custom.rows = [
        { "id": 1, "lastName": "Snow", "firstName": "Jon", "age": 35 },
        { "id": 2, "lastName": "Lannister", "firstName": "Cersei", "age": 42 },
        { "id": 3, "lastName": "Lannister", "firstName": "Jaime", "age": 45 },
        { "id": 4, "lastName": "Stark", "firstName": "Arya", "age": 16 },
        { "id": 5, "lastName": "Targaryen", "firstName": "Daenerys", "age": None },
    ]

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass