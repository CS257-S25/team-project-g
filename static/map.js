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
    className: "map-plot",
    projection: "albers-usa",
    marks: [
      Plot.geo(
        states,
        {
          stroke: "#f9f9f9",
          strokeWidth: 0.4,
          fill: (d) => banMap.get(d.properties.name),
          title: (d) => `${d.properties.name} \n ${banMap.get(d.properties.name) ? banMap.get(d.properties.name) : 0} bans`,
          tip: true,
        }
      )],
    color: {
      range: ["#F9D6D6", "#F1AFAF", "#E98282", "#D14F4F", "#B22E2E"],
      unknown: "#464548",
      type: "log",
      label: "Number of book bans",
      legend: true,
    }

  })

  const div = document.querySelector("#map");
  div.append(plot);

}

window.addEventListener("DOMContentLoaded", async (_evt) => {
  await main();
})


// test