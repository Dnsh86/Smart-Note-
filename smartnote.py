""" NOTEPAD APP """

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json

app = QApplication([])
main_page.resize(750,750)
main_page.setWindowTitle("Notepad App")

notes = list()
list_notes = QListWidget()
list_notes_text = QLabel("List notes:")
btn_create = QPushButton("Create note")
btn_del = QPushButton("Delete note")
btn_save = QPushButton("Save note")

tags = list()
list_tags = QListWidget()
list_tags_text = QLabel("List tag:")
btn_add_tag = QPushButton("Add tag")
btn_search_tag = QPushButton("Search note by tag")
btn_untag = QPushButton("Untag")

field_tag = QLineEdit('')
field_tag.setPlaceholderText("Enter a tag...")

kolom_text = QTextEdit()

main_layout = QHBoxLayout()
layout_kolom_text = QVBoxLayout()
layout_kolom_text.addWidget(kolom_text)
layout_note_tag = QVBoxLayout()
layout_note_tag.addWidget(list_notes_text)
layout_note_tag.addWidget(list_notes)

layout_list_row1 = QHBoxLayout()
layout_list_row1.addWidget(ntm_create)
layout_list_row1.addWidget(btn_del)

layout_list_row2 = QHBoxLayout()
layout_list_row2.addWidget(btn_save)

layout_note_tag.addWidget(layout_list_row1)
layout_note_tag.addWidget(layout_list_row2)

layout_note_tag.addWidget(list_tags)
layout_note_tag.addWidget(field_tag)

layout_tag_row1 = QHBoxLayout()
layout_tag_row1.addWidget(btn_add_tag)
layout_tag_row1.addWidget(btn_untag)

layout_tag_row2 = QHBoxLayout()
layout_tag_row2.addWidget(btm_search_tag)

layout_note_tag.addWidget(layout_tag_row1)
layout_note_tag.addWidget(layout_tag_row2)

main_layout.addLayout(layout_kolom_text, stretch=2)
main_layout.addLayout(layout_note_tag, stretch=1)

def create_note():
    note_name, ok = QInputdataDialog.getText(main_page,"Add note", "Judul Note:")
    if ok and note_name!= "":
        note = list()
        note = [note_name, '',[]]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        with open(str(len(notes)-1)+".txt","w") as file:
            file.write(note[0]+'\n')
        print(notes)
    
    else:
        print("Belom ada judul notes")

def del_note():
    if list_notes.selectedItems():
        judul_note = list_notes.selectedItems()[0].text()
        
        for note in notes:
            if note[0] == judul_note:
                list_tags.clear()
                field_tag.clear()
                list_notes.takeItems(list_notes.currentRow())
                notes.remove(note)
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')
        print(notes)
    else:
        print("Notenya pilih dulu lah")
    
def save_note():
    if list_notes.selectedItems():
        judul_note = list_notes.selectedItems()[0].text()
        indek = 0
        for note in notes:
            if note[0] == judul_note:
                note[1] = kolom_text.toPlainText()
                with open(str(indek)+'.txt','w') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]
                        file.write(tag+' ')
                    file.write('\n')
                indek +=1
            print(notes)
    else:
        print("belum ada note yang dipilih")

def show_note():
    judul_note = list_notes.selectedItems()[0].text()
    print(judul_note)
    for note in notes:
        if note[0] == judul_note:
            kolom_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])
    print(notes)

def add_tag():
    if list_notes.selectedItems():
        judul_note = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        for note in notes:
            if note[0] == judul_note and note[2] != tag:
                note[2] = tag
                list_tags.addItem(tag)
                field_tag.clear()
        with open(str(len(notes)-1)+'.txt','w') as file:
            file.write(note[0]+'\n')
        print(notes)
    else:
        print("Pilih note dulu")
    
def search_tag():
    tag = field_tag.text()
    print(btn_search_tag.text())
    if btn_search_tag.text() == "Search note by tag" and tag:
        print(tag)
        notes_filter = {}
        for note in notes:
            if tag in notes[note]["tags"]:
                notes_filter[note] = notes[note]
        btn_search_tag.setText("reset search")
        list_notes.clear()
        

