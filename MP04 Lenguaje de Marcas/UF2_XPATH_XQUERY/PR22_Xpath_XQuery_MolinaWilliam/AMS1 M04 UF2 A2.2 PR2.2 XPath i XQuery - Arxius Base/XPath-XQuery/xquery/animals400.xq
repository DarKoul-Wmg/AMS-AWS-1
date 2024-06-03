(: 
    Animals de més de 400 kg i de color gris
:)
for $animal in doc("../dades/animals.xml")/especies_animals/especie/animals/animal

where $animal/pes > 400 and $animal/color ="gris"
return concat($animal/nom, " ",$animal/pes)
