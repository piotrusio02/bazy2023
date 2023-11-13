# zadanie 1
## 1.1
```sql
CREATE TABLE postac (
  id_postaci INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  nazwa VARCHAR(40),
  rodzaj ENUM('wiking','ptak','kobieta'),
  data_ur DATE,
  wiek INT UNSIGNED);
```
## 1.2
```sql
INSERT INTO postac (nazwa,rodzaj,data_ur,wiek)
  VALUES ('Bjorn','wiking','1973-11-24','50'),
  ('Drozd','ptak','2010-11-6','13'),
  ('Tesciowa','kobieta','1930-10-10','93');
```
## 1.3
```sql
UPDATE postac SET wiek = '88' WHERE id_postaci = 3;
```
# zadanie 2
## 2.1
```sql
CREATE TABLE walizka
  ( id_walizki INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  pojemnosc INT unsigned,
  kolor ENUM('rozowy','czerwony','teczowy','zolty'),
  id_wlasciciela INT,
  FOREIGN KEY (id_wlasciciela) REFERENCES postac(id_postaci) ON DELETE CASCADE);
```
## 2.2
```sql
ALTER TABLE walizka
  ALTER COLUMN kolor
  SET DEFAULT 'rozowy';
```
## 2.3
```sql
INSERT INTO walizka (pojemnosc,kolor,id_wlasciciela)
  VALUES ('20','czerwony','1'),
  ('30','rozowy','3');
```
# zadanie 3
## 3.1
```sql
CREATE TABLE izba (
  adres_budynku varchar(50),
  nazwa_izby varchar(50),
  metraz int unsigned,
  wlasciciel INT,
  primary key(adres_budynku, nazwa_izby),
  foreign key (wlasciciel) REFERENCES postac(id_postaci) ON DELETE SET NULL);
```
## 3.2
```sql
ALTER TABLE izba ADD COLUMN
  kolor_izby varchar(50) DEFAULT 'czarny' AFTER metraz;
```
### 3.3
```sql
INSERT INTO izba (adres_budynku,nazwa_izby,metraz,wlasciciel) VALUES ('ul. Twarda 14','spizarnia','200','1');
```
# zadanie 4
## 4.1
```sql
CREATE TABLE przetwory (
  id_przetworu INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  rok_produkcji INT DEFAULT '1654', id_wykonawcy int,
  zawartosc varchar(255),
  dodatek varchar(255) DEFAULT 'papryczka chilli',
  id_konsumenta int,
  foreign key (id_wykonawcy) REFERENCES postac(id_postaci),
  foreign key (id_konsumenta) REFERENCES postac(id_postaci));
```
## 4.2
```sql
INSERT INTO przetwory (
  rok_produkcji,id_wykonawcy,zawartosc,dodatek,id_konsumenta)
VALUES
  ('2000','3','bigos','papryczka chilli','1');
```
# zadanie 5
## 5.1
```sql
INSERT INTO postac (nazwa, rodzaj, data_ur, wiek)
  VALUES ('Staszek','wiking','1974-03-29','49'),
  ('Grzesiek','wiking','1972-01-11','51'),
  ('Krystian','wiking','1970-02-21','53'),
  ('Wojtek','wiking','1965-03-15','58'),
  ('Pipkin','wiking','1980-12-26','42');
```
## 5.2
```sql
CREATE TABLE statek (
  nazwa_statku VARCHAR(50) PRIMARY KEY,
  rodzaj_statku ENUM('Szkuner','Bark','Fregata'),
  data_wodowania DATE,
  max_ladownosc INT UNSIGNED);
```
## 5.3
```sql
INSERT INTO statek (nazwa_statku, rodzaj_statku, data_wodowania, max_ladownosc) 
	VALUES ('Panna','Bark','1900-06-30','40'),
	('Niszczyciel','Fregata','1950-05-12','55');
```
## 5.4
```sql
ALTER TABLE postac ADD funkcja VARCHAR(40);
```
## 5.5
```sql
UPDATE postac 
  SET funkcja = 'Kapitan'
  Where nazwa = 'Bjorn';
```
## 5.6
```
ALTER TABLE postac 
  ADD nazwa_statku VARCHAR(30);
ALTER TABLE postac 
  ADD FOREIGN KEY (nazwa_statku) 
    REFERENCES statek(nazwa_statku);
```
## 5.7
```sql
UPDATE postac SET nazwa_statku = "Niszczyciel" WHERE id_postaci = 1;
UPDATE postac SET nazwa_statku = "Niszczyciel" WHERE id_postaci = 2;
UPDATE postac SET nazwa_statku = "Niszczyciel" WHERE id_postaci = 4;
UPDATE postac SET nazwa_statku = "Panna" WHERE id_postaci > 4;
```
## 5.8
```sql
DELETE FROM izba WHERE nazwa_izby = 'spizarnia';
```
## 5.9
```sql
DROP TABLE izba;
```
