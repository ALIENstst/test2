import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib

# N = 20
# df1 = pd.DataFrame(dict(x=np.sort(np.random.randn(N)),y=np.sort(np.random.randn(N))))
# df2 = pd.DataFrame(dict(x=df1.x+0.3*np.sort(np.random.randn(N)),y=df1.y+0.1*np.sort(np.random.randn(N))))

# p1 = (ggplot(df1,aes('x','y'))+
#       geom_line(aes(colour='x+y'),size=1.5)+
#       geom_point(aes(fill='x+y'),shape='o',size=5,color="black")+
#       scale_fill_distiller(name="point",palette="YlOrRd")+
#       scale_color_distiller(name="line",palette="Blues"))


# print(p1)



N = 20
df1 = pd.DataFrame(dict(x=np.sort(np.random.randn(N)),y=np.sort(np.random.randn(N))))
df2 = pd.DataFrame(dict(x=df1.x+0.3*np.sort(np.random.randn(N)),y=df1.y+0.1*np.sort(np.random.randn(N))))
print(df1)
p1 = (ggplot()+
      geom_line(aes('x','y',colour='x+y'),df1,size=1.5)+
      geom_point(aes('x','y',fill='x+y'),df2,shape='o',size=5,color="black")+
      scale_fill_distiller(name="point",palette="YlOrRd")+
      scale_color_distiller(name="line",palette="Blues"))


print(p1)