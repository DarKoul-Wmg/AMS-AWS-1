(: 
    Videoconsola amb color blanc i fabricant Nintendo
:)

for $consola in doc("../dades/videojocs.xml")/consoles/consola[color = "blanc"]

return concat($consola/nom, " = ",if($consola/fabricant = "Nintendo") then "Si"
else "No")