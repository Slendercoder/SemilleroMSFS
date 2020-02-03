library(ggplot2)
library(Rmisc)
library(dplyr)

dfPuntajes = read.csv('agentes.csv')
head(dfPuntajes)

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
