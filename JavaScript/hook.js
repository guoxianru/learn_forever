// 收集的常用hook脚本

// document下的createElement()方法的hook,查看创建了什么元素
(function () {
    'use strict'
    var _createElement = document.createElement.bind(document);
    document.createElement = function (elm) {
        // 这里做判断 是否创建了script这个元素
        if (elm == 'body') {
            debugger;
        }
        return _createElement(elm);
    }
})();


// headers hook  当header中包含Authorization时，则插入断点
var code = function () {
    var org = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key == 'Authorization') {
            debugger;
        }
        return org.apply(this, arguments);
    }
}
var script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head || document.documentElement).appendChild(script);
script.parentNode.removeChild(script);


// 请求hook  当请求的url里包含MmEwMD时，则插入断点
var code = function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("MmEwMD") > -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
}
var script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head || document.documentElement).appendChild(script);
script.parentNode.removeChild(script);

// docuemnt.getElementById 以及value属性的hook
// docuemnt.getElementById 以及value属性的hook,可以参考完成innerHTML的hook
document.getElementById = function (id) {
    var value = document.querySelector('#' + id).value;
    console.log('DOM操作 id: ', id)
    try {

        Object.defineProperty(document.querySelector('#' + id), 'value', {
            get: function () {
                console.log('getting -', id, 'value -', value);
                return value;
            },
            set: function (val) {
                console.log('setting -', id, 'value -', val)
                value = val;
            }
        })
    } catch (e) {
        console.log('---------华丽的分割线--------')
    }
    return document.querySelector('#' + id);
}


// 检测函数是否被hook  (大概意思是这样)
if (window.eval == 'native code') {
    console.log('发现eval函数被hook了');
}

// # 过debugger 阿布牛逼
function Closure(injectFunction) {
    return function () {
        if (!arguments.length)
            return injectFunction.apply(this, arguments)
        arguments[arguments.length - 1] = arguments[arguments.length - 1].replace(/debugger/g, "");
        return injectFunction.apply(this, arguments)
    }
}

var oldFunctionConstructor = window.Function.prototype.constructor;
window.Function.prototype.constructor = Closure(oldFunctionConstructor)
//fix native function
window.Function.prototype.constructor.toString = oldFunctionConstructor.toString.bind(oldFunctionConstructor);

var oldFunction = Function;
window.Function = Closure(oldFunction)
//fix native function
window.Function.toString = oldFunction.toString.bind(oldFunction);

var oldEval = eval;
window.eval = Closure(oldEval)
//fix native function
window.eval.toString = oldEval.toString.bind(oldEval);

// hook GeneratorFunction
var oldGeneratorFunctionConstructor = Object.getPrototypeOf(function* () {
}).constructor
var newGeneratorFunctionConstructor = Closure(oldGeneratorFunctionConstructor)
newGeneratorFunctionConstructor.toString = oldGeneratorFunctionConstructor.toString.bind(oldGeneratorFunctionConstructor);
Object.defineProperty(oldGeneratorFunctionConstructor.prototype, "constructor", {
    value: newGeneratorFunctionConstructor,
    writable: false,
    configurable: true
})

// hook Async Function
var oldAsyncFunctionConstructor = Object.getPrototypeOf(async function () {
}).constructor
var newAsyncFunctionConstructor = Closure(oldAsyncFunctionConstructor)
newAsyncFunctionConstructor.toString = oldAsyncFunctionConstructor.toString.bind(oldAsyncFunctionConstructor);
Object.defineProperty(oldAsyncFunctionConstructor.prototype, "constructor", {
    value: newAsyncFunctionConstructor,
    writable: false,
    configurable: true
})

// hook dom
var oldSetAttribute = window.Element.prototype.setAttribute;
window.Element.prototype.setAttribute = function (name, value) {
    if (typeof value == "string")
        value = value.replace(/debugger/g, "")
    // 向上调用
    oldSetAttribute.call(this, name, value)
};
var oldContentWindow = Object.getOwnPropertyDescriptor(HTMLIFrameElement.prototype, "contentWindow").get
Object.defineProperty(window.HTMLIFrameElement.prototype, "contentWindow", {
    get() {
        var newV = oldContentWindow.call(this)
        if (!newV.inject) {
            newV.inject = true;
            core.call(newV, globalConfig, newV);
        }
        return newV
    }
})
// 过debugger—1   constructor 构造器构造出来的
var _constructor = constructor;
Function.prototype.constructor = function (s) {
    if (s == "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
}

    // 过debugger—2  eval的
    (function () {
        'use strict';
        var eval_ = window.eval;
        window.eval = function (x) {
            eval_(x.replace("debugger;", "  ; "));
        };
        window.eval.toString = eval_.toString;
    })();
json
hook
var my_stringify = JSON.stringify;
JSON.stringify = function (params) {
    //这里可以添加其他逻辑比如 debugger
    console.log("json_stringify params:", params);
    return my_stringify(params);
};

var my_parse = JSON.parse;
JSON.parse = function (params) {
    //这里可以添加其他逻辑比如 debugger
    console.log("json_parse params:", params);
    return my_parse(params);
};


// 对象属性hook 属性自定义
(function () {
    // 严格模式，检查所有错误
    'use strict'
    // document 为要hook的对象 ,属性是cookie
    Object.defineProperty(document, 'cookie', {
        // hook set方法也就是赋值的方法，get就是获取的方法
        set: function (val) {
            // 这样就可以快速给下面这个代码行下断点，从而快速定位设置cookie的代码
            debugger;  // 在此处自动断下
            console.log('Hook捕获到set-cookie ->', val);
            return val;
        }
    })
})();

// cookies hook  （不是万能的 有些时候hook不到）
var cookie_cache = document.cookie;

Object.defineProperty(document, 'cookie', {
    get: function () {
        console.log('Getting cookie');
        return cookie_cache;
    },
    set: function (val) {
        console.log("Seting cookie", val);
        var cookie = val.split(";")[0];
        var ncookie = cookie.split("=");
        var flag = false;
        var cache = cookie_cache.split("; ");
        cache = cache.map(function (a) {
            if (a.split("=")[0] === ncookie[0]) {
                flag = true;
                return cookie;
            }
            return a;
        })
    }
})
cookies
var code = function () {
    var org = document.cookie.__lookupSetter__('cookie');
    document.__defineSetter__("cookie", function (cookie) {
        if (cookie.indexOf('TSdc75a61a') > -1) {
            debugger;
        }
        org = cookie;
    });
    document.__defineGetter__("cookie", function () {
        return org;
    });
}
var script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head || document.documentElement).appendChild(script);
script.parentNode.removeChild(script);

// 当cookie中匹配到了 TSdc75a61a， 则插入断点。

window
attr
// 定义hook属性
var window_flag_1 = "_t";
var window_flag_2 = "ccc";

var key_value_map = {};
var window_value = window[window_flag_1];

// hook
Object.defineProperty(window, window_flag_1, {
    get: function () {
        console.log("Getting", window, window_flag_1, "=", window_value);
        //debugger
        return window_value
    },
    set: function (val) {
        console.log("Setting", window, window_flag_1, "=", val);
        //debugger
        window_value = val;
        key_value_map[window[window_flag_1]] = window_flag_1;
        set_obj_attr(window[window_flag_1], window_flag_2);
    },

});

function set_obj_attr(obj, attr) {
    var obj_attr_value = obj[attr];
    Object.defineProperty(obj, attr, {
        get: function () {
            console.log("Getting", key_value_map[obj], attr, "=", obj_attr_value);
            //debugger
            return obj_attr_value;
        },
        set: function (val) {
            console.log("Setting", key_value_map[obj], attr, "=", val);
            //debugger
            obj_attr_value = val;
        },
    });
}

eval / Function
window.__cr_eval = window.eval;
var myeval = function (src) {
    console.log(src);
    console.log("========= eval end ===========");
    return window.__cr_eval;
}

var _myeval = myeval.bind(null);
_myeval.toString = window.__cr_eval.toString;
Object.defineProperty(window, 'eval', {value: _myeval});

window._cr_fun = window.Function
var myfun = function () {
    var args = Array.prototype.slice.call(arguments, 0, -1).join(","), src = arguments[arguments.lenght - 1];
    console.log(src);
    console.log("======== Function end =============");
    return window._cr_fun.apply(this, arguments)
}

myfun.toString = function () {
    return window._cr_fun + ""
} //小花招，这里防止代码里检测原生函数
Object.defineProperty(window, "Function", {value: myfun})

websocket
hook
// 1、webcoket 一般都是json数据格式传输，那么发生之前需要JSON.stringify
var my_stringify = JSON.stringify;
JSON.stringify = function (params) {
    //这里可以添加其他逻辑比如 debugger
    console.log("json_stringify params:", params);
    return my_stringify(params);
};

var my_parse = JSON.parse;
JSON.parse = function (params) {
    //这里可以添加其他逻辑比如 debugger
    console.log("json_parse params:", params);
    return my_parse(params);
};

// 2  webScoket 绑定在windows对象，上，根据浏览器的不同，websokcet名字可能不一样
//chrome window.WebSocket  firfox window.MozWebSocket;
window._WebSocket = window.WebSocket;

// hook send
window._WebSocket.prototype.send = function (data) {
    console.info("Hook WebSocket", data);
    return this.send(data)
}

Object.defineProperty(window, "WebSocket", {value: WebSocket})


    // hook 正则 —— 1
    (function () {
        var _RegExp = RegExp;
        RegExp = function (pattern, modifiers) {
            console.log("Some codes are setting regexp");
            debugger;
            if (modifiers) {
                return _RegExp(pattern, modifiers);
            } else {
                return _RegExp(pattern);
            }
        };
        RegExp.toString = function () {
            return "function setInterval() { [native code] }"
        };
    })();

// hook 正则 2 加在sojson头部过字符串格式化检测
(function () {
    var _RegExp = RegExp;
    RegExp = function (pattern, modifiers) {
        if (pattern == decodeURIComponent("%5Cw%2B%20*%5C(%5C)%20*%7B%5Cw%2B%20*%5B'%7C%22%5D.%2B%5B'%7C%22%5D%3B%3F%20*%7D") || pattern == decodeURIComponent("function%20*%5C(%20*%5C)")
            || pattern == decodeURIComponent("%5C%2B%5C%2B%20*(%3F%3A_0x(%3F%3A%5Ba-f0-9%5D)%7B4%2C6%7D%7C(%3F%3A%5Cb%7C%5Cd)%5Ba-z0-9%5D%7B1%2C4%7D(%3F%3A%5Cb%7C%5Cd))") || pattern == decodeURIComponent("(%5C%5C%5Bx%7Cu%5D(%5Cw)%7B2%2C4%7D)%2B")) {
            pattern = '.*?';
            console.log("发现sojson检测特征，已帮您处理。")
        }
        if (modifiers) {
            console.log("疑似最后一个检测...已帮您处理。")
            console.log("已通过全部检测，请手动处理debugger后尽情调试吧！")
            return _RegExp(pattern, modifiers);
        } else {
            return _RegExp(pattern);
        }
    };
    RegExp.toString = function () {
        return _RegExp.toString();
    };
})();

// hook canvas (定位图片生成的地方)

(function () {
    'use strict';
    let create_element = document.createElement.bind(doument);

    document.createElement = function (_element) {
        console.log("create_element:", _element);
        if (_element === "canvas") {
            debugger;
        }
        return create_element(_element);
    }
})();

// setInterval 定时器
(function () {
    setInterval_ = setInterval;
    console.log("原函数已被重命名为setInterval_")
    setInterval = function () {
    };
    setInterval.toString = function () {
        console.log("有函数正在检测setInterval是否被hook");
        return setInterval_.toString();
    };
})();

// console.log 检测 （不让你输出调试）
var oldConsole = ["debug", "error", "info", "log", "warn", "dir", "dirxml", "table", "trace", "group", "groupCollapsed", "groupEnd", "clear", "count", "countReset", "assert", "profile", "profileEnd", "time", "timeLog", "timeEnd", "timeStamp", "context", "memory"].map(key => {
    var old = console[key];
    console[key] = function () {
    };
    console[key].toString = old.toString.bind(old)
    return old;
})
