import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import os

from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import SVC
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from datetime import date
