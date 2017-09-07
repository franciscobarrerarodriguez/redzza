webpackJsonp([2,5],{

/***/ 107:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_aos__ = __webpack_require__(198);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_aos___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_aos__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_animations__ = __webpack_require__(55);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return LandingPageComponent; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var LandingPageComponent = (function () {
    function LandingPageComponent() {
        this.stateContactLayer = 'large';
    }
    LandingPageComponent.prototype.ngOnInit = function () {
        $('.modal').modal();
        __WEBPACK_IMPORTED_MODULE_1_aos__["init"]();
    };
    LandingPageComponent.prototype.quoted = function () {
        $('#modal1').modal('open');
    };
    LandingPageComponent.prototype.toVideo = function () {
        /*$('html, body').animate({
                        scrollTop: $(".videowrapper").offset().top
                    }, 1000);*/
    };
    LandingPageComponent.prototype.showContactLayer = function () {
        this.stateContactLayer = (this.stateContactLayer === 'small' ? 'large' : 'small');
    };
    LandingPageComponent.prototype.scrollFire = function () {
        var options = [
            { selector: '.btnBottom', offset: 50, callback: function (el) { Materialize.toast("This is our ScrollFire Demo!", 1500); } },
            { selector: '.btnBottom', offset: 205, callback: function (el) { Materialize.toast("Please continue scrolling!", 1500); } }
            //{selector: '#staggered-test', offset: 400, callback: function(el) { Materialize.showStaggeredList($('.btnBottom')); } }, 
            //{selector: '#image-test', offset: 500, callback: function(el) { Materialize.fadeInImage($(el)); } } ]; Materialize.scrollFire(options); 
        ];
    };
    LandingPageComponent = __decorate([
        __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_11" /* Component */])({
            selector: 'app-landing-page',
            template: __webpack_require__(338),
            styles: [__webpack_require__(256)],
            animations: [
                __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["i" /* trigger */])('contactLayer', [
                    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["j" /* state */])('small', __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["h" /* style */])({
                        transform: 'scale(1)',
                        right: '40px',
                        bottom: '60px',
                        opacity: '1'
                    })),
                    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["j" /* state */])('large', __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["h" /* style */])({
                        transform: 'scale(0)',
                        right: '-70px',
                        bottom: '-80px',
                        opacity: '0'
                    })),
                    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["k" /* transition */])('small => large', __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["l" /* animate */])('500ms ease-in')),
                    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["k" /* transition */])('large => small', __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_2__angular_animations__["l" /* animate */])('500ms ease-out')),
                ]),
            ]
        }),
        __metadata("design:paramtypes", [])
    ], LandingPageComponent);
    return LandingPageComponent;
}());

//# sourceMappingURL=landing-page.component.js.map

/***/ }),

/***/ 172:
/***/ (function(module, exports) {

function webpackEmptyContext(req) {
	throw new Error("Cannot find module '" + req + "'.");
}
webpackEmptyContext.keys = function() { return []; };
webpackEmptyContext.resolve = webpackEmptyContext;
module.exports = webpackEmptyContext;
webpackEmptyContext.id = 172;


/***/ }),

/***/ 173:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__ = __webpack_require__(186);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__app_app_module__ = __webpack_require__(190);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__environments_environment__ = __webpack_require__(195);




if (__WEBPACK_IMPORTED_MODULE_3__environments_environment__["a" /* environment */].production) {
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["a" /* enableProdMode */])();
}
__webpack_require__.i(__WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__["a" /* platformBrowserDynamic */])().bootstrapModule(__WEBPACK_IMPORTED_MODULE_2__app_app_module__["a" /* AppModule */]);
//# sourceMappingURL=main.js.map

/***/ }),

/***/ 189:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppComponent; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

var AppComponent = (function () {
    function AppComponent() {
        this.title = 'app works!';
    }
    AppComponent = __decorate([
        __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_11" /* Component */])({
            selector: 'app-root',
            template: __webpack_require__(337),
            styles: [__webpack_require__(255)]
        })
    ], AppComponent);
    return AppComponent;
}());

//# sourceMappingURL=app.component.js.map

/***/ }),

/***/ 190:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_platform_browser__ = __webpack_require__(27);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_forms__ = __webpack_require__(185);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__angular_platform_browser_animations__ = __webpack_require__(187);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__angular_http__ = __webpack_require__(106);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__app_component__ = __webpack_require__(189);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__app_routing__ = __webpack_require__(191);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__services_interceptor_intercepter_http_factory__ = __webpack_require__(194);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__components_landing_page_landing_page_component__ = __webpack_require__(107);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9_ng2_materialize__ = __webpack_require__(283);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppModule; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};






// carga rutas de routing.ts

//interceptor



var AppModule = (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["b" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_5__app_component__["a" /* AppComponent */],
                __WEBPACK_IMPORTED_MODULE_8__components_landing_page_landing_page_component__["a" /* LandingPageComponent */]
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1__angular_platform_browser__["a" /* BrowserModule */],
                __WEBPACK_IMPORTED_MODULE_2__angular_forms__["a" /* FormsModule */],
                __WEBPACK_IMPORTED_MODULE_4__angular_http__["a" /* HttpModule */],
                __WEBPACK_IMPORTED_MODULE_4__angular_http__["b" /* JsonpModule */],
                __WEBPACK_IMPORTED_MODULE_6__app_routing__["a" /* routing */],
                __WEBPACK_IMPORTED_MODULE_9_ng2_materialize__["a" /* MaterializeModule */].forRoot(),
                __WEBPACK_IMPORTED_MODULE_3__angular_platform_browser_animations__["a" /* BrowserAnimationsModule */]
            ],
            providers: [
                __WEBPACK_IMPORTED_MODULE_6__app_routing__["b" /* appRoutingProviders */],
                {
                    provide: __WEBPACK_IMPORTED_MODULE_4__angular_http__["c" /* Http */],
                    useFactory: __WEBPACK_IMPORTED_MODULE_7__services_interceptor_intercepter_http_factory__["a" /* IntercepterHttpFactory */],
                    deps: [__WEBPACK_IMPORTED_MODULE_4__angular_http__["d" /* XHRBackend */], __WEBPACK_IMPORTED_MODULE_4__angular_http__["e" /* RequestOptions */]]
                }
            ],
            bootstrap: [__WEBPACK_IMPORTED_MODULE_5__app_component__["a" /* AppComponent */]]
        })
    ], AppModule);
    return AppModule;
}());

//# sourceMappingURL=app.module.js.map

/***/ }),

/***/ 191:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_router__ = __webpack_require__(188);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__components_landing_page_landing_page_component__ = __webpack_require__(107);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "b", function() { return appRoutingProviders; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return routing; });


var appRoutes = [
    { path: '', component: __WEBPACK_IMPORTED_MODULE_1__components_landing_page_landing_page_component__["a" /* LandingPageComponent */] },
    { path: '**', component: __WEBPACK_IMPORTED_MODULE_1__components_landing_page_landing_page_component__["a" /* LandingPageComponent */] }
];
var appRoutingProviders = [];
var routing = __WEBPACK_IMPORTED_MODULE_0__angular_router__["a" /* RouterModule */].forRoot(appRoutes);
//# sourceMappingURL=app.routing.js.map

/***/ }),

/***/ 192:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return GLOBAL; });
var GLOBAL = {
    //apiGeepy:'http://localhost:8080/geepy/'
    apiGeepy: 'http://www.beeapps.co/geepy/'
};
//# sourceMappingURL=global.js.map

/***/ }),

/***/ 193:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_http__ = __webpack_require__(106);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__enviroment_global__ = __webpack_require__(192);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return InterceptedHttpService; });
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



//import { Token } from '../../models/token';
var InterceptedHttpService = (function (_super) {
    __extends(InterceptedHttpService, _super);
    function InterceptedHttpService(backend, defaultOptions) {
        return _super.call(this, backend, defaultOptions) || this;
    }
    InterceptedHttpService.prototype.get = function (url, options) {
        url = this.updateUrl(url);
        return _super.prototype.get.call(this, url, this.getRequestOptionArgs(options));
    };
    InterceptedHttpService.prototype.post = function (url, body, options) {
        url = this.updateUrl(url);
        return _super.prototype.post.call(this, url, body, this.getRequestOptionArgs(options));
    };
    InterceptedHttpService.prototype.put = function (url, body, options) {
        url = this.updateUrl(url);
        return _super.prototype.put.call(this, url, body, this.getRequestOptionArgs(options));
    };
    InterceptedHttpService.prototype.patch = function (url, body, options) {
        url = this.updateUrl(url);
        return _super.prototype.patch.call(this, url, body, this.getRequestOptionArgs(options));
    };
    InterceptedHttpService.prototype.delete = function (url, options) {
        url = this.updateUrl(url);
        return _super.prototype.delete.call(this, url, this.getRequestOptionArgs(options));
    };
    InterceptedHttpService.prototype.updateUrl = function (req) {
        return __WEBPACK_IMPORTED_MODULE_2__enviroment_global__["a" /* GLOBAL */].apiGeepy + req;
    };
    InterceptedHttpService.prototype.getRequestOptionArgs = function (options) {
        if (options == null) {
            options = new __WEBPACK_IMPORTED_MODULE_1__angular_http__["e" /* RequestOptions */]();
        }
        if (options.headers == null) {
            options.headers = new __WEBPACK_IMPORTED_MODULE_1__angular_http__["f" /* Headers */]();
        }
        options.headers.append('Content-Type', 'application/json');
        //options.headers.append('Access-Control-Allow-Origin','*');
        options.headers.append('Access-Control-Allow-Methods', 'POST, GET, OPTIONS');
        options.headers.append('Access-Control-Allow-Headers', 'x-requested-with');
        /*let accestoken="";
        if(typeof(Storage) !== "undefined") {
            let token:Token=JSON.parse(localStorage.getItem("auth"));
            if(token){
              accestoken=token.access_token;
              options.headers.append('Authorization','Bearer '+accestoken);
            }
         }*/
        return options;
    };
    InterceptedHttpService = __decorate([
        __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["c" /* Injectable */])(),
        __metadata("design:paramtypes", [typeof (_a = typeof __WEBPACK_IMPORTED_MODULE_1__angular_http__["g" /* ConnectionBackend */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_1__angular_http__["g" /* ConnectionBackend */]) === "function" && _a || Object, typeof (_b = typeof __WEBPACK_IMPORTED_MODULE_1__angular_http__["e" /* RequestOptions */] !== "undefined" && __WEBPACK_IMPORTED_MODULE_1__angular_http__["e" /* RequestOptions */]) === "function" && _b || Object])
    ], InterceptedHttpService);
    return InterceptedHttpService;
    var _a, _b;
}(__WEBPACK_IMPORTED_MODULE_1__angular_http__["c" /* Http */]));

//# sourceMappingURL=intercepted-http.service.js.map

/***/ }),

/***/ 194:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__intercepted_http_service__ = __webpack_require__(193);
/* harmony export (immutable) */ __webpack_exports__["a"] = IntercepterHttpFactory;

function IntercepterHttpFactory(xhrBackend, requestOptions) {
    return new __WEBPACK_IMPORTED_MODULE_0__intercepted_http_service__["a" /* InterceptedHttpService */](xhrBackend, requestOptions);
}
//# sourceMappingURL=intercepter-http-factory.js.map

/***/ }),

/***/ 195:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return environment; });
// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.
var environment = {
    production: false
};
//# sourceMappingURL=environment.js.map

/***/ }),

/***/ 255:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(18)();
// imports
exports.i(__webpack_require__(72), "");
exports.i(__webpack_require__(73), "");

// module
exports.push([module.i, "\n", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ 256:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(18)();
// imports


// module
exports.push([module.i, "html, body {\n  height: 100%; }\n\n/*** slot start****/\nnav {\n  position: absolute;\n  box-shadow: none;\n  background-color: rgba(0, 0, 0, 0.5);\n  z-index: 10; }\n\nnav ul a {\n  font-size: 1.2rem; }\n\n.brand-logo {\n  margin-left: 10px; }\n\n.container-icon {\n  margin: 0 auto;\n  width: 100%;\n  text-align: center;\n  top: 540px;\n  position: absolute; }\n\n.btnMenu {\n  margin-left: 10px; }\n\n.containerBtnMenu {\n  width: 60px;\n  position: absolute; }\n\n.home-inner {\n  width: 100%;\n  text-align: center;\n  position: absolute; }\n\n.btnJoinNow {\n  background-color: #00C88F;\n  padding: 15px 50px 15px 50px;\n  margin: 0 auto;\n  width: 230px;\n  margin-top: 35px;\n  border-radius: 3px;\n  transition: all 0.5s ease-in-out;\n  cursor: pointer; }\n\n.btnJoinNow:hover {\n  -webkit-transform: scale(1.1);\n          transform: scale(1.1); }\n\n.lineConect {\n  position: absolute;\n  width: 2px;\n  height: 180px;\n  left: calc(50% - 1px);\n  border: none;\n  background-color: #00C88F;\n  z-index: -1; }\n\n.btnToInfoRedzza {\n  background-color: #00C88F;\n  padding: 14px 15px 15px 15px;\n  position: absolute;\n  width: 60px;\n  height: 60px;\n  font-size: 22px;\n  margin-top: 125px;\n  border-radius: 50%;\n  left: calc( 50% - 30px); }\n\n.logo:hover {\n  -webkit-transform: rotateY(360deg);\n          transform: rotateY(360deg); }\n\n.logo {\n  margin-top: 8px;\n  margin-left: 12px;\n  height: 48px;\n  width: 290px;\n  background-image: url(\"/assets/img/landing-page/Logo-Domotinas-Vertical.png\");\n  background-size: 100% 100%;\n  transition: all 5s ease-out; }\n\n.btnCenter {\n  text-align: center;\n  width: 100%;\n  position: absolute;\n  top: 400px; }\n\n.auxLayer {\n  height: 1px;\n  width: 1px; }\n\n.containerNavElements {\n  position: relative; }\n\n.porcentualCentry {\n  position: absolute;\n  left: 50%;\n  top: 50%;\n  transform: translate(-50%, -50%);\n  -webkit-transform: translate(-50%, -50%); }\n\n/**** slot info redzza ****/\n.imgProducto {\n  background-image: url(\"/assets/img/landing-page/product.jpg\");\n  background-size: 100% 100%;\n  height: 36vw;\n  width: 45vw;\n  margin: 0 auto;\n  margin-top: 30px; }\n\n.infoRedzza {\n  margin: 20px; }\n\n.containerInfoRedzza {\n  margin: 100px 0px 100px 0px; }\n\n/***** slot is very easy *****/\n.steps-easy {\n  padding-top: 20px;\n  padding-bottom: 20px;\n  background-color: #f037a5;\n  background: linear-gradient(#fae62d -30%, #f037a5 150%); }\n\n.steps-easy p, .steps-easy h2, .steps-easy h3 {\n  color: #fff; }\n\n.steps-easy:before,\n.steps-easy:after {\n  content: \" \";\n  display: table; }\n\n.steps-easy:after {\n  clear: both; }\n\n.steps-bg {\n  height: 100%;\n  width: 100%;\n  background-image: url(\"/assets/svg/hero-burst-easy.svg\");\n  background-repeat: no-repeat;\n  z-index: 0;\n  color: #FFFFFF !important; }\n\n.imgDeskLines {\n  background-image: url(\"/assets/svg/des.svg\");\n  background-size: 100% 100%;\n  height: 26vw;\n  width: 35vw;\n  margin: 0 auto;\n  margin-top: 30px; }\n\n@-webkit-keyframes scale {\n  0% {\n    -webkit-transform: scale(1);\n            transform: scale(1); }\n  50% {\n    -webkit-transform: scale(1.03);\n            transform: scale(1.03); }\n  100% {\n    -webkit-transform: sacle(1);\n            transform: sacle(1); } }\n\n@keyframes scale {\n  0% {\n    -webkit-transform: scale(1);\n            transform: scale(1); }\n  50% {\n    -webkit-transform: scale(1.03);\n            transform: scale(1.03); }\n  100% {\n    -webkit-transform: sacle(1);\n            transform: sacle(1); } }\n\n@media (max-width: 992px) {\n  .container-icon {\n    top: 963px; }\n  .porcentualCentry {\n    position: absolute;\n    left: 40%;\n    top: 30%;\n    transform: translate(-40%, -30%);\n    -webkit-transform: translate(-40%, -30%);\n    background-size: 100% 100%; }\n  .imgProducto {\n    height: 73vw;\n    width: 90vw; }\n  .imgDeskLines {\n    height: 46vw;\n    width: 60vw;\n    margin: 0 auto;\n    margin-top: 30px; }\n  .desc {\n    padding: 20px 100px 20px 100px; }\n  .desc p {\n    font-size: 25px; } }\n\n@media (max-width: 767px) {\n  h2 {\n    font-size: 2.1rem; }\n  h5 {\n    font-size: 1.2rem; }\n  .container-icon {\n    top: 505px; }\n  .leyendToReferences {\n    height: 470px; }\n  .descriptionCost2 {\n    height: 265px;\n    padding: 0px 30px 0px 60px; }\n  .descriptionCost {\n    padding: 0px 30px 0px 60px; }\n  .containersValues {\n    background-image: none; }\n  .brand-logo {\n    margin-left: 0px; }\n  .imgProducto {\n    background-image: url(\"/assets/img/landing-page/product.jpg\");\n    background-size: 100% 100%;\n    height: 68vw;\n    width: 80vw; }\n  .desc {\n    padding: 20px; }\n  .desc p {\n    font-size: 15px; } }\n\n@media (min-width: 601px) {\n  .iconMenu {\n    height: 0px !important;\n    line-height: 40px !important; } }\n\n@media (min-height: 1300px) {\n  .porcentualCentry {\n    position: absolute;\n    left: 20%;\n    top: 20%;\n    transform: translate(-20%, -20%);\n    -webkit-transform: translate(-20%, -20%); } }\n", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ 337:
/***/ (function(module, exports) {

module.exports = "<router-outlet></router-outlet>"

/***/ }),

/***/ 338:
/***/ (function(module, exports) {

module.exports = "\n<!-- NAVBAR -->\n<nav>\n    <div class=\"nav-wrapper\">\n      <a href=\"#\" class=\"brand-logo\">Redzza</a>\n      <ul id=\"nav-mobile\" class=\"right hide-on-med-and-down\">\n        <li><a href=\"#\">Ingresar</a></li>\n        <li><a href=\"#\">Regístrate</a></li>\n      </ul>\n    </div>\n  </nav>\n<!-- PARALAX DESKTOP -->\n<div class=\"hide-on-med-and-down\" data-aos=\"fade-up\">\n  <mz-parallax [height]=\"750\" >\n    <img src=\"assets/img/landing-page/imgSlotHome1.jpg\">\n  </mz-parallax>\n  <div class=\"home-inner porcentualCentry\"> \n      <div class=\"home-content\">\n        <h2 class=\"text-cyan white-text\">Redzza</h2>\n        <h5 class=\"white-text\">Como quieres, no como te toca</h5>\n        <div class=\"btnJoinNow grey-text text-darken-3\" (click)=\"quoted()\">UNETE AHORA</div>\n      </div>\n      <div class=\"containerNavElements\">\n        <div class=\"lineConect\"></div>\n        <div class=\"btnToInfoRedzza\"><i class=\"mdi mdi-chevron-down grey-text text-darken-3\"></i></div>\n      </div>\n    </div>\n</div>\n<!-- PARALAX TABLET -->\n<div class=\"hide-on-large-only hide-on-small-only\">\n  <mz-parallax [height]=\"900\">\n    <img src=\"assets/img/landing-page/imgSlotHome1.jpg\">\n  </mz-parallax>\n  <div class=\"home-inner porcentualCentry\"> \n      <div class=\"home-content \">\n        <h2 class=\"text-cyan white-text\">Redzza</h2>\n        <h5 class=\"white-text\">Como quieres, no como te toca</h5>\n        <div class=\"btnJoinNow grey-text text-darken-3\" (click)=\"quoted()\">UNETE AHORA</div>\n      </div>\n      <div class=\"lineConect\"></div>\n      <div class=\"btnToInfoRedzza\"><i class=\"mdi mdi-chevron-down grey-text text-darken-3\"></i></div>\n    </div>\n</div>\n<!-- PARALAX MOVIL -->\n<div class=\"hide-on-med-and-up\">\n  <mz-parallax [height]=\"550\">\n    <img src=\"assets/img/landing-page/imgSlotHome1.jpg\">\n  </mz-parallax>\n  <div class=\"home-inner porcentualCentry\"> \n      <div class=\"home-content \">\n        <h2 class=\"text-cyan white-text\">Redzza</h2>\n        <h5 class=\"white-text\">Como quieres, no como te toca</h5>\n        <div class=\"btnJoinNow grey-text text-darken-3\" (click)=\"quoted()\">UNETE AHORA</div>\n      </div>\n      <div class=\"lineConect\"></div>\n      <div class=\"btnToInfoRedzza\"><i class=\"mdi mdi-chevron-down grey-text text-darken-3\"></i></div>\n    </div>\n</div>\n<!-- INFO REDZZA -->\n<div class=\"row containerInfoRedzza\">\n    <div class=\"col s12 m12 l6\">\n      <div class=\"infoRedzza\" data-aos=\"fade-right\" data-aos-once=\"true\">\n        <h2>¿Qué hay en Redzza?</h2>\n        <h3>\n          Intercambios\n        </h3>\n        <p>\n          Redzza es una plataforma para el intercambio, aqui podras cualquier\n          cosa que quieras intercambiar;\n          tambien podras ver lo que otras personas tienen para intercambiar.\n        </p>\n        <h3>\n          Sorpresas\n        </h3>\n        <p>\n          Redzza conecta a las personas que tienen cosas que pueden ser un\n          tesoro para otras, muchas de ellas te sorprenderan.\n        </p>\n        <h3>\n          Seguridad\n        </h3>\n        <p>\n          Redzza te ofrece distintos metodos para que los intercambios que\n          realices sean completamente seguros, solo tienes que elegir uno.\n        </p>\n      </div>\n\n    </div>\n    <div class=\"col s12 m12 l6\">\n      <div class=\"imgProducto\" data-aos=\"fade-left\" data-aos-once=\"true\"></div>\n    </div>\n</div>\n<!-- IS VERY EASY -->\n<div class=\"steps-easy\" data-aos=\"fade-up\" data-aos-once=\"true\">\n  <div class=\"row steps-bg\">\n      <div class=\"col s12  l6\">\n        <div class=\"imgDeskLines\"></div>\n      </div>\n      <div class=\"col s12 l6\">\n        <div class=\"desc\">\n          <h3>Es muy facil</h3>\n          <h2>Publica</h2>\n          <p>\n            Puedes publicar cualquier articulo, de seguro a alguien le va a interesar.\n          </p>\n          <h2>Busca</h2>\n          <p>\n            ¿Aún no encuentras lo que buscas? Tal vez no habías buscado aquí.\n          </p>\n          <h2>Intercambia</h2>\n          <p>\n            Una forma milenaria de tener lo que quieres, solo que si moverte de tu cama.\n          </p>\n        </div>\n      </div>\n  </div>\n</div>\n<!-- SLIDER NAV BAR -->\n<mz-sidenav>\n  [id]=\"'sidenav-demo'\"\n  [collapseButtonId]=\"'btn-sidenav-demo'\">\n  <mz-sidenav-header>\n    Sidenav header\n  </mz-sidenav-header>\n  <mz-sidenav-subheader>Link Subheader</mz-sidenav-subheader>\n  <mz-sidenav-link>\n    <a href=\"#\">First Link</a>\n  </mz-sidenav-link>\n  <mz-sidenav-divider></mz-sidenav-divider>\n  <mz-sidenav-link [active]=\"true\">\n    <a href=\"#\">Active Link</a>\n  </mz-sidenav-link>\n  <mz-sidenav-divider></mz-sidenav-divider>\n  <mz-sidenav-link>\n    <a href=\"#\" class=\"waves-effect\">Second Link With Waves</a>\n  </mz-sidenav-link>\n</mz-sidenav>\n<!-- modal -->\n<div id=\"modal1\" class=\"modal bottom-sheet\">\n    <div class=\"modal-content\">\n      <h4>Modal Header</h4>\n      <p>A bunch of text</p>\n    </div>\n    <div class=\"modal-footer\">\n      <a href=\"#!\" class=\"modal-action modal-close waves-effect waves-green btn-flat\">Agree</a>\n    </div>\n  </div>\n\n"

/***/ }),

/***/ 423:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(182);
module.exports = __webpack_require__(173);


/***/ })

},[423]);
//# sourceMappingURL=main.bundle.js.map