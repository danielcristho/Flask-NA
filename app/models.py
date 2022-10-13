from app import db
from datetime import datetime
from flask import url_for

class ValidationError(ValueError):
    pass

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(64), unique=True)
    loopback = db.Column(db.String(120), unique=True)
    mgmt_ip = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(64))
    vendor = db.Column(db.String(64))
    os = db.Column(db.String(64))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def get_url(self):
        return url_for('get_device', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'hostname': self.hostname,
            'loopback': self.loopback,
            'mgmt_ip': self.mgmt_ip,
            'role': self.role,
            'vendor': self.vendor,
            'os': self.os
        }

    def import_data(self, data):
        try:
            self.hostname = data['hostname']
            self.loopback = data['loopback']
            self.mgmt_ip  = data['mgmt_ip']
            self.role     = data['role']
            self.vendor   = data['vendor']
            self.os       = data['os']
        except KeyError as e:
            raise ValidationError('Invalid device: missing ' + e.args[0])
        return self