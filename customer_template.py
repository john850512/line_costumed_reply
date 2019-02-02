from linebot.models import *

def create_customer_template():
    bubble = BubbleContainer(
        direction='ltr',
        body=BoxComponent(
            layout='vertical',
            contents=[
                # title
                TextComponent(text='信用卡優惠查詢', weight='bold', size='xl'),
                # info
                BoxComponent(
                    layout='vertical',
                    margin='lg',
                    spacing='sm',
                    contents=[
                        BoxComponent(
                            layout='baseline',
                            spacing='sm',
                            contents=[
                                TextComponent(
                                    text='類別',
                                    color='#aaaaaa',
                                    size='sm',
                                    flex=1
                                ),
                                TextComponent(
                                    text='休閒娛樂',
                                    wrap=True,
                                    color='#666666',
                                    size='sm',
                                    flex=5
                                )
                            ],
                        ),
                    ],
                )
            ],
        ),
        footer=BoxComponent(
            layout='vertical',
            spacing='sm',
            contents=[
                # first row
                BoxComponent(
                    layout='horizontal',
                    spacing='sm',
                    contents=[
                        # callAction, separator, websiteAction
                        SpacerComponent(size='sm'),
                        # callAction
                        ImageComponent(
                            url='https://i.imgur.com/ZvAirq6.png',
                            size='full',
                            aspect_ratio='20:13',
                            aspect_mode='cover',
                            action=MessageAction(label='LOVE 晶緻悠遊寵愛紅卡', text='LOVE 晶緻悠遊寵愛紅卡')
                        ),
                        # separator
                        SeparatorComponent(),
                        # websiteAction
                        ImageComponent(
                            url='https://i.imgur.com/rR6lQka.jpg',
                            size='full',
                            aspect_ratio='20:13',
                            aspect_mode='cover',
                            action=MessageAction(label='HappyCash & HAPPY GO 聯名卡(愛戀紅)', text='HappyCash & HAPPY GO 聯名卡(愛戀紅)')
                        )
                    ]
                ),
                # second row
                BoxComponent(
                    layout='horizontal',
                    spacing='sm',
                    contents=[
                        # callAction, separator, websiteAction
                        SpacerComponent(size='sm'),
                        # callAction
                        ImageComponent(
                            url='https://i.imgur.com/GSXzOsv.png',
                            size='full',
                            aspect_ratio='20:13',
                            aspect_mode='cover',
                            action=MessageAction(label='華南夢時代聯名卡', text='華南夢時代聯名卡')
                        ),
                        # separator
                        SeparatorComponent(),
                        # websiteAction
                        ImageComponent(
                            url='https://i.imgur.com/K4cAACy.jpg',
                            size='full',
                            aspect_ratio='20:13',
                            aspect_mode='cover',
                            action=MessageAction(label='HappyCash & HAPPY GO 聯名卡(爵愛黑)', text='HappyCash & HAPPY GO 聯名卡(爵愛黑)')
                        )
                    ]
                ),
                # third row
                BoxComponent(
                    layout='horizontal',
                    spacing='sm',
                    contents=[
                        # callAction, separator, websiteAction
                        SpacerComponent(size='sm'),
                        # callAction
                        ImageComponent(
                            url='https://i.imgur.com/6Vd175b.jpg',
                            size='full',
                            aspect_ratio='20:13',
                            aspect_mode='cover',
                            action=MessageAction(label='HappyCash & HAPPY GO 聯名卡(超級現金回饋)', text='HappyCash & HAPPY GO 聯名卡(超級現金回饋)')
                        ),
                        # separator
                        SeparatorComponent(),
                        # websiteAction
                        ImageComponent(
                            url='https://i.imgur.com/oTyud1r.png',
                            size='full',
                            aspect_ratio='20:13',
                            aspect_mode='cover',
                            action=MessageAction(label='現金回饋', text='現金回饋')
                        )
                    ]
                ),
            ]
        ),
    )
    flex_template = FlexSendMessage(alt_text="hello", contents=bubble)
    return flex_template