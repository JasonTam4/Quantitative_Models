import pandas as pd
import json
from datetime import datetime


def get_daily_change_list(value_list):
    daily_change_list = []
    for i in range(0, len(value_list)-1):
        change = int(value_list[i+1]) - int(value_list[i])
        daily_change_list.append(change)

    return daily_change_list


def get_delta_fear_and_greed(offset):
    file_path = r'Fear-&-Greed/fear_and_greed.csv'

    df = pd.read_csv(file_path, dtype={"Date": str, "Value": str, "Classification": str})
    df['Value'] = df['Value'].str.replace(',', '').astype(float)

    if offset > 0:
        indices_to_drop = range(df.index[-1], df.index[-1] - offset, -1)
    elif offset < 0:
        indices_to_drop = range(abs(offset))
    else:
        indices_to_drop = []

    #print(indices_to_drop)
    df_dropped = df.drop(index=indices_to_drop)
    #print(df_dropped)
    value_list = df_dropped['Value'].tolist()
    #print(f"fear and greed: {len(value_list)}")

    daily_change_list = get_daily_change_list(value_list)

    return daily_change_list
    


def get_delta_btc(offset):
    file_path = r'Fear-&-Greed\BTC-USD.csv'

    df = pd.read_csv(file_path, dtype={"Date": str, "Open": str,"High": str ,"Low": str, "Close": str, "Volume": str})
    df['Close'] = df['Close'].str.replace(',', '').astype(float)

    if offset > 0:
        indices_to_drop = range(offset)
    elif offset < 0:
        indices_to_drop = range(df.index[-1], df.index[-1] + offset, -1)
    else:
        indices_to_drop = []

    df_dropped = df.drop(index=indices_to_drop)
    value_list = df_dropped['Close'].tolist()
    #print(f"btc: {len(value_list)}")

    daily_change_list = get_daily_change_list(value_list)

    return daily_change_list



def main(offset):

    correlation_list = []
    for ia in range(-abs(offset), abs(offset)):
        fear_and_greed_list = get_delta_fear_and_greed(ia)
        btc_list = get_delta_btc(ia)

        num_items = 1
        if len(btc_list) == len(fear_and_greed_list):
            num_items = len(btc_list)
        
        count = 0
        for ib in range(0, num_items):
            # Comparison to see if the movement of the price of btc and the value of Fear & Greed are the same. See below for explaination of why 12
            if (fear_and_greed_list[ib] * btc_list[ib] > 0) or ((fear_and_greed_list[ib] == 0) and (btc_list[ib] < 12)):
                count += 1
        
        correlation = round(count/num_items, 4)

        print(f"For an offset of: {ia} and {num_items} items, there is a correlation of: {correlation}")
        correlation_list.append(correlation)
    
    print(f"Max correlation: {max(correlation_list)}")
    print(f"Avg correlation: {sum(correlation_list)/len(correlation_list)}")
    

"""
The parameter indicates whether we want to test for leading or lagging indicator. 
Put positive integer to test if Fear & Greed is a leading indicator by x days
"""
main(10)

"""
Why 12 bucks?
Here are some runs with different bucks:

10 bucks:
Max correlation: 0.6906
Avg correlation: 0.49946566666666664

15 bucks:
Max correlation: 0.6924
Avg correlation: 0.50085325

12 bucks:
Max correlation: 0.6911
Avg correlation: 0.5001236

12 bucks is closest to 0.5 correlation which should be the average
"""