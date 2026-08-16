"""
MAIN : MAIN MODULE WHICH CONTROLS THE WHOLE WORK FLOW OF PROGRAM
"""

from browser import launch_browser, close_browser

from extractor import (
    extract_basic_info,
    extract_stats,
    extract_repositories,
    build_profile_data
)

from exporter import json_data, csv_data
from screenshot import snapshot
from navigator import visit_profile, visit_repositories
from logger import logger

from playwright.sync_api import sync_playwright
import pandas as pd


def extract_profile(username):
    """
    Main extraction workflow.
    Returns all extracted data for the Streamlit UI.
    """

    browser = None

    username = username.strip().lower()

    if not username:
        return {
            "success": False,
            "error": "Username cannot be empty."
        }

    logger.info(
        f"GitHub Profile Extractor Started | Username: {username}"
    )

    try:

        with sync_playwright() as playwright:

            # Launch browser
            browser, context, page = launch_browser(
                playwright=playwright
            )

            # Open profile
            profile = visit_profile(
                page=page,
                username=username
            )

            # Save profile screenshot
            snapshot(page=profile)

            # Open repositories
            repositories = visit_repositories(
                page=page
            )

            # -----------------------------
            # DATA EXTRACTION
            # -----------------------------

            basic_info = extract_basic_info(
                profile
            )

            stats = extract_stats(
                profile
            )

            repos = extract_repositories(
                repositories
            )

            # -----------------------------
            # BUILD FINAL PROFILE DATA
            # -----------------------------

            data = build_profile_data(
                basic_info=basic_info,
                statistical_info=stats,
                repositories=repos
            )

            # -----------------------------
            # EXPORT DATA
            # -----------------------------

            json_data(data)

            dataframe = pd.DataFrame(
                repos["details"]
            )

            csv_data(dataframe)

            # Close browser
            if browser:
                close_browser(
                    browser=browser
                )

        logger.info(
            "GitHub Profile Extracted Successfully!"
        )

        return {
            "success": True,
            "username": username,
            "profile": data,
            "repositories": repos,
            "dataframe": dataframe
        }

    except Exception as e:

        logger.error(
            f"Error Occurred | {e}"
        )

        if browser:
            try:
                close_browser(browser=browser)
            except Exception:
                pass

        return {
            "success": False,
            "error": str(e)
        }


# -----------------------------------------
# CLI VERSION
# -----------------------------------------

def main():

    print("=" * 52)
    print("      GitHub Profile Extractor v1.0")
    print("=" * 52)

    username = input(
        "\nEnter Your GitHub Profile Username : "
    ).strip().lower()

    result = extract_profile(username)

    if result["success"]:

        print("\n" + "=" * 52)
        print("✔ Profile Extracted Successfully!")
        print("=" * 52)

        print("\nFiles Generated\n")
        print("📄 JSON        : data/json/profile.json")
        print("📊 CSV         : data/csv/repositories.csv")
        print("📸 Screenshot  : screenshots/profile.png")

        print(
            "\nThank you for using GitHub Profile Extractor 🚀"
        )

    else:

        print(
            f"\n❌ Extraction Failed: {result['error']}"
        )


if __name__ == "__main__":
    main()