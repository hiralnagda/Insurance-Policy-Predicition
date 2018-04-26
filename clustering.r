myRdata<-read.csv("insurance_data5.csv",header=TRUE)
myRdata.features=myRdata
myRdata.features=myRdata
View(myRdata.features)
myRdata.features$policy_number<-NULL
myRdata.features$Occupation<-NULL
myRdata.features$Smoking.and.alcohol<-NULL
myRdata.features$Weight<-NULL
myRdata.features$Height<-NULL
myRdata.features$Policy1<-NULL
myRdata.features$Policy2<-NULL
myRdata.features$Term<-NULL
myRdata.features$sumAssured<-NULL
myRdata.features$Regularity<-NULL
myRdata.features$Po<-NULL
results<-kmeans(myRdata.features,8)
results
results$cluster
table(results$cluster,myRdata$Policy1)
plot(myRdata[c("Age","Income")],col=results$cluster)
plot(myRdata[c("Age","Income")],col=myRdata$Policy1)



