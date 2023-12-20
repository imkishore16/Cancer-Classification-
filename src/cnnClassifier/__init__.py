import os
import sys
import logging

#this is a custom logger file

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# logger.info("test") so output will be time INFO:(since we used infromation level log) , then the file name , message 
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")