from csv import reader  

author_name = input("Введите ФИО автора: ")  

try:  
    with open('books.csv', 'r', encoding='utf-8') as r_file: 
        csv_reader = reader(r_file, delimiter=';')  
        print('Книги автора:')  

        books_found = False   
        for row in csv_reader:    
            year = row[6].strip()  
            if (year in ['2015', '2018']) and (author_name in row[4]):  
                print(row[1][1:]) 
                books_found = True  

        if not books_found:  
            print("Книги не найдены.")  

except FileNotFoundError:  
    print("Файл 'books.csv' не найден.")  
except Exception as e:  
    print(f"Произошла ошибка: {e}")
