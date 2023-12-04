# zadanie 1
## 1.1
```sql
CREATE TABLE kreatura SELECT * FROM wikingowie.kreatura;
CREATE TABLE zasob SELECT * FROM wikingowie.zasob;
CREATE TABLE ekwipunek SELECT * FROM wikingowie.ekwipunek;
```
## 1.2
```sql
SELECT * FROM zasob;
```
## 1.3
```sql
SELECT * FROM zasob WHERE rodzaj="jedzenie";
```
## 1.4
```sql
SELECT idZasobu, ilosc FROM ekwipunek WHERE idKreatury IN (1,3,5);
```

# zadanie 2
## 2.1
```sql
SELECT * FROM kreatura WHERE rodzaj<>"wiedzma" AND udzwig>50;
```
##2.2
```sql
SELECT * FROM zasob WHERE waga BETWEEN 2 AND 5;
```
##2.3
```sql
SELECT * FROM kreatura WHERE nazwa LIKE "%or%" AND udzwig BETWEEN 30 AND 70; (pusto)
```

# zadanie 3
## 3.1
```sql
SELECT * FROM zasob WHERE MONTH(dataPozyskania) IN (7,8);
```
## 3.2
```sql
SELECT * FROM zasob WHERE rodzaj IS NOT NULL ORDER BY waga ASC;
```
## 3.3
```sql
SELECT * FROM kreatura ORDER BY dataUr ASC LIMIT 5;
```
# zadanie 4
## 4.1
```sql
SELECT DISTINCT rodzaj FROM zasob;
```
## 4.2
```sql
SELECT CONCAT(nazwa,' - ',rodzaj) FROM kreatura WHERE rodzaj LIKE "wi%";
```
## 4.3
```sql
SELECT nazwa, waga * ilosc AS "calkowita waga" FROM zasob WHERE YEAR(dataPozyskania) BETWEEN 2000 AND 2007;
```

# zadanie 5
## 5.1
```sql
SELECT nazwa, waga*ilosc*0.7 AS "netto", waga*ilosc*0.3 AS "odpad" FROM zasob WHERE rodzaj="jedzenie";
```

## 5.2
```sql
SELECT * FROM zasob WHERE rodzaj IS NULL;
```

## 5.3
```sql
SELECT DISTINCT nazwa, rodzaj FROM zasob WHERE nazwa LIKE "Ba%" OR nazwa LIKE "%os" ORDER BY nazwa ASC;
```
