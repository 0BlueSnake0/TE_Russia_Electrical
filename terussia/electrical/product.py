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
        "description":{},  
        "text_image_blocks":{
            "block0":{
                "static_image":"/static/main/images/products/distribution-blocks/distr-blocks-0.png",
                "static_image_settings":{
                    "width":"80%",    
                    "height":"auto" 
                },
                "text":"""
                """,
            }    
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
                        "image":"/static/main/images/modals/relays/panel-plugin.png", 
                        "text":"""
                            Установка на DIN-рейку через адаптер. 
                            Отличается высокой надежностью, длительным сроком 
                            службы и широким спектром опций контактов для 
                            поддержки различных нагрузок.
                            Отличие от других реле (под пайку) заключается в 
                            специальных усиленных контактных выводах, так 
                            в впроцессе эксплуатации реле может быть 
                            неоднократно вставлено и удалено из клемной 
                            колодки.
                        """,
                        "title":"Panel Plug-in Relays",
                        "subtitle":"Реле для установки на цоколь",
                    },
                },
            },
            "par1":{
                "subtitle":"Power PCB Relays",
                "text":"""
                В исполнении на печатную плату. Высокопроизводительные и 
                высоконадежные реле соответствуют мировым стандартам для печатных плат на рынке. 
                """, 
                "modals":{
                    "Power PCB Relays":{
                        "id":"modal-1",
                        "image":"/static/main/images/modals/relays/power-pcb.png", 
                        "text":""" 
                            Реле в исполнении на печатную плату. 
                            Высокопроизводительные и высоконадежные реле 
                            соответствуют мировым стандартам для печатных 
                            плат на рынке.
                        """,
                        "title":"Power PCB Relays",
                        "subtitle":"Силовые реле на плату",
                    },
                },

            },
            "par2":{
                "subtitle":"Miniature PCB Relays",
                "text":""" 
                Миниатюрные реле на печатную плату. Предлагает небольшую  высоту 
                исполнения в сочетании с высокой мощностьюю. В исполении с  открытым или перекидным контактом.
                """, 
                "modals":{
                    "Miniature PCB Relays":{
                        "id":"modal-2",
                        "image":"/static/main/images/modals/relays/miniature-pcb.png", 
                        "text":""" 
                        """,
                        "title":"Miniature PCB Relays",
                        "subtitle":"Мини реле на плату",
                    },
                },

            },
            "par3":{
                "subtitle":"Solid State Relays",
                "text":""" 
                Твердотельные реле с длительным сроком службы и низким 
                уровнем обслуживания при низком энергопотреблении, которые могут работать в жестких условиях.
                """, 
                "modals":{
                    "Solid State Relays":{
                        "id":"modal-3",
                        "image":"/static/main/images/modals/relays/solid-state.png", 
                        "text":"""  
                            Твердотельные реле с длительным сроком службы и 
                            низким уровнем обслуживания при низком 
                            энергопотреблении, которые могут работать в 
                            жестких условиях.
                        """,
                        "title":"Solid State Relays",
                        "subtitle":"Твёрдотельные реле",
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
                        "image":"/static/main/images/modals/relays/signal.png", 
                        "text":""" 
                            Высокопроизводительные и надежные реле, которые 
                            производятся в малогабаритном дизайне. 
                            Подходят для коммутаций, для нагрузок до 5А.
                        """,
                        "title":"Signal Relays",
                        "subtitle":"Сигнальные реле",
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
                        "image":"/static/main/images/modals/relays/inrush-power.png", 
                        "text":""" 
                            Предназначены для монтажа на печатной плате. 
                            Работают с пусковыми токами до 800 А и в основном 
                            используются в освещении, датчиках движения,
                            настенных розетках и шинных системах.
                        """,
                        "title":"Inrush Power Relays",
                        "subtitle":"Пусковые реле",
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
                        "image":"/static/main/images/modals/relays/force-guided.png", 
                        "text":""" 
                            Реле с механически сблокированными контактами. 
                            Ключевые электромеханические переключающие компоненты, 
                            используемые в цепях безопасности, востребованы в 
                            системах управления лифтами, 
                            эскалаторами, конвеерами, там где необходима повышенная
                            надежность.
                        """,
                        "title":"Force Guided Relays",
                        "subtitle":"Высоконадежные реле с обратной связью",
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
            }
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