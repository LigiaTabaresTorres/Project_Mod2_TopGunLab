
class Indexes:
  _instance = None
      
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self, fin_info):
    self.fin_info = fin_info
    self.value = {}
    self.respuesta = {}

    self.Liquidez = {
      'fin_info': self.fin_info,
      'activos_corrientes': self.fin_info.get('activos_corrientes', 0),
      'pasivos_corrientes': self.fin_info.get('pasivos_corrientes', 1),
      'inventario':self.fin_info.get('inventario', 0),
      'efectivo':self.fin_info.get('efectivo', 0),
    }

    self.Solvencia = {
      'deuda_pasivos': self.fin_info.get('deuda_pasivos', 0),
      'patrimonio': self.fin_info.get('patrimonio', 1),
    }  

    self.Eficiencia = {
      'rotacion_inventario': self.fin_info.get('rotacion_inventario', 0),
      'ventas': self.fin_info.get('ventas', 0),
      'activo_fijo': self.fin_info.get('activo_fijo', 0),
    }

    self.Rentabilidad = {
      'beneficio_neto': self.fin_info.get('beneficio_neto', 0),
      'patrimonio': self.fin_info.get('patrimonio', 0),
    }

    self.Valuacion = {
      'beneficio_neto': self.fin_info.get('beneficio_neto', 0),
	    'dividendos': self.fin_info.get('dividendos', 0),
	    'acciones_totales': self.fin_info.get('acciones_totales', 0),
      'precio_acción': self.fin_info.get('precio_acción', 0),
      'acciones_propias': self.fin_info.get('acciones_propias', 0),
      'patrimonio': self.fin_info.get('patrimonio', 1),
    }

    

  #Indicadores de Liquidez
  def current_ratio(self):
    current_ratio = self.Liquidez.get('activos_corrientes')/self.Liquidez.get('pasivos_corrientes')
    self.value.update({
      'current_ratio': current_ratio,
    })
    self.respuesta.update({
      'current_ratio': f'Se espera que el resultado del indicador sea de al menos 1.5. Esto significaría que la empresa supera con activos a sus pasivos casi por el doble. Es decir, un 50%.'
    })
    return current_ratio

  def quick_ratio(self):
    quick_ratio = (self.Liquidez.get('activos_corrientes')-self.Liquidez.get('inventario'))/self.Liquidez.get('pasivos_corrientes')
    self.value.update({
      'quick_ratio': quick_ratio,
    })
    self.respuesta.update({
      'quick_ratio': f'Se espera que el resultado del indicador se encuentre por encima de 1.0, para considerar que la empresa sí se mantiene líquida a pesar de no vender su inventario.'
    })
    return quick_ratio
  def cash_ratio(self):
    cash_ratio = self.Liquidez.get('efectivo')/self.Liquidez.get('pasivos_corrientes')
    self.value.update({
      'cash_ratio': cash_ratio,
    })
    self.respuesta.update({
      'cash_ratio': f'Se espera que el resultado del indicador se encuentre por encima de 1.0, para considerar que puede pagar sus deudas del corto plazo con lo que tiene actualmente en el banco.'
    })    
    return cash_ratio
  #Indicador de Solvencia 
  def debt_equity(self):
    debt_equity = self.Solvencia.get('deuda_pasivos')/self.Solvencia.get('patrimonio')
    self.value.update({
      'debt_equity': debt_equity,
    }), self.respuesta.update({
      'debt_equity': f'Se espera que el resultado del indicador se encuentre por debajo de 0.5. Esto quiere decir, que el patrimonio de la empresa supera la deuda.'
    })  
    return debt_equity
  #Indicadores de Eficiencia
  def days_inventory(self):
    days_inventory = 365/self.Eficiencia.get('rotacion_inventario')
    self.value.update({
      'days_inventory': days_inventory,
    })
    self.respuesta.update({
      'days_inventory': f'Este indicador mostrará, cada cuantos días la empresa renueva su inventario. Entre más grande sea la rotacion de inventario, significa que la empresa renueva el inventario más cantidad de veces por año.'
    })  
    return days_inventory

  def assets_turnover(self):
    assets_turnover = self.Eficiencia.get('ventas')/self.Eficiencia.get('activo_fijo')
    self.value.update({
      'assets_turnover': assets_turnover,
    }) 
    self.respuesta.update({
      'assets_turnover': f'Este indicador sirve para comparar la empresa con empresas competidoras. Al hallar el assets turnover de las empresas competidoras. Podrá hacer una comparación con el promedio de todos los assets turnover. Así sabrá que, si su assets turnover esta por encima del promedio de los assets turnover de las demás empresas. Entonces, quiere decir que su empresa rota más veces su activo que las demás empresas, es decir, utiliza correctamente sus activos para generar ingresos.'
    }) 
    return assets_turnover
  #Indicadores de Rentabilidad
  def return_on_equity(self):
    roe = self.Rentabilidad.get('beneficio_neto')/self.Rentabilidad.get('patrimonio')
    self.value.update({
      'roe': roe,
    }), self.respuesta.update({
      'roe': f'Por {roe} dólar(es) de patrimonio, genera un dólar de ganancia.'
    }) 
    return roe
  def net_margin(self):
    net_margin = self.Rentabilidad.get('beneficio_neto')/self.Rentabilidad.get('ventas')
    self.value.update({
      'net_margin': net_margin,
    })
    self.respuesta.update({
      'net_margin': f'De cada 100 dólares que entran a la empresa, {net_margin} se quedan en la empresa.'
    }) 
    return net_margin
  #Indicadores de Valuación
  def earnings_per_share(self):
    eps = (self.Valuacion.get('beneficio_neto')-self.Valuacion.get('dividendos'))/self.Valuacion.get('acciones_totales')
    self.value.update({
      'eps': eps,
    })
    self.respuesta.update({
      'eps': f'La empresa genera {eps} dólar(es) de beneficio por cada acción.'
    })
    return eps 
  def price_earnings_ratio(self):
    per = self.Valuacion.get('precio_acción')/self.earnings_per_share
    self.value.update({
      'per': per,
    })
    self.respuesta.update({
      'per': f'Realmente pagas {per} por cada dólar de beneficio producido para tus acciones'
    }) 
    return per
  def price_to_sales_ratio(self):
    ps = self.Valuacion.get('precio_acción')/(self.Eficiencia.get('ventas')/self.Valuacion.get('acciones_propias'))
    self.value.update({
      'ps': ps,
    })
    self.respuesta.update({
      'ps': f'Realmente pagas {ps} por cada dólar de ventas producido para tus acciones.'
    }) 
    return ps
  def book_value(self):
    bv = self.Valuacion.get('patrimonio')/self.Valuacion.get('acciones_propias')
    self.value.update({
      'bv': bv,
    })
    self.respuesta.update({
      'bv': f'El procentaje {bv}, representa el porcentaje del patrimonio que le corresponde a cada acción. Es decir, mientras más acciones tengas, mayor porcentaje de patrimonio te corresponderá.'
    }) 
    return bv
  def price_to_book_value(self):
    pbv = self.Valuacion.get('precio_acción')/self.book_value
    self.value.update({
      'pbv': pbv,
    })
    self.respuesta.update({
      'pbv': f'Un PBV de 0.5 significa que el valor de lo que posee la empresa (BV) es dos veces mayor al precio actual de la acción. Por lo tanto sería un indicador de compra de acciones.'
    })   
    return pbv
  
  def load(self, name):
    self.functions= {
      'current_ratio': self.current_ratio,
      'quick_ratio': self.quick_ratio,
      'cash_ratio': self.cash_ratio,
      'debt_equity': self.debt_equity,
      'days_inventory': self.days_inventory,
      'assets_turnover': self.assets_turnover,
      'roe': self.return_on_equity,
      'net_margin': self.net_margin,
      'earnings_per_share': self.earnings_per_share,
      'price_earnings_ratio': self.price_earnings_ratio,
      'book_value': self.book_value,
      'price_to_book_value': self.price_to_book_value,
    }
    
    return self.functions[name]()

  def condiciones(self):
    if self.current_ratio() and self.quick_ratio() and self.cash_ratio() > 1:
      return f'La empresa evaluada es Líquida. Es decir, que la empresa puede pagar sus deudas de corto plazo. Puede ser buena idea comprar acciones de esta empresa, solo falta comprobar si liquidez.'
    elif self.debt_equity() < 0.5:
      return f'La empresa evaluada es Solvente. Es decir, que la empresa está financiada mucho más por el patrimonio que por la deuda. Es buena idea comprar acciones de esta empresa, evalua su rentabilidad para mayor seguridad.'
    else:
      if self.days_inventory() < 92:
        return f'La empresa evaluada es Eficiente. A pesar de no ser Líquida y Solvente. Esto quiere decir, que la empresa es capaz de pagar las deudas vendiendo su inventario.'
    
    if self.return_on_equity() < 10:
      return f'La empresa evaluada es Rentable. Obtiene un dólar de ganancia por menos de 10 dólares de patrimonio. Es hora de comprar acciones.'
    if self.price_to_book_value() < 0.5:
      return f'La empresa evaluada tiene valor intrínseco. Es decir, lo que debería cotizar la empresa enrealidad.'

    
  