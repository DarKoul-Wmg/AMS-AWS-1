<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/cancons">
        <html>
            <head>
                <title>Cançons</title>
                <link rel="stylesheet" type="text/css" href="../cancons.css"/>
            </head>
            <body>
                <h1>Llista de Cançons</h1>
                <ul>
                    <xsl:for-each select="canco">
                        <li>
                            <a href="{@id}.html"><xsl:value-of select="titol"/></a>
                        </li>
                    </xsl:for-each>
                </ul>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
