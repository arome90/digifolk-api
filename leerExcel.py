import pandas as pd
import json

def excel_to_json(input_excel, output_json):
    # Lee el archivo Excel
    df = pd.read_excel(input_excel, sheet_name='Coplas')

    # Convierte cada fila a un diccionario y agrega a la lista
    data = []
    obra = ""
    pieza = {}
    for index, row in df.iterrows():
        if(str(row.to_dict()["Obra"]) != "nan"): 
            if obra != "":
                data.append(pieza)
            obra = row.to_dict()["Obra"]
            pieza = row.to_dict()
            versos = []
            versos.append(row.to_dict()["Versos"])
        else:
            if str(row.to_dict()["Versos"]) != "nan":
                versos.append(row.to_dict()["Versos"])
            else:
                versos.append("")
            pieza["Versos"] = versos
            

    # Exporta la lista de diccionarios a JSON
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)



# Especifica el nombre del archivo Excel de entrada y el nombre del archivo JSON de salida
input_excel_file = 'DIGIFOLK Ejemplos de coplas.xlsx'
output_json_file = 'salida.json'

# Llama a la función para convertir Excel a JSON
excel_to_json(input_excel_file, output_json_file)

print(f"La conversión de {input_excel_file} a {output_json_file} se ha completado con éxito.")
