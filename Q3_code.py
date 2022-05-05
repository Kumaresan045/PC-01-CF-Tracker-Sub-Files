import json
import urllib.request
import time

user_URL = "https://codeforces.com/api/user.status?handle=Kumaresan03&from=1&count=1000"
with urllib.request.urlopen(user_URL) as url:
    user_data = json.loads(url.read().decode())
d_tag={}
pcount=0
tresh_time=time.time()-24*60*60*10
for sub in user_data["result"]:
    if sub["creationTimeSeconds"] >= tresh_time:
        pcount+=1
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
