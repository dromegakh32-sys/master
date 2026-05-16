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

Information






"""
To save changes in GitHub, type the command in the terminal.

git add .
git commit -m "update hello.py"
git push

"""


