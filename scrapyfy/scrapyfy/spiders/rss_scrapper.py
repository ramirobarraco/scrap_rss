import scrapy
import pandas as pd
import w3lib.html
    
    
class ScrapeRssSpider(scrapy.Spider):
    name = 'scrape-rss'
    
    def start_requests(self):
        urls = [
            'https://www.lanacion.com.ar/arc/outboundfeeds/rss/?outputType=xml',
            'https://www.infobae.com/argentina-rss.xml',
            'https://www.infobae.com/feeds/rss/',
            'https://www.pagina12.com.ar/rss/secciones/el-pais/notas',
            'https://www.pagina12.com.ar/rss/secciones/economia/notas',
            'https://www.pagina12.com.ar/rss/secciones/sociedad/notas',
            'https://www.pagina12.com.ar/rss/secciones/el-mundo/notas',
            'https://www.pagina12.com.ar/rss/secciones/deportes/notas',
            'https://www.pagina12.com.ar/rss/secciones/cultura/notas',
            'https://www.pagina12.com.ar/rss/secciones/universidad/notas',
            'https://www.pagina12.com.ar/rss/secciones/ciencia/notas',
            'https://www.pagina12.com.ar/rss/secciones/psicologia/notas',
            'https://www.pagina12.com.ar/rss/secciones/ajedrez/notas',
            'https://www.pagina12.com.ar/rss/secciones/la-ventana/notas',
            'https://www.pagina12.com.ar/rss/secciones/dialogos/notas',
            'https://www.pagina12.com.ar/rss/secciones/hoy/notas',
            'https://www.pagina12.com.ar/rss/secciones/plastica/notas',
            'https://www.pagina12.com.ar/rss/secciones/cartas-de-lectores/notas'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        response.selector.remove_namespaces()
        for post in response.xpath('//channel/item'):
            yield {
                'creator' : response.xpath('//channel/title//text()').extract_first(),
                'title' : w3lib.html.remove_tags(post.xpath('title//text()').extract_first()),
                'description' : post.xpath('description//text()').extract_first(),
                'date' : post.xpath('pubDate//text()').extract_first(),
                'content' : w3lib.html.remove_tags(post.xpath('encoded//text()').extract_first())
            }


