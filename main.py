"""
MAIN : MAIN MODULE WHICH CONTROLS THE WHOLE WORK FLOW OF PROGRAM
"""

from browser import (
    launch_browser,
    close_browser
)
from extractor import (
    extract_basic_info,
    extract_stats,
    extract_repositories,
    build_profile_data
)
from exporter import (
    json_data,
    csv_data
)
from screenshot import snapshot
from navigator import visit_profile,visit_repositories
from logger import logger
from playwright.sync_api import sync_playwright
import pandas as pd

def main():
    
    browser = None
    logger.info("GitHub Profile Extractor Started...")
    username = input("Enter Your GitHub Profile Username :").strip().lower()
    
    print("=" * 52)
    print("      GitHub Profile Extractor v1.0")
    print("=" * 52)

    print(f"\n🔎 Target Profile : {username}\n")
    
    try:
        
        with sync_playwright() as playwright:
            browser,context,page = launch_browser(playwright=playwright)
            print("🌐 Launching Browser...                 ✅")
            profile = visit_profile(
                page=page,
                username=username
            )
            print("📄 Opening GitHub Profile...            ✅")
            
            snapshot(page=profile)  #profile snapshot
            
            repositories = visit_repositories(page=page)
            
            #Data Extraction
            basic_info = extract_basic_info(profile)
            stats = extract_stats(profile)
            repos = extract_repositories(repositories)
            print(f"📂 Extracting Repositories...           ✅ ({repos['total repositories']} Found)")
            #Data
            data = build_profile_data(
                basic_info=basic_info,
                statistical_info=stats,
                repositories=repos
            )
             
            #Files Conversion
            json_data(data)
            dataframe = pd.DataFrame(repos['details'])
            csv_data(dataframe)
            
            if browser:  
                close_browser(browser=browser)
                
        logger.info("GitHub Profile Extracted Successfully!")
        print("\n" + "=" * 52)
        print("✔ Profile Extracted Successfully!")
        print("=" * 52)

        print("\nFiles Generated\n")
        print("📄 JSON        : data/json/profile.json")
        print("📊 CSV         : data/csv/repositories.csv")
        print("📸 Screenshot  : screenshots/profile.png")

        print("\nThank you for using GitHub Profile Extractor 🚀")
    except Exception as e:
        logger.error(f"Error Occurred | {e}")
    
        
    
    
if __name__ == "__main__":
    main()