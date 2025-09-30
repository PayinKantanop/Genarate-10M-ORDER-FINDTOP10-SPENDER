import pandas as pd
import time

def topspenderFinding(path_input=r'D:\Panda Top Spender\large_order_data_2024.csv',path_output=r'D:\Panda Top Spender\top10spender_month.csv'):
    start_time = time.time()
    sales_df = pd.read_csv(
        path_input,
        parse_dates=['Transaction_datetime'],
        dtype={'Amount': 'float32', 'Customer_no':'object'}
    )
    print(f"โหลดข้อมูล {len(sales_df):,} records สำเร็จใน {time.time() - start_time:.2f} วินาที")
    sales_df['Month'] = sales_df['Transaction_datetime'].dt.to_period('M')
    monthly_customer_spend = sales_df.groupby(['Month', 'Customer_no'])['Amount'].sum()
    top_spenders = monthly_customer_spend.groupby(level='Month', group_keys=False).nlargest(10)
    top_spenders_df = top_spenders.reset_index()
    top_spenders_df.to_csv(path_output, index=False)

    return top_spenders_df

if __name__ == '__main__':
    top_spenders_result = topspenderFinding()
    print("\n--- ตัวอย่างผลลัพธ์ Top Spenders ---")
    print(top_spenders_result.head(20))

    

    