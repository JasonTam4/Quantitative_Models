from matplotlib import pyplot as plt
import pandas as pd
import json
from datetime import datetime
"""
Hypothesis: 
Fear to greed index is either a lagging or leading indicator

Method: 
Find the change in price of bitcoin each day and compare it to the change in value of the fear to greed index each day. See if there is a relation

Result:
Trailing 1 day had a 0.64 correlation. Leading 1 day had a 0.41 correlation. Basically, not that useful
"""

def main():
    fear_and_greed_list = delta_fear_and_greed()
    btc_list = delta_btc()

    count = 0
    for i in range(0, 28):
        if fear_and_greed_list[i] * btc_list[i] > 0:
            count += 1
    
    correlation = count/29

    print(correlation)



def delta_fear_and_greed():
    file_path = 'Fear-&-Greed-Graph/fear_&_greed_data.json'

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Convert the JSON data into a DataFrame
    df = pd.DataFrame(data['data'])

    timestamp_list = df['timestamp'].tolist()
    value_list = df['value'].tolist()
    print(f"greed: {len(value_list)}")

    value_daily_change_list = []

    for i in range(0, len(value_list)-1):
        change = int(value_list[i+1]) - int(value_list[i])
        value_daily_change_list.append(change)


    value_list = df['timestamp'].tolist()
    for i in range(0, len(value_list)-1):
        dt_object = datetime.utcfromtimestamp(int(value_list[i]))

        # Print the datetime object
        print(dt_object)




    return value_daily_change_list
    #print(len(timestamp_list))
    #print(len(value_list))
    #print(df)
    #plt.plot(timestamp_list, value_list, color="navy")
    #plt.show()

    #print(df)
    # find daily change of btc and compare to crypto fear index



def delta_btc():
    file_path = 'Fear-&-Greed-Graph/Bitcoin Historical Data.csv'

    df = pd.read_csv(file_path, dtype={"Date": str, "Price": str, "Open": str,"High": str ,"Low": str, "Vol.": str, "Change %": str})

    df['Price'] = df['Price'].str.replace(',', '').astype(float)
    value_list = df['Price'].tolist()
    print(f"btc: {len(value_list)}")

    value_daily_change_list = []

    for i in range(0, len(value_list)-1):
        change = value_list[i+1] - value_list[i]
        value_daily_change_list.append(change)

    return value_daily_change_list

    

main()