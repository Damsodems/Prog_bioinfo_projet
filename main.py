#projet Cetinsoy

#librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

#imports des csv, renommage et nettoyage

coverage_by_country = pd.read_csv('art_coverage_by_country_clean.csv').dropna()
children_coverage_by_country = pd.read_csv('art_pediatric_coverage_by_country_clean.csv').dropna()
nbr_adults_cases_15_to_49 = pd.read_csv('no_of_cases_adults_15_to_49_by_country_clean.csv').dropna()
nbr_of_death_by_country = pd.read_csv('no_of_deaths_by_country_clean.csv').dropna()
nbr_of_people_living_with_hiv = pd.read_csv('no_of_people_living_with_hiv_by_country_clean.csv').dropna()
prevention_mother_chil_by_country = pd.read_csv('prevention_of_mother_to_child_transmission_by_country_clean.csv').dropna()


#Utilisation premier csv : art_coverage_by_country_clean.csv

#création d'un nouveau data frame pour montrer dans quels pays les personnes avec le VIH reçoivent le plus un traitement antirétroviraux
coverage_ART_HIV = coverage_by_country[['Country','Estimated ART coverage among people living with HIV (%)_median']]
coverage_ART_HIV = coverage_ART_HIV.sort_values(by = ['Estimated ART coverage among people living with HIV (%)_median'], ascending=False)

#création d'un nouveau data frame pour créer une carte montrant quels sont les pays les plus touchés par le VIH
map_nbr_hiv_people = coverage_by_country[['Country', 'Estimated number of people living with HIV_median']]

#création de la map de la répartion du nombre de personne vivant avec le VIH par pays


#Utilisation second csv : art_pediatric_coverage_by_country_clean.csv




#nettoyage

