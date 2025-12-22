import os 
import sys
import logging
logg_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir='logs'
log_file=os.path.join(log_dir,'logging.log')
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logg_str,
    handlers=[
      logging.FileHandler(log_file),
      logging.StreamHandler(sys.stdout)  
    ]
    
    
    )
logger = logging.getLogger('ds-project')