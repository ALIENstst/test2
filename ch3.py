import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd 

#plt.rc('font',family='Times New Roman')
matplotlib.rcParams['font.family'] = 'Times New Roman'

df=pd.read_csv("Facet_Data.csv")
p1=(ggplot(df, aes(x='SOD',y='tau',fill='Class',shape='Class')) + 
    geom_point(color="black",stroke=0.25,alpha=0.8)+
    scale_size(range = (1, 6))+
    scale_shape_manual(values=('o','s','D'))+
    theme(text=element_text(size=12,colour = "black"),
        aspect_ratio =1,
        dpi=100,
       figure_size=(4,4))) #shape=21,color="black",fill="red",size=3,stroke=0.1
print(p1)

anova_result = f_oneway(
    df[df['Class'] == 'Control']['age'],
    df[df['Class'] == 'Impaired']['age'],
    df[df['Class'] == 'Uncertain']['age'],
)

# One-way ANOVA
print("ANOVA Result:")
print("F-statistic:", anova_result.statistic)
print("P-value:", anova_result.pvalue)

# Tukey's Range Test
tukey_result = pairwise_tukeyhsd(df['age'], df['Class'])
print("\nTukey's Range Test:")
print(tukey_result)