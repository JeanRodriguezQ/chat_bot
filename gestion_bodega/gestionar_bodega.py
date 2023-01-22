'''Gestión de Bodega'''

def guardar_json(datos):
  import json
  archivo = open('bodega_autos.json', 'w+')
  json.dump(datos,archivo,indent=4)

def start_bodega():

  bodega = {"sedán":{
            "nissan":{
              "modelo":"sentra",
              "year":2022,
              "potencia_HP":149,
              "rango de precio":[19950,22700],
              "consumo_MPG": 39,
              "tipo" : "gasolina",
              "plazas" : 5,
              "transmicion": "automatico",
              },
            "honda":{
              "modelo":"accord",
              "year":"",
              "potencia_HP":192,            
              "rango de precio":[26520,38450],
              "consumo_MPG": 47,
              "tipo": "hibrido",
              "plazas": 5,
              "transmicion": "automatico"
              },
            "toyota":{
              "modelo":"corolla", 
              "year":"",
              "potencia_HP":122,
              
              "rango de precio":[26520,38450],
              "consumo_MPG": 47,
              "tipo": "hibrido",
              "plazas": 5,
              "transmicion": "automatico"
              },
            },
            
          "pickup":{
            "toyota":{
              "modelo":"hilux",
              "year":"",
              "potencia_HP":122,
              
              "rango de precio":[45300,48000],
              "consumo_MPG": 26.72,
              "tipo": "diesel",
              "plazas": 2,
              "transmicion": "automatico"
                    
                },
            "ford":{
              "modelo":"ranger",
              "year":"",
              "potencia_HP":122,
              
              "rango de precio":[45300,48000],
              "consumo_MPG": 24.24,
              "tipo": "diesel ",
              "plazas": 5,
              "transmicion": "manual"
                    
                },
            "isuzu":{
              "modelo":"Dmax",
              "year":"",
              "potencia_HP":122,
              
              "rango de precio":[71000],
              "consumo_MPG": 14.9,
              "tipo": "diesel ",
              "plazas": 5,
              "transmicion": "manual"      
                }


            },
          "camioneta":{
            "honda":{
              "modelo":"HR-V",
              "year":"",
              "potencia_HP":119,
              
              "rango de precio":[26990,30990],
              "consumo_MPG": 46.1,
              "tipo": "gasolina ",
              "plazas": 5,
              "transmicion": "manual"
                    
                },
            "toyota":{
              "modelo":"highlander",
              "year":"",
              "potencia_HP":122,
              
              "rango de precio":[36420,46075],
              "consumo_MPG":24.1,
              "tipo": "gasolina ",
              "plazas": 5,
              "transmicion": "automatico"
                    
                },
            "nissan":{
              "modelo":"X-Trail",
              "year":"",
              "potencia_HP":163,
              
              "rango de precio":[42160,56510],
              "consumo_MPG": 44.3,
              "tipo": "hibrido",
              "plazas": 5,
              "transmicion": "automatico"
              }
              },
          "coupé":{

            "bmw":{
              "modelo":"serie 8",
              "year":"",
              "potencia_HP":350,
              
              "rango de precio":[103306,198481],
              "consumo_MPG": 22,
              "tipo": "electrico ",                                                                                                                                                                         
      
              "plazas": "4",
              "transmicion": "automatico"
                    
                },
            "subaru":{
              "modelo":"BRZ",
              "year":"",
              "potencia_HP":163,
              
              "rango de precio":[42160,56510],
              "consumo_MPG": 44.3,
              "tipo": "hibrido",
              "plazas": 5,
              "transmicion": "automatico"
              },
                    


            },
          "deportivo":{
            "nissan":{
              "modelo":"gtr nismo",
              "year":2017,
              "potencia_HP":592,
              
              "rango de precio":[106050,146.000],
              "consumo_MPG": 19.9,
              "tipo": "gasolina ",
              "plazas": 4,
              "transmicion": "automatico"
                    
                },
            "toyota":{
              "modelo":"gr supra",
              "year":2023,
              "potencia_HP":368,
              "rango de precio":[103306,198481],
              "consumo_MPG": 29.0,
              "tipo": "electrico ",
              "plazas": "4",
              "transmicion": "automatico"
                    
                },
            "corvette":{
              "modelo":"stingray",
              "year":2019,
              "potencia_HP":495,
              
              "rango de precio":[139999,159999],
              "consumo_MPG": 15,
              "tipo": "gasolina",
              "plazas": 2,
              "transmicion": "automatico"      


              }
            }
  }
  guardar_json(bodega)
# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    start_bodega()
