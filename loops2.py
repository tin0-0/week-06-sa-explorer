#name="Mzansi"

#for letter in name:
    #print(letter,end="")

#for word in ["gauteng", "Limpopo", "kZN"]:
    #print(word)
provinces = ["gauteng", 
                "western cape",
                "kZN"]
#print(len(provinces))
#
#for i, p in enumerate(provinces, 1):
  #  print(f"{i}. {p}")
provinces_String="GP, WC, KZN, EC, FS, LP, MP, NC, NW"
provincesAbb=provinces_String.split(", ").split(",")
print(provincesAbb)