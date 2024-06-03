(:
    Per cada estació, mostra els habitants
    que té la seva ciutat 
:)

for $estacio in doc("../dades/ciutats-estacions.xml")/estacions/estacio
for $ciutat in doc ("../dades/ciutats.xml")/ciutats/ciutat[@id = $estacio/ciutat]

return concat($ciutat/nom, " - ", $estacio/nom," : ",$ciutat/habitants," habitants")