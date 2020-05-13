Wrappers de les APIs externes
-----------------------------

Les següents classes fan de wrappers de les APIs externes que proporcionen les diferents plataformes que usa airhopping
per gestionar pagaments i reserves de vols, cotxes i allotjaments.


classe Banc:

    Encapsula l'accés a la plataforma bancària per realitzar pagaments

    El mètode do_payment reb com a pàràmetres l'usuari que fa el pagament i les dades del pagament

    Les classes 'User' i 'PaymentData' són classes pròpies de airhopping que heu de definir

    La classe 'User' conté informació de l'usuari que fa el pagament
    La classe 'PaymentData' 'PaymentData' conté les dades necessàries per poder efectuar el pagament:
    - Tipus de targeta : VISA o Mastercard
    - Nom del titular (el que apareix a la targeta)
    - Número de la targeta
    - Codi de seguretat
    - Import


classe Skyscanner:

    Encapsula l'accés a la plataforma Skyscanner.com per gestionar vols

    El mètode confirm_reserve reb com a pàràmetres l'usuari que ha fet la pre-reserva i la llista de vols que es volen reservar

    Les classes 'User' i 'Flights' són classes pròpies de airhopping que heu de definir
    'Flights' encapsula la API externa proporcionada per Skyscanner.com

    La classe 'User' conté informació de l'usuari que fa la reserva
    La classe 'Flights' conté la llista de vols pels quals es vol confirmar la reserva. De cada vol té la següent informació:
    - Codi del vol
    - Destinació
    - Número de passatgers


classe Rentalcars:

    Encapsula l'accés a la plataforma Rentalcars.com per gestionar cotxes

    El mètode confirm_reserve reb com a pàràmetres l'usuari que ha fet la pre-reserva i la llista de cotxes que es volen reservar

    Les classes 'User' i 'Cars' són classes pròpies de airhopping que heu de definir
    'Cars' encapsula la API externa proporcionada per Rentalcars.com

    La classe 'User' conté informació de l'usuari que fa la reserva
    La classe 'Cars' conté la llista de cotxes pels quals es vol confirmar la reserva. De cada cotxe té la següent informació:
    - Codi del cotxe
    - Marca del cotxe
    - Lloc de recollida
    - Durada en dies de la reserva


classe Hotels:

    Encapsula l'accés a la plataforma Booking.com per gestionar allotjaments

    El mètode confirm_reserve reb com a pàràmetres l'usuari que ha fet la pre-reserva i la llista d'hotels' que es volen reservar

    Les classes 'User' i 'Hotels' són classes pròpies de airhopping que heu de definir
    'Hotels' encapsula la API externa proporcionada per booking.com

    La classe 'User' conté informació de l'usuari que fa la reserva
    La classe 'Hotels' conté la llista d'hotels' pels quals es vol confirmar la reserva. De cada hotel té la següent informació:
    - Codi de l'hotel
    - Nom de l'hotel
    - Número d'hostes
    - Número d'habitacions
    - Durada en dies de la reserva
