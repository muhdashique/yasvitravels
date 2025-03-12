# In your middleware.py file
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class NoCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Add stronger cache prevention headers
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0, private'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        # Add additional header to prevent back/forward cache in Firefox
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
        return response

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Exempt login page and public pages from authentication check
        exempt_urls = [reverse('login'), reverse('index'), reverse('send_email')]
        
        # Check for static files or other excluded paths
        excluded_paths = ['/static/', '/media/']
        for path in excluded_paths:
            if request.path.startswith(path):
                return None
        
        # If the user is trying to access a protected page but isn't logged in
        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('login')