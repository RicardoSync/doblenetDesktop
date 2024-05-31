from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logotipo
        self.image('desarrollador.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(80)
        # Título
        self.cell(30, 10, 'FACTURA', 0, 1, 'R')
        self.ln(20)
    
    def footer(self):
        # Posición a 1.5 cm del final
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Número de página
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def crear_factura(dna, nombre, fecha, monto, no_recibo, concepto, folio, id_transaccion):
    # Crear el objeto PDF
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar el logotipo
    pdf.image("desarrollador.png", x=10, y=8, w=33)  # Ajusta la ruta y tamaño según sea necesario
    pdf.ln(40)  # Espacio después del logotipo

    # Encabezado de la compañía
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Nombre de su compañía', 0, 1, 'L')
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, 'Lema de su compañía', 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 10, 'Ciudad, Código postal', 0, 1, 'L')
    pdf.cell(0, 10, 'Teléfono (503) 555-0190    Fax (503) 555-0191', 0, 1, 'L')

    # Información de la factura
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'FACTURA A:', 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 10, f'Nombre: {nombre}', 0, 1, 'L')
    pdf.cell(0, 10, f'DNA: {dna}', 0, 1, 'L')
    
    # Fecha y número de factura
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, f'FECHA: {fecha}    FACTURA NO: {no_recibo}', 0, 1, 'R')

    # Descripción del proyecto o servicio
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'POR: {concepto}', 0, 1, 'L')

    # Tabla de detalles
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(80, 10, 'DESCRIPCIÓN', 1)
    pdf.cell(30, 10, 'HORAS', 1)
    pdf.cell(30, 10, 'TASA', 1)
    pdf.cell(30, 10, 'CANTIDAD', 1)
    pdf.ln(10)
    pdf.set_font('Arial', '', 10)
    # Aquí deberías agregar los ítems reales en lugar de un ejemplo
    items = [
        {'descripcion': 'Servicio 1', 'horas': 5, 'tasa': 50, 'cantidad': 250},
        {'descripcion': 'Servicio 2', 'horas': 3, 'tasa': 75, 'cantidad': 225},
    ]
    for item in items:
        pdf.cell(80, 10, item['descripcion'], 1)
        pdf.cell(30, 10, str(item['horas']), 1)
        pdf.cell(30, 10, str(item['tasa']), 1)
        pdf.cell(30, 10, f"{item['cantidad']:.2f} €".encode('latin1'), 1)
        pdf.ln(10)

    # Totales
    pdf.ln(10)
    subtotal = sum(item['cantidad'] for item in items)
    impuesto = subtotal * 0.1  # Asumiendo un impuesto del 10%
    total = subtotal + impuesto
    pdf.cell(110, 10, '', 0)
    pdf.cell(30, 10, 'SUBTOTAL', 1)
    pdf.cell(30, 10, f"{subtotal:.2f} €".encode('latin1'), 1)
    pdf.ln(10)
    pdf.cell(110, 10, '', 0)
    pdf.cell(30, 10, 'IMPUESTO', 1)
    pdf.cell(30, 10, f"{impuesto:.2f} €".encode('latin1'), 1)
    pdf.ln(10)
    pdf.cell(110, 10, '', 0)
    pdf.cell(30, 10, 'TOTAL', 1)
    pdf.cell(30, 10, f"{total:.2f} €".encode('latin1'), 1)

    # Guardar el archivo PDF
    pdf_file = f"factura_{no_recibo}.pdf"
    pdf.output(pdf_file, 'F')
    print(f"Factura guardada como {pdf_file}")

# Ejemplo de uso
crear_factura('1234567890', 'Cliente Ejemplo', '03/01/2019', 0, 100, 'Descripción del proyecto o servicio', 'Folio123', 'IDtransaccion123')
