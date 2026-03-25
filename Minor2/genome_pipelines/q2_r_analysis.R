data("ToothGrowth")
head(ToothGrowth)

# Summary statistics
summary_stats <- summary(ToothGrowth)

# Mean tooth length
mean_len <- mean(ToothGrowth$len)

# Median tooth length
median_len <- median(ToothGrowth$len)

# Standard deviation
sd_len <- sd(ToothGrowth$len)

# Create statistics table
stats_table <- data.frame(
  Mean = mean_len,
  Median = median_len,
  SD = sd_len
)
print(stats_table)

write.csv(stats_table, "r_output/statistics_table.csv")

group_mean <- aggregate(len ~ supp, data = ToothGrowth, mean)

print(group_mean)

write.csv(group_mean, "r_output/group_mean.csv")

# Histogram
png("r_output/histogram.png")
hist(ToothGrowth$len,
     main = "Histogram of Tooth Length",
     xlab = "Tooth Length",
     col = "lightblue")
dev.off()

# Boxplot
png("r_output/boxplot.png")
boxplot(len ~ supp,
        data = ToothGrowth,
        main = "Tooth Length by Supplement",
        xlab = "Supplement Type",
        ylab = "Tooth Length",
        col = c("orange","green"))
dev.off()

# Bar Plot (Mean Tooth Length)
png("r_output/barplot.png")
barplot(group_mean$len,
        names.arg = group_mean$supp,
        main = "Average Tooth Length by Supplement",
        xlab = "Supplement",
        ylab = "Mean Length",
        col = "purple")
dev.off()

# Scatter Plot
png("r_output/scatterplot.png")
plot(ToothGrowth$dose,
     ToothGrowth$len,
     main = "Dose vs Tooth Length",
     xlab = "Dose",
     ylab = "Tooth Length",
     col = "red",
     pch = 19)
dev.off()

cat("Analysis complete. Output saved in r_output folder.")