"""
NAVIGATOR : CONTROL PROFILE VISITING AND NAVIGATION
"""

from logger import logger
from urllib.parse import urljoin
from config import BASE_URL

def visit_profile(
    page,
    username : str,
):
    """_NAVIGATE TO GITHUB PROFILE AND WAIT UNTIL THE PAGE LOAD_

    Args:
        username (str): _USERNAME OF PROFILE_
        page (_Playwright object_): _BROWSER LANDING PAGE_

    Returns:
        _OBJECT_: _PROFILE PAGE _
    """
    
    try : 
        
        logger.info("Redirecting to GitHub Profile...")
        
        profile_url = urljoin(BASE_URL,username)
        
        logger.info(f"Opening : {profile_url}")
        
        page.goto(
            profile_url
        )
        page.wait_for_load_state("networkidle")
        
        return page
    
    except Exception as e:
        logger.error(f"Profile visiting failed | {e}")
        raise
    
