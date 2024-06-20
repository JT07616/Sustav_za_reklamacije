# Sustav za reklamacije



Aplikacija "Sustav za reklamacije" omogućava korisnicima jednostavno praćenje i upravljanje procesom reklamacija. Pomoću alata za unos, pregled, uređivanje i vizualizaciju, aplikacija omogućuje praćenje i rješavanje reklamacija, poboljšavajući korisničko iskustvo i operativnu učinkovitost web trgovine.

## Usecase dijagram

<p align="center">
  <img src="https://github.com/JT07616/Sustav_za_reklamacije/assets/170039228/a2a74a7c-bc1c-4c8d-a191-a99542f0b08d" alt="Sustav_reklamacija (2)">
</p>



## Funkcionalnosti

- **Unos reklamacija**: Omogućava korisniku unos novih reklamacija u sustav.
- **Pretraživanje reklamacija**: Omogućava korisniku pregled reklamacija na temelju unesenih parametara.
- **Sortiranje reklamacija**: Omogućava korisniku sortiranje reklamacija prema datumu ili broju narudžbe.
- **Uređivanje reklamacija**: Omogućava korisniku ažuriranje informacija za odabrane reklamacije.
- **Brisanje reklamacija**: Omogućava korisniku brisanje određenih reklamacija iz sustava.
- **Vizualizacija reklamacija**: Omogućava korisniku pregled grafičkih prikaza podataka o reklamacijama.

## Pokretanje aplikacije

1. **Preuzimanje aplikacije**: Posjetite [GitHub repozitorij](https://github.com/JT07616/Sustav_za_reklamacije.git), kliknite na "Code" i preuzmite ZIP datoteku, zatim ekstraktirajte ZIP datoteku u željeni direktorij.

2. **Ulazak u direktorij**: Otvorite terminal ili naredbeni redak i uđite u direktorij gdje ste ekstraktirali datoteku:
      ```sh
      cd Sustav_za_reklamacije
      ```
3. **Stvaranje Docker slike:** Upišite naredbu za stvaranje Docker slike:
      ```sh
      docker build -t reklamacija .
      ```
4. **Pokretanje Docker containera:** Upišite naredbu za pokretanje containera.
      ```sh
      docker run -d -p 5001:8080 reklamacija
      ```


