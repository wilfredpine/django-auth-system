import logging
from django.conf import settings

# Get the logger
logger = logging.getLogger('django')

class LogIPMiddleware:
    """
    Middleware to log the IP address of the incoming request.
    The method of obtaining the IP address is determined by the DEBUG setting.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture the user's public IP address
        ip_address = self.get_client_ip(request)
        
        # Log the IP address (you can also include other info like the requested URL)
        logger.info(f"Request from IP: {ip_address}, Path: {request.path}")
        
        # Call the next middleware or view
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """
        Returns the client's IP address, considering proxies (like load balancers).
        This method checks the DEBUG setting and adjusts how the IP is retrieved.
        """
        if settings.DEBUG:
            # In development, use REMOTE_ADDR directly
            ip = request.META.get('REMOTE_ADDR')
        else:
            # In production, use X-Forwarded-For if available
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Get the first forwarded IP
            else:
                ip = request.META.get('REMOTE_ADDR')
        return ip
