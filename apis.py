from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Union
from datetime import datetime
import sys
sys.path.append('./')
from tools import fft, envelope_spectrum


DEBIAS = True
app = FastAPI()

class InputDataModel(BaseModel):
    data: List[Dict[str, Union[str, List[float]]]]
    freq_list: List[int]

def process_fft(data: Dict, freq_list: List[int], debias=True) -> Dict:
    try:
        processed_data = {}
        for key, value in data.items():
            freq, magnitude = fft(value, debias)
            filtered_freq = freq.tolist()
            filtered_magnitude = magnitude.tolist()
            if freq_list:
                filtered_freq = []
                filtered_magnitude = []
                for f, m in zip(freq.tolist(), magnitude.tolist()):
                    if f in freq_list:
                        filtered_freq.append(f)
                        filtered_magnitude.append(m)
            processed_data[key] = {"freq": filtered_freq, "magnitude": filtered_magnitude}
        return processed_data
    except Exception as e:
        print(f"Error processing data: {e}")
        raise e

def process_envelope(data: Dict, freq_list: List[int], debias=True) -> Dict:
    try:
        processed_data = {}
        for key, value in data.items():
            freq, envelope = envelope_spectrum(value, debias)
            filtered_freq = freq.tolist()
            filtered_envelope = envelope.tolist()
            if freq_list:
                filtered_freq = []
                filtered_envelope = []
                for f, e in zip(freq.tolist(), envelope.tolist()):
                    if f in freq_list:
                        filtered_freq.append(f)
                        filtered_envelope.append(e)
            processed_data[key] = {"freq": filtered_freq, "envelope": filtered_envelope}
        return processed_data
    except Exception as e:
        print(f"Error processing data: {e}")
        raise e

@app.post("/api/data_fft")
def data_fft(input_data: InputDataModel):
    '''
    curl -X POST -H "Content-Type: application/json" -d '{
    "freq_list":[],
    "data": [
    {
      "ts": "2024-01-30T12:34:56",
      "acc_rms_x": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    },
    {
      "ts": "2024-01-30T14:34:56",
      "acc_rms_x": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    }
  ]
}' http://127.0.0.1:8000/api/data_fft
    '''
    try:
        rows = input_data.data
        freq_list = input_data.freq_list
        processed_data = [{"ts": row.get("ts"), "data_fft": process_fft({key: value for key, value in row.items() if key != 'ts' and value is not None}, freq_list, DEBIAS)} for row in rows]

        return {"fft_return": processed_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input data: {e}")

@app.post("/api/data_es")
def data_es(input_data: InputDataModel):
    try:
        rows = input_data.data
        freq_list = input_data.freq_list
        processed_data = [{"ts": row.get("ts"), "data_es": process_envelope({key: value for key, value in row.items() if key != 'ts' and value is not None}, freq_list, DEBIAS)} for row in rows]

        return {"es_return": processed_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input data: {e}")

# 启动 FastAPI 应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("apis:app", host="127.0.0.1", port=8000, reload=True)
