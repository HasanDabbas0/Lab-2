from csv import reader  

# فتح ملف الإخراج في وضع الكتابة  
with open('3.txt', 'w') as output:  
    # فتح ملف البيانات 'books-en.csv' للقراءة  
    with open('books-en.csv', 'r') as r_file:  
        file = reader(r_file, delimiter=';')  
      
        # استخدام enumerate لعد الصفوف  
        for k, row in enumerate(file):  
            # تخطي الصف الأول (رؤوس الأعمدة) إذا كان موجودًا  
            if k == 0:  
                continue  

            # كتابة الصفوف من 1 إلى 20 في الملف النصي  
            if 1 <= k <= 20:  
                output.write(f"{k}. {row[2]}. {row[1]} - {row[3]} \n")
