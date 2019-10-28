library(ggplot2)
library(Rmisc)


dfPuntajes = read.csv('tallaFinita.csv')
dfPuntajes = t(dfPuntajes)
colnames(dfPuntajes) <- c("0", "1", "2", "3", "4", "5", "6", "7")

dfPuntajes$X <- rownames(dfPuntajes)

head(dfPuntajes)

p1 <-ggplot(data = dfPuntajes, aes(x = X, y = "X0")) + 
  geom_line(aes(y = "1"))

p1
