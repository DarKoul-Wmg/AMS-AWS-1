(:
    Fer anar aquest exemple amb:
    java -cp BaseX104.jar org.basex.BaseX exemple-fruites00.xq 
:)
(: 
    Totes les fruites amb preu > 0.4 i de color "groc" 
    Mostra 'Oferta' o 'Fruita' segons el preu
:)
for $x in doc("../dades/fruites.xml")/fruites/fruita
where $x/preu>=0.4 and $x/color="groc"
order by $x/nom
return 
    if ($x/preu < 0.6) then (
        concat("Oferta: ", $x/nom, " = ", $x/preu)
    ) else (
        concat("Fruita: ", $x/nom, " = ", $x/preu)
    )