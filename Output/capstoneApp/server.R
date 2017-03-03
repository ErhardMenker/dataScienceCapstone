#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define server logic required to draw a histogram
shinyServer(function(input, output) { 
   
    # show the next word if prediction requested & button submitted, else show empty string 
    output$value <- reactive({
        ifelse(input$PredictOn, predictNextWord(input$text), "")
    }) 
  
}) 
