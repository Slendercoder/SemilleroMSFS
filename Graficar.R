library(ggplot2)
library(Rmisc)


dfPuntajes = read.csv('tallaFinita.csv')
head(dfPuntajes)

g1 <- ggplot(dfPuntajes) +
  geom_line()

