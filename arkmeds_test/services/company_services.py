import requests
import os
import json
from ..company.services import Services

class CompanyServices:
  def get_data_about_company(id, headers):
    return requests.get(f"{CompanyServices.base_url()}/company/{id}", headers=headers).json()

  def get_equipaments_from_company(companys, headers):
    companysFiltered = Services.filter_only_non_type_five_companies(companys)

    equipaments_by_company = []

    for company in companysFiltered:
      equipament = requests.get(f"{CompanyServices.base_url()}/equipamentos_paginados/?empresa_id={company['id']}", headers=headers).json()
      equipaments_by_company.append(equipament)

    return equipaments_by_company

  def create_call_for_equipment(payload, headers):
    return requests.post(
      f"https://desenvolvimento.arkmeds.com/api/v2/chamado/novo/",
      data=payload,
      headers=headers,
    )

  def get_all_calls_for_a_device_by_id(device_id, headers):
    return requests.get(
      f"{CompanyServices.base_url()}/chamado/?equipamento_id={device_id}",
      headers=headers
    )


  def base_url():
    return os.getenv('BASE_URL')
