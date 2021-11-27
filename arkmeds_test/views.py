from django.http import HttpResponse
from django.shortcuts import render
import requests

from arkmeds_test.database.connection import create_detailed_company_table, create_equipament_table, save_detailed_company_data
from .company.services import Services
from .services.company_services import CompanyServices
import json

def create_call_for_equipment(request):
  create_detailed_company_table()
  create_equipament_table()

  result = requests.get(f"{CompanyServices.base_url()}/empresa/", headers=Services.build_headers()).json()
  first_twently_results = result[:1]
  companys = []

  for company in first_twently_results:
    companys.append(CompanyServices.get_data_about_company(company['id'], Services.build_headers()))

  for company in companys:
    save_detailed_company_data(
      company['tipo'] or None,
      company['nome'] or None,
      company['superior'] or None,
      company['nome_fantasia'] or None,
      company['cnpj'] or None,
      company['cep'] or None,
      company['observacoes'] or None,
      company['contato'] or None,
      company['email'] or None,
      company['telefone1'] or None,
      company['telefone2'] or None,
      company['ramal1'] or None,
      company['ramal2'] or None,
      company['fax'] or None,
      company['rua'] or None,
      company['numero'] or None,
      company['complemento'] or None,
      company['bairro'] or None,
      company['cidade'] or None,
      company['estado'] or None
    )


  equipaments = CompanyServices.get_equipaments_from_company(companys, Services.build_headers())

  for equipament in equipaments[0]['results']:
    payload = Services.build_data_for_create_call(equipament)
    result = CompanyServices.create_call_for_equipment(payload, Services.build_headers())
    calls_for_equipament = CompanyServices.get_all_calls_for_a_device_by_id(equipament['id'], Services.build_headers()).json()
    print(calls_for_equipament['results'])
    break



  return render(request, 'arkmeds_test/create_call_for_equipments.html', {'payload': json.dumps(equipaments)})
