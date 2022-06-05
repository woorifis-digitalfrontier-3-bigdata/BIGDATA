var express = require('express');
var router = express.Router();
const request = require('request');
const {logger} = require('../config/winston');
const dotenv = require('dotenv');
dotenv.config(); // LOAD CONFIG

router.use(function(req, res, next) {
  next();
});

router.get('/', function(req, res) {
  res.send('hi1');
});

router.get('/about', function(req, res) {
  res.send('hi2');
});

let kakaoOptions = {
    url: 'https://dapi.kakao.com/v3/search/book?target=title',  // target에 해당하는 것을 적기
    method: 'GET',
    headers: {
      'Authorization': `KakaoAK ${process.env.RESTAPI_KEY}`
    },
    qs: {
      query : '미움받을용기'     // 현재 책으로 검색할 것이라 책 제목을 적었다.
    },
    encoding: 'UTF-8',
  }

router.get('/news', (req, res)=> { //람다식

   request.get(kakaoOptions, (error, response, body)=> { //function이 =>로 해결되네
     if (!error && response.statusCode == 200) {
       let newsItems = JSON.parse(body).items; //items - title, link, description, pubDate
        logger.info(`example kakao`);
        logger.debug(`example kakao`);
        res.writeHead(200, {'Content-Type': 'text/json;charset=utf-8'});
        res.end(body);
    
     } else {
       res.status(response.statusCode).end(); //출력하는 부분
       console.log('error = ' + response.statusCode);
     }
   });
 });

module.exports = router;