import requests
import json

BASE_URL = "https://api.appsheet.com/api/v2"
APP_ID = "8e772aab-61ee-4a52-b00c-f319a780fffb"
TABLE_NAME = "maestro_reglas"
ACCESS_KEY = "V2-KM5Oi-WoGs8-oLlV6-k8pUi-nvKrA-Aw2CK-OaFn5-ozg8W"


def get_all_rows_from_table(app_id, table_name, access_key):
    """
    Devuelve todas las filas de la tabla 'table_name' de la app 'app_id'
    usando la acción 'Find' con un FilterCondition que devuelva TRUE
    para todos los registros.
    """
    url = f"{BASE_URL}/apps/{app_id}/tables/{table_name}/Action"

    headers = {
        "ApplicationAccessKey": access_key,
        "Content-Type": "application/json"
    }

    payload = {
        "Action": "Find",
        "Properties": {
            "Locale": "es-ES",
            "Location": "0.0,0.0",
            "Timezone": "UTC"
        },
        "Rows": [],
        "FilterCondition": "TRUE"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.ok:
        return response.json()
    else:
        raise Exception(
            f"Error al obtener datos: {response.status_code} - {response.text}"
        )


if __name__ == "__main__":
    try:
        data = get_all_rows_from_table(APP_ID, TABLE_NAME, ACCESS_KEY)
        print("Datos obtenidos con éxito:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as e:
        print("Ocurrió un error:", str(e))
