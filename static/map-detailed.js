import { BanMap, AllContent, DetailedRender } from "./map.js";
window.addEventListener("DOMContentLoaded", async (_evt) => {
    const allContent = new AllContent()
    const detailedRender = new DetailedRender()

    const map = new BanMap(allContent, detailedRender)
    const plot = await map.createPlot()

    const div = document.querySelector("#map");
    div.append(plot);
})