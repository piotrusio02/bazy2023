## zadanie 1
```sql
SELECT imie, nazwisko, YEAR(data_urodzenia) FROM pracownik
```
## zadanie 2
```sql
SELECT imie, nazwisko, 2024 - YEAR(data_urodzenia) as wiek FROM pracownik
```
## zadanie 3
```sql
SELECT dzial.nazwa, COUNT(id_pracownika) as liczba_pracownikow FROM
dzial inner join pracownik ON dzial.id_dzialu = pracownik.dzial GROUP BY dzial.nazwa;
```
## zadanie 4
```sql
SELECT kategoria.nazwa_kategori, count(id_towaru) as liczba_produktow FROM
kategoria INNER JOIN towar ON kategoria.id_kategori = towar.kategoria GROUP BY kategoria.nazwa_kategori
```
