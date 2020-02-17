library(ggplot2)
library(Rmisc)
library(dplyr)
library(gapminder)

dfPuntajes = read.csv('/home/lovelace/Semillero/agentes.csv')

head(dfPuntajes,2) # head(<object>, <range>): returns all entrance in <object>'s file between range [0,<range>]
tail(dfPuntajes,3) # tail(<object>, <range>): returns all entrance in <object>'s file between range [<range>, len(<object>)]

df_summary <- dfPuntajes %>% dplyr::group_by(Ronda,Politica) %>% dplyr::summarise(PuntajePromedioPorPoliticaCadaRonda = mean(Puntaje, na.rm=TRUE))
head(df_summary)

p1 <- ggplot(data = df_summary, aes(x=Ronda, y=PuntajePromedioPorPoliticaCadaRonda, group=Politica, color=Politica)) + geom_line(size=0.5) + labs(color = "Politica") + theme_bw()
p1

p2 <- ggplot(data = df_summary, aes(Ronda, PuntajePromedioPorPoliticaCadaRonda)) + geom_point(aes(color = factor(Politica), size=Politica), alpha=0.5)
p2

p3 <- ggplot(data = df_summary, aes(Ronda, PuntajePromedioPorPoliticaCadaRonda)) + geom_point(aes(color = factor(Politica)), alpha=0.5) + facet_wrap(~factor(Politica))
p3

p4 <- ggplot(data = df_summary, aes(Ronda, PuntajePromedioPorPoliticaCadaRonda)) + geom_point(aes(color = factor(Politica)), alpha=0.5) + facet_wrap(~factor(Politica), scale="free")
p4
