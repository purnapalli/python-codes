import os

def list_bad_bundles(products, folders, path_to_check):
    for product in products:
        base_path = path_to_check
        #product_path = base_path+product+"/2019.37/"
        product_path = base_path + "/" + product + "/"
        for bundle in os.listdir(product_path):
            bundle_path = product_path+bundle+"/"
            for file in os.listdir(bundle_path):
                if "readme.txt" in file:
                    f = open(bundle_path+file)
                    out = f.read()
                    versions_present = []
                    for folder in folders:
                        if folder in out:
                            versions_present.append(folder)
                    if len(versions_present) != 0:
                        print("Versions Present :", ','.join(versions_present), end=" & ")
                        print("Bundle Path :", bundle_path)
        #print("***********************************************************************************************************************************************************")
        #print()
        print(end="")


#product_names = ["Fenway","Camden","Wrigley","Busch","Morganite","Moonstone","Jasper","Citrine","Ammolite","Pearl"]
products = ['Agate']
folders_to_check = ["ljlinux_2411097.elf"]

dates = list("0"+str(i) if i < 10 else str(i) for i in range(1,30))
print(dates)
for date in dates:
    try:
        path = "//jedibdlserver.boi.rd.hpicorp.net/JediSystems/Published/DailyBuilds/RCBranches/24r/2020/08/"+date+"/Products"
        #path = "//hubbdlserver.psr.rd.hpicorp.net/JediSystems/Published/DailyBuilds/24s/2020/07/"+date+"/Products"
        list_bad_bundles(products, folders_to_check, path)
    except FileNotFoundError as e:
        print(e)
        continue

