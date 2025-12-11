import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def wait_for_final_result(driver, timeout=30):
    def check_result(driver):
        result_div = driver.find_element(By.ID, 'result')
        text = result_div.text.lower()
        if 'fetch successful' in text:
            return 'success'
        if 'fetch failed' in text or 'error:' in text:
            return 'error'
        return None
    try:
        wait = WebDriverWait(driver, timeout)
        return wait.until(lambda d: check_result(d))
    except TimeoutException:
        return 'too long'

def modify_url(url):
    if url.endswith('/'):
        return url + 'api/v2/transactions'
    else:
        return url + '/api/v2/transactions'

def test_urls():
    # Read URLs from file
    with open('explorer_urls.txt', 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    
    if not urls:
        print("No URLs found in explorer_urls.txt")
        return []
    print(f"Testing {len(urls)} URL(s)...")
    
    # Initialize Chrome driver with undetected-chromedriver
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    print("Starting Chrome...")
    driver = uc.Chrome(options=options)
    results = []
    
    try:
        # Go to the test page
        print("Navigating to https://isstuev.github.io/")
        driver.get('https://isstuev.github.io/')
        
        # Find the input field and button
        url_input = driver.find_element(By.ID, 'urlInput')
        test_button = driver.find_element(By.XPATH, "//button[text()='Test Fetch']")
        
        # Test each URL
        for url in urls:
            mod_url = modify_url(url)
            print(f"Testing URL: {mod_url}")
            try:
                # Clear and fill input
                url_input.clear()
                url_input.send_keys(mod_url)
                print("Clicked test button...")
                
                # Click test button
                test_button.click()
                
                # Wait for a final result (success, error, or too long)
                result = wait_for_final_result(driver, timeout=30)
                print(f"Result: {result}")
                results.append(f"{mod_url} | {result}")
                
            except Exception as e:
                print(f"Exception: {e}")
                results.append(f"{mod_url} | error")
            
            # Small delay between requests
            time.sleep(1)
    
    finally:
        print("Quitting Chrome...")
        driver.quit()
    
    # Save results to file
    with open('url_test_results.txt', 'w') as f:
        for result in results:
            f.write(f"{result}\n")
    print("Results saved to url_test_results.txt")
    return results

if __name__ == "__main__":
    results = test_urls()
    print(f"Tested {len(results)} URL(s). Results saved to url_test_results.txt") 