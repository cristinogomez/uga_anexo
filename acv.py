import streamlit as st
import datetime as dt
from datetime import datetime
import pandas as pd

def getdata():
      df=pd.read_csv("ACV.csv",encoding='utf-8',parse_dates=['Fecha'])
      return df
def acv():    
    st.subheader("Bloqueos Agendas ACV")
    df = getdata()
    #df['Fecha']= pd.to_datetime(df['Fecha'])
    col3,col4 = st.columns([2, 1])
    with col3:
        med=st.selectbox('Medico',['Requejo','Fernandez','Autogestion','Zafra','Fariñas','Martinez Leon','Mondragon'])
        df_filtrado_medico = df[df['Medico']== med]
        with st.container(border=True):
            dff=st.dataframe(df_filtrado_medico,selection_mode = "single-row"
                        ,column_config={
                                    "Fecha": st.column_config.DateColumn("Fecha del bloqueo",format="DD/MM/YYYY")}
                        ,hide_index=True,use_container_width=800)
    with col4:
      with st.container(border=True):
            #st.metric('Total Huecos Bloquedos',value=int(df_filtrado_medico["Bloqueos"].sum()))
                st.caption('Estructura Agenda COT-:blue[Primeras]')
                st.text("Agenda Mañana\nHorarios Primeras:\n09:00-09:40-10:40-11:20-12:20-13:00")
                st.text("Agenda Tarde\nHorarios Primeras:\n15:30-16:00-16:45-17:15-18:00-18:30")

    col1,col2 =st.columns([2, 1])

    
    with col1:
        with st.form('my_form1'):
            #df['Fecha']= pd.to_datetime(df['Fecha'])
            edited_df = st.data_editor(df,
                                        width=800,
                                        height=540,
                                        column_config={
                                                        "Fecha": st.column_config.DateColumn("Fecha del bloqueo",format="DD/MM/YYYY"),
                                                        "Medico": st.column_config.SelectboxColumn(
                                                        "Facultativo",
                                                        options=[
                                                                "Martinez Leon",
                                                                "Requejo",
                                                                "Fariñas",
                                                                "Zafra",
                                                                "Fernandez",
                                                                "Mondragon",
                                                                "Autogestion"
                                                                ],
                                                                ),
                                                        "Bloqueos":st.column_config.NumberColumn("Número de huecos bloqueados",
                                                                                                min_value=0,
                                                                                                max_value=15,
                                                                                                default=2,
                                                                                                step=1)},
                                        num_rows='dynamic',use_container_width=True)          
            
            boton_guardar=st.form_submit_button('Save')


        if boton_guardar:
            edited_df.to_csv('ACV.csv',index=False)
            mensaje=st.success('Los datos se han guardado corecctamente')
            st.rerun()
    with col2:
        st.subheader("Notificaciones")

        huecos=int(df["Bloqueos"].sum())

        medico=(df["Medico"].iloc[0])
        st.info(f"Total número de citas bloqueados: {huecos}. El primer hueco bloquedo corresponde a: {medico}")
        df['Fecha']= pd.to_datetime(df['Fecha'])
        fechaTarget = dt.date.today()+dt.timedelta (days = 7)

        df_filtrado=df[df['Fecha']<= str(fechaTarget)]
        
        st.text('Huecos bloquedos que se deben citar:')
        with st.container(border=True):
            st.dataframe(df_filtrado,
                        column_config={
                        "Fecha": st.column_config.DateColumn("Fecha del bloqueo",format="DD/MM/YYYY")}
                        ,hide_index=True)    
