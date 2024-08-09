import os
from dotenv import load_dotenv
import vanna
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp


load_dotenv()


vn = VannaDefault(model='chinook', api_key=os.getenv("vanna_api_key"))
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')


VannaFlaskApp(vn).run()