from fastapi import FastAPI
import pandas as pd
from typing import List
import datetime
from pydantic import BaseModel as PydanticBaseModel
# import requests
import logging

# Configuración básica del logger
logging.basicConfig(filename='app_logs.log', level=logging.INFO)

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

# BaseModel para el endpoint "/all_data/"
class AllData(BaseModel):
    Name: str 
    Symbol: str 
    Date: str
    High: float 
    Low: float 
    Open: float 
    Close: float 
    Volume: float 
    Marketcap: float 

# BaseModel para el endpoint "/close_price_variation/"
class ClosePriceVariation(BaseModel):
    Date: str
    Close: float
    Symbol: str
    
# BaseModel para el endpoint "/open_price_variation/"
class OpenPriceVariation(BaseModel):
    Date: str
    Open: float
    Symbol: str
    
# BaseModel para el endpoint "/transaction_volume/"
class TransactionVolume(BaseModel):
    Symbol: str
    Volume: float
    
# BaseModel para el endpoint "/marketcap_histogram/"
class MarketCapHistogram(BaseModel):
    MarketCap: float
    Symbol: str

# BaseModel para el endpoint "/high_low_relation/"
class HighLowRelation(BaseModel):
    High: float
    Low: float
    Symbol: str
        
app = FastAPI(
    title="Servidor de datos",
    description="Historico de cryptomonedas",
    version="0.1.0",
)

csv_file = './archivo_combinado.csv'
data = pd.read_csv(csv_file)

# Endpoint "/all_data/"
@app.get("/all_data/", response_model=List[AllData])
def retrieve_all_data():
    todosmisdatos = data.fillna(0)
    all_data_list = [
        AllData(
            Name=row['Name'],
            Symbol=row['Symbol'],
            Date=row['Date'],
            High=row['High'],
            Low=row['Low'],
            Open=row['Open'],
            Close=row['Close'],
            Volume=row['Volume'],
            Marketcap=row['Marketcap']
        )
        for row in todosmisdatos.to_dict('records')
    ]
    logging.info("Vuelco de todos los datos para los estadisticos descriptivos")
    return all_data_list


'''
# METODO POST
# Endpoint "/add_data/"
@app.post("/add_data/", response_model=list[AllData])
async def add_data(all_data: AllData):
    new_data = {
        'Name': all_data.Name,
        'Symbol': all_data.Symbol,
        'Date': all_data.Date,
        'High': all_data.High,
        'Low': all_data.Low,
        'Open': all_data.Open,
        'Close': all_data.Close,
        'Volume': all_data.Volume,
        'Marketcap': all_data.Marketcap
    }
    data = data.append(new_data, ignore_index=True)
    return {"message": "Data added successfully"}
  
url = "http://fastapi:8000/add_data/"

data_to_send = {
    "Name": "Bitcoin",
    "Symbol": "BTC",
    "Date": "20130429",
    "High": 147.48800659179688,
    "Low": 134.0,
    "Open": 134.44400024414062,
    "Close": 144.5399932861328,
    "Volume": 0.0,
    "Marketcap": 1603768864.5
}

response = requests.post(url, json=data_to_send)
'''

@app.get("/close_price_variation/", response_model=List[ClosePriceVariation])
def retrieve_close_price_variation():
    datos_cpv = data[['Date', 'Close', 'Symbol']]
    datos_cpv_na = datos_cpv.fillna(0)
    close_price_variation_list = [
        ClosePriceVariation(
            Date=row['Date'],
            Close=row['Close'],
            Symbol=row['Symbol']
        )
        for row in datos_cpv_na.to_dict('records')
    ]
    logging.info("Vuelco de Date, Close y Symbol")
    return close_price_variation_list

@app.get("/open_price_variation/", response_model=List[OpenPriceVariation])
def retrieve_open_price_variation():
    datos_opv = data[['Date', 'Open', 'Symbol']]
    datos_opv_na = datos_opv.fillna(0)
    open_price_variation_list = [
        OpenPriceVariation(
            Date=row['Date'],
            Open=row['Open'],
            Symbol=row['Symbol']
        )
        for row in datos_opv_na.to_dict('records')
    ]
    logging.info("Vuelco de Date, Open y Symbol")
    return open_price_variation_list

@app.get("/transaction_volume/", response_model=List[TransactionVolume])
def retrieve_transaction_volume():
    datos_tv = data[['Symbol', 'Volume']]
    datos_tv_na = datos_tv.fillna(0)
    transaction_volume_list = [
        TransactionVolume(
            Symbol=row['Symbol'],
            Volume=row['Volume']
        )
        for row in datos_tv_na.to_dict('records')
    ]
    logging.info("Vuelco de Volume y Symbol")
    return transaction_volume_list

@app.get("/marketcap_histogram/", response_model=List[MarketCapHistogram])
def retrieve_marketcap_histogram():
    marketcap_data = data[['Marketcap', 'Symbol']]
    marketcap_data_na = marketcap_data.fillna(0)
    marketcap_histogram_list = [
        MarketCapHistogram(
            MarketCap=row['Marketcap'],
            Symbol=row['Symbol']
        )
        for row in marketcap_data_na.to_dict('records')
    ]
    logging.info("Vuelco de Marketcap y Symbol")
    return marketcap_histogram_list

@app.get("/high_low_relation/", response_model=List[HighLowRelation])
def retrieve_high_low_relation():
    datos_hlr = data[['High', 'Low', 'Symbol']]
    high_low_relation_list = [
        HighLowRelation(
            High=row['High'],
            Low=row['Low'],
            Symbol=row['Symbol']
        )
        for row in datos_hlr.to_dict('records')
    ]
    logging.info("Vuelco de High, Low y Symbol")
    return high_low_relation_list
