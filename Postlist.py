from beem.account import Account
from beem.comment import Comment
from beem.exceptions import ContentDoesNotExistsException
username = "farizal"
account = Account(username)
c_list = {}
count = 1
f = open("test.txt",'w',encoding="utf-8")
for c in map(Comment, account.history(only_ops=["comment"])):
    if c.permlink in c_list:
      continue
    try:
         c.refresh()
    except ContentDoesNotExistsException:
         continue
    c_list[c.permlink] = 1
    if not c.is_comment():
        print("%d " % count)
        count +=1
        f.write("[" + c.title + "]" + "(" +"https://steemit.com/"+ c.parent_permlink + "/@"+username+"/"+ c.permlink + ")" + "\n")
f.close()
print("DONE")