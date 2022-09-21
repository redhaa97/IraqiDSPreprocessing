
def convertEmojiToWords(dataSet):
    import re

    happyPattren = [r'\U0001F600', r'\U0001F603', r'\U0001F604',
                    r'\U0001F601',  r'\U0001F60A', r'\U0001F638', r'\U0001F63A',
                    r'\U0001F923', r'\U0001F602', r'\U0001F606', r'\U0001F639',
                    r'\U0001F48C', r'\U0001F498', r'\U0001F49D', r'\U0001F90D',
                    r'\U0001F496', r'\U0001F497', r'\U0001F493', r'\U0001F49E',
                    r'\U0001F495', r'\U0001F49F', r'\U0001F494', r'\U0001F49F',
                    r'\U00002763', r'\U00002764', r'\U0001F9E1', r'\U0001F49B',
                    r'\U0001F49A', r'\U0001F49A', r'\U0001F499', r'\U0001F49C',
                    r'\U0001F90E', r'\U0001F5A4', r'\U0001F60E', r'\U00002665',
                    r'\U0001F60A', r'\U0001F970', r'\U0001F60D', r'\U0001F929',
                    r'\U0001F618', r'\U0001F617', r'\U0000263A',  r'\U0001F61A',
                    r'\U0001F619', r'\U0001F60B', r'\U0001F61B', r'\U0001F61C',
                    r'\U0001F92A',  r'\U0001F911', r'\U0001F917', r'\U0001F60C',
                    r'\U0001F973', r'\U0001F63D', r'\U0001F63B', r'\U0001F44F',
                    r'\U0001F470', r'\U0001F469\U0000200D\U0001F393',
                    r'\U0001F468\U0000200D\U0001F393', r'\U0001F935', r'\U0001F648',
                    r'\U0001F649', r'\U0001F64A', r'\U0001F4AF', r'\U0001F4A2',
                    r'\U0001F4A5', r'\U0001F4AB', r'\U0000270C', r'\U0001F918',
                    r'\U0001F44D', r'\U0001F483' , r'\U0001F57A', r'\U0001F46F',
                    r'\U00002728', r'\U0001F388', r'\U0001F389', r'\U0001F38A',
                    r'\U0001F382', r'\U0001F48B', r'\U00002661', r'\U0001F4DD',
                    ]
    for emoji in happyPattren:
        match = re.search(emoji, dataSet)
        if match:
            dataSet = re.sub(emoji, " سعيد ", dataSet)

    fearPattren = [r'\U0001F626', r'\U0001F627', r'\U0001F628', r'\U0001F630',
                   r'\U0001F625', r'\U0001F622', r'\U0001F631', r'\U0001F623',
                   r'\U0001F613', r'\U0001F62B', r'\U0001F61F', r'\U0001F480',
                   r'\U00002620', r'\U0001F479', r'\U0001F47A', r'\U0001F47B',
                   r'\U0001F47D', r'\U0001F47E', r'\U0001F635', ]
    for emoji in fearPattren:
        match = re.search(emoji, dataSet)
        if match:
            dataSet = re.sub(emoji, " خوف ", dataSet)


    sadPattren = [r'\U0001F614', r'\U0001F62A', r'\U0001F641', r'\U00002639',
                  r'\U0001F62D', r'\U0001F61E', r'\U0001F629', r'\U0001F63F',
                  r'\U00002764\U0000FE0F\U0000200D\U0001FA79', r'\U0001F972',
                  r'\U0001F912',  r'\U0001F494', r'\U0001F912']
    for emoji in sadPattren:
        match = re.search(emoji, dataSet)
        if match:
            dataSet = re.sub(emoji, " حزن ", dataSet)

    angryPattren = [r'\U0001F624', r'\U0001F621', r'\U0001F620',
                    r'\U0001F92C', r'\U0001F63E',
                    r'\U0001F90C', r'\U0001F90F', r'\U0001F47F',
                    r'\U0001F595', r'\U0001F44A', r'\U0001F91B',
                    r'\U0001F91C', r'\U0001F450', r'\U0001F31A',
                    r'\U00002764\U0000FE0F\U0000200D\U0001F525']
    for emoji in angryPattren:
        match = re.search(emoji, dataSet)
        if match:
            dataSet = re.sub(emoji, " غضب ", dataSet)

    disgustPattren = [r'\U0001F610', r'\U0001F611', r'\U0001F612',
                      r'\U0001F637', r'\U0001F922', r'\U0001F92E', r'\U0001F927',
                      r'\U0001F616', r'\U0001F4A9', r'\U0001F4A8',r'\U0001F61D',
                      r'\U0001F4A6']
    for emoji in disgustPattren:
        match = re.search(emoji, dataSet)
        if match:
            dataSet = re.sub(emoji, " قرف ", dataSet)

    surprisePattren = [r'\U0001F635', r'\U0001F92F', r'\U0001F64A',
                      r'\U0001F62E', r'\U0001F62F', r'\U0001F632', r'\U0001F633',
                      r'\U0001F60F', r'\U0001F640', r'\U0001F4A3', r'\U0001F92D',
                      r'\U0001F636', r'\U0001F381', r'\U0001F92B']
    for emoji in surprisePattren:
        match = re.search(emoji, dataSet)
        if match:
            dataSet = re.sub(emoji, " مفاجئة ", dataSet)

    removedPattren = [r'\U0001F975', r'\U0001F976', r'\U0001F974',
                      r'\U0001F920', r'\U0001F978', r'\U0001F913', r'\U0001F9D0',
                      r'\U0001F615', r'\U0001F608', r'\U0001F921', r'\U0001F916'
                      r'\U0001F4A8', r'\U0001F573	', r'\U0001F4AC', r'\U0001F5E8'
                      r'\U0001F441\U0000FE0F\U0000200D\U0001F5E8\U0000FE0F',
                      r'\U0001F5EF', r'\U0001F4AD', r'\U0001F4A4', r'\U0001F91A',
                      r'\U0001F44B', r'\U0001F590', r'\U0000270B', r'\U0001F596',
                      r'\U0001F90F', r'\U0001F91E', r'\U0001F91F', r'\U0001F918',
                      r'\U0001F919', r'\U0001F448', r'\U0001F449', r'\U0001F446',
                      r'\U0001F447', r'\U0000261D', r'\U0001F44E', r'\U0000270A',
                      r'\U0001F64C', r'\U0001F932', r'\U0001F91D', r'\U0001F64F',
                      r'\U0000270D', r'\U0001F485', r'\U0001F933', r'\U0001F915',
                      r'\U0001F642', r'\U0001F643' , r'\U0001F44C', r'\U0001F33A',
                      r'\U0001F33B', r'\U0001F33C', r'\U0001F337', r'\U0001F331',
                      r'\U0001F342', r'\U0001F341', r'\U0001F343', r'\U0001F340',
                      r'\U00002618', r'\U0001F33F', r'\U0001F33E', r'\U0001F335',
                      r'\U0001F334', r'\U0001F333', r'\U0001F332', r'\U0001F338',
                      r'\U0001F4AE', r'\U0001F490', r'\U0001F3F5', r'\U0001F940',
                      r'\U0001F339', r'\U0001F41B', r'\U0001F98B', r'\U0001F438',
                      r'\U0001F40D', r'\U0001F475', r'\U0001F605', r'\U0001F45E',
                      r'\U0001F6AB', r'\U0001F40A', r'\U0001F3FC',  r'\U0001F609',
                      r'\U0001F430', r'\U0001F955', r'\U00002193', r'\U0001F634',
                      r'\U0001F4AA', r'\U0001F468', r'\U0001F64C', r'\U0001F3FB',
                      r'\U0001F393', r'\U0001F3C7', r'\U0001F607', r'\U0001F698',
                      r'\U0001F354', r'\U0001F355', r'\U0001F32E', r'\U0001F379',
                      r'\U0001F374', r'\U0001F31F', r'\U0001F308', r'\U000026C5',
                      r'\U000026C8', r'\U0001F324', r'\U0001F325', r'\U0001F326',
                      r'\U0001F327', r'\U0001F328', r'\U0001F329	', r'\U0001F32A',
                      r'\U0001F32B', r'\U0001F32C', r'\U0001F300', r'\U00002601',
                      r'\U0001F30C', r'\U0001F46A', r'\U0001F32A', r'\U0001F32B',
                      r'\U000026C8', r'\U0000263B', r'\U0001F62C', r'\U0001F3B6',
                      r'\U0001F3A4', r'\U0001F528', r'\U0001F31E', r'\U0001F51E',
                      r'\U0001F198', r'\U0001F3C3', r'\U00002615', r'\U0001F311',
                      r'\U0001F390', r'\U0001F36B', r'\U0001F914', r'\U0000274E',
                      r'\U0001F48F', r'\U00002B55', r'\U0000274C', r'\U000026B0',
                      r'\U0001F52B', r'\U0001F491', r'\U0001F5E3', r'\U0001F52C',
                      r'\U00002697', r'\U0001F3ED', r'\U0001F647', r'\U00002622',
                      r'\U0001F30D', r'\U0001F487', r'\U0001F4BC', r'\U0001F469',
                      r'\U0001F64D', r'\U00002708', r'\U0001F478', r'\U0001F52A',
                      r'\U0001F46B', r'\U0001F467', r'\U0001F30F', r'\U0001F30E',
                      r'\U0001F592', r'\U0001F386', r'\U0001F387', r'\U000020E3',
                      r'\U0001F46F\U0000200D\U00002642\U0000FE0F',r'\U0000262F',
                      r'\U0001F46F\U0000200D\U00002640\U0000FE0F',r'\U0000262E	',
                      r'\U0001F46D', r'\U0001F380', r'\U0001F3FD',
                      ]
    for emoji in removedPattren:
        match = re.search(emoji, dataSet)
        if match:
            dataSet = re.sub(emoji, ' ', dataSet)


    return dataSet

