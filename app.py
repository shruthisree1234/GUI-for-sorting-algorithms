import tkinter as tk
import time
from compare_module import *
from sort_module import *

arr=[]

def getArray(arr):
    text2.delete(1.0, "end-1c")
    text3.delete(1.0, "end-1c")
    arr.clear()
    arr.extend(list(map(int,(text1.get(1.0, "end-1c")).split(","))))

def displayText():
    if(arr!=[]):
        text2.insert('end-1c', str(arr))

def bSort(arr):
    getArray(arr)
    start_time = time.perf_counter ()
    bubbleSort(arr)
    tot_time= time.perf_counter () - start_time
    details_str="SIZE OF ARRAY : "+str(len(arr))+"\nBUBBLE SORT"+"\nTIME TAKEN : "+str(tot_time)+"s\nTIME COMPLEXITY : O(n^2)"
    text3.insert('end-1c', details_str)
    displayText()

def iSort(arr):
    getArray(arr)
    start_time = time.perf_counter ()
    insertionSort(arr)
    tot_time= time.perf_counter () - start_time
    details_str="SIZE OF ARRAY : "+str(len(arr))+"\nINSERTION SORT"+"\nTIME TAKEN : "+str(tot_time)+"s\nTIME COMPLEXITY : O(n^2)"
    text3.insert('end-1c', details_str)
    displayText()

def sSort(arr):
    getArray(arr)
    start_time = time.perf_counter ()
    selectionSort(arr)
    tot_time= time.perf_counter () - start_time
    details_str="SIZE OF ARRAY : "+str(len(arr))+"\nSELECTION SORT"+"\nTIME TAKEN : "+str(tot_time)+"s\nTIME COMPLEXITY : O(n^2)"
    text3.insert('end-1c', details_str)
    displayText()

def qSort(arr):
    getArray(arr)
    start_time = time.perf_counter ()
    quickSort(arr,0,len(arr)-1)
    tot_time= time.perf_counter () - start_time
    details_str="SIZE OF ARRAY : "+str(len(arr))+"\nQUICK SORT"+"\nTIME TAKEN : "+str(tot_time)+"s\nTIME COMPLEXITY : O(n^2)"
    text3.insert('end-1c', details_str)
    displayText()

def qSortThreeWay(arr):
    getArray(arr)
    start_time = time.perf_counter ()
    quickSortThreeWay(arr,0,len(arr)-1)
    tot_time= time.perf_counter () - start_time
    details_str="SIZE OF ARRAY : "+str(len(arr))+"\nTHREE WAY QUICK SORT"+"\nTIME TAKEN : "+str(tot_time)+"s\nTIME COMPLEXITY : O(n^2)"
    text3.insert('end-1c', details_str)
    displayText()

def mSort(arr):
    getArray(arr)
    start_time = time.perf_counter ()
    mergeSort(arr)
    tot_time= time.perf_counter () - start_time
    details_str="SIZE OF ARRAY : "+str(len(arr))+"\nMERGE SORT"+"\nTIME TAKEN : "+str(tot_time)+"s\nTIME COMPLEXITY : O(nlogn)"
    text3.insert('end-1c', details_str)
    displayText()

def hSort(arr):
    getArray(arr)
    start_time = time.perf_counter ()
    heapSort(arr)
    tot_time= time.perf_counter () - start_time
    details_str="SIZE OF ARRAY : "+str(len(arr))+"\nHEAP SORT"+"\nTIME TAKEN : "+str(tot_time)+"s\nTIME COMPLEXITY : O(nlogn)"
    text3.insert('end-1c', details_str)
    displayText()

def compCall():
    compare(int(text4.get(1.0, "end-1c")),int(text5.get(1.0, "end-1c")))

master=tk.Tk()

master.attributes('-fullscreen', True)

master.title("SORTING ALGORITHMS & IT'S COMPARISON")

canvas=tk.Canvas(master,bg="black")
canvas.place(relheight=1, relwidth=1)

frame=tk.Frame(master, bg="#ff6600")

frame.place(relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1)

title=tk.Label(frame, text = "SORTING ALGORITHMS", fg = "black", bg = "#ff6600", font = ("Gill Sans MT",30))
title.place(relx=0.3, rely=0.05)

label1=tk.Label(frame, text = "INPUT ARRAY :",  padx = 10, pady = 10, fg = "black", bg = "#ff6600", font = ("Gill Sans MT",12))
label1.place(relx=0.1, rely=0.2)

text1=tk.Text(frame, height = 1, width = 40, padx = 10, pady= 10, bg = "black", fg = "#ff6600", font = ("Gill Sans MT",10))
text1.place(relx=0.1, rely = 0.3)

label2=tk.Label(frame, text = "SORTED ARRAY :",  padx = 10, pady = 10, fg = "black", bg = "#ff6600", font = ("Gill Sans MT",12))
label2.place(relx=0.1, rely=0.4)

text2=tk.Text(frame, height = 1, width = 40, padx = 10, pady = 10, bg = "white", fg = "black", font = ("Gill Sans MT",10))
text2.place(relx=0.1, rely=0.5)

label3=tk.Label(frame, text = "SORTING DESCRIPTION :",  padx = 10, pady = 10, fg = "black", bg = "#ff6600", font = ("Gill Sans MT",12))
label3.place(relx=0.1, rely=0.6)

text3=tk.Text(frame, height = 4, width = 40, padx = 10, pady = 10, bg = "white", fg = "black", font = ("Gill Sans MT",10))
text3.place(relx=0.1, rely=0.7)

bsort=tk.Button(frame, text = "BUBBLE SORT", width = 20, padx = 20, pady = 10, bg = "black", fg = "#ff6600", command  = lambda: bSort(arr), font = ("Gill Sans MT",10))
bsort.place(rely=0.2, relx=0.4)

isort=tk.Button(frame, text = "INSERTION SORT", width = 20, padx = 20, pady = 10, bg = "black", fg = "#ff6600", command = lambda: iSort(arr), font = ("Gill Sans MT",10))
isort.place(rely=0.3, relx=0.4)

ssort=tk.Button(frame, text = "SELECTION SORT", width = 20, padx = 20, pady = 10, bg = "black", fg = "#ff6600", command = lambda: sSort(arr), font = ("Gill Sans MT",10))
ssort.place(rely=0.4, relx=0.4)

qsort=tk.Button(frame, text = "QUICK SORT", width = 20, padx = 20, pady = 10, bg = "black", fg = "#ff6600", command = lambda: qSort(arr), font = ("Gill Sans MT",10))
qsort.place(rely=0.5, relx=0.4)

qtsort=tk.Button(frame, text = "3 WAY QUICK  SORT", width = 20, padx = 20, pady = 10, bg = "black", fg = "#ff6600", command = lambda: qSortThreeWay(arr), font = ("Gill Sans MT",10))
qtsort.place(rely=0.6, relx=0.4)

msort=tk.Button(frame, text = "MERGE SORT", width = 20, padx = 20, pady = 10, bg = "black", fg = "#ff6600", command = lambda: mSort(arr), font = ("Gill Sans MT",10))
msort.place(rely=0.7, relx=0.4)

hsort=tk.Button(frame, text = "HEAP SORT", width = 20, padx = 20, pady = 10, bg = "black", fg = "#ff6600", command = lambda: hSort(arr), font = ("Gill Sans MT",10))
hsort.place(rely=0.8, relx=0.4)

label4=tk.Label(frame, text = "MINIMUM SIZE :",  padx = 10, pady = 10, fg = "black", bg = "#ff6600", font = ("Gill Sans MT",12))
label4.place(relx=0.6, rely=0.45)

label5=tk.Label(frame, text = "MAXIMUM SIZE :",  padx = 10, pady = 10, fg = "black", bg = "#ff6600", font = ("Gill Sans MT",12))
label5.place(relx=0.8, rely=0.45)

label6=tk.Label(frame, text = "COMPARISON OF DURATION OF DIFFERENT\nALGORITHMS FOR SORTING ARRAYS OF DIFFERENT SIZES",  padx = 10, pady = 10, fg = "black", bg = "#ff6600", font = ("Gill Sans MT",12), justify = "center")
label6.place(relx=0.5875, rely=0.35)

text4=tk.Text(frame, height = 1, width = 20, padx = 10, pady = 10, bg = "black", fg = "#ff6600", font = ("Gill Sans MT",10))
text4.place(relx=0.6, rely=0.55)

text5=tk.Text(frame, height = 1, width = 20, padx = 10, pady = 10, bg = "black", fg = "#ff6600", font = ("Gill Sans MT",10))
text5.place(relx=0.8, rely=0.55)

comp=tk.Button(frame, text = "COMPARE", width = 20, padx = 20, pady = 10, bg = "white", fg = "#ff6600", command = compCall, font = ("Gill Sans MT",10))
comp.place(rely=0.65, relx=0.7)

master.mainloop()