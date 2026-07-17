import random
import uuid
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# CATALOGOS HEDONISTAS Y CLÍNICOS MEXICANOS
NOMBRES_H = ["Juan", "José", "Francisco", "Pedro", "Manuel", "Jesús", "Carlos", "Miguel", "Jorge", "Alejandro", "Luis", "Fernando", "Ricardo", "Javier", "Rafael"]
NOMBRES_M = ["María", "Guadalupe", "Juana", "Margarita", "Verónica", "Leticia", "Rosa", "Gabriela", "Patricia", "Ana", "Luisa", "Elena", "Sofia", "Carmen", "Teresa"]
APELLIDOS = ["Hernández", "García", "Martínez", "López", "González", "Pérez", "Rodríguez", "Sánchez", "Ramírez", "Cruz", "Flores", "Gómez", "Morales", "Vázquez", "Jiménez", "Reyes", "Díaz", "Torres", "Gutiérrez", "Castro"]
AFILIACIONES = ["IMSS", "IMSS-Bienestar", "ISSSTE", "ISSSTEP", "Particular"]
ALERGENOS = ["Ninguna", "Ninguna", "Ninguna", "Penicilina", "Sulfonamidas", "AINES (Aspirina/Ibuprofeno)", "Medio de Contraste Yodado"]
SERVICIOS = ["Urgencias", "Consulta General", "Medicina Interna", "Pediatría"]

MATRIZ_CLINICA = {
    "Diabetes Mellitus Tipo 2": {
        "cie10": "E11", 
        "sintoma": "Poliuria, polidipsia y fatiga crónica", 
        "farmaco": "Metformina 850mg cada 12 hrs VO + Empagliflozina 10mg al día VO"
    },
    "Hipertensión Arterial Esencial": {
        "cie10": "I10", 
        "sintoma": "Cefalea holocraneal pulsátil y acúfenos", 
        "farmaco": "Losartán 50mg cada 12 hrs VO + Amlodipino 5mg cada 24 hrs VO"
    },
    "Infección de Vías Urinarias": {
        "cie10": "N39.0", 
        "sintoma": "Disuria, tenesmo vesical y dolor suprapúbico", 
        "farmaco": "Nitrofurantoína 100mg cada 6 hrs VO por 7 días"
    },
    "Gastroenteritis Infecciosa": {
        "cie10": "A09", 
        "sintoma": "Evacuaciones líquidas recurrentes, dolor cólico y náusea", 
        "farmaco": "Ciprofloxacino 500mg cada 12 hrs VO por 5 días + Loperamida si aplica"
    },
    "Rinofaringitis Aguda": {
        "cie10": "J00", 
        "sintoma": "Rinorrea hialina, odinofagia intensa y estornudos", 
        "farmaco": "Paracetamol 500mg cada 8 hrs VO + Loratadina 10mg cada 24 hrs VO"
    },
    "Asma Bronquial Exacerbada": {
        "cie10": "J45.9", 
        "sintoma": "Disnea de medianos esfuerzos y sibilancias espiratorias bilaterales", 
        "farmaco": "Salbutamol 2 disparos cada 4 hrs en aerosol + Budesonida inhalada"
    },
    "Insuficiencia Renal Crónica Estadío 4": {
        "cie10": "N18.4", 
        "sintoma": "Edema de miembros inferiores, astenia y oliguria", 
        "farmaco": "Eritropoyetina 4000 UI SC semanal + Carbonato de Calcio 500mg con comidas"
    }
}
DIAG_LISTA = list(MATRIZ_CLINICA.keys())

def generar_curp_y_rfc(nombre, ap_p, ap_m, f_nac, sexo):
    def c(s): return s[0].upper() if s else "X"
    def voc(s):
        for l in s[1:]:
            if l.upper() in "AEIOU": return l.upper()
        return "X"
    def cons(s):
        for l in s[1:]:
            if l.upper() not in "AEIOU" and l.isalpha(): return l.upper()
        return "X"
    
    aa = str(f_nac.year)[2:]
    mm = f"{f_nac.month:02d}"
    dd = f"{f_nac.day:02d}"
    s_cod = "H" if sexo == "MASCULINO" else "M"
    
    curp = f"{c(ap_p)}{voc(ap_p)}{c(ap_m)}{c(nombre)}{aa}{mm}{dd}{s_cod}PL{cons(ap_p)}{cons(ap_m)}{cons(nombre)}0{random.randint(0,9)}"
    rfc = f"{c(ap_p)}{voc(ap_p)}{c(ap_m)}{c(nombre)}{aa}{mm}{dd}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')}{random.randint(10,99)}"
    return curp, rfc

def generar_dataset_expedientes(total_registros=5500):
    datos = []
    fecha_hoy = datetime.now()
    
    for i in range(total_registros):
        sexo = random.choice(["MASCULINO", "FEMENINO"])
        nombre = random.choice(NOMBRES_H) if sexo == "MASCULINO" else random.choice(NOMBRES_M)
        if random.random() > 0.4:
            nombre += " " + (random.choice(NOMBRES_H) if sexo == "MASCULINO" else random.choice(NOMBRES_M))
        ap_paterno = random.choice(APELLIDOS)
        ap_materno = random.choice(APELLIDOS)
        while ap_paterno == ap_materno:
            ap_materno = random.choice(APELLIDOS)
            
        edad = int(np.clip(np.random.normal(48, 22), 0, 96))
        fecha_nac = fecha_hoy - timedelta(days=(edad * 365 + random.randint(0, 364)))
        curp, rfc = generar_curp_y_rfc(nombre.split()[0], ap_paterno, ap_materno, fecha_nac, sexo)
        
        latitud = round(random.uniform(18.0, 20.7), 6)
        longitud = round(random.uniform(-98.4, -96.8), 6)
        
        afiliacion = random.choice(AFILIACIONES)
        nss = f"{random.randint(10,99)}-{random.randint(10,99)}-{random.randint(10,99)}-{random.randint(1000,9999)}"
        servicio = random.choice(SERVICIOS) if edad >= 12 else "Pediatría"
        
        # ANTECEDENTES COMO TEXTO EXPLÍCITO ("Sí" / "No")
        ahf_dm = "Sí" if random.random() > 0.6 else "No"
        ahf_has = "Sí" if random.random() > 0.5 else "No"
        ahf_ca = "Sí" if random.random() > 0.8 else "No"
        app_tab = "Sí" if random.random() > 0.75 and edad > 16 else "No"
        app_alc = "Sí" if random.random() > 0.70 and edad > 16 else "No"
        alergias = random.choice(ALERGENOS)
        
        diag = random.choice(DIAG_LISTA)
        if edad < 12 and diag in ["Diabetes Mellitus Tipo 2", "Insuficiencia Renal Crónica Estadío 4", "Hipertensión Arterial Esencial"]:
            diag = "Rinofaringitis Aguda"
            
        cie10 = MATRIZ_CLINICA[diag]["cie10"]
        sintoma = MATRIZ_CLINICA[diag]["sintoma"]
        farmaco = MATRIZ_CLINICA[diag]["farmaco"]
        
        pas, pad = random.randint(116, 122), random.randint(76, 82)
        fc, fr = random.randint(68, 78), random.randint(14, 18)
        temp = round(random.uniform(36.2, 36.7), 1)
        spo2 = random.randint(96, 99)
        triage = "Verde / No Urgente"
        
        if diag == "Hipertensión Arterial Esencial":
            pas, pad = random.randint(142, 175), random.randint(92, 108)
            triage = "Amarillo / Valorable" if pas < 160 else "Naranja / Urgencia"
        elif diag in ["Gastroenteritis Infecciosa", "Infección de Vías Urinarias"]:
            temp = round(random.uniform(37.6, 39.4), 1)
            fc, fr = random.randint(88, 112), random.randint(18, 22)
            triage = "Amarillo / Valorable"
        elif diag == "Asma Bronquial Exacerbada":
            spo2 = random.randint(86, 92)
            fr, fc = random.randint(22, 28), random.randint(95, 115)
            triage = "Naranja / Urgencia" if spo2 > 88 else "Rojo / Emergencia"
            
        if edad < 12:
            estatura = round(np.random.normal(115, 12), 1)
            peso = round(np.random.normal(26, 6), 1)
        else:
            base_est = 166 if sexo == "MASCULINO" else 154
            estatura = round(np.random.normal(base_est, 5), 1)
            base_peso = 76 if sexo == "MASCULINO" else 64
            peso = round(np.random.normal(base_peso, 11), 1)
            
        imc = round(peso / ((estatura / 100) ** 2), 1)
        
        if imc < 18.5: estado_nut = "Desnutrición / Bajo Peso"
        elif 18.5 <= imc < 25.0: estado_nut = "Normal"
        elif 25.0 <= imc < 30.0: estado_nut = "Sobrepeso"
        else: estado_nut = "Obesidad"
        
        medico_cedula = f"{random.randint(1000000, 9999999)}"
        dias_atras = random.randint(0, 180)
        horas_atras = random.randint(0, 23)
        minutos_atras = random.randint(0, 59)
        fecha_registro = fecha_hoy - timedelta(days=dias_atras, hours=horas_atras, minutes=minutos_atras)
        
        expediente = {
            "ID_Expediente": f"EXP-2026-{i+1:05d}",
            "CURP": curp,
            "RFC": rfc,
            "Nombre": nombre,
            "Apellido_Paterno": ap_paterno,
            "Apellido_Materno": ap_materno,
            "Fecha_Nacimiento": fecha_nac.strftime("%Y-%m-%d"),
            "Edad": edad,
            "Sexo_Biologico": sexo,
            "Estado": "Puebla",
            "Latitud": latitud,
            "Longitud": longitud,
            "Afiliacion_Salud": afiliacion,
            "Numero_Seguridad_Social": nss,
            "Tipo_Servicio_Ingreso": servicio,
            # Cadenas de texto puras
            "Antecedentes_Familiares_Diabetes": ahf_dm,
            "Antecedentes_Familiares_Hipertension": ahf_has,
            "Antecedentes_Familiares_Cancer": ahf_ca,
            "Antecedentes_Personales_Tabaquismo": app_tab,
            "Antecedentes_Personales_Alcoholismo": app_alc,
            "Alergias_Declaradas": alergias,
            "Clasificacion_Triage": triage,
            "Presion_Sistolica_mmHg": pas,
            "Presion_Diastolica_mmHg": pad,
            "Frecuencia_Cardiaca_lpm": fc,
            "Frecuencia_Respiratoria_rpm": fr,
            "Temperatura_C": temp,
            "Saturacion_Oxigeno_SpO2": spo2,
            "Estatura_cm": estatura,
            "Peso_kg": peso,
            "IMC": imc,
            "Estado_Nutricional": estado_nut,
            "CIE10_Diagnostico": cie10,
            "Diagnostico_Principal": diag,
            "Sintoma_Principal": sintoma,
            "Tratamiento_Farmacologico": farmaco,
            "Medico_Tratante_Cedula": medico_cedula,
            "Fecha_Hora_Apertura_Expediente": fecha_registro.strftime("%Y-%m-%d %H:%M:%S")
        }
        datos.append(expediente)
        
    return pd.DataFrame(datos)

# Generar 5,500 registros limpios
df_expedientes = generar_dataset_expedientes(5500)
df_expedientes.to_csv("expedientes_clinicos_puebla_1.csv", index=False, encoding="utf-8-sig")
print("¡Proceso finalizado con éxito!")