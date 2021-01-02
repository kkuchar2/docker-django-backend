# url = "https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2"
#
#
# class CovidDataFetcher:
#
#     @staticmethod
#     def fetch_data():
#         page = urlopen(url)
#         html_bytes = page.read()
#         html_raw = html_bytes.decode("utf-8")
#         parsed_html = BeautifulSoup(html_raw, "html.parser")
#         cases = parsed_html.find('pre', attrs={'id': 'registerData'}, recursive=True)
#         d = json.loads(cases.next)
#         a = json.loads(d['parsedData'])
#         joined_date = d['fileName'][0:8]
#         day = joined_date[0:2]
#         month = joined_date[2:4]
#         year = joined_date[4:8]
#         date_str = f"{day}-{month}-{year}"
#         dt = datetime.strptime(date_str, '%d-%m-%Y')
#         q = a[0]
#         today_cases = q['Liczba']
#         print(f'Day: {dt}, cases: {today_cases}')
#         return dt, today_cases
#
#
# @celery_app.task
# def fetch_covid(a, b):
#     print("Fetching covid data...")
#     date, count = CovidDataFetcher.fetch_data()
#     COVID.objects.update_or_create(date=date, count=count)
#     print("Saved to db")
#
#
# fetch_covid(0, 0)