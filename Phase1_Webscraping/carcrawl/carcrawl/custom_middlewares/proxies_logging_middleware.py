import logging

class ProxiesLoggingMiddleware:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process_request(self, request, spider):
        # Extract the proxy IP address from the request's meta
        proxy_ip = request.meta.get('proxy')
        if proxy_ip:
            self.logger.info(f"Requesting {request.url} using proxy: {proxy_ip}")