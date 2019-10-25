# -*- coding: utf-8 -*-

# Scrapy settings for mySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mySpider'

SPIDER_MODULES = ['mySpider.spiders']
NEWSPIDER_MODULE = 'mySpider.spiders'
# 设置中文字符集
FEED_EXPORT_ENCODING = 'utf-8'
# 定义错误等级以及日志
# LOG_LEVEL = 'ERROR'
# LOG_FILE = 'log.txt'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'mySpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
# 修改这个参数为false
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9,de;q=0.8,en;q=0.7',
    'Referer': 'https://news.163.com/',
    'Cookie': 'UM_distinctid=16b98102a76390-084cf01152f125-e343166-1fa400-16b98102a77b3; _ntes_nnid=cb3813e9ab1b5878f19415d7840b693c,1561624325750; __gads=ID=c3ad1ea95ede16cd:T=1561624325:S=ALNI_MaicPS_8ur_mQY6-4oE5ImO0Glr2g; mail_psc_fingerprint=6767ebc3b4e0c4c44791250e551d81c7; _ntes_nuid=cb3813e9ab1b5878f19415d7840b693c; usertrack=CrH/WV1coiN2FWjYAxEsAg==; P_INFO=m18530893662@163.com|1566438698|0|mail163|00&99|shh&1566352065&carddav#shh&null#10#0#0|185662&1|mail163&note_client|18530893662@163.com; BAIDU_SSP_lcr=https://www.google.com/; NNSSPID=d901b243922547e08372ec97f3c8cb8f; _antanalysis_s_id=1566803554893; ntes_renjian=; ne_analysis_trace_id=1566870359964; s_n_f_l_n3=c4635c25116285cb1566870592495; vinfo_n_f_l_n3=c4635c25116285cb.1.7.1561624325763.1566870361194.1566870627583',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'mySpider.pipelines.MyspiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# mongodb 数据库配置
ITEM_PIPELINES = {
    'mySpider.pipelines.KdbPipeline': 300,
}
MONGO_HOST = '94.191.53.141'
MONGO_PORT = '27017'
MONGO_DATABASE = 'wangyi'
