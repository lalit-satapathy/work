import json
import glob
import os

cnt = 0
all_files = []
for fds in glob.glob("**/kibana/**/*.json",recursive=True):
 cnt +=1
 all_files.append(fds)
print("Run from integration repo: main/integrations/packages") 
print("Total kibana json files:",cnt) 

matches = 0
out_file = open("out.csv","w")
for f in sorted(all_files):
  fh = open(f)
  top_data = json.load(fh)
  if "attributes" in top_data:
    if "title" in top_data["attributes"] and "type" in top_data :
      if top_data["type"] == "dashboard":
        package_name = f.split("/")[0]
        print(package_name,top_data["attributes"]["title"])
        out_str = package_name + "," + top_data["attributes"]["title"]
        print(out_str,file=out_file)    
        matches +=1
out_file.close()
print("output file: out.csv", " matched dashboard files:",matches)