import pandas as pd
import tkinter as tk

def search(nums,target):
    start = 0
    end=len(nums)-1
    print(end)
    while start <= end:
        mid = start + (end-start)//2
        if str(nums.loc[mid,0])>target:
            end=mid-1
        elif str(nums.loc[mid,0])<target:
            start = mid+1
        else:
            return mid
    return -1

df1 = pd.read_excel("E:\\Manas\\Python\\Audit.xlsx",sheet_name="MAIN")
df2 = pd.read_excel("E:\\Manas\\Python\\Audit.xlsx",sheet_name="AUDIT")

search(df1,'196150737115')