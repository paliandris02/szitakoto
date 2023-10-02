import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm

def Estimate(data):
    raw_scraped_data = pd.read_excel("src/revel/data.xlsx")
    raw_scraped_data=raw_scraped_data.drop(columns=['Unnamed: 0','property_id','property_url','desc','price_in_eur','lang','listing_type','page_num','max_page','max_listing','timestamp'])
    raw_scraped_data.columns
    Y = pd.DataFrame()
    Y['price_in_huf'] = raw_scraped_data['price_in_huf']
    Y['price_in_huf'] = Y['price_in_huf'].str[:-3].str.replace(" ","").apply(int)
    X = raw_scraped_data[['area_size', 'condition_of_real_estate', 'city_district']]# 'floors','building_material', 'type_of_heating', 'condition_of_real_estate','year_built', 'ground_area_size', 'property_type', 'convenience_level','orientation', 'ownership_status', 'furnished']]
    X['area_size'] = X['area_size'].str.replace("square meter","").str.replace(" ","").apply(int)
    
   # categorical_vars = ['city_district', 'building_material', 'type_of_heating', 'condition_of_real_estate','property_type', 'convenience_level', 'orientation', 'ownership_status', 'furnished']

    
    X_dummies = pd.get_dummies(X, columns=['condition_of_real_estate', 'city_district'])

    raw_scraped_data['condition_of_real_estate'].value_counts()
    
   # X = X_dummies.iloc[:, :7]
    X = X_dummies
    X = sm.add_constant(X)
    
    model = sm.OLS(Y, X).fit()

    model.summary()    
    
    new_data = pd.DataFrame(columns=X.columns)
    
    new_data = new_data.drop(columns=['const'])
    
    new_row = {"const": 1,'area_size': 25, 'condition_of_real_estate_Average': 0, 'condition_of_real_estate_Building in progress': 0
               , 'condition_of_real_estate_Excellent': 0, 'condition_of_real_estate_Good': 0
               , 'condition_of_real_estate_Renovated': 0
               , 'condition_of_real_estate_Structurally complete': 0
               , 'condition_of_real_estate_To be renovated': 1
               #, 'city_district_Budapest, District I': 0
               ,'city_district_Budapest, District II': 0, 'city_district_Budapest, District III': 0,
               'city_district_Budapest, District IV': 0, 'city_district_Budapest, District V': 0, 'city_district_Budapest, District VI': 0,
               'city_district_Budapest, District VII': 0, 'city_district_Budapest, District VIII': 0, 'city_district_Budapest, District IX': 0,
               'city_district_Budapest, District X': 0, 'city_district_Budapest, District XI': 0, 'city_district_Budapest, District XII': 0
               , 'city_district_Budapest, District XIII': 0, 'city_district_Budapest, District XIV': 0, 'city_district_Budapest, District XV': 1
               , 'city_district_Budapest, District XVI': 0, 'city_district_Budapest, District XVII': 0, 'city_district_Budapest, District XVIII': 0
               , 'city_district_Budapest, District XIX': 0, 'city_district_Budapest, District XX': 0, 'city_district_Budapest, District XXI': 0
               , 'city_district_Budapest, District XXII': 0, 'city_district_Budapest, District XXIII': 0
    }

#    new_row = {'const': 1,'area_size': 100, 'condition_of_real_estate_Average': 1, 'condition_of_real_estate_Building in progress': 0
#               , 'condition_of_real_estate_Excellent': 0, 'condition_of_real_estate_Good': 0
#               , 'condition_of_real_estate_Renovated': 0
#               , 'condition_of_real_estate_Structurally complete': 0
#               , 'condition_of_real_estate_To be renovated': 0
#               }
    
    new_data = new_data.append(new_row,ignore_index=True)
    new_data = sm.add_constant(new_data)
    model.predict(new_data)
    
    return data
