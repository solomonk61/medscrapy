> docker run -v $(pwd):/runtime/app aciobanu/scrapy
> docker run -v $(pwd):/runtime/app aciobanu/scrapy genspider psychdb psychdb.com
> docker run -v $(pwd):/runtime/app aciobanu/scrapy crawl psychdb