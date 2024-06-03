(: 
    Animals de l'espècie amb id=1 que pesen menys de 500 kg
:)

for $animal in doc("../dades/animals.xml")/especies_animals/especie[@id =1]/animals
/animal

where $animal/pes < 500
return concat($animal/nom, " ",$animal/pes)
