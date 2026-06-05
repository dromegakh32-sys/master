"""
🐍 Python Training Notes (Organized Version)
📚 شرح أساسيات input و print و string و int
"""

# ======================================================
# 1️⃣ إدخال البيانات ⌨️
# ======================================================

name = input("Enter your name: ")
# 📌 إدخال نص من المستخدم وتخزينه في متغير


# ======================================================
# 2️⃣ الطباعة 🖨️
# ======================================================

# 🔹 دمج النص باستخدام +
print("hello, " + name)

# 🔹 فاصلة (تضيف مسافة تلقائياً)
print("hello,", name)

# 🔹 f-string (الأفضل ⭐)
print(f"hello, {name}")


# ======================================================
# 3️⃣ خصائص الطباعة ⚙️
# ======================================================

# 🔗 sep → تحديد الفاصل
print("أحمد", "محمد", "سارة", sep=", ")

# 🧵 end → تحديد نهاية السطر
print("مرحبا", end="!!! ")
print("كيف حالك؟")


# ======================================================
# 4️⃣ التعامل مع النصوص (str) ✏️
# ======================================================

# 🧼 حذف المسافات
name = name.strip()

# 🔠 تكبير أول حرف
name = name.capitalize()

# 🔤 تكبير أول حرف لكل كلمة
name = name.title()

# 🎯 دمج العمليات (الأفضل)
name = name.strip().title()

print(f"hello, {name}")


# ======================================================
# 5️⃣ تقسيم الاسم ✂️
# ======================================================

first, last = name.split()
# 📌 تقسيم الاسم إلى جزئين

print(f"hello, {first}")

# 🧠 ملاحظة ذكية
"""
إذا الاسم كان كلمة واحدة فقط، هذا السطر ممكن يعطي خطأ:
"""
first, last = name.split()
# ======================================================
# 6️⃣ التعامل مع الأرقام (int) 🔢
# ======================================================

x = int(input("what's x: "))
y = int(input("what's y: "))

# ➕ عملية جمع
print(x + y)


# ======================================================
# 7️⃣ دوال (Functions) ⚡
# ======================================================

# 🔹 الطريقة 1
def squared(n):
    return n * n

def main():
    x = int(input("what's x: "))
    print("x squared is", squared(x))

main()


# ======================================================
# 8️⃣ طريقة أخرى للتربيع 🔁
# ======================================================

def squared(n):
    return pow(n, 2)

def main():
    x = int(input("what's x: "))
    print(f"x squared is {squared(x)}")

main()

"""
SHORTS
visual studio code for CS50

Codes to be written in the terminal

$=تعني في الترمنال اكتب امرك هنا

ls(list)= يسمح لك بسرد كافة الملفات في مجلدك الحالي

example = ls hello.py
            ⬇
      اسم المجلد



rm = يستخدم لحذف ملف او مجلد

example = rm hello.py
            ⬇
اسم المجلد المراد حذفه



mv = يسم لك بنسخ او اعادة تسمية ملف

example1 = mv hello.py app.py (Change file name)
                         ⬇
         الاسم الجديد المراد التغيير اليه

example2 = mv hello.py myfolder/  (Transfer file to folder)
                            ⬇
             اسم المجلد المراد النقل اليه



cp = يسمحلك بنسخ ملف


example = cp hello.py copy.py
                 ⬇
ينسخ الملف (hello.py) ويصنع نسخة اسمها(copy.py)

example2 =  cp hello.py myfolder/
                   ⬇
      📁 نسخ ملف داخل مجلد


mkdir = يسمح لك لانشاء دليل وهو مجلد

example = mkdir projects
               ⬇
         ينشئ مجلد اسمه (projects)


rmdir = يسمح بحذف ملف شرط ان يكون فارغ

example = rmdir test
                ⬇
 يحذف ملف اسمه (test) شرط ان يكون فارغ


clear = يمسح الاشياء الموجودة داخل نافذة الترمنال فقط ويكت فقط بدون اي اضافة

🔴🔴🔴🔴 All commands are written in the terminal.

# 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢
⚙️انواع الرموز المستخدمة في بايثون لطرح الاسلة
   Types of text used in Python to ask questions

🟢
1 >
معناه اكبر من
Its meaning is greater than
🟢
2 >=
معناه اكبر من او يساوي
It means greater than or equal to
🟢
3 <
معناه اصغر من
It means smaller than
🟢
4 <=
معناه اصغر من او يساوي
It means less than or equal to
🟢
5 ==
تعني يساوي (للمقارنة بين قيمتين).
It means equal (to compare two values).
🟢
6 !=
تعني لا يساوي
It means not equal
🟢
7 +
تعني الجمع
The plural means
🟢
8 -
تعني الطرح
This symbol means subtraction.
🟢
9 *
تعني ضرب الارقام
It means multiplying numbers
🟢
10 /
تعني قسمة الارقام
Dividing numbers means
🔴
11 % = باقي القسمة.


🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
جميعها تكتب بعد if
All of them are written after "if".
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
"""
#عمل كود باستخدام if و الرموز الشرطية
#Create code using if and conditional characters

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")


# الكود نفسه باستخام elif
# The same code using elif

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# نفس الكود باستخدام else
# The same code using else


x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# نفس الكود باستخدام (or)اذا كنا نهتمين بمعرفة اذا ما كانت القيميتين متساويتين و بطرقة ابسط من الاول و الثاني
# The same code using OR if we are interested in knowing whether the two values ​​are equal, and in a simpler way than the first and second.
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# نفس الكود باستخدام "!=" و بطريقة ابسط
# The same code using "!=ط but in a simpler way

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# كود يحسب درجات الطلاب باستخدام "and"
# Code that calculates student grades using "and"

score=int(input("score: "))

if score>=90 and score <=100 :
    print("score: a")
elif score>=80 and score <90 :
    print("score: b")
elif score>=70 and score<80 :
    print("score: c")
elif score>=60 and score<70 :
    print("score: d")
else :
    print("score: f")


# نفس الكود لكن بطريقة ابسط
# Same code but in a simpler way


score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



# كود يبين اذا كان الرقم زوجي ام فردي
# Code that shows whether the number is even or odd
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# نفس الكود لكن بطريقة اخرى
# Same code but in a different way
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# دالة match= "match هي جملة في Python تقارن قيمة متغير مع عدة حالات محددة، وتنفذ الكود المناسب عند أول تطابق."

# 🟢 كود مثال لي دالة match
# 🟢 Example code for the match function

name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


# نفس الكود لكن بطرية ابسط
# Same code but in a simpler way

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# 🟢| = أو



"""
الفرق بين if elif else
The difference between if, elif, else
🟦if: إذا الشرط صحيح ينفذ الأمر

🟨elif: إذا الأول غلط جرّب شرط ثاني

🟥else: إذا كل الشروط غلط نفّذ هذا

🟢 تذكّر: or = "أو".

🟢 تذكّر: and = "و". يجب أن تكون جميع الشروط صحيحة.
"""











































"""
To save changes in GitHub, type the command in the terminal.

git add .
git commit -m "update hello.py"
git push

"""


