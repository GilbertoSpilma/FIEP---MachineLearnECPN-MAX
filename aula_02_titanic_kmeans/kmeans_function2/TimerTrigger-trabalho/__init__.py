import datetime
import logging

import azure.functions as func

#versão2
x=2
a=3
y=2+3
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')
        print(y)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    print(y)