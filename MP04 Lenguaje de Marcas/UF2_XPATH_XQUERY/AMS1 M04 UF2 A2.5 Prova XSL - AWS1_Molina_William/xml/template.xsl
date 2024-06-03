<?xml version="1.0" encoding="UTF-8"?>
<!-- 
Enunciat:

    Fes que a la pàgina android.html hi hagi una llista amb
    tota la informació dels dispositious android que hi ha a l'arxiu dades.xml
    aquesta informació ha de fer servir l'arxiu android.css
    i tenir una estètica fosca en la que
    s'alterna cada fila de la llista entre negre i gris fosc

    Fes que a la pàgina ios.html hi hagi una llista amb
    tota la informació dels dispositius ios que hi ha a l'arxiu dades.xml
    aquesta informació ha de fer servir l'arxiu ios.css
    i tenir una estètica juvenil amb colors múltiples

	Per a les dues pagines, les images s'han de localitzar a la esquerra de cada producte.
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="paramType"/>

    <xsl:template match="/root">
        <html>
            <head>
                <title><xsl:value-of select="$paramType"/></title>
                <link rel="stylesheet" type="text/css" href="{concat($paramType, '.css')}"/>
            </head>
            <body>
                <h1>Llista de dispositius <xsl:value-of select="$paramType"/></h1>
                
                <xsl:choose>
                    <xsl:when test="$paramType = 'android'">
                        <xsl:apply-templates select="android_device"/>
                    </xsl:when>
                    <xsl:when test="$paramType = 'ios'">
                        <xsl:apply-templates select="ios_device"/>
                    </xsl:when>
                </xsl:choose>
            </body>
        </html>
    </xsl:template>

    <!-- Template para Android -->
    <xsl:template match="android_device">
        <div class="device">
            
                <img>
                    <xsl:attribute name="src">
                        <xsl:value-of select="picture"></xsl:value-of>
                    </xsl:attribute>
                    <xsl:attribute name="alt">
                       Dispositivo android
                    </xsl:attribute>
                </img>
            <div class ="info">
                <h3>Model: <xsl:value-of select="model"/></h3>
                <ul>
                    <li>Brand: <xsl:value-of select="brand"/></li>
                    <li>Year: <xsl:value-of select="year"/></li>
                    <li>Colors:</li>
                    <ul>
                        <xsl:for-each select="colors/color">
                            <li><xsl:value-of select="."/></li>
                        </xsl:for-each>
                    </ul>
                </ul>
            </div>
        </div>
    </xsl:template>

    <!-- Template para IOS -->
    <xsl:template match="ios_device">
        <div class="device">
                <img>
                    <xsl:attribute name="src">
                        <xsl:value-of select="picture"></xsl:value-of>
                    </xsl:attribute>
                    <xsl:attribute name="alt">
                       Dispositivo android
                    </xsl:attribute>
                </img>
            <div class ="info">
                <h3>Model: <xsl:value-of select="model"/></h3>
                <ul>
                    <li>Brand: <xsl:value-of select="brand"/></li>
                    <li>Year: <xsl:value-of select="year"/></li>
                    <li>Colors:</li>
                    <ul>
                        <xsl:for-each select="colors/color">
                            <li><xsl:value-of select="."/></li>
                        </xsl:for-each>
                    </ul>
                </ul>
            </div>
        </div>
    </xsl:template>

</xsl:stylesheet>
