import time
import json

class Services:
  def build_headers():
    return {
      "authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RlZGV2QGFya21lZHMuY29tIiwidXNlcl9pZCI6NTgsImVtYWlsIjoidGVzdGVkZXZAYXJrbWVkcy5jb20iLCJleHAiOjE2MzczNTM4NzN9.rC_87pTxKPQVqwe88bHI0SzXpliReSHwMjKwjVrrYos",
      "Content-Type": "application/json"
    }

  def build_data_for_create_call(equipament):
    return json.dumps({
          'equipament': equipament['id'],
          'solicitante': equipament['proprietario']['id'],
          'tipo_servico': 3,
          'problema': 5,
          'observacoes': 'sdsads',
          'data_criacao': Services.current_date_in_timestamp_format_in_milliseconds(),
          'id_tipo_ordem_servico': 1
      })

  def current_date_in_timestamp_format_in_milliseconds():
    return round(time.time() * 1000)

  def filter_only_non_type_five_companies(companys):
    excluded_type = 5
    filtered_companys = []

    for company in companys:
      if (company['tipo'] != excluded_type):
        filtered_companys.append(company)

    return filtered_companys
