import os
from flask import Flask, request, render_template, redirect, url_for, flash
from pony.orm import Database, Required, PrimaryKey, db_session, select, desc
from datetime import datetime
import calendar

app = Flask(__name__)
app.secret_key = 'supersecretkey'
db = Database()

class Reklamacija(db.Entity):
    id_reklamacije = PrimaryKey(int, auto=True)
    broj_narudzbe = Required(int)
    kupac = Required(str)
    datum_reklamacije = Required(datetime)
    opis = Required(str)
    status = Required(str)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reklamacije', methods=['GET', 'POST'])
@db_session
def reklamacija():
    search_values = {
        'id_reklamacije': request.form.get(
            'id_reklamacije') if request.method == 'POST' and 'search' in request.form else '',
        'broj_narudzbe': request.form.get(
            'broj_narudzbe') if request.method == 'POST' and 'search' in request.form else '',
        'kupac': request.form.get('kupac') if request.method == 'POST' and 'search' in request.form else '',
        'status': request.form.get('status') if request.method == 'POST' and 'search' in request.form else '',
    }
    reklamacije = select(r for r in Reklamacija)

    if request.method == 'POST':
        if 'search' in request.form:
            if search_values['id_reklamacije']:
                reklamacije = reklamacije.filter(lambda r: r.id_reklamacije == int(search_values['id_reklamacije']))
            if search_values['broj_narudzbe']:
                reklamacije = reklamacije.filter(lambda r: r.broj_narudzbe == int(search_values['broj_narudzbe']))
            if search_values['kupac']:
                reklamacije = reklamacije.filter(lambda r: r.kupac == search_values['kupac'])
            if search_values['status']:
                reklamacije = reklamacije.filter(lambda r: r.status == search_values['status'])
            reklamacije = reklamacije[:]
            if not reklamacije:
                flash("Niti jedna reklamacija ne odgovara traženim vrijednostima.", "danger")
                reklamacije = None
            return render_template('reklamacija.html', reklamacije=reklamacije, search_values=search_values, is_search=True)
        else:
            try:
                id_reklamacije = int(request.form['id_reklamacije'])
                if Reklamacija.get(id_reklamacije=id_reklamacije):
                    raise ValueError("Reklamacija s tim ID već postoji.")

                broj_narudzbe = int(request.form['broj_narudzbe'])
                kupac = request.form['kupac']
                datum_reklamacije = datetime.strptime(request.form['datum_reklamacije'], '%Y-%m-%dT%H:%M')
                opis = request.form['opis']
                status = request.form['status']
                Reklamacija(id_reklamacije=id_reklamacije, broj_narudzbe=broj_narudzbe, kupac=kupac,
                            datum_reklamacije=datum_reklamacije, opis=opis, status=status)
                db.commit()
                flash("Reklamacija je uspješno dodana.", "success")
            except Exception as e:
                flash(str(e), "danger")
    else:
        if sort := request.args.get('sort'):
            if sort == 'datum_asc':
                reklamacije = reklamacije.order_by(Reklamacija.datum_reklamacije)
            elif sort == 'datum_desc':
                reklamacije = reklamacije.order_by(desc(Reklamacija.datum_reklamacije))
            elif sort == 'broj_asc':
                reklamacije = reklamacije.order_by(Reklamacija.broj_narudzbe)
            elif sort == 'broj_desc':
                reklamacije = reklamacije.order_by(desc(Reklamacija.broj_narudzbe))
        reklamacije = reklamacije[:]

    return render_template('reklamacija.html', reklamacije=reklamacije, search_values=search_values, is_search=False)


@app.route('/uredi/<int:id>', methods=['POST'])
@db_session
def uredi_reklamaciju(id):
    try:
        reklamacija = Reklamacija.get(id_reklamacije=id)
        if not reklamacija:
            raise ValueError("Reklamacija nije pronađena")

        reklamacija.broj_narudzbe = int(request.form['broj_narudzbe'])
        reklamacija.kupac = request.form['kupac']
        reklamacija.datum_reklamacije = datetime.strptime(request.form['datum_reklamacije'], '%Y-%m-%dT%H:%M')
        reklamacija.opis = request.form['opis']
        reklamacija.status = request.form['status']
        flash("Reklamacija je uspješno ažurirana.", "success")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for('reklamacija'))


@app.route('/obrisi/<int:id>', methods=['POST'])
@db_session
def obrisi_reklamaciju(id):
    try:
        reklamacija = Reklamacija.get(id_reklamacije=id)
        if reklamacija:
            reklamacija.delete()
            db.commit()
            flash("Reklamacija je uspješno obrisana.", "success")
        else:
            raise ValueError("Reklamacija nije pronađena")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for('reklamacija'))


@app.route('/vizualizacija')
@db_session
def vizualizacija():
    reklamacije = select(r for r in Reklamacija)[:]

    mjeseci_eng = [r.datum_reklamacije.strftime('%m') for r in reklamacije]
    mjeseci_hr = [calendar.month_name[int(month)] for month in mjeseci_eng]
    mjesec_broj = {mjesec: mjeseci_hr.count(mjesec) for mjesec in set(mjeseci_hr)}

    mjeseci_po_redu = [calendar.month_name[i] for i in range(1, 13)]
    labels_mjeseci = [mjesec for mjesec in mjeseci_po_redu if mjesec in mjesec_broj]
    data_mjeseci = [mjesec_broj[mjesec] for mjesec in labels_mjeseci]

    status_broj = {"Obrađeno": 0, "Neobrađeno": 0}
    for r in reklamacije:
        status_broj[r.status] += 1
    labels_status = list(status_broj.keys())
    data_status = list(status_broj.values())

    return render_template('vizualizacija.html', labels_mjeseci=labels_mjeseci, data_mjeseci=data_mjeseci,
                           labels_status=labels_status, data_status=data_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
