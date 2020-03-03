library(ggplot2)
library(Rmisc)
library(dplyr)
#library(plotly)
library("gridExtra")


dfPuntajes = read.csv('agentes.csv')
#dfPuntajes = read.csv('alatorio.csv')
dfPuntajes = read.csv('coordinado.csv')
dfPuntajes = read.csv('nocoordinado.csv')


#dfPuntajes$Estado = as.numeric(levels(dfPuntajes$Estado))[dfPuntajes$Estado]
#dfPuntajes$Ronda = as.numeric(levels(dfPuntajes$Ronda))[dfPuntajes$Ronda]
#dfPuntajes$Politica = lapply(dfPuntajes$Politica, function(x) factor(x))
#dfPuntajes$Politica = factor(dfPuntajes$Politica)

#typeof(dfPuntajes$Estado)
#head(dfPuntajes)

#dfPuntajes = dfPuntajes[dfPuntajes$Identificador ==1100, ]
##################################################################################################
# Dibuja proporcion de asistencia por ronda
##################################################################################################

df_summary <- dfPuntajes %>% # the names of the new data frame and the data frame to be summarised
  dplyr::group_by(Ronda) %>%   # the grouping variable
  dplyr::summarise(Asistencia = mean(Estado, na.rm=TRUE),  # calculates the mean of each group
                   sd_RD = sd(Estado, na.rm=TRUE), # calculates the standard deviation of each group
                   n_RD = n()) # calculates the standard error of each group
head(df_summary)

p1 <- ggplot(data = df_summary, aes(x=Ronda, y=Asistencia)) + 
  geom_line(size=0.9) +
  geom_ribbon(aes(ymin = Asistencia - sd_RD,
                  ymax = Asistencia + sd_RD), alpha = 0.2) +
#  ylim(c(-0.1,1.1)) +
  labs(color = "Identificador") +
  theme_bw()+ggtitle("Asistencia Por Ronda")

p1


##################################################################################################
# Dibuja GRAFICA_PUNTAJE-Promedio-Politica_VS_RONDA => ESTEBAN
##################################################################################################

df_summary <- dfPuntajes %>% # the names of the new data frame and the data frame to be summarised
  dplyr::group_by(Identificador, Ronda) %>%   # the grouping variable
  dplyr::summarise(Asistencia = mean(Estado, na.rm=TRUE),  # calculates the mean of each group
                   sd_RD = sd(Estado, na.rm=TRUE), # calculates the standard deviation of each group
                   n_RD = n()) # calculates the standard error of each group
head(df_summary)

p2 <- ggplot(data = df_summary, aes(x=Ronda, y=Asistencia)) + 
  geom_line(size=0.9) +
  #  geom_ribbon(aes(ymin = Asistencia - sd_RD,
  #                  ymax = Asistencia + sd_RD), alpha = 0.2) +
  #  ylim(c(-0.1,1.1)) +
  labs(color = "Identificador") +
  theme_bw()+ggtitle("Politica vs Ronda")

p2

##################################################################################################
# Dibuja GRAFICA_USO-Politica_VS_RONDA => MIGUEL
##################################################################################################

dUso<- dfPuntajes %>% # the names of the new data frame and the data frame to be summarised
  dplyr::group_by(Identificador, Ronda,Politica)# Agrupando por grupo,Identificador,Politica


dUso = count(dUso,Politica,name = "n") # Conteo de rondas por politicas vs ronda
dUso$Politica <- as.character(dUso$Politica) # Convirtiendo el valor n?merico de politica a categorico/String

head(dUso)

p3 <- ggplot(data = dUso, aes(x=Ronda, y=n, group=Politica, colour=Politica)) + 
  geom_line(alpha=0.4)+labs(y="Uso de Politica",title="Uso Vs Ronda")+ggtitle("Politica vs Ronda")

p3

#------------------GRAFICA INTERACTIVA -------------------------#

dUso2 = data.frame(dUso) #Convirtiendo a dataframe para que plotly lo lea sin problemas

p2 <- plot_ly(data = dUso2, x=~Ronda,y=~n,color=~Politica) %>%
  add_lines() %>% 
    layout(
      title ="Uso vs Ronda",
        xaxis=list(title="Ronda"),
        yaxis=list(title="Uso")
      )

p2

##################################################################################################
# Dibuja GRAFICA INDIVIDUAL => MIGUEL
##################################################################################################

dfPuntajes2 = dfPuntajes[complete.cases(dfPuntajes),]
p4 <- ggplot(dfPuntajes2,aes(x=Puntaje,y=Consistencia))+geom_point(alpha = 0.5)+ggtitle("Consistencia individual de agentes")
p4

##################################################################################################
# Dibuja GRAFICA PUNTAJE POR RONDA => MIGUEL
##################################################################################################
dfpuntaje1 <- dfPuntajes  %>%
  group_by(Ronda) %>%   # the grouping variable
  dplyr::summarise(Puntaje_Promedio = mean(cumsum(Puntaje), na.rm=TRUE),
                   sd_RD = sd(Puntaje, na.rm=TRUE))  # calculates the mean of each group)
cumsum(dfPuntajes$Puntaje)
dfpuntaje1

p5 <- ggplot(data = dfpuntaje1, aes(x=Ronda, y=Puntaje_Promedio)) + 
  geom_line(size=0.9) +
  geom_ribbon(aes(ymin = Puntaje_Promedio - sd_RD,
                  ymax = Puntaje_Promedio + sd_RD), alpha = 0.2) +
  #  ylim(c(-0.1,1.1)) +
  labs(color = "Identificador") +
  theme_bw()+ggtitle("Puntaje Acumulado vs Ronda")

p5


##################################################################################################
# GRAFICAS UNIDAS
##################################################################################################

grid.arrange(p1, p3,p4,p5, nrow = 2,top="No Coordinado")
