# zadanie 1
## 1.1
```sql
SELECT AVG(waga) FROM kreatura WHERE rodzaj = "wiking";
```
## 1.2
```sql
SELECT AVG(waga), COUNT(rodzaj) FROM kreatura GROUP BY rodzaj;
```
## 1.3
```sql
SELECT rodzaj, ROUND(AVG(YEAR(CURDATE())-YEAR(dataUr))) FROM kreatura GROUP BY rodzaj;
```
# zadanie 2
## 2.1
```sql
SELECT rodzaj, SUM(ilosc*waga) FROM zasob GROUP BY rodzaj;
```
##2.2
```sql
SELECT nazwa, AVG(waga) FROM zasob GROUP BY nazwa HAVING SUM(ilosc) >= 4 AND SUM(ilosc*waga)>10;
```
##2.3
```sql
SELECT rodzaj, COUNT(DISTINCT nazwa) FROM zasob GROUP BY rodzaj HAVING COUNT(DISTINCT nazwa)>1 AND COUNT(DISTINCT nazwa)<>COUNT(nazwa);
```

# zadanie 3
## 3.1
```sql
SELECT kreatura.nazwa, SUM(ekwipunek.ilosc) FROM kreatura NATURAL JOIN ekwipunek GROUP BY kreatura.nazwa;
```
## 3.2
```sql
SELECT kreatura.nazwa, zasob.nazwa FROM zasob, ekwipunek, kreatura 
WHERE ekwipunek.idKreatury=kreatura.idKreatury AND ekwipunek.idZasobu=zasob.idZasobu ORDER BY kreatura.nazwa;
```
## 3.3
```sql
SELECT nazwa FROM kreatura WHERE nazwa NOT IN
(SELECT DISTINCT kreatura.nazwa FROM kreatura, ekwipunek WHERE kreatura.idKreatury=ekwipunek.idKreatury);
```
# zadanie 4
## 4.1
```sql
SELECT kreatura.nazwa, zasob.nazwa FROM ekwipunek 
NATURAL JOIN kreatura INNER JOIN zasob ON zasob.idZasobu=ekwipunek.idZasobu 
WHERE kreatura.rodzaj="wiking" AND YEAR(dataUr) BETWEEN 1670 AND 1679 ORDER BY kreatura.nazwa, zasob.nazwa;
```
## 4.2
```sql
SELECT kreatura.nazwa FROM ekwipunek NATURAL JOIN kreatura INNER JOIN zasob ON zasob.idZasobu=ekwipunek.idZasobu 
WHERE zasob.rodzaj="jedzenie" ORDER BY kreatura.dataUr DESC LIMIT 5;
```
## 4.3
```sql
SELECT CONCAT(A.nazwa,' - ', B.nazwa) AS polaczenie FROM kreatura A, kreatura B WHERE A.idKreatury+5=B.idKreatury;
```

# zadanie 5
## 5.1
```sql
SELECT kreatura.rodzaj, AVG(zasob.waga*ekwipunek.ilosc) 
FROM ekwipunek NATURAL JOIN kreatura INNER JOIN zasob ON zasob.idZasobu=ekwipunek.idZasobu 
GROUP BY kreatura.rodzaj HAVING SUM(ekwipunek.ilosc)<30 AND kreatura.rodzaj NOT IN("malpa","waz");
```

## 5.2
```sql
SELECT a.nazwa, a.rodzaj, a.dataUr FROM kreatura a 
INNER JOIN (SELECT rodzaj, MIN(dataUr) AS minimalna, MAX(dataUr) AS maksymalna FROM kreatura GROUP BY rodzaj) b 
ON a.rodzaj=b.rodzaj 
WHERE a.dataUr=b.minimalna OR a.dataUr=b.maksymalna ORDER BY rodzaj;
```
