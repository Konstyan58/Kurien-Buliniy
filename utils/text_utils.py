import requests


def s(latitude, longituide, API_TOKEN):
    my_link = f"https://api.airvisual.com/v2/nearest_city?lat={latitude}&lon={longituide}&key={API_TOKEN}"

    dsapros_na_site = requests.get(my_link)

    datas = dsapros_na_site.json()

    cntry = datas['data']['country']
    ppltn = datas['data']['current']['pollution']['aqius']
    temp = datas['data']['current']['weather']['tp']
    vlsnst = datas['data']['current']['weather']['hu']

    return cntry, ppltn, temp, vlsnst
