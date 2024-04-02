import BERT
import json

o = BERT.Bert()
res = o.get_query("IP Lawyer")
res_json = json.dumps(res)
print(res_json)
