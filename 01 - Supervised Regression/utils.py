import ast
import pandas as pd
import numpy as np 
import xgboost as xgb

import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)



def count_verification_methods(x):
    x = ast.literal_eval(x)
    if x is not None:
        return len(x)
    else: 
        return 0
    
def get_nbr_bathrooms(x):
    if x is np.nan:
        return 0
    elif "half-bath" in x.lower():
        return 0.5
    else:
        return float(x.split(" ")[0])

    
def test_shared_bath(x):
    if "shared" in str(x):
        return 1
    else:
        return 0
    


def preprocess(input_file="data/listings.csv"):
    # read data
    df = pd.read_csv(input_file, low_memory=False)

    # anchor date
    todays_date = pd.to_datetime("2022-11-20")

    # clean price variable
    df['price'] = df.price.str.replace("\$|,", "", regex=True).astype("float32")

    # remove price = 0 rows
    df = df[df.price != 0]

    # log transform of the target
    df['target'] = np.log(df.price)

    # Feature enginnering numeric variables
    df['host_response_rate'] = df.host_response_rate.str.replace("%", "").astype("float32")

    df['host_acceptance_rate'] = df.host_acceptance_rate.str.replace("%", "").astype("float32")

    lkp_boolean = {"t":1, "f":0}
    df['host_is_superhost'] = df.host_is_superhost.map(lkp_boolean)
    df['instant_bookable'] = df.instant_bookable.map(lkp_boolean)
    df['shared_bathrooms'] = df.bathrooms_text.apply(test_shared_bath)
    df['nbr_bathrooms'] = df.bathrooms_text.apply(get_nbr_bathrooms)
    df['host_lives_nbh'] = (df.host_neighbourhood == df.neighbourhood_cleansed).astype("int8")

    # Feature engineering - categorical variables
    host_response_time_lkp = {'within an hour':"hour", 
                              'within a day':"one_day", 
                              'within a few hours':"few_hours", 
                              'a few days or more':"few_days"}
    df['host_response_time'] = df.host_response_time.map(host_response_time_lkp)

    df['nbr_host_verifications'] = df.host_verifications.apply(count_verification_methods)

    # handle date features
    df['days_since_host'] = (todays_date - pd.to_datetime(df.host_since)).dt.days
    df['days_since_first_review'] = (todays_date - pd.to_datetime(df.first_review)).dt.days
    df['days_since_last_review'] = (todays_date - pd.to_datetime(df.last_review)).dt.days

    # Feature list
    numeric_features = ["host_response_rate", "host_acceptance_rate", "host_is_superhost", 
                       "host_listings_count", "instant_bookable", 
                       "latitude", "longitude", "accommodates", "bedrooms", "beds", 
                        "nbr_bathrooms", "shared_bathrooms", "host_lives_nbh", 
                       "nbr_host_verifications", "days_since_host", 
                       "days_since_first_review", "days_since_last_review"]

    categorical_features = ["host_response_time", "neighbourhood_group_cleansed", 
                            "neighbourhood_cleansed", "property_type", "room_type"]
    
    target_variable = 'target'
    all_columns = [target_variable] + numeric_features + categorical_features
    df = df[all_columns]

    return df, numeric_features, categorical_features, target_variable
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





def compute_feature_importance(bst, feature_names):

    importance_data = []
    importance_data.append(pd.DataFrame({"name":feature_names}))

    importance_types = ['weight', 'gain', 'cover']
    for imp_type in importance_types:
        # Feature importance
        bst_score = bst.get_score(importance_type=imp_type)
        # Get importance
        importance = [bst_score.get("f"+str(i), 0)  for i in range(len(feature_names))]
        importance_data.append(pd.DataFrame({imp_type:importance}))


    df_importance = pd.concat(importance_data, axis=1)
    return df_importance


