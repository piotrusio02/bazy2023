# zadanie 1
##1.1
```sql
CREATE TABLE kreatura SELECT * FROM wikingowie.kreatura;
CREATE TABLE zasob SELECT * FROM wikingowie.zasob;
CREATE TABLE ekwipunek SELECT * FROM wikingowie.ekwipunek;
```
##1.2
```sql
SELECT * FROM zasob;
```
##1.3
```sql
SELECT * FROM zasob WHERE rodzaj="jedzenie";
```
##1.4
```sql
SELECT idZasobu, ilosc FROM ekwipunek WHERE idKreatury IN (1,3,5);
```

