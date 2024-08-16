#import ipywidgets as widgets
import sys
from pathlib import Path
import os
import importlib
import model.evaluation as evaluation
from digital_twin_dl_model import DL_models


data_icu = True

"""
radio_input6=widgets.RadioButtons(options=['Time-series LSTM','Time-series CNN','Hybrid LSTM','Hybrid CNN'],value='Time-series LSTM')
display(radio_input6)
print("Please select below option for cross-validation")
radio_input7 = widgets.RadioButtons(options=['No CV','5-fold CV','10-fold CV'],value='5-fold CV')
display(radio_input7)
print("Do you want to do oversampling for minority calss ?")
radio_input8 = widgets.RadioButtons(options=['True','False'],value='True')
display(radio_input8)
x
if radio_input7.value=='No CV':
    cv=0
elif radio_input7.value=='5-fold CV':
    cv=int(5)x
elif radio_input7.value=='10-fold CV':
    cv=int(10)
"""
    

model = DL_models(data_icu,
                  diag_flag=True,
                  proc_flag=True,
                  out_flag=True,
                  chart_flag=True,
                  med_flag=True,
                  lab_flag=False,
                  model_type='Hybrid LSTM',
                  k_fold=int(5),
                  oversampling='True',
                  model_name='attn_icu_read',
                  train=True)

#ml=ML_models(data_icu,k_fold=int(5),model_type='Logistic Regression',concat='Conactenate',oversampling='False')