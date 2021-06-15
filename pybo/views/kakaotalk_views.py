from datetime import datetime

from flask import Blueprint, render_template, request, url_for, jsonify
from werkzeug.utils import redirect

from pybo.weatherapi import get_wdata
from pybo.Naver_API import navermovie
from pybo.movie_recommend import get_movie
bp=Blueprint('kakaotalk', __name__,url_prefix='/kakaotalk')

@bp.route('/weather/', methods=['GET','POST'])
def kakaoweather():
    req=request.get_json()
    print(req)
    #날씨 지역 블럭이 들어오면 지역정보만 프린트
    if req['intent']['name']=='날씨 지역 블록':
        print(req['action']['params']['지역명'])
        result=get_wdata(req['action']['params']['지역명'])
        print(result['현재 일기'])
        imgurl = "https://pbs.twimg.com/profile_images/970346143421906944/mowSlHqs_400x400.jpg"

        if result['현재 일기']=="맑음" or "":
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {

                            "simpleText": {"text": result['현재 일기']}
                        },
                        {
                            "simpleImage": {
                                "imageUrl":imgurl,
                                "altText": "맑음 이미지"
                            }
                        }
                    ]
                }
            }

        elif result['현재 일기']=='구름 많음' or '흐림':
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {"text": result['현재 일기']}
                        },
                        {
                            "simpleImage": {
                                "imageUrl": "https://thumb.ac-illust.com/4f/4f53657bae829388ac54be7f6b6af886_t.jpeg",
                                "altText": "구름많음 이미지"
                                }
                            }
                        ]
                    }
                }
        elif result['현재 일기']=='비' or '약한 비 단속적' or '비 끝' :
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {"text": result['현재 일기']}
                        },
                        {
                            "simpleImage": {
                                "imageUrl":"https://i.pinimg.com/474x/10/e8/94/10e894ca4d03d3afaf98ece49f429673.jpg",
                                "altText": "비 이미지"
                                }
                            }
                        ]
                    }
                }
        elif result['현재 일기']=='연무' or '박무' or '안개 짙어짐' or '안개 옅어짐':
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {"text": result['현재 일기']}
                        },
                        {
                            "simpleImage": {
                                "imageUrl": "https://image.flaticon.com/icons/png/512/2531/2531622.png",
                                "altText": "안개 이미지"
                            }
                        }
                    ]
                }
            }
        else:
            res={
                "version":"2.0",
                "template": {
                    "outputs":[
                        {
                            "simpleText":{"text":result['현재 일기']}
                        },
                        {
                            "simpleImage": {
                                "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz-pkwWFCmE485Lc7tD36zfKRknnOwowB7iH_T_kGAzBlR7rkqP3LHA8m9x1DctbruAv4&usqp=CAU",
                                "altText":"흐린 뒤 맑음이미지"
                            }
                        },
                        {
                            "basicCard": {
                                "title": "보물상자",
                                "description": "보물상자 안에는 뭐가 있을까",
                                "thumbnail": {
                                    "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                                },
                                "profile": {
                                    "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                                    "nickname": "보물상자"
                                },
                                "social": {
                                    "like": 1238,
                                    "comment": 8,
                                    "share": 780
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "열어보기",
                                        "messageText": "짜잔! 우리가 찾던 보물입니다"
                                    },
                                    {
                                        "action": "webLink",
                                        "label": "구경하기",
                                        "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                                    }
                                ]
                            }
                        },
                        {
                            "basicCard": {
                                "title": "영화순위",
                                "description": "지금 영화 1위는 어떤 영화일까요?",
                                "thumbnail": {
                                    "imageUrl": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=187322#"
                                },
                                "profile": {
                                    "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                                    "nickname": "보물상자"
                                },
                                "social": {
                                    "like": 1238,
                                    "comment": 8,
                                    "share": 780
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "1위영화",
                                        "messageText": "1위영화입니다"
                                    },
                                    {
                                        "action": "webLink",
                                        "label": "예매하기",
                                        "webLinkUrl": "https://ticket.movie.naver.com/Ticket/Reserve.aspx"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
    return jsonify(res)

@bp.route('/treasure/', methods=['GET','POST'])
def treasure():
    req = request.get_json()
    if req['intent']['name']=='보물상자':
        req=request.get_json()
        print(req)
        res= {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "listCard": {
                  "header": {
                    "title": "카카오 i 디벨로퍼스를 소개합니다"
                  },
                  "items": [
                    {
                      "title": "Kakao i Developers",
                      "description": "새로운 AI의 내일과 일상의 변화",
                      "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                      "link": {
                        "web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                      }
                    },
                    {
                      "title": "Kakao i Open Builder",
                      "description": "카카오톡 채널 챗봇 만들기",
                      "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
                      "link": {
                        "web": "https://namu.wiki/w/%EB%AC%B4%EC%A7%80(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                      }
                    },
                    {
                      "title": "Kakao i Voice Service",
                      "description": "보이스봇 / KVS 제휴 신청하기",
                      "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
                      "link": {
                        "web": "https://namu.wiki/w/%EC%96%B4%ED%94%BC%EC%B9%98"
                      }
                    }
                  ],
                  "buttons": [
                    {
                      "label": "구경가기",
                      "action": "webLink",
                      "webLinkUrl": "https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88"
                    }
                  ]
                }
              }
            ]
          }
        }
    return jsonify(res)


@bp.route('/movie/', methods=['GET','POST'])
def kakaomovie():
    req=request.get_json()
    #print('첫번째 req', req)
    # if req['intent']['name']=='영화 정보 블록': #아래랑 겹쳐서 빼버림..
    #     #print(req)
    #     #print(req['action']['params']['sys_movie_name'])
    #     result=navermovie(req['action']['params']['sys_movie_name'])
    #     #print(result)
    #     res = {
    #         "version": "2.0",
    #         "template": {
    #             "outputs": [
    #                 {
    #                     "basicCard": {
    #                         "title": "영화정보",
    #                         "description": ["result[items][title]", "result[items][director]","result[items][actor]", "result[items][userRating]"],
    #                         "thumbnail": {
    #                             "imageUrl": "result[items][image]"
    #                         },
    #                         "social": {
    #                             "like": 1238,
    #                             "comment": 8,
    #                             "share": 780
    #                         },
    #                         "buttons": [
    #                             {
    #                                 "action": "webLink",
    #                                 "label": "예매하기",
    #                                 "webLinkUrl": "https://ticket.movie.naver.com/Ticket/Reserve.aspx"
    #                             }
    #                         ]
    #                     }
    #                 }
    #             ]
    #         }
    #     }

    if req['intent']['name'] == '영화 추천 블록':
        result = get_movie()

        moviedata1 = navermovie(result[0][0])
        moviedata2 = navermovie(result[1][0])
        moviedata3 = navermovie(result[2][0])

        print(moviedata1['items'][0]['title'])
        print(moviedata1['items'][0]['subtitle'])
        print(moviedata1['items'][0]['image'])
        print(moviedata1['items'][0]['link'])

        print(result[0][0])

        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "listCard": {
                            "header": {
                                "title": "추천영화"
                            },
                            "items": [
                                {
                                    "title": moviedata1['items'][0]['title'],
                                    "description": moviedata1['items'][0]['subtitle'],
                                    "imageUrl": moviedata1['items'][0]['image'],
                                    "link": {
                                        "web": moviedata1['items'][0]['link']
                                    }
                                },
                                {
                                    "title": moviedata2['items'][0]['title'],
                                    "description": moviedata2['items'][0]['subtitle'],
                                    "imageUrl": moviedata2['items'][0]['image'],
                                    "link": {
                                        "web": moviedata2['items'][0]['link']
                                    }
                                },
                                {
                                    "title": moviedata3['items'][0]['title'],
                                    "description": moviedata3['items'][0]['subtitle'],
                                    "imageUrl": moviedata3['items'][0]['image'],
                                    "link": {
                                        "web": moviedata3['items'][0]['link']
                                    }
                                }
                            ],
                            "buttons": [
                                {
                                    "label": "구경가기",
                                    "action": "webLink",
                                    "webLinkUrl": "https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88"
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(res)