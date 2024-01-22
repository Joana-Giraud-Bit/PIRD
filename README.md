# PIRD
## Introduction about the project
This Github repository is associated with a research project focused on predicting the electrical consumption of domestic hot water using a statistical model. The primary objective is to efficiently store and manage renewable energy for meeting the daily energy needs of buildings. Accurate prediction of a building's energy consumption is essential to aligning it with energy production. The focus of this study is on predicting the electrical energy required for heating domestic hot water, which constitutes a significant portion (7.5-40%) of overall energy consumption according to the International Energy Agency. Reliable predictions can reduce environmental impact by enabling the reliance on renewable energy production.  
However to store energy for heating domestic hot water, a solution involves using a tank that receives solar panel-generated hot water. The challenge is to determining the number of tanks needed, considering whether a signle tank is sufficient for one apartment or should serve a group. Furthermore, we also want to determine the quantity of water required for consistent hot water supply. Calculating the average consumption of apartments provides an indicator for the accumulated amount needed. As solar panel-generated energy is intermittent, determining the required accumulation allows storing enough water during periods of solar availability. The goal is then to identify a timeframe with consistent consumptions patterns, facilitating the sizing of a tank associated with the necessary water volume.  

In order to address these questions, we conducted the following research and developed corresponding code.  

## Detailed folders
First of all, you will come across several folders on this Github repository. The next section provide detailed descriptions of each folder and its contents.  

The `Data` folder contains CSV files with measurements spanning two years, and detailed explanations about the data can be found within that folder.  
The `Code` folder includes the scripts used for the research. Each script is accompanied by a corresponding Jupyter notebook in the `Jupyter Notebook` folder.  
These notebooks provide comprehensive explanations for each line of code, highlight the libraries employed, and offer insights into the rationale behind the coding decisions made during the course of the project.  


## The Code and Jupyter Notebooks' order with their associated paper section
To guide you through our work, we've organized the code in a specific order:  

1- `Average Domestic Hot Water (DHW) and electrical analysis per day per Rive De Gier.py` associated with the `Average_DHW_and_electrical_analysis_per_day_per_Rive_De_Gier.ipynb` Jupyter Notebook.  

1bis- `Average Domestic Hot Water (DHW) and electrical analysis per day per Villefontaine.py` associated with the `Average_DHW_and_electrical_analysis_per_day_per_Villefontaine.ipynb` Jupyter Notebook.  

2-`Data_Visualization_For_One_Apartment` for the Code and Jupyter Notebook.  

3-`Correlation analysis between the apartments` for the Code and Jupyter Notebook.  

4-`Correlation analysis of apartment to themselves` for the Code and Jupyter Notebook.  

There are two versions of the first code, labeled as '1' and '1bis', these versions are essentially identifical but based on different datasets corresponding to different cities. The purpose of having two versions of Code 1 was to study each city and its values independantly, without being influenced by the other. To review the findings and discussions, please refer to the section d.i titled "Average visualization analyzes of the DHW and electrical consumption" in the PDF named `Prediction of electrical consumption of domestic hot water based on statistical model_Joana GIRAUD-BIT`.

Code 2 assists us in visualizing the domestic hot water consumption and electrical consumption linked to hot water for a sole apartment. To review the findings and discussions, please refer to the section d.ii titled "Visualization of the apartments for five-days" in the PDF named `Prediction of electrical consumption of domestic hot water based on statistical model_Joana GIRAUD-BIT`.

Code 3 elaborates on our initial hypothesis, aiming to establish correlations between different apartments. To review the findings and discussions, please refer to the section d.iii titled "Correlation analysis of the apartment together as a time series", d.iv titled "Correlation analysis of the apartments together using each apartment's hourly average of a ten-day period" and d.v titled "Correlation analysis of the apartment together using a three-hours average of a ten-day period" in the PDF named `Prediction of electrical consumption of domestic hot water based on statistical model_Joana GIRAUD-BIT`.

The final Code addresses our second hypothesis, exploring correlations whithin individual apartments. To review the findings and discussions, please refer to the section d.vi titled "Correlation analysis of the apartments and their average with themselves" in the PDF named `Prediction of electrical consumption of domestic hot water based on statistical model_Joana GIRAUD-BIT`.


## Binder link

If you want to test my different codes, you can use this binder link.  

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Joana-Giraud-Bit/PIRD/HEAD)
