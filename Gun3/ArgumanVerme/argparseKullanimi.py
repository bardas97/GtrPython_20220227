#illa dışarıdan bir değer beklediğimizde argparse kullanırız.


import argparse

my_parser = argparse.ArgumentParser(description="Dosya yolunu ister...")

#python .\argparseKullanimi.py "C:\\klasor"
#python .\argparseKullanimi.py a_yol="C:\\klasor"
my_parser.add_argument("Yol",
                       metavar='a_yol', #dışarıdan değer girerken kullanılacak ifade
                       type=str,
                       help="Dosya yolunu giriniz."
                      )

argumanlar = my_parser.parse_args()

#print(argumanlar)
print("Girilen Değer: ", argumanlar.Yol)