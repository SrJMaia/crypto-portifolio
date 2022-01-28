import requests
import pandas as pd

def get_fear_greed_df(size = 5):
    """
    Getting fear greed index by api
    size -- the number of days to get
    """
    response = requests.get(f"https://api.alternative.me/fng/?limit={size}&format=csv&date_format=global")    
    if response.status_code != 200:
        print(f"Fear Greed Index api error {response.status_code}.")
        return
    response = response.content.decode("utf-8").split("\n")[4:4+size]
    response = [x.split(",") for x in response]
    date = [x[0] for x in response]
    fgi_value = [x[1] for x in response]
    fgi_classfication = [x[2] for x in response]
    return pd.DataFrame(data={"date":date,"value":fgi_value,"classificaiton":fgi_classfication})