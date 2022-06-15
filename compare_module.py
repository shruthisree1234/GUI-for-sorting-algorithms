import time
import random
import matplotlib.pyplot as plt
from sort_module import *

def compare(m, n):  
    b_arr=[]
    s_arr=[]
    i_arr=[]
    qt_arr=[]
    q_arr=[]
    h_arr=[]
    m_arr=[]

    for i in range(m,n):
        A=random.sample(range(-1000,1000),i)

        arr=A.copy()
        bstart_time = time.perf_counter ()
        bubbleSort(arr)
        bubble_time = time.perf_counter () - bstart_time

        arr=A.copy()
        sstart_time = time.perf_counter ()
        selectionSort(arr)
        select_time = time.perf_counter () - sstart_time

        arr=A.copy()
        istart_time = time.perf_counter ()
        insertionSort(arr)
        insert_time = time.perf_counter () - istart_time

        arr=A.copy()
        qtstart_time = time.perf_counter ()
        quickSortThreeWay(arr,0,len(arr)-1)
        quickt_time = time.perf_counter () - qtstart_time

        arr=A.copy()
        qstart_time = time.perf_counter ()
        quickSort(arr,0,len(arr)-1)
        quick_time = time.perf_counter () - qstart_time

        arr=A.copy()
        hstart_time = time.perf_counter ()
        heapSort(arr)
        heap_time = time.perf_counter () - hstart_time

        arr=A.copy()
        mstart_time = time.perf_counter ()
        mergeSort(arr)
        merge_time = time.perf_counter () - mstart_time
        
        b_arr.append(bubble_time)
        s_arr.append(select_time)
        i_arr.append(insert_time)
        qt_arr.append(quickt_time)
        q_arr.append(quick_time)
        h_arr.append(heap_time)
        m_arr.append(merge_time)

    plt.plot(list(range(m,n)),b_arr,color="red",label="bubble")
    plt.plot(list(range(m,n)),s_arr,color="orange",label="selection")
    plt.plot(list(range(m,n)),i_arr,color="yellow",label="insertion")
    plt.plot(list(range(m,n)),qt_arr,color="green",label="quick 3 way")    
    plt.plot(list(range(m,n)),q_arr,color="blue",label="quick")    
    plt.plot(list(range(m,n)),h_arr,color="magenta",label="heap")
    plt.plot(list(range(m,n)),m_arr,color="purple",label="merge")
    plt.legend()
    plt.show()

