import pandas as pd
import numpy as np
from tqdm import tqdm

NUM_RECORDS = 10_000_000
NUM_CUSTOMERS = 50_000
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"

# สร้างข้อมูล
Transaction_datetime = pd.to_datetime(np.random.choice(pd.date_range(START_DATE, END_DATE), NUM_RECORDS))
Amount = np.random.randint(1001, 1001 + NUM_CUSTOMERS, NUM_RECORDS)
Customer_no = np.round(np.random.uniform(10.0, 5000.0, NUM_RECORDS), 2)

# สร้าง DataFrame และบันทึกเป็น CSV
df = pd.DataFrame({
    'Transaction_datetime': Transaction_datetime,
    'Amount': Amount,
    'Customer_no': Customer_no
})
print(f"กำลังบันทึกไฟล์...")
df.to_csv(r'D:\Panda Top Spender\large_order_data_2024.csv', index=False)

print("สร้างไฟล์ข้อมูลสำเร็จ!")