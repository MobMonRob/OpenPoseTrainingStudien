# Studienarbeit
Es gibt drei verschine Programme welche als hilfe dienen um im zukünfigen Arbeiten das traniren , bzw das sammeln der daten vereinfachen.

## Capture Video mit 3D daten
Das Python skript "CaptureImages" Nimmt kammera daten auf und die dazugehörigen 3d daten. Die daten werden in folgenen unterortnern gespeichert 
1. frames
2. ViconData

Vorm starten des Skriptes muss die Methode getViconData(Client) angepast werden, die methode ist elider nicht gerneisch da sie je nach setUp unterschidliche logik beinhalten muss. Diese Methode muss als JSon die 3D posion des Aktuellen Frame zurück geben. Wie das Geht, sieht man in folgener Doku https://docs.vicon.com/display/DSSDK111/Vicon+DataStream+SDK+Quick+Start+Guide+for+Python

## Landmarks Entfernen
Die Landmarks welche auf den bildern sich befinden, welche benötigt werden um genaue 3D daten zu messen, mussen vorm Traniren entfernt werden, hierfür gibt es ein skript welches dies automatisirt macht. Das Skript Benötigt Hierfür nur informationen über die zu entfernenden Farben. Dies Farben müssen hierbei in HSV farbraum angegeben werden, um die RGB werdte des bildes in die richtigen HSV werte zu übersetzen gibt es ein Skript mit den namen RGBtoHSV.py Dieses Skript fragt über die Konsole nach den RGB werten Und gibt die passenden HSV werte raus. Da OpenCV andere zahlen bereiche als üblich benutzt kann man hierfür leider kein online toll nutzen, und muss den ümweg über das selbst geschribene consolnen program nehmen.

Das Program benötig pro farbe eine obere und untere genze, alle farben die dazuwischen sind, werden später durch seine umgebung ersetzt. Aus erfahrun ergibt es sinn die greznen in jede richtung um 30 punkte zu verschiben im vergleich zur ursprungs farbe.

Nachdem das Program gestartet wurde, fragt es nach einen ortner in den alle bilder bearbeitet werden, wichtig hierbei zu beachten ist das das ursprungs bild überschriben mit den neun bild wird.

