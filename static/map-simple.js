import * as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/+esm";
import * as topojson from "https://cdn.jsdelivr.net/npm/topojson-client@3/+esm";


async function main() {
  const stateRes = await fetch('static/states-10m.json')
  const us = await stateRes.json();


  const banEndpoint = `${window.location.origin}/get-most-banned-states`;
  const banRes = await fetch(banEndpoint)
  const banList = await banRes.json();

  const states = topojson.feature(us, us.objects.states)
  const statesFeatures = states.features

  const banMap = new Map(banList.map(({ name, bans }) => [name, bans]))


  const plot = Plot.plot({
    projection: "albers-usa",
    marks: [
      Plot.geo(
        states,
        {
          stroke: "#000000",
          strokeWidth: 1,
          fill: (d) => banMap.get(d.properties.name),
        }
      )],
    color: {
      scheme: "reds",
      unknown: "#fff",
      type: "log",
      // label: "Number of book bans",
      // legend: true,
    }

  })

  const div = document.querySelector("#map");
  div.append(plot);

}

window.addEventListener("DOMContentLoaded", async (_evt) => {
  await main();
})
