from app import create_app, db
from app.models.ssd import SSD

app = create_app()

with app.app_context():
    db.create_all()

    # Optional: Add some initial data
    if SSD.query.count() == 0:
        ssd1 = SSD(model='Samsung 860 EVO', health_status='Good')
        ssd2 = SSD(model='Crucial MX500', health_status='Warning')
        db.session.add(ssd1)
        db.session.add(ssd2)
        db.session.commit()
