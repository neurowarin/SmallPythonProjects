import sqlite3

con = sqlite3.connect('Student.db')
cur = con.cursor()

cur.execute('SELECT * FROM Student')
print(cur.fetchall())

def menu():
    print("1.add")
    print("2.update")
    print("3.delete")

def enter(n):
    global con,cur
    if n==1:
        name = input("Name - ")
        surname = input("Surname - ")
        group = input("Group - ")
        university = input("University - ")
        cur.execute('INSERT INTO Student(Name,Surname,Univer,Groupe) VALUES(?,?,?,?)',(name,surname,university,group))
        con.commit()
        cur.execute('SELECT * FROM Student')
        print(cur.fetchall())
    elif n == 2:
        i = int(input("id - "))
        name = input("Name - ")
        surname = input("Surname - ")
        group = input("Group - ")
        university = input("University - ")
        cur.execute('UPDATE Student SET Name = ?, Surname = ?, Univer = ?, Groupe = ? WHERE id = ?', (name,surname,university,group,i))
        con.commit()
        cur.execute('SELECT * FROM Student')
        print(cur.fetchall())
    elif n == 3:
        ix = int(input("id - "))
        a = tuple(str(ix))
        cur.execute('DELETE FROM Student WHERE id = ?', a)
        con.commit()
        cur.execute('SELECT * FROM Student')
        print(cur.fetchall())
    else:
        print("Unknown command")

menu()
n = int(input("diya - "))
while n!=0:
    enter(n)
    n = int(input("diya - "))
con.close()
