#Librairies
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import altair as alt
from PIL import Image

#Import csv
coverage_by_country = pd.read_csv('art_coverage_by_country_clean.csv').dropna()
children_coverage_by_country = pd.read_csv('art_pediatric_coverage_by_country_clean.csv').dropna()
nbr_adults_cases_15_to_49 = pd.read_csv('no_of_cases_adults_15_to_49_by_country_clean.csv').dropna()
nbr_of_death_by_country = pd.read_csv('no_of_deaths_by_country_clean.csv').dropna()
nbr_of_people_living_with_hiv = pd.read_csv('no_of_people_living_with_hiv_by_country_clean.csv').dropna()
prevention_mother_chil_by_country = pd.read_csv('prevention_of_mother_to_child_transmission_by_country_clean.csv').dropna()


#Title
st.title("Rétrospective sur l'évolution du Sida ces dernières années dans le monde")
st.markdown("Projet Bioinformatique Semestre 1 - Python")

st.sidebar.title("Navigation")
st.sidebar.markdown("Ici vous pourrez choisir ce que vous voulez voir sur le dashboard")

#Introduction
if not st.sidebar.checkbox("Masquer la vidéo de présentation", True, key='5'):
    st.header("15 minutes pour en apprendre plus sur le sida")
    st.subheader("- By Inserm")
    video_file = open('Sida.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


#Affichage des csv
st.sidebar.header("Nos CSV")
select = st.sidebar.selectbox('Naviguer parmi nos csv', ['art_coverage_by_country_clean', 'art_pediatric_coverage_by_country_clean', 'nbr_of_cases_adults_15_to_49_by_country_clean', 'nbr_of_deaths_by_country_clean', 'nbr_of_people_living_with_hiv_by_country_clean', 'prevention_of_mother_to_child_transmission_by_country_clean'], key='1')

if not st.sidebar.checkbox("Masquer", True, key='1'):
    st.title("Nos CSV")
    if select == 'art_coverage_by_country_clean':
        st.markdown('art_coverage_by_country_clean')
        st.dataframe(coverage_by_country)
    else :
        if select == 'art_pediatric_coverage_by_country_clean':
            st.markdown('art_pediatric_coverage_by_country_clean')
            st.dataframe(children_coverage_by_country)
        else :
            if select == 'nbr_of_cases_adults_15_to_49_by_country_clean':
                st.markdown('nbr_of_cases_adults_15_to_49_by_country_clean')
                st.dataframe(nbr_adults_cases_15_to_49)
            else :
                if select == 'nbr_of_deaths_by_country_clean':
                    st.markdown('nbr_of_deaths_by_country_clean')
                    st.dataframe(nbr_of_death_by_country)
                else :
                    if select == 'nbr_of_people_living_with_hiv_by_country_clean':
                        st.markdown('nbr_of_people_living_with_hiv_by_country_clean')
                        st.dataframe(nbr_of_people_living_with_hiv)
                    else :
                        st.markdown('prevention_of_mother_to_child_transmission_by_country_clean')
                        st.dataframe(prevention_mother_chil_by_country)


#Fct évolution du nombre de personne malade du HIV par pays
def graphByCountry(mytab=None):
    if mytab.empty:
        return 'Nous ne possèdons pas les données du pays que vous venez de sélectionner'
   
    st.header('Evolution du nombre de personne vivant avec le HIV en ' + select2)
    fig = go.Figure(data=go.Scatter(x = mytab['Year'], y =mytab['Count_median']))
    fig.update_layout(title = None, xaxis_title = 'Année', yaxis_title = 'Personne vivant avec le HIV')
    st.plotly_chart(fig)
    

st.sidebar.title("Evolution du nombre de personne malade du HIV par pays")
select2 = st.sidebar.text_input("Entrer le nom du pays dont vous voulez connaître les données")
graphByCountry(nbr_of_people_living_with_hiv[(nbr_of_people_living_with_hiv['Country'] == select2)])


#Fct répartition des cas en fonction des différentes régions du monde

#réarrangement du csv : no_of_people_living_with_hiv_by_country_clean.csv pour l'affichage
nbr_of_people_living_with_hiv_2000 = nbr_of_people_living_with_hiv[(nbr_of_people_living_with_hiv['Year'] == 2000)]
nbr_of_people_living_with_hiv_2005 = nbr_of_people_living_with_hiv[(nbr_of_people_living_with_hiv['Year'] == 2005)]
nbr_of_people_living_with_hiv_2010 = nbr_of_people_living_with_hiv[(nbr_of_people_living_with_hiv['Year'] == 2010)]
nbr_of_people_living_with_hiv_2018 = nbr_of_people_living_with_hiv[(nbr_of_people_living_with_hiv['Year'] == 2018)]

#Mise en place de l'histogramme
st.sidebar.title("Régions du monde et nombre de cas")
date_data = st.sidebar.radio("Choisir l'année que vous voulez étudier", ('2000', '2005', '2010', '2018'), key = '2')

if not st.sidebar.checkbox("Masquer", True, key='2'):
    if date_data == '2000':
        st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2000")
        graph = nbr_of_people_living_with_hiv_2000.groupby("WHO Region").sum()['Count_median']
        st.bar_chart(graph)
    else :
        if date_data == '2005':
            st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2005")
            graph = nbr_of_people_living_with_hiv_2005.groupby("WHO Region").sum()['Count_median']
            st.bar_chart(graph)
        else :
            if date_data == '2010':
                st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2010")
                graph = nbr_of_people_living_with_hiv_2010.groupby("WHO Region").sum()['Count_median']
                st.bar_chart(graph)
            else : 
                st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2018")
                graph = nbr_of_people_living_with_hiv_2018.groupby("WHO Region").sum()['Count_median']
                st.bar_chart(graph)
        
        
#Affichage des classements des pays

#Classement des pays par rapport au pourcentage de gesn traités parmis les personnes malades
coverage_ART_HIV = coverage_by_country[['Country','Estimated ART coverage among people living with HIV (%)_median']]
coverage_ART_HIV = coverage_ART_HIV.sort_values(by = ['Estimated ART coverage among people living with HIV (%)_median'], ascending=False)

#Classement des pays par rapport au pourcentage du niveau de prévention de transmission de la maladie de la mère à son enfant
table_prevention_mother_child = prevention_mother_chil_by_country[['Country','Percentage Recieved_median']]
table_prevention_mother_child = table_prevention_mother_child.sort_values(by = ['Percentage Recieved_median'], ascending=False)

#Choix du graphique
select3 = st.sidebar.selectbox("Choisissez le graphique que vous souhaitez voir", ['Gens traités parmis les personnes malades', 'Prévention de transmission de la maladie de la mère à son enfant'], key='3')

if not st.sidebar.checkbox("Masquer", True, key='3'):
    if select3 == 'Gens traités parmis les personnes malades':
        #graphique
        st.header("Classement des pays par rapport au pourcentage de gesn traités parmis les personnes malades")
        fig = px.bar(coverage_ART_HIV, y='Estimated ART coverage among people living with HIV (%)_median', x='Country', text='Estimated ART coverage among people living with HIV (%)_median')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.write(fig)

        #carte
        image1 = Image.open('HIV_receive_ART.jpg')
        st.header("Accès au traitement antiviral par pays")
        st.image(image1, caption = 'carte extraite du site : Science et avenir', use_column_width = True)

    else:
        st.header("Classement des pays par rapport au pourcentage du niveau de préventi on de transmission de la maladie de la mère à son enfant")
        fig = px.bar(table_prevention_mother_child, y = 'Percentage Recieved_median', x ='Country', text = 'Percentage Recieved_median')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.write(fig)


#Création de la map
def plot_map(df, col, pal):
    df = df[df[col] > 0]
    fig = px.choropleth(df, locations="Country", locationmode='country names',
                  color=col, hover_name="Country",
                  title=col, color_continuous_scale=pal,width=1500)
    fig.show()

st.sidebar.title("Nos Cartes")
st.sidebar.write("Ces maps représentent un comptage d'objets par pays")
opt = st.sidebar.selectbox("Choissisez une option pour la map",["Cas", "Morts","Vivant"])
if not st.sidebar.checkbox("Masquer", True, ):
    if (opt == "Cas"):
        plot_map(nbr_adults_cases_15_to_49, 'Count_median', 'matter')
    elif(opt == "Morts"):
        plot_map(nbr_of_death_by_country, 'Count_median', 'matter')
    elif(opt == "Vivant"):
        plot_map(nbr_of_people_living_with_hiv, 'Count_median', 'matter')


#plot en images
st.sidebar.title("Comparaison du nombre de Cas et du nombre de Morts par régions")
if st.sidebar.button("Appuyez ici"):
    col1, col2 = st.beta_columns(2)
    #col1
    col1.header("Nombre de cas")
    #bn_cas = cases.groupby(['WHO Region']).agg({'Count_median': 'sum'})
    #fig1 = plt.figure(figsize=(10, 5))
    #sns.barplot(bn_cas.index, bn_cas["Count_median"]).set_title("Nombre de cas par région");
    #fig1.show()
    #col1.fig1.show()
    img = Image.open("Nombre_de_cas.jpg")
    col1.image(img, use_column_width=True)
    #col2
    col2.header("Nombre de mort")
    img2 = Image.open("nombre_de_mort.jpg")
    col2.image(img2, use_column_width=True)


#Surprise
st.sidebar.title("Pour la fin.. ")
if st.sidebar.button("Surprise !"):
    st.balloons()
    st.success('Fin de la presentation')