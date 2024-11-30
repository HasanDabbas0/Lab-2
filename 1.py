from csv import reader  

def count_long_titles(file_path, title_length_threshold):  
    try:  
        count = 0  
        with open(file_path, 'r', encoding='utf-8') as r_file:  
            csv_reader = reader(r_file, delimiter=';')  
            for row in csv_reader:  
                # تحقق مما إذا كان الصف يحتوي على عنوان (العمود الثاني)  
                if len(row) > 1 and len(row[1]) > title_length_threshold:  
                    count += 1   
        return count  
    except FileNotFoundError:  
        print("لا يمكن العثور على الملف. تأكد من أن المسار صحيح.")  
        return None  
    except Exception as e:  
        print(f"حدث خطأ: {e}")  
        return None  

# تحديد المسار إلى ملف CSV  
file_path = 'books-en.csv'  
title_length_threshold = 30  

# استدعاء الدالة لطباعة النتيجة  
result = count_long_titles(file_path, title_length_threshold)  
if result is not None:  
    print(f'عدد الكتب التي تحتوي على عناوين تزيد عن {title_length_threshold} حرفًا: {result}')
