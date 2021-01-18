import streamlit as st
import pandas as pd
import numpy as np
import bokeh
import matplotlib as plt
import plotly.graph_objects as go
import seaborn as sns
from PIL import Image
import plotly.express as px



#loading files
#attention à set les index plus tard!!!

@st.cache
def load_art():
    data = pd.read_csv('art_coverage_by_country_clean.csv', )
    return data

@st.cache
def load_art_ped():
    data = pd.read_csv('art_pediatric_coverage_by_country_clean.csv')
    return data

@st.cache
def load_cases():
    data = pd.read_csv('no_of_cases_adults_15_to_49_by_country_clean.csv')
    return data

@st.cache
def load_deaths():
    data = pd.read_csv('no_of_deaths_by_country_clean.csv')
    return data

@st.cache
def load_living():
    data = pd.read_csv('no_of_people_living_with_hiv_by_country_clean.csv')
    return data

@st.cache
def load_prevention():
    data = pd.read_csv('prevention_of_mother_to_child_transmission_by_country_clean.csv')
    return data


#Traitement des CSV
art = load_art()#df
art_ped = load_art_ped()#df
cases = load_cases()#df
deaths = load_deaths()#df
living = load_living()#df
prevention = load_prevention()#df

art = art.dropna()
art_ped = art_ped.dropna()
cases = cases.dropna()
deaths = deaths.dropna()
living = living.dropna()
prevention = prevention.dropna()





#Traitement du Streamlit pure
#def main

#st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Rétrospective sur l'évolution du Sida ces dernières années dans le monde")
st.markdown("Projet Bioinformatique Semestre 1 - Python")

st.sidebar.title("Navigation")
st.sidebar.markdown("Ici vous pourrez choisir ce que vous voulez voir sur le dashboard")

# Affichage des csv
st.sidebar.title("Nos CSV")
select = st.sidebar.selectbox('Naviguer parmi nos csv',
                              ['art', 'art_ped',
                               'cases', 'deaths',
                               'living',
                               'prevention'], key='1')

if not st.sidebar.checkbox("Hide", True, key='1'):
    st.title("Nos CSV")
    if select == 'art':
        st.markdown('art')
        st.dataframe(art)
    else:
        if select == 'art_ped':
            st.markdown('art_ped')
            st.dataframe(art_ped)
        else:
            if select == 'cases':
                st.markdown('cases')
                st.dataframe(cases)
            else:
                if select == 'deaths':
                    st.markdown('deaths')
                    st.dataframe(deaths)
                else:
                    if select == 'living':
                        st.markdown('living')
                        st.dataframe(living)
                    else:
                        st.markdown('prevention')
                        st.dataframe(prevention)


# Fct évolution du nombre de personne malade du HIV par pays
def graphByCountry(mytab=None):
    if mytab.empty:
        return 'Nous ne possèdons pas les données du pays que vous venez de sélectionner'

    fig = go.Figure(data=go.Scatter(x=mytab['Year'], y=mytab['Count_median']))
    fig.update_layout(title='Evolution du nombre de personne vivant avec le HIV en ' + select2, xaxis_title='Année',
                      yaxis_title='Personne vivant avec le HIV')
    st.plotly_chart(fig)


st.sidebar.title("Evolution du nombre de personne malade du HIV par pays")
select2 = st.sidebar.text_input("Entrer le nom du pays dont vous voulez connaître les données")
graphByCountry(living[(living['Country'] == select2)])

#if st.button("Presentation"):
 #   st.write("Nos fichier representent les données concernant le VIH et le SIDA ")



st.sidebar.header("Région")
# Create a list of possible values and multiselect menu with them in it
st.sidebar.subheader("Choisissez une ou plusieurs régions:")
REG = art['WHO Region'].unique()
region = st.sidebar.multiselect("Régions", REG)

# Mask to filter dataframe
mask_region = art['WHO Region'].isin(REG)

art_region = art.copy()
art_region = art[mask_region]


coveragebyregion1 = art_region.groupby("WHO Region").mean()["Estimated ART coverage among people living with HIV (%)_median"]
#st.bar_chart(coveragebyregion1)

st.write(region)
#("Europe","Africa","Americas","Eastern Mediterranean","South-East Asia", "Western Pacific")

#"""for regions in region.values():
#  if (regions == "Europe"):
#       mask_Euro = art["WHO Region"] == "Europe"
#       mask_region = mask_Euro
 #   elif (regions == "Africa"):
#      mask_Afr = art["WHO Region"] == "Africa"
#       mask_region = mask_region & mask_Afr
 #   elif (regions == "Americas"):
#      mask_Ame = art["WHO Region"] == "Americas"
#       mask_region = mask_region & mask_Ame"""


st.sidebar.header("Comparaison du nombre de Cas et du nombre de Morts par régions")
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

nbr_of_people_living_with_hiv_2000 = living[(living['Year'] == 2000)]
nbr_of_people_living_with_hiv_2005 = living[(living['Year'] == 2005)]
nbr_of_people_living_with_hiv_2010 = living[(living['Year'] == 2010)]
nbr_of_people_living_with_hiv_2018 = living[(living['Year'] == 2018)]

# Mise en place de l'histogramme
st.sidebar.title("Régions du monde et nombre de cas")
date_data = st.sidebar.radio("Choisir l'année que vous voulez étudier", ('2000', '2005', '2010', '2018'), key='2')

if not st.sidebar.checkbox("Hide", True, key='2'):
    if date_data == '2000':
        st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2000")
        graph = nbr_of_people_living_with_hiv_2000.groupby("WHO Region").sum()['Count_median']
        st.bar_chart(graph)
    else:
        if date_data == '2005':
            st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2005")
            graph = nbr_of_people_living_with_hiv_2005.groupby("WHO Region").sum()['Count_median']
            st.bar_chart(graph)
        else:
            if date_data == '2010':
                st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2010")
                graph = nbr_of_people_living_with_hiv_2010.groupby("WHO Region").sum()['Count_median']
                st.bar_chart(graph)
            else:
                st.header("Répartition par pays du nombre de personne atteintes par le sida en Afrique en 2018")
                graph = nbr_of_people_living_with_hiv_2018.groupby("WHO Region").sum()['Count_median']
                st.bar_chart(graph)

# Affichage des classements des pays
coverage_ART_HIV = art[['Country', 'Estimated ART coverage among people living with HIV (%)_median']]
coverage_ART_HIV = coverage_ART_HIV.sort_values(by=['Estimated ART coverage among people living with HIV (%)_median'],
                                                ascending=False)

table_prevention_mother_child = prevention[['Country', 'Percentage Recieved_median']]
table_prevention_mother_child = table_prevention_mother_child.sort_values(by=['Percentage Recieved_median'],
                                                                          ascending=False)

select3 = st.sidebar.selectbox("Choisissez le graphique que vous souhaitez voir", [
    'Classement des pays par rapport au pourcentage de gesn traités parmis les personnes malades',
    'Classement des pays par rapport au pourcentage du niveau de prévention de transmission de la maladie de la mère à son enfant'],
                               key='3')

if not st.sidebar.checkbox("Hide", True, key='3'):
    if select3 == 'Classement des pays par rapport au pourcentage de gesn traités parmis les personnes malades':
        fig = px.bar(coverage_ART_HIV, y='Estimated ART coverage among people living with HIV (%)_median', x='Country',
                     text='Estimated ART coverage among people living with HIV (%)_median')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.write(fig)

    else:
        fig = px.bar(table_prevention_mother_child, y='Percentage Recieved_median', x='Country',
                     text='Percentage Recieved_median')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        st.write(fig)



def plot_map(df, col, pal):
    df = df[df[col]>0]
    fig = px.choropleth(df, locations="Country", locationmode='country names',
                  color=col, hover_name="Country",
                  title=col, color_continuous_scale=pal,width=1500)
#     fig.update_layout(coloraxis_showscale=False)
    fig.show()

st.sidebar.header("MAPS")
st.sidebar.write("Ces maps reprensent un comptage d'objets par pays")
opt = st.sidebar.selectbox("Choissisez une option pour la map",["Cas", "Morts","Vivant"])
if not st.sidebar.checkbox("Show", True, ):
    if (opt == "Cas"):
        plot_map(cases, 'Count_median', 'matter')
    elif(opt == "Morts"):
        plot_map(deaths, 'Count_median', 'matter')
    elif(opt == "Vivant"):
        plot_map(living, 'Count_median', 'matter')



st.sidebar.header("Pour la fin.. ")
if st.sidebar.button("Surprise !"):
    st.balloons()
    st.success('Fin de la presentation')

#st.experimental_show(plot_map(living, 'Count_median', 'matter'))

#st.map(plot_map(living, 'Count_median', 'matter'))




#col = st.selectbox(
   #  'Choisissez une colonne',
     #('Country', 'Reported number of people receiving ART',
      #'Estimated number of people living with HIV', 'Estimated ART coverage among people living with HIV (%)','Estimated number of people living with HIV_median',
      #'Estimated number of people living with HIV_min'))

#st.write('You selected:', col )

#st.bar_chart(art[col])
#st.pyplot(art[col])

#if st.checkbox("Show/Hide"):
   # st.area_chart(art['Estimated ART coverage among people living with HIV (%)'])