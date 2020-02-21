library(ggplot2)
library(Rmisc)
library(dplyr)
library(plotly)

dfPuntajes = read.csv('agentes.csv')
dfPuntajes$Estado = as.numeric(dfPuntajes$Estado)
head(dfPuntajes)

dfPuntajes = dfPuntajes[dfPuntajes$Identificador ==1100, ]
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
  theme_bw()

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

p1 <- ggplot(data = df_summary, aes(x=Ronda, y=Asistencia, group=Identificador, color=Identificador)) + 
  geom_line(size=0.9) +
  #  geom_ribbon(aes(ymin = Asistencia - sd_RD,
  #                  ymax = Asistencia + sd_RD), alpha = 0.2) +
  #  ylim(c(-0.1,1.1)) +
  labs(color = "Identificador") +
  theme_bw()

p1

##################################################################################################
# Dibuja GRAFICA_USO-Politica_VS_RONDA => MIGUEL
##################################################################################################

dUso<- dfPuntajes %>% # the names of the new data frame and the data frame to be summarised
  dplyr::group_by(Identificador, Ronda,Politica) # Agrupando por grupo,Identificador,Politica


dUso = count(dUso,Politica, wt = NULL, sort = FALSE, name = "n") # Conteo de rondas por politicas vs ronda
dUso$Politica <- as.character(dUso$Politica) # Convirtiendo el valor n?merico de politica a categorico/String

#head(dUso)

p1 <- ggplot(data = dUso, aes(x=Ronda, y=n, group=Politica, colour=Politica)) + 
  geom_line(alpha=0.4)+labs(y="Uso de Politica",title="Uso Vs Ronda")

p1

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
