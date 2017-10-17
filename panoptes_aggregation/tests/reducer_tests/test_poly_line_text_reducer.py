import unittest
import urllib
import flask
import json
from panoptes_aggregation.reducers.poly_line_text_reducer import process_data, poly_line_text_reducer
from panoptes_aggregation.reducers.test_utils import extract_in_data

extracted_data = [
    {
        'frame0': {
            'points': {
                'x': [
                    [27.765213012695312, 307.7162780761719, 489.5647888183594, 628.343994140625, 984.8629150390625],
                    [111.51124572753906, 312.5017395019531, 436.9244689941406, 578.0963134765625],
                    [30.157958984375, 252.68313598632812, 468.0301208496094, 786.26513671875, 989.6483154296875],
                    [243.1121826171875, 384.2840881347656, 532.6341552734375, 733.624755859375],
                    [1149.962158203125, 1353.345458984375, 1551.9432373046875, 1788.8248291015625, 2152.52197265625],
                    [1118.8565673828125, 1271.9921875, 1599.798095703125],
                    [1245.6719970703125, 1425.1278076171875, 1604.5836181640625, 1760.1119384765625],
                    [1346.167236328125, 1429.9132080078125, 1595.0125732421875, 1796.0030517578125]
                ],
                'y': [
                    [419.1290588378906, 409.5580749511719, 404.7725524902344, 399.9870910644531, 397.5943298339844],
                    [533.980712890625, 366.4886779785156, 246.85147094726562, 131.99972534179688],
                    [313.8482971191406, 297.0990905761719, 292.3136291503906, 292.3136291503906, 285.1353454589844],
                    [541.158935546875, 428.7000427246094, 316.2410583496094, 122.42880249023438],
                    [297.0990905761719, 275.5644226074219, 265.9934387207031, 261.2079162597656, 273.1716613769531],
                    [376.0596618652344, 373.6669006347656, 373.6669006347656],
                    [498.0895690917969, 335.3829650878906, 172.67642211914062, 69.78839111328125],
                    [533.980712890625, 452.6274719238281, 325.8120422363281, 158.31991577148438]
                ]
            },
            'text': [
                ['words', 'on', 'a', 'page.'],
                ['There', 'is', 'this'],
                ['Here', 'are', 'some', 'test'],
                ['text', 'as', 'well'],
                ['There', 'are', 'two', 'columns'],
                ['of', 'text.'],
                ['This', 'looks', 'like'],
                ['a', 'big', 'mess']
            ],
            'slope': [
                -1.3125665780470608,
                -40.966719469829826,
                -1.4137500414163335,
                -40.33550980324749,
                -1.252950483811786,
                -0.23999309197815955,
                -40.103966913878772,
                -39.504439692518773
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [32.550689697265625, 264.6468811035156, 451.2809143066406, 783.872314453125, 984.8629150390625],
                    [30.157958984375, 305.3235168457031, 479.9938659667969, 640.3077392578125, 992.0411376953125],
                    [1243.2791748046875, 1410.7713623046875, 1599.798095703125, 1755.326416015625],
                    [1346.167236328125, 1434.69873046875, 1575.87060546875, 1798.3958740234375],
                    [1128.427490234375, 1362.9163818359375, 1544.7650146484375, 1796.0030517578125, 2142.950927734375],
                    [1114.071044921875, 1274.3848876953125, 1587.8343505859375],
                    [104.33302307128906, 310.1090087890625, 444.1026916503906, 563.7398681640625],
                    [245.50491333007812, 396.247802734375, 539.8125, 731.23193359375]
                ],
                'y': [
                    [285.1353454589844, 282.7426452636719, 282.7426452636719, 280.3498840332031, 268.3861389160156],
                    [402.3798522949219, 397.5943298339844, 395.2015686035156, 395.2015686035156, 395.2015686035156],
                    [481.3403625488281, 313.8482971191406, 143.96347045898438, 45.8609619140625],
                    [526.802490234375, 447.8419494628906, 323.4192810058594, 148.74893188476562],
                    [282.7426452636719, 273.1716613769531, 265.9934387207031, 258.8152160644531, 270.7789001464844],
                    [399.9870910644531, 378.4523620605469, 380.8451232910156],
                    [536.37353515625, 361.7031555175781, 246.85147094726562, 148.74893188476562],
                    [543.5517578125, 428.7000427246094, 297.0990905761719, 129.60702514648438]
                ]
            },
            'text': [
                ['Here', 'are', 'some', 'test'],
                ['words', 'on', 'a', 'page.'],
                ['This', 'looks', 'like'],
                ['a', 'big', 'mess'],
                ['There', 'are', 'two', 'columns'],
                ['of', 'text.'],
                ['There', 'is', 'this'],
                ['test', 'as', 'well']
            ],
            'slope': [
                -0.84300379948873472,
                -0.41169221645914822,
                -40.611219258654081,
                -39.867717105940628,
                -0.77370202671330712,
                -1.9350479072142399,
                -40.214619322353997,
                -40.655937635767046
            ]
        },
        'frame1': {
            'points': {'x': [[1, 180, 250]], 'y': [[1, 1, 1]]},
            'text': [['page', '2']],
            'slope': [0]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [274.21783447265625, 458.4591369628906],
                    [793.443359375, 968.1136474609375],
                    [1137.99853515625, 1365.3092041015625, 1549.5504150390625, 1803.181396484375],
                    [1365.3092041015625, 1446.6624755859375, 1597.4053955078125],
                    [1425.1278076171875, 1595.0125732421875, 1757.71923828125],
                    [305.3235168457031, 439.3171691894531, 573.3109130859375],
                    [42.121673583984375, 276.610595703125],
                    [1283.9559326171875, 1561.51416015625]
                ],
                'y': [
                    [292.3136291503906, 277.9571228027344],
                    [287.5281066894531, 273.1716613769531],
                    [285.1353454589844, 270.7789001464844, 270.7789001464844, 268.3861389160156],
                    [531.5880126953125, 457.4129333496094, 325.8120422363281],
                    [313.8482971191406, 158.31991577148438, 60.217437744140625],
                    [347.3467102050781, 251.63693237304688, 127.21426391601562],
                    [419.1290588378906, 404.7725524902344],
                    [392.8088684082031, 380.8451232910156]
                ]
            },
            'text': [
                ['are'],
                ['test'],
                ['There', 'are', 'two'],
                ['a', 'big'],
                ['looks', 'like'],
                ['is', 'this'],
                ['words'],
                ['text.']
            ],
            'slope': [
                -4.4556155742029677,
                -4.6986750689269563,
                -1.3197776039098639,
                -41.505307247628032,
                -37.369459226192326,
                -39.400653706482863,
                -3.503541802690775,
                -2.4681237681723815
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [1248.064697265625, 1422.7349853515625, 1609.3690185546875, 1762.504638671875],
                    [1346.167236328125, 1434.69873046875, 1595.0125732421875, 1800.78857421875],
                    [37.336181640625, 314.8945007324219, 491.9575500488281, 645.0931396484375, 977.6846923828125],
                    [39.72892761230469, 255.07589721679688, 475.2083435058594, 788.6578369140625, 1013.5758056640625],
                    [106.72576904296875, 324.4654846191406, 441.7099304199219, 597.23828125],
                    [1145.1767578125, 1286.3486328125, 1587.8343505859375],
                    [247.89767456054688, 408.2115173339844, 551.776123046875, 759.9449462890625],
                    [1137.99853515625, 1353.345458984375, 1544.7650146484375, 1829.50146484375, 2162.093017578125]
                ],
                'y': [
                    [483.7331237792969, 325.8120422363281, 153.53445434570312, 67.39566040039062],
                    [526.802490234375, 450.2347106933594, 316.2410583496094, 155.92721557617188],
                    [399.9870910644531, 402.3798522949219, 395.2015686035156, 390.4161071777344, 392.8088684082031],
                    [297.0990905761719, 287.5281066894531, 287.5281066894531, 289.9208679199219, 280.3498840332031],
                    [545.9444580078125, 359.3104553222656, 246.85147094726562, 127.21426391601562],
                    [390.4161071777344, 373.6669006347656, 373.6669006347656],
                    [548.337158203125, 419.1290588378906, 309.0628356933594, 127.21426391601562],
                    [287.5281066894531, 275.5644226074219, 273.1716613769531, 261.2079162597656, 268.3861389160156]
                ]
            },
            'text': [
                ['This', 'looks', 'like'],
                ['a', 'big', 'mess'],
                ['words', 'on', 'a', 'page.'],
                ['Here', 'are', 'some', 'test'],
                ['There', 'is', 'this'],
                ['of', 'text.'],
                ['text', 'as', 'well'],
                ['There', 'are', 'two', 'columns']
            ],
            'slope': [
                -39.504825159192279,
                -39.180903129348373,
                -0.61606969523056521,
                -0.69199657727551112,
                -40.728595229744641,
                -1.8257636189450075,
                -39.334667288762937,
                -1.122924085203026
            ]
        },
        'frame1': {
            'points': {'x': [[1.1, 180.1, 251]], 'y': [[0.9, 0.9, 0.9]]},
            'text': [['page', '2']],
            'slope': [0]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [1362.9163818359375, 1537.5867919921875],
                    [1817.537841796875, 2150.129150390625],
                    [501.5285339355469, 771.9085693359375],
                    [39.72892761230469, 288.5743103027344],
                    [446.4953918457031, 539.8125],
                    [1355.7381591796875, 1432.3060302734375],
                    [1405.98583984375, 1599.798095703125],
                    [312.5017395019531, 415.3897399902344],
                    [283.788818359375, 441.7099304199219],
                    [1604.5836181640625, 1805.5740966796875]
                ],
                'y': [
                    [268.3861389160156, 268.3861389160156],
                    [265.9934387207031, 270.7789001464844],
                    [294.7063293457031, 282.7426452636719],
                    [421.5217590332031, 411.9508361816406],
                    [392.8088684082031, 297.0990905761719],
                    [524.4097900390625, 450.2347106933594],
                    [311.4555358886719, 158.31991577148438],
                    [352.1322326660156, 282.7426452636719],
                    [280.3498840332031, 275.5644226074219],
                    [321.0265197753906, 158.31991577148438]
                ]
            },
            'text': [
                ['are'],
                ['columns'],
                ['some'],
                ['words'],
                ['as'],
                ['a'],
                ['looks'],
                ['is'],
                ['are'],
                ['mess']
            ],
            'slope': [
                0.0,
                0.82433851000468594,
                -2.5335516344556051,
                -2.2025858834389824,
                -45.725201352978438,
                -44.090601879970329,
                -38.313092593810111,
                -33.996461321522638,
                -1.7356948677716408,
                -38.990998547208093
            ]
        }
    }
]

processed_data = {
    'frame0': {
        'x': [
            [27.765213012695312, 307.7162780761719, 489.5647888183594, 628.343994140625, 984.8629150390625],
            [111.51124572753906, 312.5017395019531, 436.9244689941406, 578.0963134765625],
            [30.157958984375, 252.68313598632812, 468.0301208496094, 786.26513671875, 989.6483154296875],
            [243.1121826171875, 384.2840881347656, 532.6341552734375, 733.624755859375],
            [1149.962158203125, 1353.345458984375, 1551.9432373046875, 1788.8248291015625, 2152.52197265625],
            [1118.8565673828125, 1271.9921875, 1599.798095703125],
            [1245.6719970703125, 1425.1278076171875, 1604.5836181640625, 1760.1119384765625],
            [1346.167236328125, 1429.9132080078125, 1595.0125732421875, 1796.0030517578125],
            [32.550689697265625, 264.6468811035156, 451.2809143066406, 783.872314453125, 984.8629150390625],
            [30.157958984375, 305.3235168457031, 479.9938659667969, 640.3077392578125, 992.0411376953125],
            [1243.2791748046875, 1410.7713623046875, 1599.798095703125, 1755.326416015625],
            [1346.167236328125, 1434.69873046875, 1575.87060546875, 1798.3958740234375],
            [1128.427490234375, 1362.9163818359375, 1544.7650146484375, 1796.0030517578125, 2142.950927734375],
            [1114.071044921875, 1274.3848876953125, 1587.8343505859375],
            [104.33302307128906, 310.1090087890625, 444.1026916503906, 563.7398681640625],
            [245.50491333007812, 396.247802734375, 539.8125, 731.23193359375],
            [274.21783447265625, 458.4591369628906],
            [793.443359375, 968.1136474609375],
            [1137.99853515625, 1365.3092041015625, 1549.5504150390625, 1803.181396484375],
            [1365.3092041015625, 1446.6624755859375, 1597.4053955078125],
            [1425.1278076171875, 1595.0125732421875, 1757.71923828125],
            [305.3235168457031, 439.3171691894531, 573.3109130859375],
            [42.121673583984375, 276.610595703125],
            [1283.9559326171875, 1561.51416015625],
            [1248.064697265625, 1422.7349853515625, 1609.3690185546875, 1762.504638671875],
            [1346.167236328125, 1434.69873046875, 1595.0125732421875, 1800.78857421875],
            [37.336181640625, 314.8945007324219, 491.9575500488281, 645.0931396484375, 977.6846923828125],
            [39.72892761230469, 255.07589721679688, 475.2083435058594, 788.6578369140625, 1013.5758056640625],
            [106.72576904296875, 324.4654846191406, 441.7099304199219, 597.23828125],
            [1145.1767578125, 1286.3486328125, 1587.8343505859375],
            [247.89767456054688, 408.2115173339844, 551.776123046875, 759.9449462890625],
            [1137.99853515625, 1353.345458984375, 1544.7650146484375, 1829.50146484375, 2162.093017578125],
            [1362.9163818359375, 1537.5867919921875],
            [1817.537841796875, 2150.129150390625],
            [501.5285339355469, 771.9085693359375],
            [39.72892761230469, 288.5743103027344],
            [446.4953918457031, 539.8125],
            [1355.7381591796875, 1432.3060302734375],
            [1405.98583984375, 1599.798095703125],
            [312.5017395019531, 415.3897399902344],
            [283.788818359375, 441.7099304199219],
            [1604.5836181640625, 1805.5740966796875]
        ],
        'y': [
            [419.1290588378906, 409.5580749511719, 404.7725524902344, 399.9870910644531, 397.5943298339844],
            [533.980712890625, 366.4886779785156, 246.85147094726562, 131.99972534179688],
            [313.8482971191406, 297.0990905761719, 292.3136291503906, 292.3136291503906, 285.1353454589844],
            [541.158935546875, 428.7000427246094, 316.2410583496094, 122.42880249023438],
            [297.0990905761719, 275.5644226074219, 265.9934387207031, 261.2079162597656, 273.1716613769531],
            [376.0596618652344, 373.6669006347656, 373.6669006347656],
            [498.0895690917969, 335.3829650878906, 172.67642211914062, 69.78839111328125],
            [533.980712890625, 452.6274719238281, 325.8120422363281, 158.31991577148438],
            [285.1353454589844, 282.7426452636719, 282.7426452636719, 280.3498840332031, 268.3861389160156],
            [402.3798522949219, 397.5943298339844, 395.2015686035156, 395.2015686035156, 395.2015686035156],
            [481.3403625488281, 313.8482971191406, 143.96347045898438, 45.8609619140625],
            [526.802490234375, 447.8419494628906, 323.4192810058594, 148.74893188476562],
            [282.7426452636719, 273.1716613769531, 265.9934387207031, 258.8152160644531, 270.7789001464844],
            [399.9870910644531, 378.4523620605469, 380.8451232910156],
            [536.37353515625, 361.7031555175781, 246.85147094726562, 148.74893188476562],
            [543.5517578125, 428.7000427246094, 297.0990905761719, 129.60702514648438],
            [292.3136291503906, 277.9571228027344],
            [287.5281066894531, 273.1716613769531],
            [285.1353454589844, 270.7789001464844, 270.7789001464844, 268.3861389160156],
            [531.5880126953125, 457.4129333496094, 325.8120422363281],
            [313.8482971191406, 158.31991577148438, 60.217437744140625],
            [347.3467102050781, 251.63693237304688, 127.21426391601562],
            [419.1290588378906, 404.7725524902344],
            [392.8088684082031, 380.8451232910156],
            [483.7331237792969, 325.8120422363281, 153.53445434570312, 67.39566040039062],
            [526.802490234375, 450.2347106933594, 316.2410583496094, 155.92721557617188],
            [399.9870910644531, 402.3798522949219, 395.2015686035156, 390.4161071777344, 392.8088684082031],
            [297.0990905761719, 287.5281066894531, 287.5281066894531, 289.9208679199219, 280.3498840332031],
            [545.9444580078125, 359.3104553222656, 246.85147094726562, 127.21426391601562],
            [390.4161071777344, 373.6669006347656, 373.6669006347656],
            [548.337158203125, 419.1290588378906, 309.0628356933594, 127.21426391601562],
            [287.5281066894531, 275.5644226074219, 273.1716613769531, 261.2079162597656, 268.3861389160156],
            [268.3861389160156, 268.3861389160156],
            [265.9934387207031, 270.7789001464844],
            [294.7063293457031, 282.7426452636719],
            [421.5217590332031, 411.9508361816406],
            [392.8088684082031, 297.0990905761719],
            [524.4097900390625, 450.2347106933594],
            [311.4555358886719, 158.31991577148438],
            [352.1322326660156, 282.7426452636719],
            [280.3498840332031, 275.5644226074219],
            [321.0265197753906, 158.31991577148438]
        ],
        'text': [
            ['words', 'on', 'a', 'page.'],
            ['There', 'is', 'this'],
            ['Here', 'are', 'some', 'test'],
            ['text', 'as', 'well'],
            ['There', 'are', 'two', 'columns'],
            ['of', 'text.'],
            ['This', 'looks', 'like'],
            ['a', 'big', 'mess'],
            ['Here', 'are', 'some', 'test'],
            ['words', 'on', 'a', 'page.'],
            ['This', 'looks', 'like'],
            ['a', 'big', 'mess'],
            ['There', 'are', 'two', 'columns'],
            ['of', 'text.'],
            ['There', 'is', 'this'],
            ['test', 'as', 'well'],
            ['are'],
            ['test'],
            ['There', 'are', 'two'],
            ['a', 'big'],
            ['looks', 'like'],
            ['is', 'this'],
            ['words'],
            ['text.'],
            ['This', 'looks', 'like'],
            ['a', 'big', 'mess'],
            ['words', 'on', 'a', 'page.'],
            ['Here', 'are', 'some', 'test'],
            ['There', 'is', 'this'],
            ['of', 'text.'],
            ['text', 'as', 'well'],
            ['There', 'are', 'two', 'columns'],
            ['are'],
            ['columns'],
            ['some'],
            ['words'],
            ['as'],
            ['a'],
            ['looks'],
            ['is'],
            ['are'],
            ['mess']
        ],
        'slope': [
            -1.3125665780470608,
            -40.966719469829826,
            -1.4137500414163335,
            -40.33550980324749,
            -1.252950483811786,
            -0.23999309197815955,
            -40.103966913878772,
            -39.504439692518773,
            -0.84300379948873472,
            -0.41169221645914822,
            -40.611219258654081,
            -39.867717105940628,
            -0.77370202671330712,
            -1.9350479072142399,
            -40.214619322353997,
            -40.655937635767046,
            -4.4556155742029677,
            -4.6986750689269563,
            -1.3197776039098639,
            -41.505307247628032,
            -37.369459226192326,
            -39.400653706482863,
            -3.503541802690775,
            -2.4681237681723815,
            -39.504825159192279,
            -39.180903129348373,
            -0.61606969523056521,
            -0.69199657727551112,
            -40.728595229744641,
            -1.8257636189450075,
            -39.334667288762937,
            -1.122924085203026,
            0.0,
            0.82433851000468594,
            -2.5335516344556051,
            -2.2025858834389824,
            -45.725201352978438,
            -44.090601879970329,
            -38.313092593810111,
            -33.996461321522638,
            -1.7356948677716408,
            -38.990998547208093
        ]
    },
    'frame1': {
        'x': [
            [1, 180, 250],
            [1.1, 180.1, 251]
        ],
        'y': [
            [1, 1, 1],
            [0.9, 0.9, 0.9]
        ],
        'text': [
            ['page', '2'],
            ['page', '2']
        ],
        'slope': [
            0,
            0
        ]
    }
}

reduced_data = {
    'frame0': [
        {
            'clusters_x': [
                34.145858764648438,
                266.0825134277344,
                466.03616333007812,
                784.82944335937498,
                989.0501708984375
            ],
            'clusters_y': [
                298.69424438476562,
                288.00667114257811,
                285.1353759765625,
                286.57102661132814,
                276.76075744628906
            ],
            'clusters_text': [
                ['Here', 'Here', '', '', 'Here', '', ''],
                ['are', 'are', 'are', '', 'are', '', 'are'],
                ['some', 'some', '', '', 'some', 'some', ''],
                ['test', 'test', '', 'test', 'test', '', ''],
                ['', '', '', '', '', '', '']
            ],
            'number_views': 7,
            'consensus_score': 4.0,
            'gutter_label': 0,
            'line_slope': -1.5696676279703352,
            'slope_label': 0
        },
        {
            'clusters_x': [
                35.421990966796876,
                298.62384033203125,
                487.17206827799481,
                637.91495768229163,
                984.8629150390625
            ],
            'clusters_y': [
                412.42936401367189,
                405.25112915039062,
                398.39189656575519,
                395.20158894856769,
                395.20158894856769
            ],
            'clusters_text': [
                ['words', 'words', 'words', 'words', 'words'],
                ['on', 'on', '', 'on', ''],
                ['a', 'a', '', 'a', ''],
                ['page.', 'page.', '', 'page.', ''],
                ['', '', '', '', '']
            ],
            'number_views': 5,
            'consensus_score': 3.5,
            'gutter_label': 0,
            'line_slope': -1.5696676279703352,
            'slope_label': 0
        },
        {
            'clusters_x': [
                1138.5966796875,
                1359.5665771484375,
                1545.7220947265625,
                1807.009716796875,
                2151.9237670898438
            ],
            'clusters_y': [
                288.12629699707031,
                272.6931091308594,
                268.86471557617188,
                263.12212524414065,
                270.77890014648438
            ],
            'clusters_text': [
                ['There', 'There', 'There', 'There', '', ''],
                ['are', 'are', 'are', 'are', 'are', ''],
                ['two', 'two', 'two', 'two', '', ''],
                ['columns', 'columns', '', 'columns', '', 'columns'],
                ['', '', '', '', '', '']
            ],
            'number_views': 6,
            'consensus_score': 4.25,
            'gutter_label': 1,
            'line_slope': -1.5696676279703352,
            'slope_label': 0
        },
        {
            'clusters_x': [
                1126.0347900390625,
                1279.17041015625,
                1584.2452392578125
            ],
            'clusters_y': [
                388.82095336914062,
                379.64875793457031,
                377.25601196289062
            ],
            'clusters_text': [
                ['of', 'of', '', 'of'],
                ['text.', 'text.', 'text.', 'text.'],
                ['', '', '', '']
            ],
            'number_views': 4,
            'consensus_score': 3.5,
            'gutter_label': 1,
            'line_slope': -1.5696676279703352,
            'slope_label': 0
        },
        {
            'clusters_x': [
                107.52334594726562,
                312.9802978515625,
                435.4888000488281,
                578.0963439941406
            ],
            'clusters_y': [
                538.7662353515625,
                357.3962463378906,
                254.98679809570314,
                133.79429626464844
            ],
            'clusters_text': [
                ['There', 'There', '', 'There', ''],
                ['is', 'is', 'is', 'is', 'is'],
                ['this', 'this', 'this', 'this', ''],
                ['', '', '', '', '']
            ],
            'number_views': 5,
            'consensus_score': 4.0,
            'gutter_label': 0,
            'line_slope': -40.020044794251575,
            'slope_label': 1
        },
        {
            'clusters_x': [
                245.50492350260416,
                408.80970001220703,
                541.0088195800781,
                741.6005452473959
            ],
            'clusters_y': [
                544.3492838541666,
                417.3345031738281,
                304.8755187988281,
                126.4166971842448
            ],
            'clusters_text': [
                ['text', 'test', 'text', ''],
                ['as', 'as', 'as', 'as'],
                ['well', 'well', 'well', ''],
                ['', '', '', '']
            ],
            'number_views': 4,
            'consensus_score': 3.0,
            'gutter_label': 0,
            'line_slope': -40.020044794251575,
            'slope_label': 1
        },
        {
            'clusters_x': [
                1245.6719563802083,
                1417.9495605468751,
                1601.7122802734375,
                1758.9155578613281
            ],
            'clusters_y': [
                487.72101847330731,
                320.06942749023438,
                157.36283569335939,
                60.81561279296875
            ],
            'clusters_text': [
                ['This', 'This', '', 'This', ''],
                ['looks', 'looks', 'looks', 'looks', 'looks'],
                ['like', 'like', 'like', 'like', ''],
                ['', '', '', '', '']
            ],
            'number_views': 5,
            'consensus_score': 4.0,
            'gutter_label': 1,
            'line_slope': -40.020044794251575,
            'slope_label': 1
        },
        {
            'clusters_x': [
                1351.9098144531249,
                1435.6558349609375,
                1593.576953125,
                1800.1903991699219
            ],
            'clusters_y': [
                528.71669921875002,
                451.67035522460935,
                322.46218872070312,
                155.32899475097656
            ],
            'clusters_text': [
                ['a', 'a', 'a', 'a', 'a', ''],
                ['big', 'big', 'big', 'big', '', ''],
                ['mess', 'mess', '', 'mess', '', 'mess'],
                ['', '', '', '', '', '']
            ],
            'number_views': 6,
            'consensus_score': 4.333333333333333,
            'gutter_label': 1,
            'line_slope': -40.020044794251575,
            'slope_label': 1
        }
    ],
    'frame1': [
        {
            'clusters_x': [
                1.05,
                180.05000000000001,
                250.5
            ],
            'clusters_y': [
                0.94999999999999996,
                0.94999999999999996,
                0.94999999999999996
            ],
            'clusters_text': [
                ['page', 'page'],
                ['2', '2'],
                ['', '']
            ],
            'number_views': 2,
            'consensus_score': 2.0,
            'gutter_label': 0,
            'line_slope': 0.0,
            'slope_label': 0
        }
    ]
}


class TestClusterLines(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.kwargs = {
            'eps_slope': 25,
            'eps_line': 40,
            'eps_word': 50,
            'min_samples': 1
        }

    def test_process_data(self):
        result = process_data(extracted_data)
        self.assertDictEqual(dict(result), processed_data)

    def test_cluster_lines(self):
        result = poly_line_text_reducer._original(processed_data, metric='euclidean', dot_freq='word', gutter_tol=0, min_word_count=1, **self.kwargs)
        self.assertDictEqual(dict(result), reduced_data)

    def test_poly_line_text_reducer(self):
        result = poly_line_text_reducer(extracted_data, **self.kwargs)
        self.assertDictEqual(dict(result), reduced_data)

    def test_poly_line_text_reducer_request(self):
        app = flask.Flask(__name__)
        request_kwargs = {
            'data': json.dumps(extract_in_data(extracted_data)),
            'content_type': 'application/json'
        }
        url_params = '?{0}'.format(urllib.parse.urlencode(self.kwargs))
        with app.test_request_context(url_params, **request_kwargs):
            result = poly_line_text_reducer(flask.request)
            self.assertDictEqual(dict(result), reduced_data)


if __name__ == '__main__':
    unittest.main()
