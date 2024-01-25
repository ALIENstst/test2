import pandas as pd
import numpy as np
from plotnine import *
import matplotlib.pyplot as plt 

N=100
df=pd.DataFrame(dict(group=np.repeat([1,2], N*2),
                     y=np.append(np.append(np.random.normal(5,1,N),np.random.normal(2,1,N)),
                                 np.append(np.random.normal(1,1,N),np.random.normal(3,1,N))),
                     x=np.tile(["A","B","A","B"], N)))
print(df)

base_plot=(ggplot(df, aes(x='x', y= 'y', fill='factor(group)'))  #factor是類別型而不是數字
           +geom_boxplot(outlier_size = 0,colour='k')
           +geom_jitter(aes(group='factor(group)'),
                        shape='o',alpha=0.5, position=position_jitterdodge())
           +scale_fill_manual(values = ("#F8766D","#00BFC4"),guide = guide_legend(title='Group'))
           +theme(
               axis_title=element_text(size=18,face="plain",color="black"),
               axis_text=element_text(size=16,face="plain",color="black"),
               legend_position=(0.8,0.8),
               aspect_ratio =1.05,
               figure_size = (5,5),
               dpi = 100
           ))
  



print(base_plot)