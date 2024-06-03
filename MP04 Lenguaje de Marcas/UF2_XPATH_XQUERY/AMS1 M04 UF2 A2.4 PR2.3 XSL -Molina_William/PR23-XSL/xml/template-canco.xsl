<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="paramId"/>

    <xsl:template match="/">
        <xsl:for-each select="cancons/canco">
            <xsl:variable name="currentId" select="@id"/>
            <!-- Verificar si el ID de la canción coincide con el valor de $paramId -->
            <xsl:if test="$currentId = $paramId">
                <!-- Aplicar las plantillas para la canción actual -->
                <xsl:apply-templates select="."/>
            </xsl:if>

        </xsl:for-each>
    </xsl:template>

    <xsl:template match="canco">
        <html>
            <head>
                <title><xsl:value-of select="titol"/></title>
                <xsl:choose>
                    <xsl:when test="$paramId &gt; 9">
                        <link rel="stylesheet" type="text/css" href="cancoMolinaWilliam.css"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <link rel="stylesheet" type="text/css" href="canco.css"/>
                    </xsl:otherwise>
                </xsl:choose>
            </head>
            <body>
                <h1><xsl:value-of select="titol"/></h1>
                <ul>
                    <li>Autor: <xsl:value-of select="autor"/></li>
                    <li>Año: <xsl:value-of select="any"/></li>
                    <li>Album: <xsl:value-of select="album"/></li>
                </ul>
                
                <img src="{concat('./imatges/', format-number($paramId, '00'), '.jpeg')}" alt="Portada del álbum"/>
                    
                <xsl:apply-templates select="lletra"/>
                
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="lletra">
        <div class="lletra">
            <h2>Lletra:</h2>
            <xsl:for-each select="estrofa">
                <div class="estrofa">
                    <xsl:for-each select="vers">
                        <p><xsl:value-of select="."/></p>
                    </xsl:for-each>
                </div>
            </xsl:for-each>
        </div>
    </xsl:template>
</xsl:stylesheet>
