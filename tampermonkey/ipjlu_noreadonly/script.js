// ==UserScript==
// @name         吉大校园网自助营业厅密码输入
// @namespace    https://github.com/Yesterday17/Gadgets
// @version      1.0.1
// @description  解除吉林大学校园网自助营业厅密码输入环节的强制手动输入。
// @author       Yesterday17
// @match        https://ip.jlu.edu.cn/pay/*
// @run-at       document-body
// @supportURL   https://github.com/Yesterday17/Gadgets/issues
// ==/UserScript==

(() => {
  document.querySelectorAll('[readonly]').forEach(ro => {
    ro.removeAttribute('readonly');
    ro.removeAttribute('onclick');
  });
})();
