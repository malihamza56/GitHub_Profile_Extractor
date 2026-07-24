"""
LOGGER : AN INSTANCE USED IN WHOLE ARCHITECTURE
FOR LOGGING FILES
"""

from pathlib import Path
import logging

Path("logs").mkdir(exist_ok=True)

#BASIC CONFIGURATION FOR LOGGER
logging.basicConfig(
    level=logging.INFO,
    filename="logs/github_extractor.log",
    filemode='w',
    format= "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s"
)


#LOGGER INSTANCE
logger = logging.getLogger(__name__)