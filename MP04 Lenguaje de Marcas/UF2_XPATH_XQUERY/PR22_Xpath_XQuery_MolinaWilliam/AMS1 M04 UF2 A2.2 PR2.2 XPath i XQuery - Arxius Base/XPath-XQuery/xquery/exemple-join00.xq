(:
    Fer anar aquest exemple amb:
    java -cp BaseX104.jar org.basex.BaseX exemple-join00.xq 
:)
(: 
    Join entre la taula fruites i la taula fruiteries
    Mostra les fruites de cada fruiteria pel nom 
:)
for $fruiteria in doc("../dades/fruiteries.xml")/fruiteries/fruiteria
for $fruita in doc("../dades/fruites.xml")/fruites/fruita[@id=$fruiteria/fruites/fruita/@id]
order by $fruiteria/nom, $fruita/nom
return concat("<fruiteria><nom>", $fruiteria/nom, "</nom><fruita>", $fruita/nom, "</fruita></fruiteria>")