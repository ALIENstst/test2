import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib


df= pd.read_csv("logarithmic_scale.csv")
df_melt=pd.melt(df,id_vars='VIN(V)',var_name='Class',value_name='value')
print(df_melt)
p1=(ggplot(df_melt,aes(x='VIN(V)',y='value',color='Class')) + 
  geom_line(size=1)+
  scale_x_continuous(breaks=np.arange(-20,21,5),limits=(-20,20)) +
  scale_y_log10(name='log(value)',limits=(0.00001,10))+
  scale_color_manual(values=("#36BED9","#FF0000"))+
  theme_classic()+
  theme(text=element_text(size=12,colour = "black"),
        # panel_grid_major=element_line(color="#C7C7C7",linetype ='--'),
        aspect_ratio =0.8,
        dpi=100,
       figure_size=(5,5),
     legend_position=(0.8,0.8),
     legend_background=element_rect(fill="none")))

print(p1)
