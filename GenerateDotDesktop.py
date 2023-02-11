import json


class DotDesktop:

    def Generate():
        with open('config.json') as Config:
            data = json.load(Config)

            for s in data['CFG']:
                print('\nConfig:\n-------------------------------')

                AppName = (s['Name'])           # str
                print('Application Name:', AppName)

                AppType = (s['Type'])           # str
                print('Application Type:', AppType)

                AppVersion = (s['Version'])     # str
                print('Application Version:', AppVersion)

                AppComment = (s['Comment'])     # str
                print('Application Comment:', AppComment)

                AppCategories = (s['Categories']) # str
                print('Application Categories:', AppCategories)

                AppIcon = (s['Icon'])           # str
                print('Application Icon:', AppIcon)

                AppExec = (s['Exec'])           # str
                print('Application Execute:', AppExec)

                AppTerminal = (s['Terminal'])   # bool
                print('Application Terminal:', AppTerminal)

                print('-------------------------------')

        dotDesktop = open(AppName + '.desktop', 'w')
        dotDesktop.write(f'[Desktop Entry]\nName={AppName}\nType={AppType}\nVersion={AppVersion}\nComment={AppComment}\nCategories={AppCategories}\nIcon={AppIcon}\nExec={AppExec}\nTerminal={AppTerminal}')
        dotDesktop.close()
