import random
import tkinter as tk
from tkinter import ttk
import time

def bucket_sort(arr):
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    output_text.delete("1.0", tk.END)  # Limpa a área de texto

    output_text.insert(tk.END, "Lista não ordenada:\n")
    output_text.insert(tk.END, str(arr) + "\n")

    for num in arr:
        index = num // 10
        buckets[index].append(num)
        output_text.insert(tk.END, f"Adicionando {num} ao balde {index+1} => {buckets}\n")
        root.update()
        time.sleep(1)

    sorted_arr = []
    for bucket in buckets:
        bucket.sort()
        sorted_arr.extend(bucket)
        output_text.insert(tk.END, f"Ordenando o balde {bucket} => {sorted_arr}\n")
        root.update()
        time.sleep(1)

    output_text.insert(tk.END, "Lista ordenada:\n")
    output_text.insert(tk.END, str(sorted_arr) + "\n")

    return sorted_arr

def sort_button_click():
    input_numbers = input_entry.get()
    try:
        numbers = [int(x) for x in input_numbers.split(",")]
        sorted_numbers = bucket_sort(numbers)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Erro: Insira números separados por vírgula.")
        return

root = tk.Tk()
root.title("Bucket Sort Visualizer")
root.geometry("600x500")  # Define o tamanho da janela

frame = ttk.Frame(root)
frame.grid(column=0, row=0)

input_label = ttk.Label(frame, text="Insira números separados por vírgula:")
input_label.grid(column=0, row=0, padx=10, pady=10)

input_entry = ttk.Entry(frame)
input_entry.grid(column=1, row=0, padx=10, pady=10)

sort_button = ttk.Button(frame, text="Ordenar", command=sort_button_click)
sort_button.grid(column=2, row=0, padx=10, pady=10)

output_text = tk.Text(frame, wrap=tk.WORD, width=50, height=20)  # Aumenta o tamanho da área de texto
output_text.grid(column=0, row=1, columnspan=3, padx=10, pady=10)

root.mainloop()
