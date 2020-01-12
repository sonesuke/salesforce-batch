from common import *

print("start")

sf = login()
contents = sf.query_all("SELECT Id, Email, FirstName, LastName FROM Contact")
df = sf_to_df(contents)
print(df)

df = pd.DataFrame({'Email': ['abc1@abc.com', 'abc2@abc.com'], 'FirstName': ['aaa1', 'aaa2'], 'LastName': ['bbb', 'bbb']})
data = df_to_sf(df)
#sf.bulk.Contact.insert(data)

print("proc1 end")