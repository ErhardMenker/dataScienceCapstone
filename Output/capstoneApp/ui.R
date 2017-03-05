#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

    sidebarLayout(
        sidebarPanel(
            # Copy the line below to make a text input box
            textInput("text", label = h4("Input Sentence Fragment:"), value = ""),
            checkboxInput(inputId = "PredictOn", label = "Turn on Predictor?", value = FALSE),
            submitButton("Predict")
        ),
        
        mainPanel(
            h4("Prediction:"),
            hr(),
            fluidRow(column(3, verbatimTextOutput("value")))
        )
    )
))
