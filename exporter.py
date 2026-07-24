"""
EXPORTER : EXPORT WHOLE DATA TO FORMATTED FILES
"""


from logger import logger
import json


def json_data(data):
    
    print("📄 Exporting JSON...                    ✅")
    try:
        logger.info("Converting to Json...")
    
        with open(
            "data/profile.json",
            'w',
            encoding="utf-8",
        ) as f:
            
            json.dump(
                data,
                f,
                indent=4,
                
            )
            
        logger.info("Data converted to Json successfully")
        
    except Exception as e:
        logger.error(f"Json conversion failed | {e}")
        raise
    
    

def csv_data(dataFrame):
    
    
    print("📊 Exporting CSV...                     ✅")
    try:
        logger.info("Converting to CSV...")
        
        dataFrame.to_csv(
            "data/profile.csv",
            index=False
        )
        
        logger.info("Data converted to CSV successfully")
        
    except Exception as e:
        logger.error(f"CSV conversion failed | {e}")
        raise
    