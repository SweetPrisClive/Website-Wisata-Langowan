import streamlit as st
import pandas as pd


#find more emojis here: http://webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="WISATA LANGOWAN", page_icon=":earth_asia:", layout="wide")

#--- HEADER SECTION
st.subheader ("Hi, We are Clive, Sweety and Talita :wave:")
st.title("Website Wisata Langowan")
st.write("We are students of the information systems study program at the University of Sam Ratulangi, Manado, Indonesia")
st.write("[More >]( )")


st.markdown('Destination is **_really_ cool**.')



#reasons why you should visit langowan
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Reasons WHY You Should Visit Langowan")
        st.write("##")
        st.write(
            """
            Karena terdapat berbagai macam tempat wisata yang masih belum diketahui banyak orang, 
            yang tentunya dengan keindahan tersebut maka para pengunjung dapat merasakan keindahan 
            serta kenyamanan saat mengunjungi destinasi wisata yang ad di Langowan khususnya.
            """
        )



#show video
video_file = open('Trimla.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


st.write("Creator: Zefanya Talumewo.")

st.write("[Source Video: >](https://www.youtube.com/watch?v=gxFcnrAD9NY)")


with st.container():
    st.write("---")

city = pd.DataFrame({
    'awesome cities' : ['Langowan'],
    'lat' : [1.153460],
    'lon' : [124.840142]
})
st.map(city)






# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/bedgenius836@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

