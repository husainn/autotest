import os

project_path = os.path.dirname(os.path.dirname(__file__))


testdata_path = os.path.join(project_path,'test_data','test_cases.xlsx')

result_path = os.path.join(project_path,'runner','result.html')

conf_path = os.path.join(project_path,'conf','auto_test.conf')
