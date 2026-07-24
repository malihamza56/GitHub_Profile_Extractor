"""
EXTRACTOR : EXTRACT THE REQUIRED DETAILS FROM USER PROFILE
"""


from logger import logger

def extract_basic_info(page):
    
    
    """_Extract Basic Details of 
        User's GitHub Profile_

    Returns:
        _Dict_: _Details of User Profile in dict_
    """
    
    links = []
    print("👤 Extracting Basic Information...      ✅")
    try :
        logger.info("Extracting Basic Information...")
        
        pfp = page.locator(".avatar")
        src = pfp.get_attribute("src")
        if src:
            pfp = src
            
       
        name = page.locator(".p-name").text_content().strip()
        
        username = page.locator(".p-nickname").text_content().strip()
        
        bio = page.locator(".user-profile-bio").text_content().strip()
            
        gmail_locator = page.locator("li[itemprop='email'] a")
        
        gmail = None
        
        if gmail_locator.count() > 0:
            gmail = gmail.text_content().strip()
        else:
            gmail = "not public"
            
        social = page.locator("[itemprop='social']")
        count = social.count()
        
        for i in range(count):
            
            link = social.nth(i)
            href = link.get_attribute("href")
            if href:
                links.append(href)
            else:
                links = "private"
            
        logger.info("Basic Details Extracted Successfully !")
        
        return {
                "name" : name,
                "username" : username,
                "bio" : bio,
                "pfp" : pfp,
                "gmail" : gmail,
                "social" : links
                }
                
    
    except Exception as e:
        logger.error(f"Basic details extraction failed | {e}")
        raise
    
        
        
def extract_stats(page):
    
    """_Extract User's profile Followers & Following count_

    Returns:
        _DIct_: _Dictionary of following and followers count_
    """
    
    print("📊 Extracting Statistics...             ✅")
    
    try:
        
        logger.info("Extracting Statistical Data...")
        
        following = page.locator("a[href$='tab=following'] .text-bold").text_content().strip()
        follower = page.locator("a[href$='tab=followers'] .text-bold").text_content().strip()
        
        logger.info("Statistical Data Extracted successfully")
        
        return {
            "followers" : follower,
            "following" : following
        }
        
    except Exception as e:
        logger.error(f"Statistical Data Extraction Failed | {e}")
        raise
    
    
    
def extract_repositories(page):

    """Extract All repositories data from user's GitHub Profile"""

    repos = []
    
    
    try:

        logger.info("Extracting Repositories data...")

        container = page.locator("div#user-repositories-list")
        repositories = container.locator("li[itemprop='owns']")
        count = repositories.count()

        logger.info(f"Repositories found : {count}")

        for i in range(count):

            repository = repositories.nth(i)

            # Repository Title
            title_locator = repository.locator("[itemprop='name codeRepository']")
            if title_locator.count() > 0:
                title = title_locator.text_content().strip()
            else:
                title = "Not Available"

            # Description
            description_locator = repository.locator("[itemprop='description']")
            if description_locator.count() > 0:
                description = description_locator.text_content().strip()
            else:
                description = "Not Available"

            # Label
            label_locator = repository.locator(".Label")
            if label_locator.count() > 0:
                label = label_locator.text_content().strip()
            else:
                label = "Not Available"

            # Programming Language
            language_locator = repository.locator("[itemprop='programmingLanguage']")
            if language_locator.count() > 0:
                language = language_locator.text_content().strip()
            else:
                language = "Not Available"

            repos.append(
                {
                    "id": i + 1,
                    "title": title,
                    "description": description,
                    "visibility": label,
                    "programmingLanguage": language,
                }
            )

        logger.info("Repositories Extracted Successfully!")

        return {
            "total repositories": count,
            "details": repos,
        }

    except Exception as e:
        logger.error(f"Repository Extraction Failed | {e}")
        raise
            
        
    
    
def build_profile_data(
    basic_info : dict,
    statistical_info : dict,
    repositories : dict
):
    
    """_Build the final profile dictionary by combining all extracted data._

    Returns:
        _dict_: _Master Dict_
    """
        
    try:
        
        data = {
                **basic_info,
                **statistical_info,
                "repositories" : repositories
            }
        
        logger.info("Making major dict...")
        
        logger.info("Dictionary Created")
        
        return data
        
    except Exception as e:
        logger.error(f"Dictionary Failed | {e}")
        raise