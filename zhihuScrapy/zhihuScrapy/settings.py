# -*- coding: utf-8 -*-

# Scrapy settings for zhihuScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuScrapy'

SPIDER_MODULES = ['zhihuScrapy.spiders']
NEWSPIDER_MODULE = 'zhihuScrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuScrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Host' : 'huiben.iboniao.com',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'Connection' : 'keep-alive',
  'Upgrade-Insecure-Requests' : '1',
  'Sec-Fetch-Site' : 'none',
  'Sec-Fetch-Mode' : 'navigate',
  'Accept-Encoding': 'gzip,deflate',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuScrapy.middlewares.ZhihuscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'zhihuScrapy.middlewares.ZhihuscrapyDownloaderMiddleware': 543,
}

FEED_EXPORT_ENCODING = 'utf-8'

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihuScrapy.pipelines.ZhihuscrapyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_URL = '127.0.0.1' #这里设置本地数据库
MONGO_PORT = '27017' #这里设置数据库服务端口
MONGO_DATABASE = 'zhihu' #这里指定数据库的名字，如果不存在就创建
# SCHEDULER = 'scrapy_redis.scheduler.Scheduler' #启用redis调度器
# DUPEFILTER_CLASS = 'crapy_redis.dupefilter.RFPDupeFilter' #启用redis的过滤器
# SCHEDULER_PERSIST = True  #开启不清空队列,这样就可以暂停爬取
# ITEM_PIPELINES = {
#     'scrapy_redis.pipelines.RedisPipeline': 301  
#     # 开启这个管道后所有的数据都将被送往master主机,这样不利于网络的通畅,通常来说都是各自存在各自的机器让最后再汇总当然你也可以开启.
# }
# REDIS_URL = 'redis://localhost:6379' 
# 配置master数据库信息,如果没有密码只要填写用户名就好,user默认为(root),hostname为弹性ip地址,r

ITEM_PIPELINES = {
    'zhihuScrapy.pipelines.MongoPipeline': 300,
}