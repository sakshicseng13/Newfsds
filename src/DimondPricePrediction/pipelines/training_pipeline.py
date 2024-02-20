from src.DimondPricePrediction.components.data_ingestion import DataIngestion

from src.DimondPricePrediction.components.data_transformation import DataTransformation

from src.DimondPricePrediction.components.model_trainer import ModelTrainer

#from src.DimondPricePrediction.components.model_evaluation import ModelEvaluation


import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import pandas as pd

    
data_ingestion=DataIngestion()
train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
        
        
   
data_transformation = DataTransformation()
train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)
        
        
    
    
   
model_trainer=ModelTrainer()
model_trainer.initate_model_training(train_arr,test_arr)
       
                
   