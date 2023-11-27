print("Joanna"[3])

lang = "python"
print(lang[1])
print(lang[3:6])

print("pythonik"[-3:-1])

# metoda len pozwala policzyć ilość znaków
print(len("ndndnveivne8oivnevoinvovi"))

paragraf = r"""\tLorem Ipsum is simply dummy text of the printing and typesetting industry.\nLorem Ipsum has been the industry's standard dummy text  
    ever since the 1500s, when an \\version\\ unknown printer took a galley of type and scrambled it to make a type specimen book.
    It has survived not only five centuries, but also the leap into \\electronic\\ typesetting, remaining essentially unchanged.
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
print(paragraf)

# esc characters za pomocą \t tabulacja
# gdy chcemy przejść do kolejnej linii \n lub \r\n
# gdy chcemy coś wyróznić \\nasz test\\
# literka r przed cudzysłowiem tworzy łańcuch surowy i wszystkie esc characters są zawarte w konsoli jako tekst wykorzystywane np do podawania ścieżki