#import essential basics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pprint import pprint

#import error quantifying metrics
from sklearn.metrics import mean_squared_error as mse, mean_absolute_error as mae

#import data preprocessing modules
from sklearn import preprocessing as pp
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

#import all useful regression and ML models
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

#We need to access modules from the project root, so we select this directory.
import os, sys

#importing relevant modules for time series regression, residual analysis and SARIMA fitting
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from scipy.stats import norm
from statsmodels.tsa.statespace.sarimax import SARIMAX
