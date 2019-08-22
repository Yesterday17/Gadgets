// ==UserScript==
// @name         Shiny Colors Unmute
// @namespace    https://github.com/Yesterday17/Gadgets
// @version      1.0.0
// @description  Disable mute for shinycolors
// @icon         https://shinycolors.enza.fun/icon_192x192.png
// @author       Yesterday17
// @match        https://shinycolors.enza.fun/*
// @run-at       document-end
// @supportURL   https://github.com/Yesterday17/Gadgets/issues
// ==/UserScript==
;(function() {
  const mute = setInterval(() => {
    if (aoba && aoba.soundManager) {
      aoba.soundManager.mute = () => {}
      clearInterval(mute)
    }
  }, 1000)
})()
