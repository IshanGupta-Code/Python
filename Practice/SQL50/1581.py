# Customer Who Visited but Did Not Make Any Transactions
import pandas as pd

visits  = {
	'visit_id' : [1,2,4,5,6,7,8],
	'customer_id' : [23,9,30,54,96,54,54]
} 

Transactions = {
    'transaction_id' : [2,3,9,12,13],
    'visit_id' : [5,5,5,1,2],
    'amount' : [310,300,200,910,970]
}

visits = pd.DataFrame(visits)
transactions = pd.DataFrame(Transactions)

def find_customers(visits: pd.DataFrame, transactions : pd.DataFrame):
	df = visits.merge(transactions, how='left')
	df = df[df['transaction_id'].isna()].groupby(['customer_id'], as_index=False).agg(count_no_trans = ('visit_id', 'nunique')).sort_values(by='count_no_trans', ascending=True)
	print(df) 

find_customers(visits, transactions)