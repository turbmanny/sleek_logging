# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:32:34 2026

@author: manom

This code is taken by:
    
    https://stackoverflow.com/questions/20111758/how-to-insert-newline-in-python-logging
    
I also included a file handler.

"""

import logging
import types
import inspect

def log_newline(h, nof_lines:int=1) -> None:
    
    # Switch handler, output a blank line
    # h.removeHandler(h.console_handler)
    
    h.removeHandler(h.file_handler)
    h.addHandler(h.blank_handler)
    for idx in range(nof_lines):
        h.info("")
        
    # Switch back
    h.removeHandler(h.blank_handler)
    
    # h.addHandler(h.console_handler)
    h.addHandler(h.file_handler)
        
    return

def create_logger(fname:str, name:str="sleek_logger"):
    
    # # Create a console handler
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG)
    # console_handler.setFormatter(logging.Formatter(fmt="%(funcName)s %(levelfuncName)-8s: %(message)s"))

    # Create a "blank line" handler
    blank_handler = logging.StreamHandler()
    blank_handler.setLevel(logging.INFO)
    blank_handler.setFormatter(logging.Formatter(fmt=''))
    
    # Create a file handler (for writing to a file)
    file_handler = logging.FileHandler(filename=fname,
                                       mode="w", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(funcName)s %(levelname)-8s: %(message)s"))

    # Create a logger, with the previously-defined handler
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.INFO)
    # logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Save some data and add a method to logger object
    # logger.console_handler = console_handler
    logger.blank_handler = blank_handler
    logger.file_handler  = file_handler
    logger.newline       = types.MethodType(log_newline, logger)

    return logger

if __name__ == "__main__":
    logger = create_logger(fname="my_dummy_log.log")
    logger.info("Start reading new database...")
    logger.info("Updating new records...")
    logger.error("Oh no... Something happened again")
    logger.newline()
    logger.info("Finish updating final records")
    
    

