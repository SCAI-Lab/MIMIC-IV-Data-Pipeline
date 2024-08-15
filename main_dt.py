#import ipywidgets as widgets
import sys
from pathlib import Path
import os
import importlib
import model.evaluation as evaluation

from digital_twin_ml_model import ML_models

"""
print("=======Machine :earning Models=======")
radio_input5 = widgets.RadioButtons(options=['Logistic Regression','Random Forest','Gradient Bossting','Xgboost'],value='Logistic Regression')
display(radio_input5)
print("Do you wnat to conactenate the time-series feature")
radio_input6 = widgets.RadioButtons(options=['Conactenate','Aggregate'],value='Conactenate')
display(radio_input6)
print("Please select below option for cross-validation")
radio_input7 = widgets.RadioButtons(options=['No CV','5-fold CV','10-fold CV'],value='5-fold CV')
display(radio_input7)
print("Do you want to do oversampling for minority calss ?")
radio_input8 = widgets.RadioButtons(options=['True','False'],value='True')
display(radio_input8)
"""

data_icu = True

"""
if radio_input7.value=='No CV':
    cv=0
elif radio_input7.value=='5-fold CV':
    cv=int(5)
elif radio_input7.value=='10-fold CV':
    cv=int(10)
"""

ml=ML_models(data_icu,k_fold=int(5),model_type='Logistic Regression',concat='Conactenate',oversampling='True')