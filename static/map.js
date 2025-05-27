import * as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/+esm";
import * as topojson from "https://cdn.jsdelivr.net/npm/topojson-client@3/+esm";

async function loadMapData() {
  const stateRes = await fetch('static/states-10m.json')
  const us = await stateRes.json();
  const states = topojson.feature(us, us.objects.states)
  return states
}

async function loadBanData() {
  const banEndpoint = `${window.location.origin}/get-most-banned-states`;
  const banRes = await fetch(banEndpoint)
  const banList = await banRes.json();
  const banMap = new Map(banList.map(({ name, bans }) => [name, bans]))
  return banMap
}

function createPlot(states, banMap, opts = {}) {
  const {
    withLegend = false,
    withTooltip = false,
  } = opts;

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
          tip: withTooltip,
        }
      )],
    color: {
      range: ["#F9D6D6", "#F1AFAF", "#E98282", "#D14F4F", "#B22E2E"],
      unknown: "#464548",
      type: "log",
      label: withLegend ? "Number of book bans" : null,
      legend: withLegend,
    }

  })

  const div = document.querySelector("#map");
  div.append(plot);

}

async function renderMap(opts = {}) {
   const [states, banMap] = await Promise.all([loadMapData(), loadBanData()]); 
   createPlot(states, banMap, opts)
}

function renderSimpleMap() {
  return renderMap()
}

function renderDetailedMap() {
  return renderMap({withLegend:true, withTooltip:true})
}

window.addEventListener("DOMContentLoaded", async (_evt) => {
  renderDetailedMap()
})