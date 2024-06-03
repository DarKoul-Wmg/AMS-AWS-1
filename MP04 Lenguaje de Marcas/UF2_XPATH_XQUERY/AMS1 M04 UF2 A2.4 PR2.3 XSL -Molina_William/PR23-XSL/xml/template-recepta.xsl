<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="paramId"/>
    <xsl:template match="/receptes">
        <html>
            <head>
                <meta charset="UTF-8"/>
                <title>Receptes</title>
            </head>
            <body>
                <xsl:for-each select="recepta">
                    <xsl:if test="@id=$paramId">
                        <xsl:call-template name="recepta"/>
                    </xsl:if>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>

    <xsl:template name="recepta">
        <h2><xsl:value-of select="nom"/></h2>
        <h3>Ingredients:</h3>
        <xsl:for-each select="ingredients/ingredient">
            <p><xsl:value-of select="."/></p>
        </xsl:for-each>
        <h3>Elaboració:</h3>
        <xsl:for-each select="elaboracio/pas">
            <p><xsl:value-of select="."/></p>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>