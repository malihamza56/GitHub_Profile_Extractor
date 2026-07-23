"""
BROWSER : CONTROL BROWSER LAUNCHING OPERATIONS
"""


from playwright.sync_api import sync_playwright
from logger import logger


def launch_browser(playwright):
    
    """_LAUNCH BROWSER_

    Returns:
        _OBJECTS_: _BROWSER , CONTEXT , PAGE_
    """
    try :
        
        logger.info("Launching Browser...")
    
        browser = playwright.chromium.launch(headless=False)
        
        logger.info("Browser Launched Successfully")
        logger.info("Making Context...")
        
        context = browser.new_context()
        
        logger.info("Context Created Successfully")
        logger.info("Creating Page...")
        
        page = context.new_page()
        logger.info("Page Created Successfully")
            
        return browser,context,page
    
    
    except Exception as e:
        logger.error(f"Browser Launching Failed | {e}")
        raise
        
        
        
def close_browser(browser):
    
    try:
        logger.info("Closing Browser...")
        browser.close()
        logger.info("Browser Closed !")
        
    except Exception as e:
        logger.error(f"Browser Closing Error |{e}")
        raise