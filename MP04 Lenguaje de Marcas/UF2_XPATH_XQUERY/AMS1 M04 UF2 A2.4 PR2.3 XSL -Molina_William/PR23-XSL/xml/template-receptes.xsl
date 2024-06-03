<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/receptes">
        <html>
            <head>
                <meta charset="UTF-8"/>
                <title>Receptes</title>
            </head>
            <body>
                <xsl:for-each select="recepta">
                    <br/>
                    <xsl:element name="a">
                        <xsl:attribute name="href">./<xsl:value-of select="@id"/>.html</xsl:attribute>
                        <xsl:attribute name="target">_self</xsl:attribute>
                        <xsl:value-of select="nom"/>
                    </xsl:element>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>