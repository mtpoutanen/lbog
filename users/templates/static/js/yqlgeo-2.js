/*
  YQL Geo library by Christian Heilmann
  Homepage: http://isithackday.com/geo/yql-geo-library
  Copyright (c)2010 Christian Heilmann
  Code licensed under the BSD License:
  http://wait-till-i.com/license.txt
*/

/* 
Adapted by Mikko Poutanen from:
https://github.com/codepo8/YQL-Geo-Library  
*/
var yqlgeo = function(){
  var callback;
  function get(){
    var args = arguments;
    for(var i=0;i<args.length;i++){
      if(typeof args[i] === 'function'){
        callback = args[i];
      }
    }
    
    getFromText(args[0]);    
  }


  function getFromText(text){
    
       var yql = 'select * from geo.placefinder where text="' + text + '"';
    // var yql = 'select * from geo.places where woeid in ('+
    //           'select match.place.woeId from geo.placemaker where'+
    //           ' documentContent = "' + text + '" and '+
    //           'documentType="text/plain" and appid = "")';
    load(yql,'yqlgeo.retrieved');
  };

  function load(yql,cb){
    if(document.getElementById('yqlgeodata')){
      var old = document.getElementById('yqlgeodata');
      old.parentNode.removeChild(old);
    }
    var src = 'http://query.yahooapis.com/v1/public/yql?q=' +
              encodeURIComponent(yql) +
              '&format=json&diagnostics=true&callback=' +cb+'&'+
              'env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys';


    // 'http://query.yahooapis.com/v1/public/yql?q='+
    //           encodeURIComponent(yql) + '&format=json&callback=' + cb + '&'+
    //           'env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys';
    var head = document.getElementsByTagName('head')[0];
    var s = document.createElement('script');
    s.setAttribute('id','yqlgeodata');
    s.setAttribute('src',src);
    head.appendChild(s);
  };

  function retrieved(o){
    if(o.query.results !== null){
      callback(o.query.results.Result);
    } else {
      callback({error:o.query});
    }
  };
  return {
    get:get,
    retrieved:retrieved
  };
}();