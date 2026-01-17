import streamlit as st

pages = [
        st.Page("rajasthan.py", title="RAJASTHAN"),
        st.Page("ARUNACHAL_PRADESH.py", title="ARUNACHAL_PRADESH"),
        st.Page("ASSAM.PY", title="ASSAM"),
        st.Page("BIHAR.py", title="BIHAR"),
        st.Page("GOA.py", title="GOA"),
        st.Page("GUJARAT.py", title="GUJARAT"),
        st.Page("HIMACHAL_PRADESH.py", title="HIMACHAL_PRADESH"),
        st.Page("JARKAND.py", title="JHARKHAND"),
        st.Page("KARNATAKA.py", title="KARNATAKA"),
        st.Page("KERALA.py", title="KERALA"),
        st.Page("MAHARASHTRA.py", title="MAHARASHTRA"),
        st.Page("MANIPUR.py", title="MANIPUR"),
        st.Page("MIZORAM.py", title="MIZORAM"),
        st.Page("NAGALAND.py", title="NAGALAND"),
        st.Page("NCT_OF_DELHI.py", title="NCT_OF_DELHI"),
        st.Page("PUDUCHERRY.py", title="PUDUCHERRY"),
        st.Page("SIKKIM.py", title="SIKKIM"),
        st.Page("TAMIL_NADU.py", title="TAMIL_NADU"),
        st.Page("TRIPURA.py", title="TRIPURA"),
        st.Page("UTTAR_PRADESH.py", title="UTTAR_PRADESH"),
        st.Page("UTTARAKHAND.py", title="UTTARAKHAND"),
        st.Page("WEST_BENGAL.py", title="WEST_BENGAL"),
    ]


pg = st.navigation(pages)
#st.sidebar.image("D:/Book_cpny/mysql/book.jpg")
pg.run()