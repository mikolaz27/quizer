import datetime
from time import sleep

import pandas as pd

while True:
    df = pd.DataFrame(
        data={
            "timestamp": [datetime.datetime.now(), datetime.datetime.now() - datetime.timedelta(days=2)],
            "col2": [3, 4],
        }
    )
    print(df.to_string())
    sleep(2)
