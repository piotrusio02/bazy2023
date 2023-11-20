# zadanie 1
## 1.1
```sql
DELETE FROM postac WHERE id_postaci = '6';
DELETE FROM postac WHERE id_postaci = '7';
```
##1.2
```sql
ALTER TABLE walizka DROP FOREIGN KET walizka_ibfk_1;
ALTER TABLE przetwory DROP FOREIGN KEY przetwory_ibfk_1;
ALTER TABLE przetwory DROP FOREIGN KEY przetwory_ibfk_2;
ALTER TABLE postac MODIFY id_postaci INT;
ALTER TABLE DROP PRIMARY KEY;
```
# zadanie 2
##2.1
```sql
ALTER TABLE postac ADD pesel CHAR(11) NOT NULL;
UPDATE postac SET pesel = '17763874636' WHERE id_postaci='1';
UPDATE postac SET pesel = '17763874637' WHERE id_postaci='2';
UPDATE postac SET pesel = '17763874638' WHERE id_postaci='3';
UPDATE postac SET pesel = '17763874639' WHERE id_postaci='4';
UPDATE postac SET pesel = '17763874640' WHERE id_postaci='5';
UPDATE postac SET pesel = '17763874643' WHERE id_postaci='8';
ALTER TABLE postac ADD PRIMARY KEY(pesel);
```
##2.2
```sql
ALTER TABLE postac MODIFY rodzaj ENUM('wiking','ptak','kobieta','syrena');
```
##2.3
```sql
INSERT INTO postac (pesel,id_postaci,nazwa,rodzaj,wiek) VALUES ('17763874644','9','Gertruda Niszczera','syrena','50');
```
# zadanie 3
##3.1
```sql
UPDATE postac SET nazwa_statku = 'Niszczyciel' WHERE nazwa REGEXP 'a' AND rodzaj NOT REGEXP 'kobieta';
```
##3.2
```sql
UPDATE statek set max_ladownosc = 0.7*max_ladownosc WHERE data_wodowania <= '2000-01-01' AND data_wodowania >='1901-01-01';
```
##3.3
```sql
ALTER TABLE postac ADD CHECK(wiek <=1000);
```
# zadanie 4
##4.1
```sql
ALTER TABLE postac MODIFY rodzaj ENUM('wiking','ptak','kobieta','syrena','waz');
INSERT INTO postac (pesel,id_postaci,nazwa,rodzaj,data_ur,wiek) VALUES ('17763874644','10','Loko','waz','2020-11-20','3');
```
##4.2
```sql
CREATE TABLE marynarz SELECT*FROM postac WHERE nazwa IS NOT NULL;
```
##4.3
```sql
ALTER TABLE marynarz ADD FOREIGN KEY(nazwa_statku) REFERENCES statek(nazwa_statku) ON UPDATE CASCADE;
```
# zadanie 5
## 5.1
```sql
UPDATE postac SET nazwa_statku = NULL;
UPDATE marynarz SET nazwa_statku = NULL;
```
## 5.2
```sql
DELETE FROM postac WHERE id_postaci = '4';
DELETE FROM marynarz WHERE id_postaci = '4';
```
##5.3
```sql
DELETE FROM statek WHERE nazwa_statku IS NOT NULL;
```
##5.3
```sql













