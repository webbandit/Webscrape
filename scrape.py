from playwright.sync_api import sync_playwright

def run(playwright):
    
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Select the URL which one you want to open

    page.goto('https://quotes.toscrape.com')
    quotes = page.query_selector_all('.quote')
    for quote in quotes:
        text = quote.query_selector('.text').inner_text()
        author = quote.query_selector('.author').inner_text()
        result = text + ' - ' + author

    # Write the result to a file use "a" to append the result to the file or "w" to overwrite the file
    
        f = open("quotes.txt", "a")
        f.write(result + '\n')
        f.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)