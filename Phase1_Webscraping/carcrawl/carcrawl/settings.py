import os
proxy_url = os.environ.get('SMARTPROXY_URL')
# Scrapy settings for carcrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "carcrawl"

SPIDER_MODULES = ["carcrawl.spiders"]
NEWSPIDER_MODULE = "carcrawl.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.254",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 10
#CONCURRENT_REQUESTS_PER_IP = 10

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True
# Enable cookies debugging (add this line manually)
#COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "carcrawl.middlewares.CarcrawlSpiderMiddleware": 543,
#}


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.cookies.CookiesMiddleware": 543,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": None,
    "scrapy_rotated_proxy.downloadmiddlewares.proxy.RotatedProxyMiddleware": 750,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "carcrawl.middlewares.RotateUserAgentMiddleware": 400, 
    #"carcrawl.custom_middlewares.proxies_logging_middleware.ProxiesLoggingMiddleware": 751
    #"scrapy_proxy_pool.middlewares.ProxyPoolMiddleware": 610,
    #"scrapy_proxy_pool.middlewares.BanDetectionMiddleware": 620,
}

ROTATED_PROXY_ENABLED = True
PROXY_STORAGE = 'scrapy_rotated_proxy.extensions.file_storage.FileProxyStorage'
PROXY_FILE_PATH = ''

HTTPS_PROXIES = ['https://filipdom93:QpGpgf4yg2ElxxnY54@gate.smartproxy.com:7000',
                 'https://customer-filipdom93:Mozoobew12@pr.oxylabs.io:7777',
                'https://customer-filipdom93:Mozoobew12@pr.oxylabs.io:7777',
                'https://customer-filipdom93:Mozoobew12@pr.oxylabs.io:7777',
                'https://customer-filipdom93:Mozoobew12@pr.oxylabs.io:7777',
                'https://customer-filipdom93:Mozoobew12@pr.oxylabs.io:7777'
    ]

HTTP_PROXIES = ['http://filipdom93:QpGpgf4yg2ElxxnY54@gate.smartproxy.com:7000',
                'http://customer-filipdom93:Mozoobew12@pr.oxylabs.io:7777']

PROXY_SPIDER_CLOSE_WHEN_NO_PROXY = False
PROXY_RELOAD_ENABLED = True
#LOG = True
#LOG_LEVEL = 'INFO'
#LOG_FILE = 'scrapy.log'

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "carcrawl.pipelines.CarcrawlPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 2
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
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"