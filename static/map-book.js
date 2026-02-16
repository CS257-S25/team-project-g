/**
 * Module for creating a simple map plot for one book
 */
import { BanMap, OneBookContent, DetailedRender } from "./map.js";

window.addEventListener("DOMContentLoaded", async (_evt) => {
  const isbn = document.getElementsByName("isbn")[0].content

  const allContent = new OneBookContent(isbn)
  const detailedRender = new DetailedRender()

  const map = new BanMap(allContent, detailedRender)
  const plot = await map.createPlot()

  const div = document.querySelector("#map");
  div.append(plot);
})
