import json
agg_data=[]
comp_profit={}
avg={}
with open('task7.txt','r') as r:
    with open('task7_w.json','w') as w:
        avg_profit=0
        num_comp=0
        for i in r.readlines():
            num_comp += 1
            company,ownship,revenue,expences=i.rstrip().split('   ')#не работает через \t
            profit=int(revenue)-int(expences)
            if profit>0:
                avg_profit+=profit
                comp_profit[company]=profit
        avg['average_profit']=avg_profit//num_comp
        agg_data.append(comp_profit)
        agg_data.append(avg)
        json.dump(agg_data,w)









