county=False
match=False
print("county :",county)
print("match :",match)

#about irfan

irfan={"county": False,'match':False}
county=irfan['county']
match=irfan['match']
res=county or match
print("irfan is qualified for county : ",res)

#about indra

indra={"county": True,'match':False}
county=indra['county']
match=indra['match']
res=county or match
print("irfan is qualified for county : ",res)

#about rehan

rehan={"county": False,'match':True}
county=rehan['county']
match=rehan['match']
res=county or match
print("rehan is qualified for county : ",res)

#about shoiab
shoiab={"county": True,'match':True}
county=shoiab['county']
match=shoiab['match']
res=county or match
print("shoiab is qualified for county : ",res)