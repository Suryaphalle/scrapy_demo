import scrapy
import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)


class spider1(scrapy.Spider):
	name = 'wikipedia'
	start_urls = ['https://en.wikipedia.org/wiki/Battery_(electricity)']

	def parse(self, response):
		print(response.css('h1#firstHeading::text').extract())
