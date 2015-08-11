# define plot variable 
library(ggplot2)

# below is for scale_x_date and melt
library(scales)
library(reshape)

setwd("~/GitHub/NofMe")
list.files()
dat = read.table(
  "daily"
  ,header = TRUE
  ,sep ="\t"
  ,as.is = TRUE
  ,fill = TRUE
  )

dat2 = dat

# define dates as dates
dat2$Date = as.Date(dat2$Date, "%d/%m/%Y")

dat2 = dat2[order(dat2$Date),]


# make all but 'Date' numeric
for (i in 2:length(dat2[1,]) ) {
  dat2[,i] = as.numeric(dat2[,i])
}


# scale all but 'Date'
#for (i in 2:length(dat2[1,]) ) {
#  dat2[,i] = scale(dat2[,i], center = TRUE)
#}


# redo data frame 
dat2 = melt(dat2, id ="Date", variable_name = "Parameter")

# get rid NAs now
dat2 = dat2[complete.cases(dat2),]

# all in one
#ggplot(dat2, aes(Date,value))+
#  geom_line(aes(colour = Parameter))

# in all different ones
ggplot(dat2, aes(Date,value))+
  geom_line()+
  facet_grid(Parameter ~ ., scales = "free_y")+
  scale_x_date(labels = date_format("%d-%b"))
  

#for (i in 2:length(nm)){
#  print(
#    qplot(Date, nm[i], data = dat2, geom = "line")+
#      scale_x_date(labels = date_format("%d-%b") )+
#      labs(title = nm[i])
#  )
#}

# look for correlations, so aggregate first
