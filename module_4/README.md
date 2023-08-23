# Different Web-scraping Scenarios

## Logging-in
- GET and POST methods differ in the way they send parameters through. GET adds them to the query string and it is visible in the URL. This is not secure. POST sends them via the body of the request. This is more secure
- As an additional security measure, the form on the website that will eventually send the POST request to the API endpoint has a CSRF key, which authenticates the source of the form data. We need to include this in our scraping toolkit
- Thus, we use the Request and FormRequest classes along with the start_requests method to simulate a form being sent to the API endpoint