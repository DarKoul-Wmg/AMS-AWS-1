(:
    Fer anar aquest exemple amb:
    java -cp BaseX104.jar org.basex.BaseX exemple-books00.xq 
:)
(: 
    Tots els llibres amb preu > 30 
:)
for $x in doc("../dades/books.xml")/bookstore/book
where $x/price>30
order by $x/title
return concat($x/title, " = ", $x/price)