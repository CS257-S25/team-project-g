/**
 * Module for creating a simple map plot
 */
import { BanMap, AllContent, SimpleRender } from "./map.js";

window.addEventListener("DOMContentLoaded", async (_evt) => {
  const allContent = new AllContent()
  const simpleRender = new SimpleRender()

  const map = new BanMap(allContent, simpleRender)
  const plot = await map.createPlot()

  const div = document.querySelector("#map");
  div.append(plot);
})
