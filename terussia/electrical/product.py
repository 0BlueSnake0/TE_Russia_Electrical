from .catalog import CATALOGS

PRODUCTS = { 
    "clamp-connections":{
        "product_title":"Клеммные соединения",
        "description": {
            "par0":{
                "subtitle":"",
                "text":"""
                """,
                "links":{},
            }, 
        },
        "text_image_blocks":{
            "block0":{
                "static_image":"/static/main/images/products/clamp-connections/clamps-0.png",
                "static_image_settings":{
                    "width":"50%",    
                    "height":"auto" 
                },
                "text":"""
                    TE Connectivity (TE), мировой лидер в области 
                    соединения проводников предлагает широкий спектр 
                    технологий для соединения проводников в промышленном 
                    производстве, на железнодорожном и морском транспорте, 
                    в солнечной энергетике, а также во взрывоопасных средах. 
                    Компания TE Connectivity Ltd. является мировым лидером 
                    в области технологий и производства с оборотом в 14,9 
                    миллиардов долларов. На протяжении более 75 лет наши 
                    решения для соединения, зарекомендовавшие себя в самых 
                    суровых условиях, позволили добиться прогресса в области 
                    транспорта, промышленного применения, медицинских технологий, 
                    энергетики, передачи данных и для дома. Сочетая знания и 
                    умения 85 000 сотрудников, в том числе более 7 000 инженеров, 
                    работающих вместе с заказчиками в почти 150 странах, TE 
                    гарантирует, что КАЖДОЕ СОЕДИНЕНИЕ ВЫПОЛНЕНО НАДЕЖНО. 
                    Узнайте больше о наших изделиях в каталогах продукции или 
                    посетив обучение.
                """,
            }    
        }, 
        "catalog_links":{
            "Клеммные соединения Entrellec":CATALOGS["clamp-connections"]["link"],
            "Клеммы с варисторами и защитными диодами":CATALOGS["clamps-with-varistors-and-protective-diods"]["link"],
        },
        "software_link":" https://www.te.com/usa-en/products/brands/entrelec/easy-rail-designer-3d.html?tab=pgp-story",
    }, 
    "distribution-blocks":{ 
        "product_title":"Распределительные блоки", 
        "description":{
            "par0":{
                "subtitle":"",
                "text":""" 
                    Распределительные блоки DBL от TE Entrelec позволяют соединять проводники поперечным сечением до 185 кв.мм. 
                    и имеют преимущество трех конфигураций в одном изделии: однополюсное распределение, многополюсное распределение 
                    (возможна стыковка блоков за счет штифтов и пазов на корпусе) и объединение (съёмная крышка позволяет перевернуть 
                    блок для объединения потенциала в солнечной энергетике без нарушения читаемости маркировки).
                """,
            },
            "par1":{
                "subtitle":"",
                "text":""" 
                    Блоки DBL позволяют экономить до 50% места на DIN-рейке по сравнению с обычными 
                    распределительными шинами за счет компактной модульной конструкции.
                    Номинальное напряжение 1000 В переменного тока или 1500 В постоянного тока.
                    Блоки позволяют соединять медные и алюминиевые проводники.
                """,
            },
            "par2":{
                "subtitle":"",
                "text":""" 
                    Номинальное напряжение 1000 В переменного тока или 1500 В постоянного тока. 
                    Модульная защищенная конструкция сокращает потребность в шинах, 
                    изоляторах, зажимах, креплениях, защитных экранах для распределения в электрическом щите.
                    Доступны версии для распределения потенциала не только с круглых проводников, 
                    но и плоских, включая шины.
                """,
            },
        },  
        "text_image_blocks":{
            "block0":{
                "static_image":"/static/main/images/products/distribution-blocks/distr-blocks-0.png",
                "static_image_settings":{
                    "width":"80%",    
                    "height":"auto" 
                },
                "text":"""
                """,
            },
        }, 
        "catalog_links":{
            "Распределительные блоки серии DBL":CATALOGS["distribution-blocks"]["link"]
        },
    },  

    "relays":{
        "product_title":"Реле",
        "description": {
            "par0":{
                "subtitle":"Panel Plug-in Relays",
                "text":"""
                Применение на динрейку через адаптер. Отличается высокой надежностью, длительным сроком службы 
                и широким спектром опций оценки контактов для поддержки различных нагрузок.
                """, 
                "modals":{
                    "Panel Plug-in Relays":{
                        "id":"modal-0",
                        "images":[
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-0.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-1.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-2.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-3.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-4.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-5.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-6.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-7.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-8.png",
                            "/static/main/images/modals/relays/panel-plugin/panel-plugin-9.png",
                        ],  
                    }, 
                },
            },
            "par1":{
                "subtitle":"Solid State Relays",
                "text":""" 
                Твердотельные реле с длительным сроком службы и низким 
                уровнем обслуживания при низком энергопотреблении, которые могут работать в жестких условиях.
                """, 
                "modals":{
                    "Solid State Relays":{
                        "id":"modal-3", 
                        "images":[
                            "/static/main/images/modals/relays/solid-state/solid-state-0.png", 
                            "/static/main/images/modals/relays/solid-state/solid-state-1.png", 
                            "/static/main/images/modals/relays/solid-state/solid-state-2.png", 
                        ],  
                    },
                },

            },
            "par2":{
                "subtitle":"Power PCB Relays",
                "text":"""
                В исполнении на печатную плату. Высокопроизводительные и 
                высоконадежные реле соответствуют мировым стандартам для печатных плат на рынке. 
                """, 
                "modals":{
                    "Power PCB Relays":{
                        "id":"modal-1",
                        "images":[
                            "/static/main/images/modals/relays/power-pcb/power-pcb-0.png", 
                            "/static/main/images/modals/relays/power-pcb/power-pcb-1.png", 
                        ],  
                    },
                },

            },
            "par3":{
                "subtitle":"Miniature PCB Relays",
                "text":""" 
                Миниатюрные реле на печатную плату. Предлагает небольшую  высоту 
                исполнения в сочетании с высокой мощностьюю. В исполении с  открытым или перекидным контактом.
                """, 
                "modals":{
                    "Miniature PCB Relays":{
                        "id":"modal-2",   
                    },
                },

            },
            "par4":{
                "subtitle":"Signal Relays",
                "text":""" 
                Высокопроизводительные и надежные реле, 
                которые производятся в малогабаритном дизайне. Подходят для коммутаций, для нагрузок до 5А.
                """,  
                "modals":{
                    "Signal Relays":{
                        "id":"modal-4", 
                        "images":[
                            "/static/main/images/modals/relays/signal/signal-0.png", 
                        ],  
                    },
                },

            },
            "par5":{
                "subtitle":"Inrush Power Relays",
                "text":""" 
                Предназначены для монтажа на печатной плате. 
                Работают с пусковыми токами до 800 А и в основном используются в освещении, 
                в комплекте с датчиками движения.
                """, 
                "modals":{
                    "Inrush Power Relays":{
                        "id":"modal-5", 
                        "images":[
                            "/static/main/images/modals/relays/inrush-power/inrush-power-0.png", 
                        ],  
                    },
                },

            },
            "par6":{
                "subtitle":"Force Guided Relays",
                "text":""" 
                Реле повешенной надежности. 
                Ключевые электрохимические переключающие компоненты, используемые в цепях безопасности, 
                востребованны в системах управления лифтами и эскалатороми, там где необходима повышенная надежность.
                """, 
                "modals":{
                    "Force Guided Relays":{
                        "id":"modal-6", 
                        "images":[
                            "/static/main/images/modals/relays/force-guided/force-guided-0.png", 
                            "/static/main/images/modals/relays/force-guided/force-guided-1.png", 
                        ],  
                    },
                },

            },  
        },
        "text_image_blocks":{
            "block0":{
                "static_image":"/static/main/images/products/relays/relays-0.png",
                "static_image_settings":{
                    "width":"70%",    
                    "height":"auto" 
                },
                "text":"""
                """,
            }    
        }, 
        "link_blocks":{
            "link-block0":{
                "subtitle":"Реле для применения в интелектуальных системах",
                "links":{
                    "Relays Solutions Fact Sheet":"http://www.te.com/content/dam/te-com/documents/channel/global/relay_factsheet.pdf",
                    "Virtual Building Tour (must use IE to view)":"http://www.te.com/usa-en/custom/3d-building/home.html",
                    "Relays in Intelligent Buildings Applications – Customer Presentation":"http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=1-1773899-3_Relays_in_Intelligent_Buildi&DocType=DS&DocLang=English&DocFilename=ENG_DS_1-1773899-3_Relays_in_Intelligent_Buildi_1016.pdf",
                    "Relays In Intelligent Buildings – TELC Course":"https://www.te.com/commerce/uso/te-learning-connection/sso2.do?unit=360"
                    },
                "static_image":"/static/main/images/products/relays/intellectual-systems.png",
                "static_image_settings":{
                    "width":"50%",    
                    "height":"auto" 
                },
            },
        },
        "catalog_links":{
            "Промышленные реле":CATALOGS["relays"]["link"]
        },
    },  

    "cable-lugs":{
        "product_title":"Кабельные наконечники",
        "description":{},  
    }, 

    "cable-ties":{
        "product_title":"Кабельные стяжки",
        "description":{},  
    }, 

    "perforated-cable-channels":{
        "product_title":"Кабель-каналы перфорированные",
        "description":{},  
    },  

    "cable-entries":{
        "product_title":"Кабельные вводы",
        "description":{},  
    },  

    "spiral-ribbon":{
        "product_title":"Спиральная лента",
        "description":{
            "par0":{
                "subtitle":"",
                "text":"""
                """,
            }, 
        },  
        "text_image_blocks":{
            "block0":{
                "static_image":"/static/main/images/products/spiral-ribbon/spiral-ribbon-0.png",
                "static_image_settings":{
                    "width":"40%",    
                    "height":"auto" 
                }, 
                "text":"""
                    Спиральная лента SPIRAP – это очень практичный способ создания и объединения жгутов кабелей, проводов,
                    трубок и шлангов. Это экономичный и быстро реализуемый способ защиты от истирания.
                    Пластиковая лента SPIRAP предварительно намотана в непрерывные большие отрезки; может использоваться
                    для широкого диапазона диаметров жгутов.
                    После монтажа лента SPIRAP сжимается за счет своих качеств и формирует плотную и равномерную
                    защитную оплетку проводов, кабелей, трубок или шлангов.
                    Лента изготовлена из различных материалов, чтобы отвечать широкому диапазону требований для различных
                    применений.  
                """,
            },
            "block1":{
                "static_image":"/static/main/images/products/spiral-ribbon/spiral-ribbon-1.png",
                "static_image_settings":{
                    "width":"80%",    
                    "height":"auto" 
                },
                "subtitle":"Ручной инструмент",
                "text":"""
                    Доступен небольшой ручной инструмент, чтобы сделать нанесение более легким и равномерным.
                    Ручной инструмент для монтажа SPIRAP код заказа 500901 – вкладывается в каждую коробку с изделием
                    SPIRAP , такой инструмент повышает скорость применения и делает процесс нанесения более равномерным
                    по все длине пучка. Инструмент имее прорези для возможности использования со всем диапазоном изделий
                    SPIRAP.
                    Такой инструмент также можно заказать отдельно.
                """,
            },
        },
        "catalog_links":{
            "Спиральная лента SPIRAP":CATALOGS["spiral-ribbon"]["link"]
        },
    },  

    "marking":{ 
        "product_title":"Маркировка", 
        "description":{},  
    },   
}