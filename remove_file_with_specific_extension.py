import os
test = os.listdir("./filepath")
for item in test:
    if item.endswith("extension"):#extension like (.py  .java  .class)
        os.remove(os.path.join("./filepath", item))
        print("sucessfully deleted.....")
