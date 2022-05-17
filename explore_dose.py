from nferx_sdk.data_sources import SparkSQLAPI

sp = SparkSQLAPI(debug=True,data_version='MayoCDAPDev')

drug_name = "propranolol"

df_order_dose_amount_count = sp.query(f"""select cast(order_dose_amount as decimal(9,2)), count(*) as value 
from  fact_orders where drug_names like ("%{drug_name}%") group by order_dose_amount order 
by value DESC""")

df_order_dose_amount_count

df_order_frequency = sp.query(f"""select order_frequency, count(*) as value 
from  fact_orders where drug_names like ("%{drug_name}%") group by order_frequency order 
by value DESC""")

df_order_frequency
