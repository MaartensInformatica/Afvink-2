een, twee, drie, vier, vijf = input ('enter a five value: ').split()

print ('prijs eerste product: ', een)
print ('prijs tweede product: ', twee)
print ('prijs derde product: ', drie)
print ('prijs vierde product: ', vier)
print ('prijs vijfde product: ', vijf)

subtotaal = float(een+twee+drie+vier+vijf)
subtotaal = float (een) + float (twee) + float (drie) + float (vier) + float (vijf)
print (subtotaal)

salestax = float (subtotaal)*0.07
print (salestax)

totalamount = float(subtotaal) + float(salestax)
print (totalamount)


