# zadanie 1
## 1.1
```sql
delimiter $
CREATE TRIGGER kreatura_edycja BEFORE INSERT, UPDATE ON kreatura 
FOR EACH ROW 
BEGIN 
IF waga<=0 
THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Waga kreatury jest wieksza od zera'; 
END IF; 
END$
```
# zadanie 2
## 2.1
```sql
CREATE TRIGGER t4 AFTER DELETE ON wyprawa 
FOR EACH ROW 
BEGIN 
INSERT INTO archiwum_wypraw 
VALUES(old.id_wyprawy, old.nazwa, old.data_rozpoczecia, old.data_zakonczenia, 
(SELECT nazwa FROM kreatura WHERE kreatura.idKreatury = old.kierownik)); 
END$
```
# zadanie 3
## 3.1
```sql
CREATE PROCEDURE eliksir_sily(IN id INT) 
BEGIN UPDATE kreatura 
SET udzwig = udzwig * 1.2 
WHERE id_kreatury=id;
END $
```
## 3.2
```sql
CREATE FUNCTION zamien (tekst VARCHAR(255))
RETURNS VARCHAR(255)
BEGIN DECLARE res VARCHAR(255);
SET res = UPPER(tekst);
RETURN res;
END $
```
# zadanie 4
## 4.1 / 4.2
```sql
CREATE TRIGGER zad4 BEFORE INSERT ON wyprawa 
FOR EACH ROW 
BEGIN 
IF (IFNULL((SELECT id_uczestnika FROM uczestnicy WHERE id_uczestnika = 14 AND id_wyprawy=new.id_wyprawy LIMIT 1), 0) 
AND IFNULL((SELECT sektor FROM etapy_wyprawy WHERE idWyprawy=new.id_wyprawy AND sektor=7), 0)) 
THEN INSERT INTO system_alarmowy VALUES (NULL, 'Tesciowa nadchodzi !!!');
END IF; 
END $
```
## zadanie 5
# 5.1
```sql
CREATE PROCEDURE staty_udzwig (OUT srednia FLOAT, OUT suma FLOAT, OUT maks FLOAT)
BEGIN
SELECT AVG(udzwig) INTO srednia FROM kreatura;
SELECT SUM(udzwig) INTO suma FROM kreatura;
SELECT MAX(udzwig) INTO maks FROM kreatura;
END $
```
# 5.2
```sqk
CREATE PROCEDURE GetSectors(IN tripId INT)
BEGIN
    SELECT s.nazwa, s.id_sektora, CONCAT(s.wspolrzedna_x, s.wspolrzedna_y) FROM sektor s
    JOIN etapy_wyprawy e ON s.id_sektora = e.sektor
    JOIN wyprawa w ON w.id_wyprawy = e.idWyprawy
    WHERE w.id_wyprawy = tripId
    ORDER BY w.id_wyprawy;
END $
DELIMITER ;
```
