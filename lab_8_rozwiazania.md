# zadanie 1
## 1.1
```sql
TRUNCATE kreatura;
INSERT INTO kreatura SELECT * FROM wikingowie.kreatura;
CREATE TABLE uczestnicy SELECT * FROM wikingowie.uczestnicy;
CREATE TABLE etapy_wyprawy SELECT * FROM wikingowie.etapy_wyprawy;
CREATE TABLE sektor SELECT * FROM wikingowie.sektor;
CREATE TABLE wyprawa SELECT * FROM wikingowie.wyprawa;
```
## 1.2
```sql
SELECT nazwa FROM kreatura WHERE
  nazwa NOT IN(SELECT DISTINCT kreatura.nazwa
  FROM kreatura INNER JOIN uczestnicy ON
  kreatura.idKreatury=uczestnicy.id_uczestnika);
```
## 1.3
```sql
SELECT wyprawa.nazwa, SUM(ekwipunek.ilosc) FROM
  wyprawa INNER JOIN uczestnicy ON
  wyprawa.id_wyprawy=uczestnicy.id_wyprawy INNER JOIN
  ekwipunek ON uczestnicy.id_uczestnika=ekwipunek.idKreatury
  GROUP BY wyprawa.nazwa;
```
# zadanie 2
## 2.1
```sql
SELECT wyprawa.nazwa, COUNT(uczestnicy.id_uczestnika) AS liczba, GROUP_CONCAT(kreatura.nazwa) FROM
  wyprawa NATURAL JOIN uczestnicy INNER JOIN kreatura ON kreatura.idKreatury=uczestnicy.id_uczestnika
  GROUP BY wyprawa.nazwa;
```
## 2.2
```sql
SELECT etapy_wyprawy.idEtapu, sektor.nazwa, kreatura.nazwa FROM
  wyprawa INNER JOIN etapy_wyprawy ON wyprawa.id_wyprawy=etapy_wyprawy.idWyprawy INNER JOIN
  sektor ON sektor.id_sektora=etapy_wyprawy.sektor INNER JOIN kreatura ON
  wyprawa.kierownik=kreatura.idKreatury ORDER BY wyprawa.data_rozpoczecia ASC, etapy_wyprawy.kolejnosc ASC;
```
# zadanie 3
## 3.1
```sql
SELECT sektor.nazwa, COUNT(etapy_wyprawy.sektor) FROM
  sektor LEFT JOIN etapy_wyprawy ON
  etapy_wyprawy.sektor=sektor.id_sektora GROUP BY sektor.nazwa;
```
## 3.2
```sql
SELECT kreatura.nazwa, IF(COUNT(uczestnicy.id_uczestnika),"bral udzial w wyprawie","nie bral udzialu w wyprawie")
  AS wynik FROM kreatura LEFT JOIN uczestnicy ON kreatura.idKreatury=uczestnicy.id_uczestnika GROUP BY kreatura.nazwa;
```
# zadanie 4
## 4.1
```sql
SELECT wyprawa.nazwa, SUM(LENGTH(etapy_wyprawy.dziennik)) FROM
  wyprawa INNER JOIN etapy_wyprawy ON etapy_wyprawy.idWyprawy=wyprawa.id_wyprawy
  GROUP BY wyprawa.nazwa HAVING SUM(LENGTH(etapy_wyprawy.dziennik))<400;
```
## 4.2
```sql
SELECT wyprawa.nazwa, AVG(tabela.wagajednego) FROM wyprawa INNER JOIN uczestnicy ON wyprawa.id_wyprawy=uczestnicy.id_wyprawy INNER JOIN (SELECT id_uczestnika, SUM(ekwipunek.ilosc*zasob.waga) AS wagajednego FROM uczestnicy INNER JOIN ekwipunek ON uczestnicy.id_uczestnika=ekwipunek.idKreatury  INNER JOIN zasob ON ekwipunek.idZasobu=zasob.idZasobu  GROUP BY uczestnicy.id_uczestnika) tabela ON tabela.id_uczestnika=uczestnicy.id_uczestnika GROUP BY wyprawa.nazwa;
```
## zadanie 5
# 5.1
```sql
SELECT kreatura.nazwa, a.nazwa, DATEDIFF(obecnosc.data_rozpoczecia, kreatura_kopia.dataUr) AS 'wiek w dniach' 
FROM uczestnicy
INNER JOIN kreatura ON uczestnicy.id_uczestnika = kreatura.idKreatury 
INNER JOIN (SELECT wyprawa.id_wyprawy, etapy_wyprawy.sektor FROM etapy_wyprawy INNER JOIN wyprawa ON etapy_wyprawy.idWyprawy = wyprawa.id_wyprawy WHERE sektor = 7) 
AS a ON uczestnicy.id_wyprawy = a.id_wyprawy;


