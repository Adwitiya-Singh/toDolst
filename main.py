
from database import *


data = jsonread("sample_template.json", "sample_request.json")
datatwo = jsonread("sample_template.json", "sample_request_two.json")
# deleteall()
create_table()
insert(data)
insert(datatwo)
# showall_incomp()
showall()
# mark_complete(2)
# showall_incomp()
# with open('responseOther.json', 'w') as outfile:
#     json.dump(data, outfile, indent='\t')


