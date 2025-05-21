import os

def save_data(dataset, formato, caminho):
    """Salva os dados em diferentes formatos (csv, excel, json)."""
    
    # Garantir que a pasta de destino existe
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    
    # Nome do arquivo
    arquivo = os.path.join(caminho, 'datasetclean')
    
    if formato == 'csv':
        dataset.to_csv(f'{arquivo}.csv', index=False, sep=',', encoding='utf-8')
        print(f'Dados salvos como CSV em: {arquivo}.csv')
        
    elif formato == 'excel':
        dataset.to_excel(f'{arquivo}.xlsx', index=False)
        print(f'Dados salvos como Excel em: {arquivo}.xlsx')
        
    elif formato == 'json':
        dataset.to_json(f'{arquivo}.json', orient='records', lines=True)
        print(f'Dados salvos como JSON em: {arquivo}.json')
        
    else:
        print('Formato não suportado! Use "csv", "excel" ou "json".')