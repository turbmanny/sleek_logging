# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 09:48:36 2026

@author: manom
"""

import numpy as np
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="C:\\git\\mysandbox\\logging_practice\\dummy_log.log",
                    encoding='utf-8', 
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MyAnalysis:
    
    def __init__(self, program_id:str="XP_yyyymmdd.x", config:str="w7x_ref_x"):

        self.program_id = program_id
        self.config     = config
        self.logger     = logger
        self.errors     = []             # Tarck errors per step

    def run(self, steps:list=list(range(10))) -> None:

        """ Run the entire pipeline. Return True is successful, False otherwise """
        
        for step in steps:
            
            try:
                self.logger.info("Running step %d:" % step)
                self.execute_sequence()
                
            except Exception as e:
                
                self._handle_error(str(step), e)
                continue
            
        self.logger.info("Finished")

        return
    
    def execute_sequence(self) -> None:
        
        self.load_data()
        self.preprocess_data()
        self.analyze_data()
        self.save_results()
        
        return
    
    def value_to_x(self) -> float:

        n = 1

        lower_bound = 0
        upper_bound = 1

        x = np.random.uniform(lower_bound, upper_bound, n)

        return x
    
    def function_content(self) -> None:
        
        x = self.value_to_x()

        if x < 0.33:

           raise ValueError("x below 0.33")
            
        return 
        

    def load_data(self) -> None:
        
        self.logger.info("Loading data...")        
        
        self.function_content()

        return
    
    def preprocess_data(self) -> None:

        self.logger.info("Preprocessing data...")        

        self.function_content()

        return
    
    def analyze_data(self) -> None:

        self.logger.info("Analyzing data...")        

        self.function_content()

        return
    
    def save_results(self) -> None:

        self.logger.info("Saving results...")        

        self.function_content()

        return

    def _handle_error(self, step_name:str, error:Exception):

        """ Log and store errors """

        error_msg = "Step %s failed: %s" % (step_name, str(error))
        self.logger.error(error_msg, exc_info=True)
        self.logger.

        return
    
    
# Example usage
if __name__ == "__main__":
    
    pipeline = MyAnalysis(program_id="XP_20250520.35", config="w7x_ref_250")
    pipeline.run()
