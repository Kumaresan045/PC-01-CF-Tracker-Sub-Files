import json
import urllib.request
import time

user_URL = "https://codeforces.com/api/user.status?handle=Kira_1234&from=1&count=10000"
try:
    with urllib.request.urlopen(user_URL) as url:
        user_data = json.loads(url.read().decode())
    d_tag={}
    l_prob=[]
    pcount=0
    tresh_time=time.time()-24*60*60*100
    for sub in user_data["result"]:
        if (sub["verdict"]=="OK" or sub["verdict"]=="PARTIAL") and sub["problem"]["name"] not in l_prob and sub["creationTimeSeconds"] >= tresh_time:
            pcount+=1
            l_prob.append(sub["problem"]["name"])
            Tags=sub["problem"]["tags"]
            for t in Tags:
                if t in d_tag:
                    d_tag[t]+=1
                else:
                    d_tag[t]=1
    Tags=[]
    Max=max(d_tag.values())
    for x in d_tag:
        if d_tag[x]==Max:
            Tags.append(x)
    print("No. of Problems solved:",pcount)
    print("Most Solved Tags:",Tags)
except:
    print("Oopsies couldnt connect API!!\nMaybe Codeforces site is down.")
