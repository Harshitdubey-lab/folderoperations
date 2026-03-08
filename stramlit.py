import os
from pathlib import Path
import streamlit as st


st.set_page_config(page_title="File Manager", layout="centered")

st.title("📁 Python File Manager (Streamlit UI)")


# ---------------- FUNCTIONS ---------------- #

def list_items():
    p = Path(".")
    items = list(p.rglob("*"))
    return items


# ---------------- SIDEBAR ---------------- #

menu = st.sidebar.selectbox(
    "Select Action",
    [
        "Create Folder",
        "List Files & Folders",
        "Rename Folder",
        "Delete Folder",
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    ]
)


# ---------------- CREATE FOLDER ---------------- #

if menu == "Create Folder":
    st.header("📁 Create Folder")
    name = st.text_input("Enter Folder Name")

    if st.button("Create Folder"):
        p = Path(name)
        if not p.exists():
            p.mkdir()
            st.success("Folder Created Successfully")
        else:
            st.error("Folder Already Exists")


# ---------------- LIST ---------------- #

elif menu == "List Files & Folders":
    st.header("📄 Listing Files & Folders")

    items = list_items()
    for i, v in enumerate(items, 1):
        st.write(f"{i}. {v}")


# ---------------- RENAME FOLDER ---------------- #

elif menu == "Rename Folder":
    st.header("✏ Rename Folder")

    old = st.text_input("Old Folder Name")
    new = st.text_input("New Folder Name")

    if st.button("Rename"):
        old_p = Path(old)
        new_p = Path(new)

        if old_p.exists():
            if not new_p.exists():
                old_p.rename(new_p)
                st.success("Folder Renamed Successfully")
            else:
                st.error("New Name Already Exists")
        else:
            st.error("Folder Not Found")


# ---------------- DELETE FOLDER ---------------- #

elif menu == "Delete Folder":
    st.header("🗑 Delete Folder")

    name = st.text_input("Folder Name")

    if st.button("Delete"):
        p = Path(name)
        if p.exists():
            p.rmdir()
            st.success("Folder Deleted")
        else:
            st.error("Folder Not Found")


# ---------------- CREATE FILE ---------------- #

elif menu == "Create File":
    st.header("📄 Create File")

    name = st.text_input("File Name with Extension")
    data = st.text_area("Write Content")

    if st.button("Create File"):
        p = Path(name)
        if not p.exists():
            with open(p, "w") as f:
                f.write(data)
            st.success("File Created Successfully")
        else:
            st.error("File Already Exists")


# ---------------- READ FILE ---------------- #

elif menu == "Read File":
    st.header("📖 Read File")

    name = st.text_input("File Name")

    if st.button("Read"):
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as f:
                st.text_area("File Content", f.read(), height=300)
        else:
            st.error("File Not Found")


# ---------------- UPDATE FILE ---------------- #

elif menu == "Update File":
    st.header("✏ Update File")

    name = st.text_input("File Name")
    option = st.selectbox("Select Action", ["Rename", "Overwrite", "Append"])
    data = st.text_area("Content / New Name")

    if st.button("Update"):
        p = Path(name)

        if p.exists() and p.is_file():

            if option == "Rename":
                new_p = Path(data)
                p.rename(new_p)
                st.success("File Renamed")

            elif option == "Overwrite":
                with open(p, "w") as f:
                    f.write(data)
                st.success("File Overwritten")

            elif option == "Append":
                with open(p, "a") as f:
                    f.write(data)
                st.success("Content Appended")

        else:
            st.error("File Not Found")


# ---------------- DELETE FILE ---------------- #

elif menu == "Delete File":
    st.header("🗑 Delete File")

    name = st.text_input("File Name")

    if st.button("Delete"):
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            st.success("File Deleted Successfully")
        else:
            st.error("File Not Found")
