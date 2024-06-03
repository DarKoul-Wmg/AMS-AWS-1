<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="paramType"/>

    <xsl:template match="/rss">
        <html>
            <head>
                <title><xsl:value-of select="$paramType"/></title>
                <!-- CSS -->
                <link rel="stylesheet" type="text/css" href="microsiervos.css"/>
            </head>
            <body>
                <!-- Segun parametro, aplica plantilla correspondiente -->
                <xsl:choose>
                    <xsl:when test="$paramType='5'">
                        <xsl:call-template name="template5"/>
                    </xsl:when>
                    <xsl:when test="$paramType='Espai'">
                        <xsl:call-template name="templateEspai"/>
                    </xsl:when>
                    <xsl:when test="$paramType='Imparell'">
                        <xsl:call-template name="templateImparell"/>
                    </xsl:when>
                </xsl:choose>
            </body>
        </html>
    </xsl:template>

    <!-- Plantilla para las primeras 5 noticias -->
    <xsl:template name="template5">
        <xsl:for-each select="channel/item[position() &lt;= 5]">
            <div class="noticia">
                <xsl:call-template name="noticia"/>
            </div>
        </xsl:for-each>
    </xsl:template>

    <!-- Plantilla para cada noticia -->
    <xsl:template name="noticia">
        <h2><xsl:value-of select="title"/></h2>
        <h3><xsl:value-of select="category"/></h3>
        <!-- Simplemente aplicamos las plantillas de procesamiento de texto -->
        <xsl:apply-templates select="description"/>
        <hr/>
    </xsl:template>

    <!-- Plantilla para noticias de Espacio -->
    <xsl:template name="templateEspai">
        <xsl:for-each select="channel/item[contains(category, 'Espacio')]">
            <div class="noticia">
                <xsl:call-template name="noticiaEspai"/>
            </div>
        </xsl:for-each>
    </xsl:template>

    <xsl:template name="noticiaEspai">
        <h2><xsl:value-of select="title"/></h2>
        <img class="icon" src="https://cdn.icon-icons.com/icons2/1701/PNG/512/iconfinder-spaceship-2927564_112160.png" alt="Espacio"/>
        <xsl:apply-templates select="description"/>
        <hr/>
    </xsl:template>

    <!-- Plantilla para noticias impares -->
    <xsl:template name="templateImparell">
        <xsl:for-each select="channel/item[position() mod 2 != 0]">
            <div class="noticia">
                <xsl:call-template name="noticia"/>
            </div>
        </xsl:for-each>
        <script>
            document.body.classList.add('impar');
        </script>
    </xsl:template>

    <!-- Plantilla para procesar la descripción -->
    <xsl:template match="description">
        <xsl:variable name="parsedDesc">
            <!-- Parsear el contenido CDATA -->
            <xsl:call-template name="parseCDATA">
                <xsl:with-param name="content" select="."/>
            </xsl:call-template>
        </xsl:variable>
        <xsl:value-of select="$parsedDesc" disable-output-escaping="yes"/>
    </xsl:template>

    <!-- Plantilla para parsear contenido CDATA -->
    <xsl:template name="parseCDATA">
        <xsl:param name="content"/>
        <xsl:choose>
            <!-- Si el contenido contiene etiquetas <p> y no contiene etiquetas <img> ni <blockquote>, devolverlo -->
            <xsl:when test="contains($content, '&lt;p>') and not(contains($content, '&lt;img>')) and not(contains($content, '&lt;blockquote>'))">
                <xsl:variable name="start" select="substring-before($content, '&lt;p>')"/>
                <xsl:variable name="end" select="substring-after($content, '&lt;p>')"/>
                <xsl:value-of select="$start"/>
                <xsl:text disable-output-escaping="yes">&lt;p></xsl:text>
                <xsl:call-template name="parseCDATA">
                    <xsl:with-param name="content" select="$end"/>
                </xsl:call-template>
            </xsl:when>
            <!-- Si no, devolver una cadena vacía -->
            <xsl:otherwise>
                <xsl:text disable-output-escaping="yes">&lt;/p></xsl:text>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
</xsl:stylesheet>
