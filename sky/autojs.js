var window = floaty.window('<frame><vertical><horizontal><button id="stop" text="停止"w="60"/><button id="btn" text="暂停" w="60"/></horizontal><horizontal><button id="speedHigh" text="加速"w="60"/><button id="turbiHigh" text="加阻"w="60"/></horizontal><horizontal><button id="speed" text="x1" w="60"/><button id="turbidity" text="x1" w="60"/></horizontal><horizontal><button id="speedLow" text="减速" w="60"/><button id="turbiLow" text="减阻" w="60"/></horizontal></vertical></frame>');window.exitOnClose();
window.btn.click(()=>{if (window.btn.getText() != '暂停') {s = 1;window.btn.setText('暂停')} else {s = 0;window.btn.setText('继续')}})
window.speedHigh.click(()=>{speedControl=(speedControl*10+1)/10;window.speed.setText("x"+speedControl)})
window.speedLow.click(()=>{if(speedControl<=0.1){return};speedControl=(speedControl*10-1)/10;window.speed.setText("x"+speedControl)})
window.speed.click(()=>{speedControl=1;window.speed.setText("x"+speedControl)})

window.turbiHigh.click(()=>{if(turbiControl>=(time16/10)){return};turbiControl=(turbiControl*10+1)/10;window.turbidity.setText("x"+turbiControl)})
window.turbiLow.click(()=>{if(turbiControl<=0.1){return};turbiControl=(turbiControl*10-1)/10;window.turbidity.setText("x"+turbiControl)})
window.turbidity.click(()=>{turbiControl=1;window.turbidity.setText("x"+turbiControl)})

window.stop.click(()=>{engines.stopAll()})

var t=0;
var s=1;
var speedControl=1;
var turbiControl=1;
var time1=1000;//-10
var time2=500;//2/1拍时间
var time4=250;//4/1拍时间
var time8=125;//8/1拍时间
var time16=62;//16/1拍时间

setScreenMetrics(1080, 2340);//默认分辨率，以下按键位置基于此分辨率
var x=[619,900,1175,1445,1720];
var y=[260,540,819];

function ran(){return Math.random()*36-18}
function t_ran(){return 10*turbiControl+20}//按键混乱参数
function c4() {press(x[0]+ran(),y[0]+ran(),t_ran());t=t+1}
function d4() {press(x[1]+ran(),y[0]+ran(),t_ran());t=t+1}
function e4() {press(x[2]+ran(),y[0]+ran(),t_ran());t=t+1}
function f4() {press(x[3]+ran(),y[0]+ran(),t_ran());t=t+1}
function g4() {press(x[4]+ran(),y[0]+ran(),t_ran());t=t+1}
function a4() {press(x[0]+ran(),y[1]+ran(),t_ran());t=t+1}
function b4() {press(x[1]+ran(),y[1]+ran(),t_ran());t=t+1}
function c5() {press(x[2]+ran(),y[1]+ran(),t_ran());t=t+1}
function d5() {press(x[3]+ran(),y[1]+ran(),t_ran());t=t+1}
function e5() {press(x[4]+ran(),y[1]+ran(),t_ran());t=t+1}
function f5() {press(x[0]+ran(),y[2]+ran(),t_ran());t=t+1}
function g5() {press(x[1]+ran(),y[2]+ran(),t_ran());t=t+1}
function a5() {press(x[2]+ran(),y[2]+ran(),t_ran());t=t+1}
function b5() {press(x[3]+ran(),y[2]+ran(),t_ran());t=t+1}
function c6() {press(x[4]+ran(),y[2]+ran(),t_ran());t=t+1}

//t<4
function t1() {while (s != 1) {sleep(100)};if((time1/speedControl)-t*(10*turbiControl+20)<=0){sleep(10/speedControl);t=0}else{sleep((time1/speedControl)-t*(10*turbiControl+20));t=0}}//默认间隔-
function t2() {while (s != 1) {sleep(100)};if((time2/speedControl)-t*(10*turbiControl+20)<=0){sleep(10/speedControl);t=0}else{sleep((time2/speedControl)-t*(10*turbiControl+20));t=0}}//默认间隔-
function t4() {while (s != 1) {sleep(100)};if((time4/speedControl)-t*(10*turbiControl+20)<=0){sleep(10/speedControl);t=0}else{sleep((time4/speedControl)-t*(10*turbiControl+20));t=0}}//较短间隔~
function t8() {while (s != 1) {sleep(100)};if((time8/speedControl)-t*(10*turbiControl+20)<=0){sleep(10/speedControl);t=0}else{sleep((time8/speedControl)-t*(10*turbiControl+20));t=0}}//较长间隔,
function t16() {while (s != 1) {sleep(100)};if((time16/speedControl)-t*(10*turbiControl+20)<=0){sleep(10/speedControl);t=0}else{sleep((time16/speedControl))-t*(10*turbiControl+20);t=0}}//自定义间隔*点一下隔100ms
function t5() {while (s != 1) {sleep(100)};sleep(100/speedControl)}//自定义间隔*点一下隔100ms


