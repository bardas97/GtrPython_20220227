##python .\merhabaArguman.py Abdullah, Ali, Veli
import sys
'''
sys.argv bir liste döndörür
sys.argv[0] --> program adı

'''
#print("merhaba: ", sys.argv)
#print("merhaba: ", sys.argv[1:]) #dışarıdan girilen değerler

disaridanGelenler = sys.argv[1:]
print("\n".join(disaridanGelenler))

