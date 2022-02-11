import pandas as pd

mesh=0.05
f_cl=open('cl.csv','w',newline='')
f_cd=open('cd.csv','w',newline='')
f_cl.close()
f_cd.close()

f_history = pd.read_csv('history.csv')
f_history.columns=f_history.columns.str.replace('"','')
cl=f_history['       CL       ']
cd=f_history['       CD       ']

cl1=cl.tail(1)
cd1=cd.tail(1)
cl1=cl1.to_numpy()
cd1=cd1.to_numpy()

cl=pd.DataFrame({'CL':cl1})
cd =pd.DataFrame({'CD': cd1})

cl.to_csv('cl.csv',index=False)
cd.to_csv('cd.csv',index=False)

#new iteration
f_cl = pd.read_csv('cl.csv')
f_cl=pd.concat([f_cl,cl])
f_cl.to_csv('cl.csv',index=False)

