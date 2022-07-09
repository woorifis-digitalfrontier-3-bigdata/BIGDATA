var express = require('express');
var router = express.Router();
const request = require('request');
const querystring = require('querystring');
const {logger} = require('../config/winston');
const dotenv = require('dotenv');
dotenv.config(); // LOAD CONFIG

router.use(function(req, res, next) {
  next();
});

router.get("/", function(req, res){
  const a = 'example'
  res.render( 'home.html', { title: 'Express' });
});

router.get("/2", function(req, res){
  console.log(req.query)
  const val=req.query.q
  console.log(val.title)
  res.render( 'home2.html', { val });
});

router.get('/about', function(req, res) {
  res.send('hi2');
});

let kakaoOptions = {
    url: 'https://dapi.kakao.com/v3/search/book?target=title', 
    method: 'GET',
    headers: {
      'Authorization': `KakaoAK ${process.env.RESTAPI_KEY}`
    },
    qs: {
      query : '테스트'     
    },
    encoding: 'UTF-8',
  }

router.get('/news', (req, res)=> { //람다식
  console.log(req.query)
  kakaoOptions.qs.query=req.query.q
  console.log(kakaoOptions)
   request.get(kakaoOptions, (error, response, body)=> {
     if (!error && response.statusCode == 200) {
       let newsItems = JSON.parse(body).items; 
        logger.info(`example kakao`);
        logger.debug(`example kakao ${req.query.q} ${response.statusCode}`);
        res.writeHead(200, {'Content-Type': 'text/json;charset=utf-8'});
        res.end(body);
    
     } else {
       res.status(response.statusCode).end(); //출력하는 부분
       console.log('error = ' + response.statusCode);
     }
   });
 });

module.exports = router;