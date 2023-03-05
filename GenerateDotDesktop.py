class DotDesktop:

    def Generate(AppName, Type, Version, Comment, Categories, Icon, Exec, Terminal):

        dotDesktop = open(AppName + '.desktop', 'w')
        dotDesktop.write(f'[Desktop Entry]\nName={AppName}\nType={Type}\nVersion={Version}\nComment={Comment}\nCategories={Categories}\nIcon={Icon}\nExec={Exec}\nTerminal={Terminal}')
        dotDesktop.close()
