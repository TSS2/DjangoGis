/**
 *
 * @authors leomYili
 * @date    2016-01-05 11:29:15
 * @version $Id$
 */
(function() {
  function alphaPlay(obj, method) {
    var n = (method == "show") ? 0 : 100,
      ie = (window.ActiveXObject) ? true : false;
    var time = setInterval(function() {
      if (method == "show") {
        if (n < 100) {
          n += 10;
          if (ie) {
            obj.style.cssText = "filter:alpha(opacity=" + n + ")";
          } else {
            (n == 100) ? obj.style.opacity = 1: obj.style.opacity = "0." + n;
          }
        } else {
          clearTimeout(time);
          obj.style.display = "block";
        }
      } else {
        if (n > 0) {
          n -= 10;
          if (ie) {
            obj.style.cssText = "filter:alpha(opacity=" + n + ")";
          } else {
            obj.style.opacity = "0." + n;
          }
        } else {
          clearTimeout(time);
          obj.style.display = "none";
        }
      }
    }, 30);
  }

  function bind(elem, ev, callback) {
    if (document.all) {
      elem.attachEvent("on" + ev, callback);
    } else {
      elem.addEventListener(ev, callback, false);
    }
  }

  function unbind(elem, ev, callback) {
    if (typeof(callback) == "function") {
      if (document.all) {
        elem.detachEvent("on" + ev, callback);
      } else {
        elem.removeEventListener(ev, callback, false);
      }
    } else {
      if (document.all) {
        elem.detachEvent("on" + ev);
      } else {
        elem.removeEventListener(ev, false);
      }
    }
  }

  function hover(elem, overCallback, outCallback) { //实现hover事件
    var isHover = false; //判断是否悬浮在上方
    var preOvTime = new Date().getTime(); //上次悬浮时间
    function over(e) {
      var curOvTime = new Date().getTime();
      isHover = true; //处于over状态
      if (curOvTime - preOvTime > 10) { //时间间隔超过10毫秒，认为鼠标完成了mouseout事件
        overCallback(e, elem);
      }
      preOvTime = curOvTime;
    }

    function out(e) {
      var curOvTime = new Date().getTime();
      preOvTime = curOvTime;
      isHover = false;
      setTimeout(function() {
        if (!isHover) {
          outCallback(e, elem);
        }
      }, 10);
    }
    bind(elem, "mouseover", over);
    bind(elem, "mouseout", out);
  };

  function getOffset(Node, offset) {
    if (!offset) {
      offset = {};
      offset.top = 0;
      offset.left = 0;
    }
    if (Node == document.body) { //当该节点为body节点时，结束递归
      return offset;
    }
    offset.top += Node.offsetTop;
    offset.left += Node.offsetLeft;
    return getOffset(Node.parentNode, offset); //向上累加offset里的值
  }

  var el = $('.ZMenu-left-nav-a.item');
  el.click(function() {
    if ($(this).hasClass('up')) {
      $(this).removeClass('up');
      $(this).addClass('down');
      var objc = $(this).next().get(0);
      alphaPlay(objc, "show");
    } else if ($(this).hasClass('down')) {
      $(this).removeClass('down');
      $(this).addClass('up');
      var objc = $(this).next().get(0);
      alphaPlay(objc, "hiden");
    }
  });

  $(".ZMenu-left-nav-a").each(function(index,element) {
    hover(element, function(e, elem) {
      /*jquery或zepto可使用该方法
       *var x=$(element).offset().top-8;
      console.log(x);*/
      var cc=getOffset(elem).top-8;
      console.log(cc);
      $("#testlabel").css({
        top: cc + "px"
      })
    }, function(e, elem) {});
  });
  hover($(".ZMenu-left").get(0), function() {}, function(e, elem) {
    $("#testlabel").css({
      top: "16px"
    })
  });
})();
