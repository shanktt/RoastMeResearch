#!/usr/bin/env Rscript

library(RedditExtractoR)

posts <- read.csv("Jan_2020_Posts.csv")
urls <- posts$full_link
postsData <- get_thread_content(urls)

write.csv(postsData$comments, file="Jan_2020_Comments.csv", fileEncoding = "UTF-8")
write.csv(postsData$threads, file="Jan_2020_Threads.csv", fileEncoding = "UTF-8")





