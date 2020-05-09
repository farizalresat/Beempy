from beem.account import Account
from beem.comment import Comment
from beem.exceptions import ContentDoesNotExistsException
username = "farizal"
account = Account(username)
c_list = {}
count = 0
f = open("hivepostlist.md",'w',encoding="utf-8")
for c in map(Comment, account.history(only_ops=["comment"])):
    if c.permlink in c_list:
      continue
    try:
         c.refresh()
    except ContentDoesNotExistsException:
         continue
    c_list[c.permlink] = 1
    if not c.is_comment():
         title = ""
         title = title.join(c.title.splitlines()) # Settled the titles with newline problem
         print(str(count) + title)
         count +=1
         f.write(str(count) + ". [" + title + "]" +
         "(" +"https://hive.blog/"+
          c.parent_permlink + "/@"+username+"/"+
           c.permlink + ")" + "\n")
f.close()
print("DONE")
