from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Dummy data for demonstration (replace with database)
appointments = []

# Route for homepage
@app.route('/')
def index():
    return render_template('medi.html', appointments=appointments)

# Route for scheduling appointments
@app.route('/schedule', methods=['POST'])
def schedule_appointment():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        date_time = request.form['date_time']
        doctor = request.form['doctor']
        appointment = {'patient_name': patient_name, 'date_time': date_time, 'doctor': doctor}
        appointments.append(appointment)
        flash('Appointment scheduled successfully!', 'success')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
