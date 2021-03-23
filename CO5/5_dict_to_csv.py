import csv

header=["place","name","age"]
with open("city.csv","w") as file:
    write=csv.DictWriter(file,fieldnames=header)
    write.writeheader()
    limit = int(input("Enter the No.of lines you want to enter:"))
    for i in range(limit):
        row_str = input("Enter the data in order (place,name,age) separated by comma:")
        row_lst = row_str.split(",")
        write.writerow({"place":row_lst[0],"name":row_lst[1],"age":row_lst[1]})
    # write.writerow({"place":"vatakara","name":"Samuel","age":21})
    # write.writerow({"place":"kainatty","name": "Aswanth", "age":21})
    # write.writerow({"place":"Tholikkode","name":"Rojin", "age":23})
    # write.writerow({"place":"Palakkaadu", "name":"Aleena","age": 13})
with open("city.csv","r") as file:
    read=csv.DictReader(file);
    for i in read:
        print(dict(i))