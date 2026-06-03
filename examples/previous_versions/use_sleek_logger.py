# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:57:08 2026

@author: manom
"""

import methodic_logger

def my_function() -> None:
    
    logger = methodic_logger.create_logger(name=__file__, fname="my_logging_file.log")
    logger.info("Start reading new database...")
    logger.info("Updating new records...")
    logger.error("Oh no... Something happened again")
    logger.newline()
    logger.info("Finish updating final records")
    
    return

if __name__ == "__main__":
    
    my_function()