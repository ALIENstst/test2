import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib

df = pd.read_csv('Distribution_Data.csv')
df['class'] = pd.Categorical(df['class'], categories=["n", "s", "k", "mm"], ordered=True)

# jitter_plot = (
#     ggplot(df, aes(x='class', y="value", fill="class"))
#     + geom_jitter(width=0.3, size=3, stroke=0.1, show_legend=False)
#     + stat_summary(fun_data="mean_sdl", fun_args={'mult': 1}, geom="pointrange", color="black", size=0.5, show_legend=False)
#     # +stat_summary(fun_data="mean_sdl", fun_args = {'mult':1},geom="point", fill="w",color = "black",size = 5,stroke=1,show_legend=False)
#     + geom_point(stat="summary", fun_data="mean_sdl", fun_args={'mult': 1}, fill="w", color="black", size=2, stroke=0.5, show_legend=False)
#     + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
#     # +theme_matplotlib()  # 試著將這一行注釋掉
#     + theme(
#         # legend_position='none',
#         aspect_ratio=1.05,
#         dpi=100,
#         figure_size=(4, 4)
#     )
# )
# print(jitter_plot)  
print(df)
Barjitter_plot = (ggplot(df,aes(x='class',y='value',fill='class'))
# +stat_summary(fun_data="mean_sdl",fun_args={'mult':1},geom="bar",color="black",size=0.75,width=0.5,show_legend=False)
# +stat_summary(fun_data="mean_sdl",fun_args={'mult':1},geom="errorbar",color="black",size=0.75,width=0.2,show_legend=False)
+ stat_summary(fun_data="mean_cl_boot", geom="bar", color="black", size=0.75, width=0.5, show_legend=False)
+ stat_summary(fun_data="mean_cl_boot", geom="errorbar", color="black", size=0.4, width=0.1, show_legend=False)
+scale_fill_hue(s=0.9,l=0.65,h=0.0417,color_space='husl')
+ylim(0,7)
+theme(aspect_ratio=1.05,
       dpi=100,
       figure_size=(4, 4)))

print(Barjitter_plot)