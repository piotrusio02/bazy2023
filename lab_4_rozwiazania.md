# zadanie 1
## 1.1
```
CREATE TABLE postac (
  id_postaci INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  nazwa VARCHAR(40),
  rodzaj ENUM('wiking','ptak','kobieta'),
  data_ur DATE,
  wiek INT UNSIGNED);
```
## 1.2
```
INSERT INTO postac (nazwa,rodzaj,data_ur,wiek)
  VALUES ('Bjorn','wiking','1973-11-24','50'),
  ('Drozd','ptak','2010-11-6','13'),
  ('Tesciowa','kobieta','1930-10-10','93');
```
## 1.3
```
UPDATE postac SET wiek = '88' WHERE id_postaci = 3;
```
# zadanie 2
## 2.1
```
CREATE TABLE walizka
  ( id_walizki INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  pojemnosc INT unsigned,
  kolor ENUM('rozowy','czerwony','teczowy','zolty'),
  id_wlasciciela INT,
  FOREIGN KEY (id_wlasciciela) REFERENCES postac(id_postaci) ON DELETE CASCADE);
```
## 2.2
```
ALTER TABLE walizka
  ALTER COLUMN kolor
  SET DEFAULT 'rozowy';
```
## 2.3
```
INSERT INTO walizka (pojemnosc,kolor,id_wlasciciela)
  VALUES ('20','czerwony','1'),
  ('30','rozowy','3');
```
# zadanie 3
## 3.1
```
CREATE TABLE izba (
  adres_budynku varchar(50),
  nazwa_izby varchar(50),
  metraz int unsigned,
  wlasciciel INT,
  primary key(adres_budynku, nazwa_izby),
  foreign key (wlasciciel) REFERENCES postac(id_postaci) ON DELETE SET NULL);
```
## 3.2
```
ALTER TABLE izba ADD COLUMN kolor_izby varchar(50) DEFAULT 'czarny' AFTER metraz;
```
### 3.3
```
INSERT INTO izba (adres_budynku,nazwa_izby,metraz,wlasciciel) VALUES ('ul. Twarda 14','spizarnia','200','1');
```
# zadanie 4
## 4.1
```
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
```
INSERT INTO przetwory (
  rok_produkcji,id_wykonawcy,zawartosc,dodatek,id_konsumenta)
VALUES
  ('2000','3','bigos','papryczka chilli','1');
```
# zadanie 5
