# Initial information
This folder contains the CSV files containing the two-years' worth of data collected from two cities : Villefontaine and Rive de Gier.  

## Nomenclature
The nomenclature for each CSV file follows this structure; "number_suffixe code." The number corresponds to the apartment number and the suffixe code denotes the information contained in the CSV files. Specifically, "EC" stands for electrical consumption of the hot water demand and "IECS" for domestic hot water.  

## Explaination of the folders
Within the main folder, there are two subfolders, each housing files associated with the respective city. The main folder, named "Data", contains all the CSV files, while the subfolders contain their corresponding city-associated CSV files.  
This duplication of information was due to maintain data integrity in specific code sections, such as `Average Domestic Hot Water (DHW) and electrical analysis per day per Rive de Gier` and `Average Domestic Hot Water (DHW) and electrical analysis per day per Villefontaine`. This separation ensures that the visualization and analysis for one city is not influenced by potential NaN values from the other city as we remove them in the Code.  

But, the main folder retains all the data as the overarching study containing all apartments. Centralizing all data in one folder simplifies the data analysis process.
