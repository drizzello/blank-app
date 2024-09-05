import streamlit as st

st.title("🎈 Buon anniversario Banana :two:")
video_file = open("003F5C47-B4F6-42FC-A507-AFFAF3C834A9.MOV", "rb")
video_bytes = video_file.read()



opzione_1 = "Opzione 1-1.pdf"
opzione_2 = "Opzione 1-2.pdf"
opzione_3 = "Opzione 1-3.pdf"


with open(opzione_1, "rb") as pdf_file:
    document1 = pdf_file.read()
with open(opzione_2, "rb") as pdf_file:
    document2 = pdf_file.read()
with open(opzione_3, "rb") as pdf_file:
    document3 = pdf_file.read()

video, text = st.columns(2)

with video:
    st.video(video_bytes,autoplay=True, loop = True)

with text:
    st.write(
    "Per il compleanno ho fatto un po' di bricolagio."
    )
    st.write(
        "Per l'anniversario fammi essere un po' nerd :nerd_face:"
    )

    st.write(
        "Per rendere questo regalo un po' più frizzante ho deciso che potrai scegliere tra 3 opzioni..."
        )

    st.write(
        "Scegli attentamente, potresti non avere una seconda occasione :smirk_cat:"
        )


    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button("Opzione 1", document1, file_name="opzione1")

    with col2:
        st.download_button("Opzione 2", document2, file_name="opzione2")

    with col3:
        st.download_button("Opzione 3", document3, file_name="opzione3")


