import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

#Query to join the test_types tables with test_summary_unified_reporting table by ID and test type ID .
# df_columbia_1h_2025 = pd.read_sql("select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12698 and tsr.test_type_id = 19;",
#                                       con=os.getenv('RSR_SVC_CONN'))


print(df_columbia_1h_2025)