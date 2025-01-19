import streamlit as st
import pandas as pd

def acv():    
    st.subheader("Bloqueos Agendas ACV")


    df = pd.read_csv("ACV.csv",encoding='utf-8', parse_dates=['Fecha'])

    col1,col2 =st.columns(2)

    
    with col1:

        #df = pd.read_csv("ACV.csv",encoding='utf-8', parse_dates=['Fecha'])

        df_mask = df["Bloqueos"] >0
        filtered_df = df[df_mask]

        with st.form("my_form"):
                        edited_df = st.data_editor(filtered_df,
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
                df2 = pd.DataFrame(edited_df)
        
                df2.to_csv('ACV.csv',index=False)

                mensaje=st.success('Los datos se han guardado corecctamente')

                        
        st.write(df["Bloqueos"].sum())
        fecha2=df["Fecha"].iloc[0]
        fecha1=df["Fecha"].iloc[4]
        st.write(fecha1-fecha2)

    with col2:
        st.subheader("Notificaiones")

        huecos=int(df["Bloqueos"].sum())

        fecha2=(df["Fecha"].iloc[0])
        fecha=fecha2.strftime("%d/%m/%Y")
        medico=(df["Medico"].iloc[0])
        st.info(f"Total número de citas bloqueados: {huecos}. El primer hueco bloquedo es el : {medico}")
    fecha1=df["Fecha"].iloc[4]
    st.write(fecha1-fecha2)