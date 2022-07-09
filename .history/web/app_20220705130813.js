var express = require('express');
var app = express();
var cors = require('cors');
const compression = require('compression');
const nunjucks = require('nunjucks');

//var router_naver = require('./router/naver');
var router_kakao = require('./router/kakao');

app.use(cors());
app.use(compression());
app.use(express.json());

app.set('view engine', 'njk'); // 확장자를 html 로도 사용이 가능함.
nunjucks.configure('template', { // views폴더가 넌적스파일의 위치가 됨
  express: app,
  watch: true,
});

//app.use('/search_naver',router_naver);
app.use('/search_kakao',router_kakao);

app.listen(3000, () => {
  console.log('listen t0 3000')
})