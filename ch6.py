import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import *
import matplotlib.pyplot as plt 
import matplotlib

from plotnine import *
from plotnine.data import mpg
# print(mpg)
# t = (ggplot(mpg, aes('cty', 'hwy', fill='fl'))
#      + geom_point()
#      + facet_grid('year~fl')
#      + theme(text=element_text(size=12, colour="black"),
#              strip_text=element_text(size=15, colour="black"),
#              strip_background=element_rect(color='k'),
#              aspect_ratio=1.3,
#              dpi=100,
#              figure_size=(10, 10)
#              ))


# t = (ggplot(mpg, aes('cty', 'hwy', fill='fl'))
#      + geom_point()
#      + facet_wrap('~fl')
#      + theme(text=element_text(size=12, colour="black"),
#              strip_text=element_text(size=15, colour="black"),
#              strip_background=element_rect(color='k'),
#              aspect_ratio=1.3,
#              dpi=100,
#              figure_size=(10, 10)
#              ))


t = (ggplot(mpg, aes('cty', 'hwy', fill='fl'))
     + geom_point()
     + facet_grid('drv~fl',scales="free")            #scales="free" 分面網格中的每個子圖都擁有獨立的刻度。
     + theme(text=element_text(size=12, colour="black"),
             strip_text=element_text(size=15, colour="black"),
             strip_background=element_rect(color='k'),
             aspect_ratio=1.3,
             dpi=100,
             figure_size=(10, 10)
             ))

print(t)