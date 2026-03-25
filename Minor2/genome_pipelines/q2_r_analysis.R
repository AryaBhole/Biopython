# Create output folder
#added dev off after asking ai for error solution
if(!dir.exists("r_output")){
  dir.create("r_output")
}

data <- mtcars

# Save console output to file
sink("r_output/statistical_output.txt")

print("First rows of dataset:")
head(data)

print("Dataset structure:")
str(data)

print("Summary statistics:")
summary(data)

mean_mpg <- mean(data$mpg)
median_mpg <- median(data$mpg)
sd_mpg <- sd(data$mpg)

print(paste("Mean MPG:", mean_mpg))
print(paste("Median MPG:", median_mpg))
print(paste("Standard Deviation MPG:", sd_mpg))

print("Cylinder frequency table:")
table(data$cyl)

print("Correlation between MPG and Horsepower:")
cor(data$mpg, data$hp)

#barplot
png("r_output/barplot_cylinders.png")
barplot(table(data$cyl),
        main="Number of Cars by Cylinders",
        xlab="Cylinders",
        ylab="Count",
        col="skyblue")
dev.off()

#histogram
png("r_output/mpg_histogram.png")
hist(data$mpg,
     main="MPG Distribution",
     xlab="Miles per Gallon",
     col="lightgreen")
dev.off()

#scatterplot
png("r_output/mpg_vs_hp_scatter.png")
plot(data$hp, data$mpg,
     main="MPG vs Horsepower",
     xlab="Horsepower",
     ylab="MPG",
     col="red",
     pch=19)
dev.off()

#boxplot
png("r_output/mpg_boxplot.png")
boxplot(mpg ~ cyl,
        data=data,
        main="MPG by Cylinders",
        xlab="Cylinders",
        ylab="MPG",
        col="orange")
dev.off()

#piechart
png("r_output/cylinder_pie_chart.png")
pie(table(data$cyl),
    main="Cylinder Distribution",
    col=c("lightblue","lightgreen","pink"))
dev.off()

print("All outputs saved in r_output folder")