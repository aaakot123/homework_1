# 1. Stwórz Listę
# Stwórz listę zawierającą pięć różnych owoców.

lista_owocow = ["arbuz","maliny","winogrona","cytryny","gruszki"]
print(lista_owocow)

# 2. Znajdź Drugi Element Listy
# Mając listę, znajdź drugi element listy.

print(lista_owocow[1])

# 3. Zmień Element w Liście
# Zmień trzeci element listy na "malina".

lista_owocow[2] = "malina"
print(lista_owocow)

# 4. Stwórz Krotkę
# Stwórz krotkę zawierającą trzy różne kolory.

tupla_kolory = ("zielony","niebieski","czarny")
print(tupla_kolory)

# 5. Wybierz Ostatni Element Krotki
# Mając krotkę, wybierz jej ostatni element.

print(tupla_kolory[-1])

# 8. Stwórz String Zawierający Twoje Imię i Nazwisko
# Stwórz string "Jan Kowalski".

dane = "Andrzej Kotowski"
print(dane)

# 9. Podziel String na Imię i Nazwisko
# Podziel powyższy string na dwa osobne stringi: imię i nazwisko.

imie = dane.rsplit(" ")[0]
nazwisko = dane.rsplit(" ")[1]
print(imie)
print(nazwisko)

# 10. Użyj F-stringa do Połączenia Tekstu
# Stwórz string "Mam na imię Jan i mam 25 lat" używając f-stringa.

imie = "Jan"
wiek = 25
print(f"Mam na imie {imie} i mam {wiek} lat")

# 1. Zadanie: Znajdź Długość Listy
# Mając listę [1, 2, 3, 4, 5], znajdź jej długość.

lista = [1, 2, 3, 4, 5]
print(len(lista))

# 2. Zadanie: Połącz Dwie Listy
# Mając dwie listy, na przykład [1, 2, 3] i [4, 5, 6], połącz je w jedną.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l_new = l1 + l2
print(l_new)

# 3. Zadanie: Dodaj Element na Końcu Listy
# Dodaj nowy element na końcu listy [1, 2, 3], na przykład 4.

l1 = [1, 2, 3]
l1.append(4)
print(l1)

# 4. Zadanie: Wybierz Element z Krotki
# Mając krotkę (1, 2, 3, 4, 5), wybierz trzeci element.

tuple_l = (1, 2, 3, 4, 5)
print(tuple_l[2])

# 5. Zadanie: Odwróć Listę
# Odwróć kolejność elementów w liście [1, 2, 3, 4, 5].

lista_1 = [1, 2, 3, 4, 5]
lista_1.reverse()
print(lista_1)

# 6. Zadanie: Znajdź Maksymalny Element w Liście
# Znajdź największy element w liście [1, 2, 3, 4, 5].

max_value = max(lista_1)
print(max_value)

# 7. Zadanie: Formatowanie Stringa
# Stwórz string "Python", a następnie dodaj do niego string " jest super!", tworząc pełne zdanie.

tekst_1 = "Python"
tekst_2 = " jest super!"
tekst_3 = tekst_1 + tekst_2
print(tekst_3)

# 8. Zadanie: Zastąp Słowo w Stringu
# Mając string "Lubię Pythona", zastąp słowo "Pythona" słowem "programowanie".

tekst_4 = "Lubię Pythona"
tekst_6 = tekst_4.replace("Pythona", "programowanie")
print(tekst_6)

# 9. Zadanie: Wyodrębnij Podstring
# Wyodrębnij słowo "Python" ze stringa "Lubię Pythona".

tekst_7 = tekst_4.split("Python")
print(tekst_7)

# 10. Zadanie: Stwórz Listę Liczb Nieparzystych
# Stwórz listę zawierającą pierwsze pięć liczb nieparzystych.

lista_liczb_nieparzystych = list(range(1,10,2))
print(lista_liczb_nieparzystych)
