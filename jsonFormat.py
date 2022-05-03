# coding:utf8
import json
import sys,os

def getFileCon(filename):
  if not os.path.isfile(filename):
    return

  with open(filename, "r") as f:
    con = f.read()
    f.close()
    return con

def writeFile(filepath,con):
  with open(filepath, "w") as f:
    f.write(con)
    f.close()

if __name__ == "__main__":
  fl = os.listdir(".")
  for f in fl:
    g = f
    if not f.endswith(".json"):
      continue
    try:
      con = json.loads(getFileCon(f))
      # print con
      # writeFile(f,json.dumps(con,indent=4,ensure_ascii=False).decode('utf8'))
      writeFile(f,json.dumps(con,indent=4,ensure_ascii=False))
      print (g,'OK')
    except Exception as e:
      print (g,'is not json format')