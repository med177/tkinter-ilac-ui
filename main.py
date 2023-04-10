import sqlite3
import tkinter as tk
from tkinter import ttk

# Tkinter uygulaması oluştur
root = tk.Tk()
root.geometry("600x400")
root.title("Arayüz Örneği")

# Sol tarafta Listbox ve Search Bar
left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=10, pady=10)

# Listbox
listbox = tk.Listbox(left_frame, height=10, width=20)
listbox.pack(side="top", pady=10)

# Search Bar
search_bar = tk.Frame(left_frame)
search_bar.pack(side="top", pady=10)

search_entry = tk.Entry(search_bar)
search_entry.pack(side="left", padx=5)

search_button = tk.Button(search_bar, text="Ara")
search_button.pack(side="left", padx=5)

# Orta kısımdaki panel ve etiketler
middle_frame = tk.Frame(root)
middle_frame.pack(side="left", padx=10, pady=10)

label1 = ttk.Label(middle_frame, text="Etiket 1")
label1.grid(row=0, column=0, padx=5, pady=5, sticky="W")

entry1 = ttk.Entry(middle_frame, width=20)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = ttk.Label(middle_frame, text="Etiket 2")
label2.grid(row=1, column=0, padx=5, pady=5, sticky="W")

entry2 = ttk.Entry(middle_frame, width=20)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3 = ttk.Label(middle_frame, text="Etiket 3")
label3.grid(row=2, column=0, padx=5, pady=5, sticky="W")

entry3 = ttk.Entry(middle_frame, width=20)
entry3.grid(row=2, column=1, padx=5, pady=5)

label4 = ttk.Label(middle_frame, text="Etiket 4")
label4.grid(row=3, column=0, padx=5, pady=5, sticky="W")

entry4 = ttk.Entry(middle_frame, width=20)
entry4.grid(row=3, column=1, padx=5, pady=5)

label5 = ttk.Label(middle_frame, text="Etiket 5")
label5.grid(row=4, column=0, padx=5, pady=5, sticky="W")

entry5 = ttk.Entry(middle_frame, width=20)
entry5.grid(row=4, column=1, padx=5, pady=5)

label6 = ttk.Label(middle_frame, text="Etiket 6")
label6.grid(row=5, column=0, padx=5, pady=5, sticky="W")

entry6 = ttk.Entry(middle_frame, width=20)
entry6.grid(row=5, column=1, padx=5, pady=5)

# Sağdaki PictureBox ve etiketler
right_frame = tk.Frame(root)
right_frame.pack(side="left", padx=10, pady=10)

image_label = ttk.Label(right_frame, text="PictureBox")
image_label.pack(padx=5, pady=5)

image_frame = tk.Frame(right_frame)
image_frame.pack(padx=5, pady=5)

image = tk.PhotoImage(file="images/resim.png")  # resmin yolu burada belirtilir
picture_box = tk.Label(image_frame, image=image)
picture_box.pack()

label7 = ttk.Label(right_frame, text="Etiket 7")
label7.pack(pady=5)

entry7 = ttk.Entry(right_frame, width=20)
entry7.pack(pady=5)

label8 = ttk.Label(right_frame, text="Etiket 8")
label8.pack(pady=5)

entry8 = ttk.Entry(right_frame, width=20)
entry8.pack(pady=5)

# Veritabanı bağlantısı oluştur
conn = sqlite3.connect('db/rxsample.db')
cursor = conn.cursor()


def search():
    # Listbox içeriğini temizle
    listbox.delete(0, tk.END)

    # Arama sorgusunu hazırla
    search_term = search_entry.get()
    query = f"SELECT * FROM ILACLAR WHERE ILAC_ADI LIKE '%{search_term}%'"

    # Sorguyu çalıştır ve sonuçları listbox'a yerleştir
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        listbox.insert(tk.END, row[1])  # İlaç ismini listbox'a ekle


# Ara butonuna tıklandığında search() fonksiyonunu çalıştır
search_button.config(command=search)


root.mainloop()
