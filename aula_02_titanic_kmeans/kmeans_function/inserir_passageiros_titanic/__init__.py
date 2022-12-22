import datetime
import logging
import azure.functions as func
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    # if mytimer.past_due:
    #     logging.info('The timer is past due!')

    # logging.info('Python timer trigger function ran at %s', utc_timestamp)
    try:
        df = pd.read_csv('https://raw.githubusercontent.com/maxreis86/FIEP-Machine-Learning-e-Computacao-em-Nuvem/main/aula_01_titanic_h2o_automl/titanic/dataprep_df.csv')

        engine = create_engine('postgresql://maxreis86@postgres-portal:Password#1@postgres-portal.postgres.database.azure.com:5432/postgres')
        df.to_sql('titanic', engine, if_exists='replace', index = False, method = 'multi')        

        print(pd.read_sql_query('select * from titanic', engine))
        logging.info('Passageiros inseridos com sucesso')
    except Exception as e:
        logging.info(e)
        print(e)