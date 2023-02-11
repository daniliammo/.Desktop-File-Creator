class WriteConfig:

    def WriteCFG(AppName, Type, Version, Comment, Categories, Icon, Exec, Terminal):
        CFG = open('config.json', 'w')
        Result = ('''{
    "CFG": [
        {
            "Name": "''' + AppName + '''",
            "Type": "''' + Type + '''",
            "Version": "''' + Version + '''",
            "Comment": "''' + Comment + '''",
            "Categories": "''' + Categories + '''",
            "Icon": "''' + Icon + '''",
            "Exec": "''' + Exec + '''",
            "Terminal": "''' + str(Terminal) + '''"
        }
    ]
}\n''')
        CFG.write(Result)
        CFG.close()
