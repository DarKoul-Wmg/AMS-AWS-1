(: 
    Videjocs desenvolupats per "Ubisoft"
:)
for $videojoc in doc("../dades/videojocs.xml")/consoles/consola/videojocs/videojoc
where contains($videojoc/desenvolupador,"Ubisoft") 

return <joc>
<nom>{data($videojoc/nom)}</nom>
<estudi>{data($videojoc/desenvolupador)}</estudi>
</joc>