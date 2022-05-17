from nferx_sdk.data_sources import SparkSQLAPI

sp = SparkSQLAPI(debug=True,data_version='MayoCDAPDev')

drug_name = "propranolol"

df_out = sp.query(f"""select cast(order_dose_amount as decimal(9,2)), count(*) as value 
from  fact_orders where drug_names like ("%{drug_name}%") group by order_dose_amount order 
by value DESC""")
