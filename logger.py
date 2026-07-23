"""
LOGGER : AN INSTANCE USED IN WHOLE ARCHITECTURE
FOR LOGGING FILES
"""


import logging

#BASIC CONFIGURATION FOR LOGGER

logging.basicConfig(
    level=logging.INFO,
    filename="/logs/github_extractor.log",
    filemode='w',
    format="%(asctime)s - %(level)s - %(filename)s - %(message)s"
)


#LOGGER INSTANCE
logger = logging.getLogger(__name__)