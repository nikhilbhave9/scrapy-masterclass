# Different Web-scraping Scenarios

## Logging-in
- GET and POST methods differ in the way they send parameters through. GET adds them to the query string and it is visible in the URL. This is not secure. POST sends them via the body of the request. This is more secure
- As an additional security measure, the form on the website that will eventually send the POST request to the API endpoint has a CSRF key, which authenticates the source of the form data. We need to include this in our scraping toolkit
- Thus, we use the Request and FormRequest classes along with the start_requests method to simulate a form being sent to the API endpoint

## User Agents
- User agent is a parameter in the response header. It provides information about what kind of browser is making the request
- Many websites ban user agents that state they are from a library like Scrapy. Instead, we can use a user agent like "Mozilla ...." to pretend to be a normal browser
- For example, we can use the following command: <b>scrapy shell -s USER_AGENT="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0" "www.website.com"</b>