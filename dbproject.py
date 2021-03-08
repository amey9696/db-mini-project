import sqlite3 as sql
con=sql.connect("product.db")
cur=con.cursor()
# cur.execute("create table product(pid integer,pname text,pcost integer)")
# print("table is created")
# cur.execute("insert into product values(1121,'Laptop',45000)")
# cur.execute("insert into product values(1123,'Keyboard',600)")
# cur.execute("insert into product values(2231,'Pendrive',1250)")
# cur.execute("insert into product values(3212,'Harddisk',5600)")
# con.commit()
print("1.Search")
print("2.Buy")
ch=int(input("enter ur choice:"))
if ch==1:
    print("1. Search By id")
    print("2.Search by Name")
    ch2=int(input("enter ur choice:"))
    if ch2==1:
        pid=int(input("Enter the product id you want:"))
        if pid>=1 or pid<=5:
            cur.execute("select * from product where pid=?",(pid,))
            res=cur.fetchall()
            for i in res:
                for j in i:
                    print()
                print("Product id is:",i[0])
                print("product name is:",i[1])
                print("Product cost is:",i[2])
                # q=int(input("enter quanity:"))
                # bill=q*i[2]
                # print("bill amount is:",bill)
        else:
            print("product is not available")
    elif ch2==2:
        pname=input("Enter product name:")
        pname=pname.title() #convert into Sentence Case i.e if user enter LAPTOP or laptop then it convert into Laptop
        cur.execute("select * from product where pname=? ",(pname,))
        res = cur.fetchall()
        for i in res:
            for j in i:
                print()
            print("Product id is:", i[0])
            print("product name is:", i[1])
            print("Product cost is:", i[2])
elif ch==2:
    cur.execute("select * from product")
    res = cur.fetchall()
    print("id\t\tName\t\tPrice")
    print("------\t------\t-------")
    for i in res:
        for j in i:
            print(j,end="\t")
        print()
    pname = input("Enter product name to buy:")
    pname = pname.title()
    cur.execute("select * from product where pname=? ", (pname,))
    res = cur.fetchall()
    for i in res:
        for j in i:
            print()
        print("product name is:", i[1])
        print("Product cost is:", i[2])
        q = int(input("enter quanity:"))
        bill=q*i[2]
        print("bill amount is:",bill)
else:
    print("wrong choice")
con.close()