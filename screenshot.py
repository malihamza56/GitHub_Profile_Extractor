"""
SCREENSHOT MODULE : CAPTURES SCREENSHOT OF PROFILE AFTER EXTRACTION
"""

from logger import logger

def snapshot(page):
    print("📸 Capturing Screenshot...              ✅")
    try:
        logger.info("capturing Screenshot...")
        page.screenshot(path = "screenshots/profile.png",full_page = True)
        logger.info("Screenshot Captured !")
        
    except Exception as e:
        logger.error(f"Snapshot Failed | {e}")
        raise
    
    