import datetime
import logging
import azure.functions as func
import pandas

import h2o
from sqlalchemy import create_engine

x=2
a=3
y=2+3


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    
    
    print(y)




